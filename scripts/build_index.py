#!/usr/bin/env python3
"""Generate the index files at the root of the repo tree (EU-LAW.xml eu.schema.index).

  python scripts/build_index.py --root DIR --config config [--raw DIR] [--repo DIR] [--revoked-new FILE]

Files written into DIR: nomes-comuns.md (from config/nomes-comuns.txt: `id | nome comum | sigla1, sigla2`, 30 to 50
entries, every id must exist), indice.md, indice-regulamentos[-<from>-<to>].md and indice-diretivas[-<from>-<to>].md
(each <= 40 KB; a year is never split, unless it alone passes 40 KB: then -<year>-a, -<year>-b) and revogados.md.
No theme index in the first version.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT_INDEX, atomic_write, main_files  # noqa: E402

MAX_INDEX_BYTES = 40 * 1024  # the Read tool of the agents cuts files at about 25k tokens
MAX_COMMON_NAMES_BYTES = 10 * 1024
COMMON_NAMES_RANGE = (30, 50)
SUMMARY_MAX = 160


def index_group(rel):
    """Index group of a repo path: the type folder."""
    return rel.split("/")[0]


class IndexError_(Exception):
    """Index cannot be generated (missing ids, oversize...). The message is human readable."""


def cell(s):
    return re.sub(r"\s+", " ", str(s or "")).replace("|", "\\|").strip()


def parse_lines(path, min_cells):
    """Lines `a | b | c`; blank lines and '#' comments are ignored."""
    rows = []
    for n, ln in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        cells = [c.strip() for c in ln.split("|")]
        if len(cells) < min_cells or not all(cells[:min_cells]):
            raise IndexError_(f"{path}:{n}: expected {min_cells} cells separated by '|'")
        rows.append((n, cells))
    return rows


def parse_common_names(path):
    """[(id, name, [acronyms])] from lines `id | common name | acronym1, acronym2`."""
    out = []
    for n, c in parse_lines(path, 2):
        out.append((c[0], c[1], [a.strip() for a in (c[2].split(",") if len(c) > 2 else []) if a.strip()]))
    return out


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def build_common_names(mains, entries, check_count=True):
    by_id = {m["id"]: m for m in mains}
    missing = [e[0] for e in entries if e[0] not in by_id]
    if missing:
        raise IndexError_("nomes-comuns.txt: ids that do not exist in the repo: " + ", ".join(missing))
    if check_count and not (COMMON_NAMES_RANGE[0] <= len(entries) <= COMMON_NAMES_RANGE[1]):
        raise IndexError_(f"nomes-comuns.txt has {len(entries)} entries; it must have {COMMON_NAMES_RANGE[0]} to "
                          f"{COMMON_NAMES_RANGE[1]}")
    text = "# Nomes comuns e siglas\n\n" + table(
        ["nome comum", "siglas", "id", "caminho"],
        [(n, ", ".join(a), i, by_id[i]["path"]) for i, n, a in entries])
    if len(text.encode("utf-8")) > MAX_COMMON_NAMES_BYTES:
        raise IndexError_("nomes-comuns.md would be larger than 10 KB")
    return text


def shard_group(group, rows, aliases):
    """Index file(s) of one type folder. rows: main-file metadata. Returns [(name, text, (y0, y1), n_rows, types)]."""
    base = "indice-" + group.replace("/", "-")
    rows = sorted(rows, key=lambda m: (int(m["year"]), m["id"]))
    headers = ["id", "título", "caminho", "nome comum", "siglas", "sumário", "source", "last_amended", "text_version"]

    def line(m):
        name, acr = aliases.get(m["id"], ("", []))
        s = m.get("summary") or ""
        if len(s) > SUMMARY_MAX:
            s = s[:SUMMARY_MAX - 1].rstrip() + "…"
        return [m["id"], m["title"], m["path"], name, ", ".join(acr), s, m.get("source", ""), m.get("last_amended", ""), m.get("text_version", "")]

    head = f"# Índice: {group}\n\n"
    lines = {i: table(headers, [line(m)]).split("\n", 2)[2] for i, m in enumerate(rows)}
    base_size = len((head + table(headers, [])).encode("utf-8"))
    # consecutive years packed up to the size limit; a year is never split
    by_year = {}
    for i, m in enumerate(rows):
        by_year.setdefault(int(m["year"]), []).append(i)
    # consecutive years packed up to the size limit; a year is never split, unless it alone passes the limit: then it
    # is cut by id order into <year>-a, <year>-b... files of their own
    chunks, cur, size = [], [], base_size   # chunk = (years, row indexes, suffix)
    for y in sorted(by_year):
        ysize = sum(len(lines[i].encode("utf-8")) for i in by_year[y])
        if ysize + base_size > MAX_INDEX_BYTES:
            if cur:
                chunks.append((cur, [i for yy in cur for i in by_year[yy]], ""))
                cur, size = [], base_size
            piece, psize, letters = [], base_size, iter("abcdefghijklmnopqrstuvwxyz")
            for i in by_year[y]:
                n = len(lines[i].encode("utf-8"))
                if piece and psize + n > MAX_INDEX_BYTES:
                    chunks.append(([y], piece, "-" + next(letters)))
                    piece, psize = [], base_size
                piece.append(i)
                psize += n
            chunks.append(([y], piece, "-" + next(letters)))
            continue
        if cur and size + ysize > MAX_INDEX_BYTES:
            chunks.append((cur, [i for yy in cur for i in by_year[yy]], ""))
            cur, size = [], base_size
        cur.append(y)
        size += ysize
    if cur:
        chunks.append((cur, [i for yy in cur for i in by_year[yy]], ""))
    out = []
    for ys, idx, sfx in chunks:
        if sfx:
            name = f"{base}-{ys[0]}{sfx}.md"
        else:
            name = base + (f"-{ys[0]}-{ys[-1]}" if len(chunks) > 1 else "") + ".md"
        text = head + table(headers, [line(rows[i]) for i in idx])
        types = sorted({rows[i]["type"] for i in idx})
        out.append((name, text, (ys[0], ys[-1]), len(idx), types))
    return out


def parse_revoked(path):
    rows = []
    p = Path(path)
    if not p.exists():
        return rows
    for ln in p.read_text(encoding="utf-8").splitlines():
        if not ln.startswith("|"):
            continue
        c = [x.strip().replace("\\|", "|") for x in re.split(r"(?<!\\)\|", ln.strip().strip("|"))]
        if len(c) == 4 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[2]):
            rows.append({"id": c[0], "title": c[1], "date": c[2], "source": c[3]})
    return rows


def build_revoked(existing, new, present_ids):
    """Merge previous rows and newly revoked acts; an act that is in force again leaves the list."""
    merged = {r["id"]: r for r in existing}
    merged.update({r["id"]: r for r in new})
    rows = [r for r in merged.values() if r["id"] not in present_ids]
    rows.sort(key=lambda r: r["id"])
    return "# Atos revogados\n\n" + table(["id", "título", "data do fim de vigência", "ligação oficial"],
                                              [(r["id"], r["title"], r["date"], r["source"]) for r in rows]), len(rows)


def build_all(root, config_dir, raw_dir=None, repo_dir=None, revoked_new=None, check_count=True):
    """Write every index file into root. Returns the list of written file names."""
    root, config = Path(root), Path(config_dir)
    mains = main_files(root)
    names_file = config / "nomes-comuns.txt"
    if not names_file.exists():
        raise IndexError_(f"{names_file} is missing (the hand-written list of common names is required)")
    entries = parse_common_names(names_file)
    aliases = {i: (n, a) for i, n, a in entries}
    for p in root.iterdir():
        if p.is_file() and ROOT_INDEX.match(p.name):
            p.unlink()
    written = {"nomes-comuns.md": build_common_names(mains, entries, check_count)}
    groups = {}
    for m in mains:
        groups.setdefault(index_group(m["path"]), []).append(m)
    manifest = []
    for g in sorted(groups):
        for name, text, (y0, y1), n, types in shard_group(g, groups[g], aliases):
            written[name] = text
            manifest.append((name, ", ".join(types), y0, y1, n))
    existing = parse_revoked((Path(repo_dir) / "revogados.md")) if repo_dir else []
    written["revogados.md"], _ = build_revoked(existing, revoked_new or [], {m["id"] for m in mains})
    manifest.sort()
    written["indice.md"] = "# Índice\n\n" + table(["ficheiro", "tipo", "ano inicial", "ano final", "n.º de atos"], manifest)
    for name, text in written.items():
        atomic_write(root / name, text)
    return sorted(written)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Generate the index files (nomes-comuns, indice, revogados).")
    ap.add_argument("--root", required=True, help="tree with the generated diploma files; index files are written here")
    ap.add_argument("--config", required=True, help="config directory (nomes-comuns.txt)")
    ap.add_argument("--raw", default=None, help="raw cache (accepted for the common CLI; not needed by the index)")
    ap.add_argument("--repo", default=None, help="current repo: its revogados.md rows are kept")
    ap.add_argument("--revoked-new", default=None, help="JSON list of newly revoked diplomas [{id,title,date,source}]")
    ap.add_argument("--no-count-check", action="store_true", help="accept a common-names list outside 30-50 entries")
    a = ap.parse_args(argv)
    new = json.loads(Path(a.revoked_new).read_text(encoding="utf-8")) if a.revoked_new else []
    try:
        names = build_all(a.root, a.config, a.raw, a.repo, new, not a.no_count_check)
    except IndexError_ as e:
        print(f"INDEX ERROR: {e}", file=sys.stderr)
        return 1
    print(f"{len(names)} index files written", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
