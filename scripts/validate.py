#!/usr/bin/env python3
"""Validate a tree of generated EU act files (EU-LAW.xml eu.rule.validation).

  python scripts/validate.py --root DIR [--raw DIR] [--config DIR] [--json OUT]

Blocking errors (exit code 1): incomplete metadata, celex or source missing, type other than Regulamento / Diretiva,
empty article (the placeholder *(Sem texto)* of an article the source prints bare is a warning), duplicate id or celex, article count different from the one in the XHTML itself (ids art_N), recitals
missing in an original that has them, a transposition line with an id that is not in config/pt-ids.txt, plus structural
errors in parts. Gaps in article numbering and acts without articles are warnings only.
Output (--json): {"errors": [{"code", "file", "celex", "message"}], "warnings": [...]}.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (DATE_FIELDS, EMPTY_MARK, ISO_DATE, REQUIRED, STATUS_IN_FORCE, TEXT_CONSOLIDATED, TEXT_ORIGINAL, TYPES,  # noqa: E402
                    TYPE_DIRECTIVE, act_id, article_number, iter_owned_files, parse_frontmatter, split_articles)

ID_RE = re.compile(r"^(regulamento|diretiva)-ue-\d{4}-\d+(-[a-z0-9]+)*$")
NOTE_LINE = re.compile(r"^\s*-\s+\*.*\*\s*$")
ROW_RE = re.compile(r"^\|([^|\n]*)\|\s*([^|\n]+?\.md)\s*\|([^|\n]*)\|([^|\n]*)\|\s*$", re.M)
TRANSPOSITION = "## Transposição para Portugal"
LARGE_FILE_BYTES = 90 * 1024


def _issue(code, file, celex, message):
    return {"code": code, "file": file, "celex": celex, "message": message}


def number_gaps(numbers):
    """Pairs (previous, next) where the integer part of consecutive article numbers jumps by more than 1."""
    gaps, prev = [], None
    for n in numbers:
        m = re.match(r"(\d+)", n or "")
        if not m:
            continue
        cur = int(m.group(1))
        if prev is not None and cur > prev + 1:
            gaps.append((prev, cur))
        prev = cur
    return gaps


def article_empty(body):
    return not [ln for ln in body.splitlines() if ln.strip() and not NOTE_LINE.match(ln)]


def recital_lines(body, whole_file):
    """Number of recital paragraphs '(N) ...' in the Considerandos section (or in the whole file of a recitals part
    that has no Considerandos heading). Footnotes after the signature also look like '(N) ...' and are not counted."""
    i = body.find("\n## Considerandos")
    if i < 0 and not body.startswith("## Considerandos"):
        if not whole_file:
            return 0
    else:
        rest = body[i + 1:] if i >= 0 else body
        m = re.search(r"\n## (?!Considerandos)", rest[3:])
        body = rest[:m.start() + 3] if m else rest
    n = len(re.findall(r"(?m)^\(\d+\) ", body))
    if not n and re.search(r"(?m)^## Considerandos\s*\n+\S", body):
        return 1  # a single unnumbered recital
    return n


def validate(root, expected=None, pt_ids=None):
    """Returns (errors, warnings). expected: {celex: {"articles": n, "recitals": m, "kind": "original"|"consolidated"}}
    measured on the raw XHTML; pt_ids: set of Portuguese ids that exist (None: skip that check)."""
    errors, warnings = [], []
    root = Path(root)
    files = []   # (rel, meta, article numbers, empty article headings, overview body, has text, recitals, size, section)
    for p in iter_owned_files(root):
        rel = p.relative_to(root).as_posix()
        try:
            raw_text = p.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(raw_text)
        except (ValueError, OSError) as e:
            errors.append(_issue("bad_frontmatter", rel, None, str(e)))
            continue
        arts = split_articles(body)
        for head, art_body in arts:
            if art_body == EMPTY_MARK:   # the source itself prints no text here: listed so a converter bug cannot hide in it
                warnings.append(_issue("article_without_text", rel, str(meta.get("celex") or "") or None, f"the source has no text for: {head[:80]}"))
        core = [ln for ln in body.splitlines() if ln.strip() and not ln.startswith("# ")]
        part = str(meta.get("part") or "")
        i = body.find("\n" + TRANSPOSITION)
        section = body[i + 1:] if i >= 0 else ""
        files.append((rel, meta, [article_number(h) for h, _ in arts], [h for h, b in arts if article_empty(b)],
                      body if "| parte | caminho |" in body else "", bool(core),
                      recital_lines(body, part.startswith("Considerandos")), len(raw_text.encode("utf-8")), section))
    ids, by_celex = {}, {}
    for rel, meta, nums, empties, _, has_text, _, size, section in files:
        celex = str(meta.get("celex") or "") or None
        missing = [k for k in REQUIRED if meta.get(k) in (None, "")]
        if "celex" in missing:
            errors.append(_issue("missing_celex", rel, None, "celex is missing"))
        if "source" in missing:
            errors.append(_issue("missing_source", rel, celex, "source (EUR-Lex link) is missing"))
        rest = [k for k in missing if k not in ("celex", "source")]
        if rest:
            errors.append(_issue("incomplete_metadata", rel, celex, "missing fields: " + ", ".join(rest)))
        for k in DATE_FIELDS:
            if meta.get(k) and not ISO_DATE.match(str(meta[k])):
                errors.append(_issue("incomplete_metadata", rel, celex, f"{k} is not an ISO date: {meta[k]!r}"))
        if meta.get("status") and meta["status"] != STATUS_IN_FORCE:
            errors.append(_issue("incomplete_metadata", rel, celex, f"status not allowed: {meta['status']!r}"))
        tv = meta.get("text_version")
        if tv and tv not in (TEXT_CONSOLIDATED, TEXT_ORIGINAL):
            errors.append(_issue("incomplete_metadata", rel, celex, f"text_version not allowed: {tv!r}"))
        if tv == TEXT_CONSOLIDATED and not (meta.get("last_amended") and meta.get("consolidated_celex")):
            errors.append(_issue("incomplete_metadata", rel, celex, "a consolidated text needs last_amended and consolidated_celex"))
        if tv == TEXT_ORIGINAL and (meta.get("last_amended") or meta.get("consolidated_celex")):
            errors.append(_issue("incomplete_metadata", rel, celex, "an original text has no last_amended or consolidated_celex"))
        if bool(meta.get("part_of")) != bool(meta.get("part")):
            errors.append(_issue("bad_part", rel, celex, "part_of and part must both be filled or both empty"))
        if meta.get("source") and not re.match(r"^https://eur-lex\.europa\.eu/.+CELEX:\S+$", str(meta["source"])):
            errors.append(_issue("missing_source", rel, celex, f"source is not an EUR-Lex link: {meta['source']!r}"))
        if meta.get("type") and meta["type"] not in TYPES:
            errors.append(_issue("unknown_type", rel, celex, f"type must be Regulamento or Diretiva: {meta['type']!r}"))
        fid = meta.get("id")
        if fid:
            if not ID_RE.match(str(fid)):
                errors.append(_issue("bad_id", rel, celex, f"id has an invalid format: {fid!r}"))
            if Path(rel).stem != fid:
                errors.append(_issue("bad_id", rel, celex, f"file name does not match id {fid!r}"))
            if not meta.get("part_of") and celex and act_id(celex) != fid:
                errors.append(_issue("bad_id", rel, celex, f"id {fid!r} does not match the CELEX number"))
            if fid in ids:
                errors.append(_issue("duplicate_id", rel, celex, f"id {fid!r} is also used by {ids[fid]}"))
            else:
                ids[fid] = rel
        if celex:
            by_celex.setdefault(celex, []).append((rel, meta))
        for head in empties:
            errors.append(_issue("empty_article", rel, celex, f"empty article: {head[:80]}"))
        dup = sorted(n for n, c in Counter(nums).items() if c > 1)
        if dup:
            warnings.append(_issue("duplicate_article_numbers", rel, celex, "article numbers repeated: " + ", ".join(dup[:10])))
        gaps = number_gaps(nums)
        if gaps:
            warnings.append(_issue("numbering_gap", rel, celex, "gaps in article numbering: " + ", ".join(f"{a}->{b}" for a, b in gaps[:10])))
        if size > LARGE_FILE_BYTES:
            warnings.append(_issue("large_file", rel, celex, f"{size} bytes, above {LARGE_FILE_BYTES} (an article or annex that cannot be split)"))
        if section:
            if meta.get("type") != TYPE_DIRECTIVE:
                warnings.append(_issue("transposition_in_regulation", rel, celex, "only directives have a transposition section"))
            for m in re.finditer(r"\(id: ([a-z0-9-]+)", section):
                if pt_ids is not None and m.group(1) not in pt_ids:
                    errors.append(_issue("invented_transposition_id", rel, celex, f"id {m.group(1)!r} is not in the Portuguese repo"))

    for celex, group in by_celex.items():
        seen = {}
        for rel, meta in group:
            key = meta.get("part") or ""
            if key in seen:
                errors.append(_issue("duplicate_celex", rel, celex, f"celex {celex} (part {key!r}) is also used by {seen[key]}"))
            else:
                seen[key] = rel

    # parts: each part belongs to an existing overview, the overview lists exactly its parts, with the right ranges
    nums_by_rel = {rel: nums for rel, _, nums, *_ in files}
    by_rel = {rel: (meta, ovb) for rel, meta, _, _, ovb, *_ in files}
    parts_of = {}
    for rel, meta, *_ in files:
        po = meta.get("part_of")
        if not po:
            continue
        parts_of.setdefault(po, []).append(meta["id"])
        if po not in ids:
            errors.append(_issue("bad_part", rel, str(meta.get("celex")), f"overview {po!r} does not exist"))
        if not str(meta.get("id", "")).startswith(po + "-"):
            errors.append(_issue("bad_part", rel, str(meta.get("celex")), "part id must be the act id followed by the part name"))
    for po, pids in parts_of.items():
        if po not in ids:
            continue
        ov_meta, ov_body = by_rel[ids[po]]
        listed = [Path(m.group(1)).stem for m in re.finditer(r"^\|[^|\n]*\|\s*([^|\n]+?\.md)\s*\|", ov_body, re.M)]
        if sorted(listed) != sorted(pids):
            errors.append(_issue("overview_incomplete", ids[po], str(ov_meta.get("celex")),
                                 "overview does not list exactly its parts: expected " + ", ".join(sorted(pids))))
        for row in ROW_RE.finditer(ov_body):
            path, a0, a1 = row.group(2).strip(), row.group(3).strip(), row.group(4).strip()
            if path in nums_by_rel:
                got = nums_by_rel[path]
                if (a0, a1) != ((got[0], got[-1]) if got else ("", "")):
                    errors.append(_issue("overview_range_mismatch", ids[po], str(ov_meta.get("celex")),
                                         f"{path}: table says {a0!r} to {a1!r}, the file has {got[:1]} to {got[-1:]}"))

    # counts against the XHTML itself (sum over the parts of an act)
    got_art, got_rec = {}, {}
    for rel, meta, nums, _, _, _, rec, *_ in files:
        c = str(meta.get("celex"))
        got_art[c] = got_art.get(c, 0) + len(nums)
        got_rec[c] = got_rec.get(c, 0) + rec
    for celex, group in by_celex.items():
        exp = (expected or {}).get(celex)
        if not exp:
            continue
        if got_art[celex] < exp["articles"]:
            errors.append(_issue("article_count_mismatch", group[0][0], celex,
                                 f"file has {got_art[celex]} articles, the XHTML has {exp['articles']}"))
        elif got_art[celex] > exp["articles"]:  # e.g. an agreement annexed to a regulation has articles without ids
            warnings.append(_issue("article_count_excess", group[0][0], celex,
                                   f"file has {got_art[celex]} articles, the XHTML ids count {exp['articles']}"))
        if exp.get("kind") == "original" and exp["recitals"] and got_rec[celex] < exp["recitals"]:
            errors.append(_issue("recitals_missing", group[0][0], celex,
                                 f"file has {got_rec[celex]} recitals, the XHTML has {exp['recitals']}"))
        if not exp["articles"]:
            warnings.append(_issue("no_articles", group[0][0], celex, "the act has no articles (running text only)"))
    for celex, group in by_celex.items():
        if got_art[celex] == 0 and not (expected or {}).get(celex):
            warnings.append(_issue("no_articles", group[0][0], celex, "the act has no articles (running text only)"))
    return errors, warnings


def expected_from_raw(raw_dir):
    """{celex: {"articles", "recitals", "kind"}} counted on the raw XHTML when each record was downloaded."""
    p = Path(raw_dir) / "index.json"
    if not p.exists():
        return {}
    return {k: v["counts"] for k, v in json.loads(p.read_text(encoding="utf-8")).items() if v.get("counts")}


def load_pt_ids(config):
    p = Path(config) / "pt-ids.txt" if config else None
    if not p or not p.exists():
        return None
    return {ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Validate generated EU act files (blocking errors, numbering warnings).")
    ap.add_argument("--root", required=True, help="tree to validate (staging directory or repo)")
    ap.add_argument("--raw", default=None, help="raw cache: enables the article and recital count checks against the XHTML")
    ap.add_argument("--config", default=None, help="config directory with pt-ids.txt (checks the transposition ids)")
    ap.add_argument("--json", default=None, help="write the error and warning lists here")
    a = ap.parse_args(argv)
    errors, warnings = validate(a.root, expected_from_raw(a.raw) if a.raw else None, load_pt_ids(a.config))
    if a.json:
        Path(a.json).write_text(json.dumps({"errors": errors, "warnings": warnings}, ensure_ascii=False, indent=1), encoding="utf-8")
    for e in errors:
        print(f"ERROR   {e['code']}: {e['file']}: {e['message']}", file=sys.stderr)
    for w in warnings:
        print(f"warning {w['code']}: {w['file']}: {w['message']}", file=sys.stderr)
    print(f"{len(errors)} errors, {len(warnings)} warnings", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
