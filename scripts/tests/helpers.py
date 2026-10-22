"""Shared test helpers: fixtures, a fake clock and a simulated Publications Office (SPARQL + Cellar)."""
import json
import re
import shutil
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
REPO = SCRIPTS.parent
FIX = HERE / "fixtures"
sys.path.insert(0, str(SCRIPTS))

import cellar_client  # noqa: E402
import common  # noqa: E402

TODAY = "2026-10-22"


def xhtml_fixture(name):
    return (FIX / "xhtml" / name).read_text(encoding="utf-8")


class TmpCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ue-pt-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def config_dir(self, names="rgpd"):
        """Temp config: common names fixture and a Portuguese id list (a small one, with Decreto-Lei 47/2023)."""
        cfg = self.tmp / "config"
        cfg.mkdir(exist_ok=True)
        shutil.copy(FIX / "config" / "nomes-comuns.txt", cfg / "nomes-comuns.txt")
        (cfg / "pt-ids.txt").write_text("decreto-lei-47-2023\nlei-59-2019\nlei-34-2009\n", encoding="utf-8")
        return cfg

    def write_act(self, root, rel, meta, body):
        """Write an act file with a valid default front matter overridden by `meta` (None removes a field)."""
        m = {"id": "regulamento-ue-2016-679", "celex": "32016R0679", "title": "Regulamento (UE) 2016/679", "type": "Regulamento",
             "number": "2016/679", "year": 2016, "date": "2016-04-27", "status": common.STATUS_IN_FORCE,
             "text_version": common.TEXT_CONSOLIDATED, "last_amended": "2016-05-04",
             "consolidated_celex": "02016R0679-20160504",
             "source": "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02016R0679-20160504",
             "retrieved": "2026-10-22", "legal_notice": common.LEGAL_NOTICE}
        m.update(meta)
        text = common.format_frontmatter({k: v for k, v in m.items() if v is not None}) + "\n\n" + body
        p = Path(root) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
        return p


class FakeClock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self):
        return self.now

    def sleep(self, s):
        self.now += s


def row(**kw):
    return {k: v for k, v in kw.items() if v is not None}


class FakeEU:
    """Simulated Publications Office. `acts`: list of dicts {celex, rt, date, title, eli, cons: [(date, cc)], orig: bool,
    docs: {doc: xhtml}, nim: [dict]}. A document missing from `docs` answers 404."""

    def __init__(self, clock, latency=0.2):
        self.clock, self.latency = clock, latency
        self.acts = []
        self.log = []          # (start time, url, user agent, accept)
        self.fault = None      # callable(n, url) -> None | int HTTP status | "garbage" | "oserror"
        self.n = 0
        self.items = {}
        self.default_universe()

    def default_universe(self):
        gdpr = xhtml_fixture("gdpr-trimmed-consolidated.xhtml")
        self.acts = [
            {"celex": "32016R0679", "rt": "REG", "date": "2016-04-27", "title": "Regulamento (UE) 2016/679 (RGPD)", "eli": "http://data.europa.eu/eli/reg/2016/679/oj",
             "cons": [("2016-05-04", "02016R0679-20160504"), ("2027-01-01", "02016R0679-20270101")], "orig": False,
             "docs": {"02016R0679-20160504": gdpr}, "nim": []},
            {"celex": "32010R0265", "rt": "REG", "date": "2010-03-25", "title": "Regulamento (UE) n.º 265/2010", "eli": "",
             "cons": [("2016-04-12", "02010R0265-20160412")], "orig": False,
             "docs": {"02010R0265-20160412": xhtml_fixture("reg-consolidated-2010-265.xhtml")}, "nim": []},
            {"celex": "32009L0001", "rt": "DIR", "date": "2009-01-07", "title": "Diretiva 2009/1/CE da Comissão", "eli": "",
             "cons": [], "orig": True, "docs": {"32009L0001": xhtml_fixture("dir-original-2009-1.xhtml")},
             "nim": [row(nc="72009L0001PRT", dir="32009L0001", local="Decreto-Lei n.º 47/2023", type="Decreto-Lei", date="2023-06-19"),
                     row(nc="72009L0001PRT2", dir="32009L0001", local="59/2019", type="Lei", date="2019-08-08", eli="https://dre.pt/eli/lei/59/2019"),
                     row(nc="72009L0001PRT3", dir="32009L0001", local="999/2021", type="Portaria", date="2021-01-05")]},
            {"celex": "32022R1903", "rt": "REG", "date": "2022-10-06", "title": "Regulamento (UE) 2022/1903 do Conselho", "eli": "",
             "cons": [], "orig": True, "docs": {"32022R1903": xhtml_fixture("reg-original-2022-1903.xhtml")}, "nim": []},
            {"celex": "31963R0100", "rt": "REG", "date": "1963-01-01", "title": "Regulamento antigo", "eli": "",
             "cons": [], "orig": False, "docs": {}, "nim": []},      # no Portuguese xhtml at all
            {"celex": "32019L0790", "rt": "DIR", "date": "2019-04-17", "title": "Diretiva (UE) 2019/790", "eli": "",
             "cons": [("2019-05-17", "02019L0790-20190517")], "orig": True,        # the consolidation has no Portuguese text (404)
             "docs": {"32019L0790": xhtml_fixture("dir-original-2009-1.xhtml")}, "nim": []},
        ]

    def act(self, celex):
        return next(a for a in self.acts if a["celex"] == celex)

    def requests_to(self, part):
        return [e for e in self.log if part in e[1]]

    # -- transport for Cellar(transport=eu.transport)
    def transport(self, url, data, headers):
        self.n += 1
        self.log.append((self.clock(), url, headers.get("User-Agent"), headers.get("Accept")))
        self.clock.now += self.latency
        if self.fault:
            f = self.fault(self.n, url)
            if f == "oserror":
                raise OSError("simulated network failure")
            if f == "garbage":
                return 200, b"<html>the service changed</html>"
            if isinstance(f, int):
                return f, b""
        if "/sparql" in url:
            q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)["query"][0]
            return 200, json.dumps({"results": {"bindings": [{k: {"value": v} for k, v in r.items()} for r in self.sparql(q)]}}).encode()
        m = re.search(r"/resource/cellar/([^/]+)/DOC_(\d+)$", url)
        if m:
            item = self.items.get((m.group(1), int(m.group(2))))
            return (200, item) if item is not None else (404, b"")
        m = re.search(r"/resource/celex/(.+)$", url)
        assert m, url
        for a in self.acts:
            if m.group(1) in a.get("multi", {}):
                return 300, self.multi_body(m.group(1), a["multi"][m.group(1)]).encode("utf-8")
        for a in self.acts:
            if m.group(1) in a["docs"]:
                return 200, a["docs"][m.group(1)].encode("utf-8")
        return 404, b""

    def multi_body(self, doc, items):
        """HTTP 300 answer of Cellar for a manifestation with several items [(file name, content bytes)]."""
        li = ""
        for n, (name, content) in enumerate(items, 1):
            self.items[(f"{doc}.0041.02", n)] = content
            li += ('<li title="item"><a href="http://publications.europa.eu/resource/cellar/%s.0041.02/DOC_%d">'
                   '<span class="url">(x)</span></a><ul><li title="stream_name">%s</li><li title="stream_label">y</li>'
                   '<li title="stream_order" id="streamOrder">%d</li></ul></li>' % (doc, n, name, n))
        return ('<html><head><title>300 Multiple-Choice Response</title></head><body> List of URIs:<ul>'
                '<li title="manifestation">cellar:%s.0041.02<ul>%s</ul></li></ul></body></html>' % (doc, li))

    def sparql(self, q):
        if "resource_legal_date_end-of-validity" in q:
            wanted = set(re.findall(r"'([^']+)'", q.split("IN (")[1]))
            return [row(celex=a["celex"], end=a["end"]) for a in self.acts if a["celex"] in wanted and a.get("end")]
        key = re.search(r"STR\(\?(\w+)\) > '([^']*)'", q)
        limit = int(re.search(r"LIMIT (\d+)", q).group(1))
        if "act_consolidated" in q:
            rows = [row(celex=cc, cd=d) for a in self.acts for d, cc in a["cons"]]
        elif "measure_national" in q:
            rows = [r for a in self.acts if a["rt"] == "DIR" for r in a["nim"]]
        elif "manifestation_type" in q:
            rt = re.search(r"rt:(\w+)", q).group(1)
            rows = [row(celex=a["celex"]) for a in self.acts if a["rt"] == rt and a["orig"] and not a.get("left")]
        else:
            rt = re.search(r"rt:(\w+)", q).group(1)
            rows = [row(celex=a["celex"], date=a["date"], title=a["title"] or None, eli=a["eli"] or None)
                    for a in self.acts if a["rt"] == rt and not a.get("left")]
        k = key.group(1) if key else "celex"
        rows = sorted((r for r in rows if r.get(k, "") > (key.group(2) if key else "")), key=lambda r: r.get(k, ""))
        return rows[:limit]

    def client(self, **kw):
        return cellar_client.Cellar(transport=self.transport, clock=self.clock, sleep=self.clock.sleep, log=lambda m: None, **kw)
