"""Reader for the XHTML of EU legal acts (Publications Office, Cellar) built on html.parser from the standard library.

The XHTML comes in two families (EU measurements report):
  consolidated: p.title-article-norm + p.stitle-article-norm, chapters in p.title-division-1/2, annexes p.title-annex-1/2
  originals (about 2009 on): p.oj-ti-art + p.oj-sti-art, p.oj-ti-section-1/2, annexes under div#anx_N, recitals rct_N
Both carry div ids (art_N, rct_N, cpt_X, anx_N, pbl_1, enc_1); older consolidated texts have none, so the reader
works on the flat sequence of block elements and uses the ids only for counting.

events(text) returns a flat list of tuples:
  ("article", "Artigo 17.º")  ("epigraph", "Direito ...")  ("div1", "CAPÍTULO II")  ("div2", "Princípios")
  ("annex", "ANEXO I")  ("annex_name", "...")  ("pbl",)  ("recital", "12", "text")  ("enc",)  ("final",)
  ("text", "paragraph")
"""
import re
from html.parser import HTMLParser

VOID = {"br", "hr", "img", "col", "meta", "link", "input", "area", "base", "wbr"}
SKIP_TAGS = {"script", "style", "head", "title"}
# Header block of consolidated and original texts: title lines, modifiers, tables of contents, markers.
SKIP_P = {"reference", "disclaimer", "hd-modifiers", "title-doc-first", "title-doc-last", "title-doc-oj-reference",
          "title-fam-member", "title-fam-member-star", "arrow", "hd-column", "hd-toc-3", "toc-1", "toc-2", "toc-item",
          "oj-hd-date", "oj-hd-lg", "oj-hd-ti", "oj-hd-oj", "oj-hd-coll", "oj-hd-ti-1"}
ARTICLE_P = {"title-article-norm", "oj-ti-art"}
EPIGRAPH_P = {"stitle-article-norm", "oj-sti-art"}
DIV1_P = {"title-division-1", "oj-ti-section-1"}
DIV2_P = {"title-division-2", "oj-ti-section-2"}
ANNEX1_P = {"title-annex-1"}
ANNEX2_P = {"title-annex-2"}
BOLD_P = {"title-gr-seq-level-1", "title-gr-seq-level-2", "title-gr-seq-level-3", "oj-ti-grseq-1", "oj-ti-grseq-2",
          "oj-ti-grseq-3", "title-table", "oj-ti-tbl", "oj-ti-tbl-1", "title-gr-seq-level-4"}
# Heading of an article as the sources spell it: stray opening quote, "Article", typos ("Artigio", "Artigos") or no space
# before the number ("Artigo12.º").
ARTICLE_WORD = re.compile(r"(?i)art(?:icle|igio|igos|igo)(?=\W|\d|$)")
# Editorial markers of consolidated texts: start of an amended passage (►M1, ▼B, ►C2) and end (◄).
AMEND_MARK = re.compile(r"[►▼]\s?[A-Z]\d{0,3}[ \t]*|◄")
MARKER = re.compile(r"^[«“\"]?(?:\(?(?:[a-z]{1,3}|\d{1,3}|[ivxlc]{1,6}|[A-Z])\)|\(?\d{1,3}\.?\)?|[–—•·\-]|\d+\.\d+\.?)$", re.I)


class Node:
    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag, attrs=None):
        self.tag, self.attrs, self.children = tag, dict(attrs or {}), []

    @property
    def classes(self):
        return set((self.attrs.get("class") or "").split())

    @property
    def id(self):
        return self.attrs.get("id") or ""

    def nodes(self):
        return [c for c in self.children if isinstance(c, Node)]

    def iter(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.iter()


class _Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def parse(text):
    b = _Builder()
    b.feed(text)
    b.close()
    return b.root


def inline(node):
    """Visible text of a node: <br> is a newline, superscript 'o'/'a' after a number becomes º/ª, whitespace is collapsed."""
    out = []

    def walk(n):
        for c in n.children:
            if isinstance(c, str):
                out.append(c)
            elif c.tag == "br":
                out.append("\n")
            elif c.tag == "img":
                out.append(c.attrs.get("alt") or "")
            elif c.tag in SKIP_TAGS:
                continue
            elif c.classes & {"superscript", "oj-super"} and "oj-note-tag" not in c.classes:
                inner = inline(c).strip()
                prev = "".join(out)[-1:]
                if inner in ("o", "a", "os", "as") and (prev.isdigit() or prev == "."):
                    out.append({"o": "º", "a": "ª", "os": "ºs", "as": "ªs"}[inner])
                else:
                    out.append(inner)
            else:
                walk(c)
    walk(node)
    s = AMEND_MARK.sub("", "".join(out).replace("\xa0", " "))
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r" ?\n ?", "\n", s)
    return s.strip()


def article_label(text):
    """Heading of an article paragraph with the source's typos fixed ("Artigo ..."), or None when the paragraph carries the
    article class but is not an article (e.g. the table caption "Quadro 6:")."""
    t = re.sub(r"^[«“\"\s]+", "", text)
    m = ARTICLE_WORD.match(t)
    if not m:
        return None
    rest = t[m.end():]
    return "Artigo" + (" " if rest[:1].isdigit() else "") + rest


def escape_line(line):
    """A body line must never look like a heading or other block markup."""
    if re.match(r"^\s*(#|>|\+\s|\*|=+\s*$|-{3,}\s*$|_{3,}\s*$)", line):
        return "\\" + line.lstrip()
    return line


def clean_lines(text):
    return [escape_line(re.sub(r"\s+", " ", ln).strip()) for ln in text.split("\n") if ln.strip()]


# ---- tables -----------------------------------------------------------------------------------------

def _cells(tr):
    return [c for c in tr.nodes() if c.tag in ("td", "th")]


def _rows(table):
    rows = []
    for c in table.nodes():
        if c.tag == "tr":
            rows.append(c)
        elif c.tag in ("tbody", "thead", "tfoot"):
            rows += [r for r in c.nodes() if r.tag == "tr"]
    return rows


def cell_blocks(cell):
    """Text blocks of a table cell, using the same paragraph rules as the body (header classes dropped)."""
    out = []
    for kind, *rest in _blocks(cell, in_cell=True):
        if kind == "text":
            out.append(rest[0])
        elif kind == "bold":
            out.append(f"**{rest[0]}**")
    return out


def table_blocks(table):
    """Markdown for a table: a list when the first column holds list markers, a table otherwise (colspan cells are
    padded), one-line HTML when it has rowspan cells or nested tables."""
    rows = _rows(table)
    data, spans, rowspan = [], [], False
    for tr in rows:
        cells = _cells(tr)
        row, cols = [], []
        for c in cells:
            blocks = cell_blocks(c)
            n = int(c.attrs.get("colspan", "1") or 1) if (c.attrs.get("colspan", "1") or "1").isdigit() else 1
            rowspan = rowspan or ((c.attrs.get("rowspan", "1") or "1").isdigit() and int(c.attrs.get("rowspan", "1") or 1) > 1)
            row.append(blocks)
            cols.append(n)
        data.append(row)
        spans.append(cols)
    keep = [i for i, r in enumerate(data) if any(r)]
    data, spans = [data[i] for i in keep], [spans[i] for i in keep]
    if not data:
        return []
    nested = any(n.tag == "table" for n in table.iter() if n is not table)
    if not any(len(r) > 1 for r in data):
        return [ln for r in data for cell in r for ln in cell]          # layout table with a single column
    if not rowspan and all(len(r) == 2 for r in data) and all(sp == [1, 1] for sp in spans) and all(
            r[0] and len(r[0]) == 1 and MARKER.match(r[0][0].strip()) or not r[0] for r in data):
        out = []
        for r in data:
            first, rest = (r[0][0].strip() if r[0] else ""), r[1]
            if not rest:
                if first:
                    out.append(first)
                continue
            out.append((first + " " + rest[0]).strip())
            out += rest[1:]
        return out
    if rowspan or nested:   # a nested table inside a markdown cell cannot be shown: keep the structure as HTML
        return [re.sub(r"\s*\n\s*", " ", _html_of(table))]
    grid = []
    for r, sp in zip(data, spans):
        line = []
        for cell, n in zip(r, sp):
            line.append(" <br> ".join(cell).replace("|", "\\|"))
            line += [""] * (n - 1)
        grid.append(line)
    width = max(len(g) for g in grid)
    grid = [g + [""] * (width - len(g)) for g in grid]
    lines = ["| " + " | ".join(grid[0]) + " |", "|" + "---|" * width]
    lines += ["| " + " | ".join(g) + " |" for g in grid[1:]]
    return ["\n".join(lines)]


KEEP_TAGS = {"table", "tbody", "thead", "tfoot", "tr", "td", "th"}


def _html_of(n):
    """Compact HTML of a complex table: only table structure and text (superscripts and breaks resolved by inline())."""
    if isinstance(n, str):
        return n.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if n.tag in SKIP_TAGS or n.tag == "col":
        return ""
    if n.tag not in KEEP_TAGS:
        return _html_of(inline(n)) + (" " if n.tag == "p" else "")
    attrs = "".join(f' {k}="{v}"' for k, v in n.attrs.items() if k in ("rowspan", "colspan") and v not in ("", "1"))
    inner = "".join(_html_of(c) for c in n.children)
    inner = re.sub(r"\s+", " ", inner).strip() if n.tag in ("td", "th") else inner
    return f"<{n.tag}{attrs}>{inner}</{n.tag}>"


# ---- blocks and events ----------------------------------------------------------------------------------

BLOCK = {"p", "div", "table", "ul", "ol", "li", "hr", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "section", "center",
         "body", "html", "tr", "td", "th", "tbody", "thead"}
INLINE = {"span", "a", "sup", "sub", "b", "i", "em", "strong", "u", "br", "img", "small", "font", "abbr"}


def _blocks(node, in_cell=False):
    """Flat list of ("text", s) / ("bold", s) / (heading kind, ...) for the content of `node`. Text and inline elements
    sitting directly in a container form their own paragraph."""
    out, run = [], []

    def flush():
        if run:
            tmp = Node("span")
            tmp.children = list(run)
            for ln in clean_lines(inline(tmp)):
                out.append(("text", ln))
            run.clear()

    for c in node.children:
        if isinstance(c, str):
            run.append(c)
        elif c.tag in INLINE and not any(n.tag in BLOCK for n in c.iter()):
            run.append(c)
        else:
            flush()
            out.extend(_block(c, in_cell))
    flush()
    return out


def _block(el, in_cell=False):
    """Blocks of one element."""
    out = []
    tag, cl = el.tag, el.classes
    if tag in SKIP_TAGS or tag in ("hr", "col"):
        return out
    if tag == "p":
        if cl & SKIP_P:
            return out
        text = inline(el)
        if not text:
            return out
        if not in_cell:
            if cl & ARTICLE_P:
                label = article_label(re.sub(r"\s+", " ", text))
                out.append(("article", label) if label else ("bold", re.sub(r"\s+", " ", text)))
                return out
            if cl & EPIGRAPH_P:
                out.append(("epigraph", re.sub(r"\s+", " ", text)))
                return out
            if cl & DIV1_P:
                out.append(("div1", re.sub(r"\s+", " ", text)))
                return out
            if cl & DIV2_P:
                out.append(("div2", re.sub(r"\s+", " ", text)))
                return out
            if cl & ANNEX1_P:
                out.append(("annex", re.sub(r"\s+", " ", text)))
                return out
            if cl & ANNEX2_P:
                out.append(("annex_name", re.sub(r"\s+", " ", text)))
                return out
        if cl & BOLD_P:
            out.append(("bold", re.sub(r"\s+", " ", text)))
        else:
            for ln in clean_lines(text):
                out.append(("text", ln))
    elif tag == "table":
        for ln in table_blocks(el):
            for sub in ln.split("\n") if not ln.startswith("|") else [ln]:
                if sub.strip():
                    out.append(("text", sub if sub.startswith("|") else escape_line(sub)))
    elif "grid-container" in cl:                      # list item: marker column + text column
        kids = el.nodes()
        label = inline(kids[0]) if kids else ""
        body = [b for k in kids[1:] for b in _blocks(k, True) if b[0] in ("text", "bold")]
        first = True
        for kind, s in body:
            out.append(("text", (label + " " + s).strip() if first else s))
            first = False
        if not body and label:
            out.append(("text", label))
    elif tag == "div" and any(isinstance(c, Node) and c.tag == "span" and "no-parag" in c.classes for c in el.children):
        prefix = inline(next(c for c in el.nodes() if "no-parag" in c.classes))
        sub = _blocks(_strip(el), in_cell)
        if sub and sub[0][0] == "text":
            sub[0] = ("text", (prefix + " " + sub[0][1]).strip())
        else:
            sub.insert(0, ("text", prefix))
        out += sub
    elif tag in ("div", "span", "a", "ul", "ol", "li", "blockquote", "section", "body", "html", "center") and el.nodes():
        out += _marked(el, in_cell)
    elif tag in ("ul", "ol"):
        return out
    else:
        text = inline(el)
        if text:
            for ln in clean_lines(text):
                out.append(("text", ln))
    return out


def _strip(el):
    """Copy of `el` without its no-parag span."""
    n = Node(el.tag, el.attrs)
    n.children = [c for c in el.children if not (isinstance(c, Node) and "no-parag" in c.classes)]
    return n


def _marked(el, in_cell):
    """Recurse into a container, adding markers for the structural divs (ids pbl_1, rct_N, anx_N, enc_1, fnp_1)."""
    i = el.id
    if re.fullmatch(r"rct_\d+", i) and not in_cell:
        lines = [t for k, t in _blocks(el, True) if k == "text"]
        if lines:   # some sources print the marker as "5)" instead of "(5)"
            lines[0] = re.sub(rf"^\(?{i[4:]}\)\s*", f"({i[4:]}) ", lines[0]).rstrip()
        return [("recital", i[4:], "\n".join(lines))] if lines else []
    out = []
    if not in_cell:
        if i == "pbl_1":
            out.append(("pbl",))
        elif i == "enc_1":
            out.append(("enc",))
        elif re.fullmatch(r"anx_\w+", i):
            out.append(("anx_start", i))
        elif i == "fnp_1" or "oj-final" in el.classes:
            out.append(("final",))
    first_annex_title = bool(re.fullmatch(r"anx_\w+", i)) and not in_cell
    sub = _blocks(el, in_cell)
    if first_annex_title:
        # originals: the annex title is the first oj-doc-ti paragraph of div#anx_N
        for p in el.iter():
            if p.tag == "p" and "oj-doc-ti" in p.classes and inline(p):
                sub.insert(0, ("annex", inline(p)))
                break
    return out + sub


def events(text):
    """Flat event list of a document (see module docstring). Header blocks (title, disclaimer, ToC) are dropped."""
    root = parse(text)
    body = next((n for n in root.iter() if n.tag == "body"), root)
    ev = _blocks(body)
    out = []
    for e in ev:
        if e[0] == "bold":
            out.append(("text", f"**{e[1]}**"))
        else:
            out.append(e)
    return out


# ---- counting on the raw markup --------------------------------------------------------------------------

def scan_counts(text):
    """Counts taken straight from the XHTML, independent of the reader: article ids art_N, recital ids rct_N and
    article-title paragraphs."""
    art = {m for m in re.findall(r'\bid="(art_[0-9A-Za-z]+)"', text)}
    rct = {m for m in re.findall(r'\bid="(rct_[0-9]+)"', text)}
    titles = sum(1 for m in re.finditer(r'<p[^>]*class="(?:[^"]*\s)?(?:title-article-norm|oj-ti-art)(?:\s[^"]*)?"[^>]*>(.*?)</p>', text, re.S)
                 if article_label(inline(parse(m.group(1)))))   # a caption such as "Quadro 6:" is no article
    return {"articles": len(art) if art else titles, "article_ids": len(art), "article_titles": titles, "recitals": len(rct)}
