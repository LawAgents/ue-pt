#!/usr/bin/env python3
"""Convert the raw cache (fetch.py) into markdown files in the repo layout.

  python scripts/convert.py --raw DIR --out DIR [--repo DIR] [--config DIR] [--max-part-kb 70]

Layout (EU-LAW.xml eu.schema.layout):
  regulamentos/2016/regulamento-ue-2016-679.md          one file per act
  diretivas/2019/diretiva-ue-2019-790/{id}.md + {id}-{part}.md    an act split into parts: overview + one file per part
Article headings: `## Artigo 17.º — Epígrafe` (any depth # to ######). Recitals only for originals, under
`## Considerandos`; annexes as `## Anexo X`. A file passing --max-part-kb, or repeating article numbers, is split
by its structure (Capítulo, Secção... then between articles, never inside an article).
"""
import argparse
import gzip
import json
import re
import shutil
import sys
import unicodedata
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import xhtml  # noqa: E402
from common import (EMPTY_MARK, LEGAL_NOTICE, OWNED_DIRS, STATUS_IN_FORCE, TEXT_CONSOLIDATED, TEXT_ORIGINAL, TYPE_DIRS,  # noqa: E402
                    TYPE_DIRECTIVE, TYPE_REGULATION, act_id, act_number, article_number, atomic_write,
                    format_frontmatter, read_frontmatter, BASE_CELEX)

DEFAULT_MAX_PART_BYTES = 70 * 1024  # readers (Read/WebFetch) cut files at about 100 KB
OUTLINE_MAX_BYTES = 45_000
TRANSPOSITION_HEADING = "## Transposição para Portugal"
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
          "novembro", "dezembro"]
DIVISION_ORDER = ["PARTE", "LIVRO", "TÍTULO", "CAPÍTULO", "SECÇÃO", "SUBSECÇÃO"]
KEYWORD = re.compile(r"^(PARTE|LIVRO|TÍTULO|CAPÍTULO|SECÇÃO|SUBSECÇÃO|ANEXO)\b", re.I)

K_ARTICLE, K_HEADING, K_RECITAL, K_TEXT, K_FINAL = "article", "heading", "recital", "text", "final"


def slug(s, maxlen=90):
    s = re.sub(r"[ºª°]", "", s)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:maxlen].rstrip("-")


def normalize_keyword(text):
    """'CAPÍTULO II' -> 'Capítulo II' (the keyword capitalised, the rest as written)."""
    return KEYWORD.sub(lambda m: m.group(1).capitalize(), re.sub(r"\s+", " ", text).strip(), count=1)


# ---- items ------------------------------------------------------------------------------------------------

class Item:
    """One block of the act: a heading (optional) with its text, at a structure level."""
    __slots__ = ("level", "tipo", "label", "tituo", "md", "art", "size")

    def __init__(self, level, tipo, label, tituo, md):
        self.level, self.tipo, self.label, self.tituo, self.md = level, tipo, label, tituo, md
        self.art = article_number(label) if tipo == K_ARTICLE and label.startswith("Artigo ") else None
        self.size = len(md.encode("utf-8")) + 2


class _Draft:
    def __init__(self, level, tipo, label="", tituo="", heading=False):
        self.level, self.tipo, self.label, self.tituo, self.heading = level, tipo, label, tituo, heading
        self.body = []

    def item(self):
        parts = []
        if self.heading and self.label:
            parts.append("#" * min(self.level + 1, 6) + " " + self.label)
        if self.body:
            parts.append("\n\n".join(self.body))
        elif self.tipo == K_ARTICLE and self.heading:
            parts.append(EMPTY_MARK)   # the source prints the article with no text ("Não utilizado.", "Não reproduzido.")
        return Item(self.level, self.tipo, self.label, self.tituo or self.label, "\n\n".join(parts))


def division_levels(events):
    """Level of each division keyword (TÍTULO, CAPÍTULO...): its rank among the keywords this act really uses."""
    seen = []
    for e in events:
        if e[0] == "div1":
            m = KEYWORD.match(e[1])
            kw = m.group(1).upper() if m else "?"
            if kw not in seen and kw != "ANEXO":
                seen.append(kw)
    order = list(seen)
    seen.sort(key=lambda k: (DIVISION_ORDER.index(k) if k in DIVISION_ORDER else len(DIVISION_ORDER), order.index(k)))
    return {k: i + 1 for i, k in enumerate(seen)}


def build_items(events):
    """Event list (xhtml.events) -> list of Item."""
    structural = {"div1", "article", "annex", "recital", "pbl", "enc"}
    has_structure = any(e[0] in structural for e in events)
    levels = division_levels(events)
    drafts, open_level = [], 0
    started = not has_structure
    in_recitals = in_annex = False
    final_mode = False
    skip_text = None
    final_adopt = False   # the last article is empty and its text sits in the closing block (before "Feito em ...")

    def cur():
        return drafts[-1] if drafts else None

    def add_text(s):
        nonlocal final_mode
        d = cur()
        if final_mode and (d is None or d.tipo != K_FINAL):
            d = _Draft(1, K_FINAL, "Assinatura", "Assinatura", True)
            drafts.append(d)
        if d is None:
            d = _Draft(0, K_TEXT)
            drafts.append(d)
        d.body.append(s)

    for e in events:
        kind = e[0]
        if kind not in ("text", "final"):
            final_adopt = False
        if kind in structural or kind in ("final", "annex_name", "div2", "epigraph"):
            started = True
        if kind == "pbl":
            in_recitals, open_level = True, 1
            drafts.append(_Draft(1, K_HEADING, "Considerandos", "Considerandos", True))
            final_mode = False
        elif kind == "recital":
            n, text = e[1], e[2]
            d = _Draft(2, K_RECITAL, f"Considerando {n}", f"Considerando {n}", False)
            d.body.append(text)
            drafts.append(d)
        elif kind == "enc":
            in_recitals, open_level, final_mode = False, 0, False
        elif kind == "anx_start":
            in_annex = True
        elif kind == "div1":
            in_recitals = final_mode = False
            text = normalize_keyword(e[1])
            km = KEYWORD.match(text)
            kw = km.group(1).upper() if km else "?"
            if kw == "ANEXO":
                level, in_annex = 1, True
            else:
                level = levels.get(kw, 1) + (1 if in_annex else 0)
            open_level = level
            drafts.append(_Draft(level, K_HEADING, text, text, True))
        elif kind == "div2":
            d = cur()
            if d is not None and d.tipo == K_HEADING and d.heading and not d.body and " — " not in d.label:
                d.label = f"{d.label} — {e[1]}"
            else:
                add_text(f"**{e[1]}**")
        elif kind == "annex":
            in_recitals = final_mode = False
            text = normalize_keyword(e[1])
            in_annex, open_level = True, 1
            drafts.append(_Draft(1, K_HEADING, text, re.split(r" — ", text)[0], True))
            skip_text = e[1]
        elif kind == "annex_name":
            d = cur()
            if d is not None and d.tipo == K_HEADING and d.level == 1 and " — " not in d.label and not d.body:
                d.label = f"{d.label} — {e[1]}"
            else:
                add_text(f"**{e[1]}**")
        elif kind == "article":
            if in_recitals:
                open_level = 0
            in_recitals = final_mode = False
            drafts.append(_Draft(open_level + 1, K_ARTICLE, e[1], e[1], True))
        elif kind == "epigraph":
            d = cur()
            if d is not None and d.tipo == K_ARTICLE and " — " not in d.label:
                d.label = f"{d.label} — {e[1]}"
            else:
                add_text(e[1])
        elif kind == "final":
            in_recitals = False
            final_mode = True
            final_adopt = cur() is not None and cur().tipo == K_ARTICLE and not cur().body
        elif kind == "text":
            if not started:
                continue
            if final_adopt:   # ponytail: stops at "Feito em/no ..."; an act without that line keeps its signatories in the article
                if not re.match(r"Feito\s+(em|no|na|nos|nas)\b", e[1]):
                    cur().body.append(e[1])
                    continue
                final_adopt = False
            if skip_text is not None:
                same = e[1].strip("* ").lower() == skip_text.strip().lower()
                skip_text = None
                if same:
                    continue
            add_text(e[1])
    if not any(d.tipo != K_TEXT or d.body for d in drafts):
        return []
    return [d.item() for d in drafts]


# ---- splitting into parts (same algorithm as the Portuguese repo, without the approval-decree rule) ---------------

def split_units(items, level):
    """Cut `items` into units that start at an item of exactly `level`; lower-level lead items join the first."""
    units, cur, lead = [], None, []
    for it in items:
        if it.level == level:
            cur = [it]
            units.append(cur)
        elif cur is None:
            lead.append(it)
        else:
            cur.append(it)
    if lead:
        if units:
            units[0] = lead + units[0]
        else:
            units = [lead]
    return units


class Unit:
    """A run of consecutive items cut at one level: the atom that parts are packed from."""
    __slots__ = ("items", "level", "prefix", "size", "nums")

    def __init__(self, items, level, prefix=""):
        self.items, self.level, self.prefix = items, level, prefix
        self.size = sum(i.size for i in items)
        self.nums = [i.art for i in items if i.art]

    def head(self):
        for i in self.items:
            if i.level == self.level and i.label:
                return i
        return next((i for i in self.items if i.label), None)

    def name(self):
        h = self.head()
        if h is None:
            return ""
        if h.art is not None:
            return f"Artigo {h.art}"
        return h.tituo or h.label

    def end_label(self):
        return f"{self.prefix}, {self.name()}" if self.prefix and self.name() else (self.name() or self.prefix)


def pack(items, max_bytes):
    """Greedy packing of top-level units into parts; a part closes before it passes `max_bytes` or repeats an article
    number. Oversized units are opened level by level, down to single articles. Returns a list of parts (lists of Unit)."""
    base = min((i.level for i in items if i.level > 0), default=1)
    queue = deque(Unit(u, base) for u in split_units(items, base))
    parts, cur, nums, size = [], [], set(), 0
    while queue:
        u = queue.popleft()
        if u.size > max_bytes:
            sub, lv = None, None
            for lv in sorted({i.level for i in u.items[1:] if i.level > u.level}):
                sub = split_units(u.items, lv)
                if len(sub) > 1:
                    break
            if sub and len(sub) > 1:
                parent = u.head()
                own = parent.tituo if parent is not None else ""
                prefix = ", ".join(x for x in (u.prefix, own) if x)
                queue.extendleft(Unit(s, lv, prefix) for s in reversed(sub))
                continue
        clash = bool(set(u.nums) & nums) or len(set(u.nums)) != len(u.nums)
        if cur and (clash or size + u.size > max_bytes):
            parts.append(cur)
            cur, nums, size = [], set(), 0
        cur.append(u)
        nums |= set(u.nums)
        size += u.size
    parts.append(cur)
    return parts


def fit(name, limit=90):
    """Cut a long part title at a ', ' boundary (never mid-word) and mark the cut with an ellipsis."""
    name = name.strip()
    if len(name) <= limit:
        return name
    cut = name.rfind(", ", 0, limit - 1)
    if cut > 0:
        return name[:cut] + "…"
    cut = name.rfind(" ", 0, limit - 1)
    return name[:cut if cut > 0 else limit - 1] + "…"


def part_title(units):
    first, last = units[0], units[-1]
    if all(u.head() is not None and u.head().art is not None for u in units):
        arts = [u.head().art for u in units]
        pre = first.prefix + ", " if first.prefix else ""
        return fit(f"{pre}Artigo {arts[0]}" if len(arts) == 1 else f"{pre}Artigos {arts[0]} a {arts[-1]}")
    if len(units) == 1 or first.end_label() == last.end_label():
        name = first.end_label()
    else:
        c1 = [s for s in first.prefix.split(", ") if s] + [first.name()]
        c2 = [s for s in last.prefix.split(", ") if s] + [last.name()]
        common = 0
        while common < len(c1) - 1 and common < len(c2) - 1 and c1[common] == c2[common]:
            common += 1
        name = f"{', '.join(c1)} a {', '.join(c2[common:])}"
    return fit(name or "Texto")


def split_parts(items, max_bytes):
    """Returns [(title, items)]; one element means the act stays in one file."""
    packed = pack(items, max_bytes)
    if len(packed) == 1:
        return [("", [i for u in packed[0] for i in u.items])]
    out, seen = [], {}
    for p in packed:
        t = part_title(p).replace("|", "/")
        s = slug(t, 60) or "parte"
        seen[s] = seen.get(s, 0) + 1
        if seen[s] > 1:
            t = f"{t} ({seen[s]})"
        out.append((t, [i for u in p for i in u.items]))
    return out


def assemble(items):
    return "\n\n".join(i.md for i in items if i.md)


def outline(parts, max_depth=4):
    """Non-article headings in order as a nested bullet list with the part file of each. parts: [(file name, items)]."""
    heads = [(i, name) for name, its in parts for i in its if i.label and i.art is None and i.tipo in (K_HEADING, K_FINAL)]
    if not heads:
        return []
    base = min(i.level for i, _ in heads)
    return [f"{'  ' * (i.level - base)}- {i.label} ({name})" for i, name in heads if i.level - base < max_depth]


# ---- transposition ----------------------------------------------------------------------------------------------

def clean_measure_number(local, date):
    """('Decreto-Lei n.º 47/2023', '2023-06-19') -> ('47', 2023, '2023'): number, year, year as written. Free text is parsed
    leniently; None when there is no number."""
    s = (local or "").strip()
    m = re.search(r"(\d+(?:-[A-Za-z]{1,2})?)\s*/\s*(\d{2,4})", s)
    if m:
        n, y = m.group(1), m.group(2)
        raw_y = y
        if len(y) == 2:
            y = ("19" if int(y) >= 40 else "20") + y
        return n.lower(), int(y), raw_y
    m = re.search(r"\b(\d+(?:-[A-Za-z]{1,2})?)\b", s)
    if m and re.match(r"^\d{4}", date or ""):
        return m.group(1).lower(), int(date[:4]), date[:4]
    return None


def type_slug(type_act):
    s = unicodedata.normalize("NFKD", type_act or "").encode("ascii", "ignore").decode().lower()
    return "-".join(w for w in re.split(r"[^a-z0-9]+", s) if w and w not in {"de", "do", "da", "dos", "das"})


def transposition_lines(measures, pt_ids):
    """Lines '- {title} (id: {id}; fonte: {link})' for the Portuguese measures of a directive. The id is written only
    when the act exists in the Portuguese repo (type + number + year); the link only when the Publications Office gave
    one. Nothing is invented. measures: list of dicts (type, local, date, ojn, eli)."""
    out, seen = [], set()
    for m in sorted(measures, key=lambda m: (m.get("date") or "", m.get("local") or "", m.get("nc") or "")):
        typ, local, date = (m.get("type") or "").strip(), (m.get("local") or "").strip(), (m.get("date") or "")[:10]
        num = clean_measure_number(local, date)
        pid = f"{type_slug(typ)}-{num[0]}-{num[1]}" if typ and num else None
        pid = pid if pid in pt_ids else None
        if not num and not (m.get("eli") or "").startswith("http"):
            continue   # nothing identifies the measure (no number, no link): not listed
        if typ and num:
            title = f"{typ} n.º {num[0].upper()}/{num[2]}"
        else:
            title = " ".join(x for x in (typ, local) if x) or (m.get("nc") or "medida nacional")
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            y, mo, d = (int(x) for x in date.split("-"))
            title += f", de {d} de {MONTHS[mo - 1]} de {y}"
        extra = []
        if pid:
            extra.append(f"id: {pid}")
        if (m.get("eli") or "").startswith("http"):
            extra.append(f"fonte: {m['eli']}")
        line = f"- {title}" + (f" ({'; '.join(extra)})" if extra else "")
        if line not in seen:
            seen.add(line)
            out.append(line)
    return out


def transposition_section(lines):
    return (TRANSPOSITION_HEADING + "\n\n" + "\n".join(lines) + "\n") if lines else ""


def with_transposition(text, section):
    """Replace (or add, or remove) the transposition section at the end of a main file."""
    i = text.find("\n" + TRANSPOSITION_HEADING)
    base = text if i < 0 else text[:i + 1]
    base = base.rstrip("\n") + "\n"
    return base + ("\n" + section if section else "")


# ---- one act -------------------------------------------------------------------------------------------------------

class Act:
    def __init__(self, celex, act_id_, files, parts, oversize):
        self.celex, self.id, self.files, self.parts, self.oversize = celex, act_id_, files, parts, oversize


def doc_title(text):
    """Fallback title from the first title lines of the XHTML."""
    root = xhtml.parse(text)
    lines = []
    for p in root.iter():
        if p.tag == "p" and p.classes & {"title-doc-first", "oj-doc-ti"}:
            t = xhtml.inline(p)
            if t and t not in lines:
                lines.append(t)
        if len(lines) >= 3:
            break
    return " ".join(lines)


def long_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} de {MONTHS[m - 1]} de {y}"


def convert_act(entry, rec, measures=(), pt_ids=frozenset(), max_bytes=DEFAULT_MAX_PART_BYTES):
    """entry: plan entry (celex, type, date, title, eli, kind, doc, cons_date); rec: raw record with the xhtml text."""
    celex = entry["celex"]
    aid = act_id(celex)
    if not aid:
        raise ValueError(f"CELEX {celex} is not a base regulation or directive number")
    text = rec["xhtml"]
    items = build_items(xhtml.events(text))
    if not items:
        raise ValueError("no text found in the XHTML")
    typ = TYPE_REGULATION if BASE_CELEX.match(celex).group(2) == "R" else TYPE_DIRECTIVE
    year = int(BASE_CELEX.match(celex).group(1))
    consolidated = rec["kind"] == "consolidated"
    title = (entry.get("title") or "").strip() or doc_title(text) or f"{typ} {act_number(celex)}"
    meta = {
        "id": aid, "celex": celex, "title": title, "type": typ, "number": act_number(celex), "year": year,
        "date": entry.get("date") or "", "status": STATUS_IN_FORCE,
        "text_version": TEXT_CONSOLIDATED if consolidated else TEXT_ORIGINAL,
        "last_amended": rec.get("cons_date") or "" if consolidated else "",
        "consolidated_celex": rec["doc"] if consolidated else "",
        "source": f"https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:{rec['doc']}",
        "eli": entry.get("eli") or "", "retrieved": (rec.get("fetched") or "")[:10], "summary": "",
        "legal_notice": LEGAL_NOTICE,
    }
    section = transposition_section(transposition_lines(measures, pt_ids)) if typ == TYPE_DIRECTIVE else ""
    parts = split_parts(items, max_bytes)
    base_dir = f"{TYPE_DIRS[typ]}/{year}"
    oversize = [(aid, i.label or i.tituo, i.size) for i in items if i.size > max_bytes]
    files = []
    if len(parts) == 1:
        body = assemble(parts[0][1])
        txt = format_frontmatter(meta) + f"\n\n# {title}\n\n" + (body + "\n" if body else "")
        if section:
            txt = with_transposition(txt, section)
        files.append((f"{base_dir}/{aid}.md", txt))
        return Act(celex, aid, files, [], oversize)
    multi = f"{base_dir}/{aid}"
    used, rows = set(), []
    for t, its in parts:
        pid = f"{aid}-{slug(t, 60) or 'parte'}"
        while pid in used:
            pid += "-2"
        used.add(pid)
        pmeta = dict(meta, id=pid, title=f"{title} — {t}", part_of=aid, part=t)
        body = assemble(its)
        files.append((f"{multi}/{pid}.md", format_frontmatter(pmeta) + f"\n\n# {pmeta['title']}\n\n" + (body + "\n" if body else "")))
        arts = [i.art for i in its if i.art]
        rows.append((t, f"{multi}/{pid}.md", arts[0] if arts else "", arts[-1] if arts else ""))
    ov = [f"# {title}", "",
          "Este ato está dividido em partes. Cada parte é um ficheiro; os números de artigo são únicos dentro de cada ficheiro.",
          "", "| parte | caminho | primeiro artigo | último artigo |", "|---|---|---|---|"]
    ov += [f"| {t} | {path} | {a0} | {a1} |" for t, path, a0, a1 in rows]
    for depth in (4, 3, 2, 1):
        out = outline([(Path(r[1]).name, its) for r, (_, its) in zip(rows, parts)], depth)
        if sum(len(x) + 1 for x in out) <= OUTLINE_MAX_BYTES:
            break
    if out:
        ov += ["", "## Estrutura", ""] + out
    txt = format_frontmatter(meta) + "\n\n" + "\n".join(ov) + "\n"
    if section:
        txt = with_transposition(txt, section)
    files.insert(0, (f"{multi}/{aid}.md", txt))
    return Act(celex, aid, files, [Path(r[1]).stem for r in rows], oversize)


# ---- driver ------------------------------------------------------------------------------------------------------------

def repo_acts(repo):
    """{celex: {"doc", "files": [rel...], "main": rel}} for the acts already in the repo (read from front matter)."""
    out = {}
    if not repo or not Path(repo).is_dir():
        return out
    for p in sorted(x for d in OWNED_DIRS for x in (Path(repo) / d).rglob("*.md")):
        try:
            meta = read_frontmatter(p)
        except (ValueError, OSError):
            continue
        rel = p.relative_to(repo).as_posix()
        a = out.setdefault(meta["celex"], {"doc": None, "files": [], "main": None})
        a["files"].append(rel)
        if not meta.get("part_of"):
            a["main"] = rel
            a["doc"] = meta.get("consolidated_celex") or meta["celex"]
    return out


def load_nim(raw_dir):
    """{directive celex: [measure dicts]} from the raw cache."""
    p = Path(raw_dir) / "nim.json"
    out = {}
    if p.exists():
        for r in json.loads(p.read_text(encoding="utf-8")):
            out.setdefault(r["dir"], []).append(r)
    return out


def load_pt_ids(config):
    p = Path(config) / "pt-ids.txt" if config else None
    if not p or not p.exists():
        return frozenset()
    return frozenset(ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#"))


def read_rec(raw_dir, celex):
    p = Path(raw_dir) / "json" / f"{celex}.json.gz"
    if not p.exists():
        return None
    with gzip.open(p, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def convert_all(raw_dir, out_dir, repo=None, config=None, max_bytes=DEFAULT_MAX_PART_BYTES,
                log=lambda m: print(m, file=sys.stderr)):
    """Convert every selected act of the plan. Acts with a raw record are converted; acts without one are copied from
    `repo` when it already holds the same document. Returns (acts, errors). Writes only inside out_dir."""
    raw, out = Path(raw_dir), Path(out_dir)
    plan = json.loads((raw / "plan.json").read_text(encoding="utf-8"))
    nim, pt_ids = load_nim(raw), load_pt_ids(config)
    have = repo_acts(repo)
    acts, errors = [], []
    for entry in sorted(plan["acts"], key=lambda e: e["celex"]):
        celex = entry["celex"]
        try:
            rec = read_rec(raw, celex)
            if rec and rec.get("xhtml") and rec.get("wanted") == entry["doc"]:
                act = convert_act(entry, rec, nim.get(celex, ()), pt_ids, max_bytes)
                for rel, text in act.files:
                    atomic_write(out / rel, text)
                act.files = [(rel, "") for rel, _ in act.files]
                acts.append(act)
            elif rec and rec.get("excluded"):
                continue
            elif celex in have and have[celex]["doc"] in (entry["doc"], rec and rec.get("doc")):
                is_dir = bool(BASE_CELEX.match(celex)) and BASE_CELEX.match(celex).group(2) == "L"
                section = transposition_section(transposition_lines(nim.get(celex, ()), pt_ids)) if is_dir else ""
                for rel in have[celex]["files"]:
                    text = (Path(repo) / rel).read_text(encoding="utf-8")
                    if is_dir and rel == have[celex]["main"]:
                        text = with_transposition(text, section)
                    atomic_write(out / rel, text)
                acts.append(Act(celex, act_id(celex), [(r, "") for r in have[celex]["files"]], [], []))
            else:
                errors.append({"celex": celex, "error": "convert: no raw record and the repo has no copy of this document"})
        except Exception as e:  # noqa: BLE001  one bad act must not hide the others
            errors.append({"celex": celex, "error": f"convert: {type(e).__name__}: {e}"})
    log(f"converted {len(acts)} acts, {len(errors)} errors")
    return acts, errors


def main(argv=None):
    ap = argparse.ArgumentParser(description="Convert the raw cache into markdown files.")
    ap.add_argument("--raw", required=True, help="raw cache directory written by fetch.py")
    ap.add_argument("--out", required=True, help="output directory (use an empty staging directory)")
    ap.add_argument("--repo", default=None, help="existing repo: acts without a raw record are copied from it")
    ap.add_argument("--config", default=None, help="config directory (pt-ids.txt for the transposition section)")
    ap.add_argument("--max-part-kb", type=int, default=DEFAULT_MAX_PART_BYTES // 1024, help="split files above this size")
    a = ap.parse_args(argv)
    shutil.rmtree(a.out, ignore_errors=True)
    _, errors = convert_all(a.raw, a.out, a.repo, a.config, a.max_part_kb * 1024)
    for e in errors:
        print(f"ERROR {e['celex']}: {e['error']}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
