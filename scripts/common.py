"""Shared constants and helpers for the ue-pt pipeline (standard library only)."""
import json
import re
from pathlib import Path

VERSION = "0.1"
REPO_URL = "https://github.com/LawAgents/ue-pt"
USER_AGENT = f"LawAgents-ue/{VERSION} (+{REPO_URL})"

# Fixed notices (EU-LAW.xml eu.str.legal_notice / eu.str.original_notice; pt-PT on purpose: data shown to users).
# Body of an article the source prints without any text ("Não utilizado.", "Não reproduzido."), so it is not mistaken for lost text.
EMPTY_MARK = "*(Sem texto)*"
LEGAL_NOTICE = ("Texto sem valor legal: só o Jornal Oficial da União Europeia faz fé. Confirma no EUR-Lex antes de o "
                "usares. Não substitui aconselhamento jurídico.")
ORIGINAL_NOTICE = "Texto original, sem consolidação: pode ter sido alterado depois."

STATUS_IN_FORCE = "em vigor"
TEXT_CONSOLIDATED = "consolidado"
TEXT_ORIGINAL = "original sem consolidação"
TYPE_REGULATION, TYPE_DIRECTIVE = "Regulamento", "Diretiva"
TYPES = (TYPE_REGULATION, TYPE_DIRECTIVE)
TYPE_DIRS = {TYPE_REGULATION: "regulamentos", TYPE_DIRECTIVE: "diretivas"}
TYPE_ID_PREFIX = {TYPE_REGULATION: "regulamento-ue", TYPE_DIRECTIVE: "diretiva-ue"}
OWNED_DIRS = sorted(TYPE_DIRS.values())
ROOT_INDEX = re.compile(r"^(nomes-comuns|indice(-.*)?|revogados)\.md$")

# Front matter fields in file order (EU-LAW.xml eu.schema).
FIELDS = ["id", "celex", "title", "type", "number", "year", "date", "status", "text_version", "last_amended",
          "consolidated_celex", "source", "eli", "retrieved", "summary", "legal_notice", "part_of", "part"]
REQUIRED = ["id", "celex", "title", "type", "number", "year", "date", "status", "text_version", "source", "retrieved",
            "legal_notice"]
DATE_FIELDS = {"date", "last_amended", "retrieved"}
INT_FIELDS = {"year"}
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BASE_CELEX = re.compile(r"^3(\d{4})([RL])(\d{4})$")


def format_frontmatter(meta):
    """Flat `key: value` lines; strings JSON-quoted (valid YAML), dates bare ISO, year an integer."""
    lines = ["---"]
    for k in FIELDS:
        v = meta.get(k)
        if v is None or v == "":
            continue
        if k in INT_FIELDS:
            lines.append(f"{k}: {int(v)}")
        elif k in DATE_FIELDS:
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {json.dumps(str(v), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def parse_frontmatter(text):
    """Return (dict, body). Raises ValueError when there is no well-formed front matter."""
    if not text.startswith("---\n"):
        raise ValueError("missing front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        if text.endswith("\n---"):
            end = len(text) - 4
        else:
            raise ValueError("unterminated front matter")
    meta = {}
    for ln in text[4:end].split("\n"):
        if not ln.strip():
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", ln)
        if not m:
            raise ValueError(f"bad front matter line: {ln!r}")
        k, v = m.group(1), m.group(2).strip()
        if v.startswith('"'):
            v = json.loads(v)
        elif re.fullmatch(r"-?\d+", v):
            v = int(v)
        meta[k] = v
    return meta, text[end + 5:]


def read_frontmatter(path):
    """Front matter of a file reading only its head (the files can be large)."""
    with open(path, "r", encoding="utf-8") as fh:
        head = fh.read(8192)
    return parse_frontmatter(head if "\n---\n" in head else Path(path).read_text(encoding="utf-8"))[0]


def split_articles(body):
    """List of (heading_text, body_text) for every article heading in a markdown body.

    An article ends at the next heading of any level (constraint.article_heading)."""
    heads = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"^#{1,6}[ \t].*$", body, re.M)]
    out = []
    for i, (s, e, line) in enumerate(heads):
        text = line.lstrip("#").strip()
        if not re.match(r"^Artigo\s", text):
            continue
        nxt = heads[i + 1][0] if i + 1 < len(heads) else len(body)
        out.append((text, body[e:nxt].strip()))
    return out


def article_number(heading_text):
    """'Artigo 17.º — Epígrafe' -> '17.º'. None when the heading is not an article heading."""
    m = re.match(r"^Artigo\s+(\S+)", heading_text)
    return m.group(1).rstrip("—-–:") if m else None


def atomic_write(path, data, binary=False):
    """Write via tmp + rename so a reader never sees a partial file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    if binary:
        tmp.write_bytes(data)
    else:
        tmp.write_text(data, encoding="utf-8", newline="\n")
    tmp.replace(path)


def iter_owned_files(root):
    """Every markdown file of the pipeline-owned folders under root, sorted."""
    root = Path(root)
    for d in OWNED_DIRS:
        if (root / d).is_dir():
            yield from sorted((root / d).rglob("*.md"))


def main_files(root):
    """Front matter dicts (plus 'path') of the main/overview files, i.e. those that are not a part of another file."""
    out = []
    for p in iter_owned_files(root):
        try:
            meta = read_frontmatter(p)
        except (ValueError, OSError):
            continue
        if not meta.get("part_of"):
            meta["path"] = Path(p).relative_to(root).as_posix()
            out.append(meta)
    return out


def act_id(celex):
    """regulamento-ue-AAAA-N / diretiva-ue-AAAA-N from a base CELEX such as 32016R0679; None for other CELEX numbers."""
    m = BASE_CELEX.match(celex or "")
    if not m:
        return None
    year, kind, n = m.group(1), m.group(2), int(m.group(3))
    return f"{TYPE_ID_PREFIX[TYPE_REGULATION if kind == 'R' else TYPE_DIRECTIVE]}-{year}-{n}"


def act_number(celex):
    """Official number: 'AAAA/N' for directives and for regulations from 2015, 'N/AAAA' for older regulations."""
    m = BASE_CELEX.match(celex or "")
    year, kind, n = m.group(1), m.group(2), int(m.group(3))
    return f"{year}/{n}" if kind == "L" or int(year) >= 2015 else f"{n}/{year}"
