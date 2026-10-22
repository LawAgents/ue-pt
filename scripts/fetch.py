#!/usr/bin/env python3
"""Download the in-force EU regulations and directives (Portuguese text) into a raw cache outside the repo.

  python scripts/fetch.py --mode initial|weekly --raw DIR [--budget-seconds N] [--repo DIR] [--workers 8]

Source: Publications Office of the EU. Lists by SPARQL (no GROUP BY / MAX on the server, paging by key), texts by
GET https://publications.europa.eu/resource/celex/CELEX (Accept application/xhtml+xml, Accept-Language por).

Selection (EU-LAW.xml eu.rule.selection): for every in-force REG/DIR act the latest consolidated version with a date up
to today and a Portuguese xhtml; else the original Portuguese xhtml; else the act is excluded (excluded.json, not an error).

Raw cache layout (DIR):
  plan.json            the selection of the current cycle: {"acts": [...], "excluded": [...], "created", "mode"}
  nim.json             Portuguese national implementing measures of directives (for the transposition section)
  json/<celex>.json.gz {"celex","wanted","doc","kind","cons_date","xhtml","fetched"}  (xhtml None + "excluded" when no text)
  index.json           celex -> {"wanted","doc"} of the records on disk (progress marker for resume and weekly runs)
  cycle.json           progress of the current cycle (resume after a budget stop)
  excluded.json        acts left out and why
  fetch-warnings.json  skipped items of multi-item manifestations (HTTP 300): images, pdf...
  revoked/<celex>.json end-of-validity date of acts that left force (with --repo)

Modes: initial = fetch every selected act without an up-to-date record; weekly = the same, but acts that the repo already
holds with the same document are skipped too, so only new acts and acts with a new consolidated version are downloaded.
Exit codes: 0 done, 1 aborted (3 consecutive errors, HTTP 429/503 or the service changed), 2 time budget reached.
"""
import argparse
import gzip
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import xhtml  # noqa: E402
from cellar_client import Cellar, FetchAborted, POR  # noqa: E402
from common import BASE_CELEX, atomic_write  # noqa: E402

PREFIX = ("PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>\n"
          "PREFIX rt: <http://publications.europa.eu/resource/authority/resource-type/>\n")
Q_ACTS = PREFIX + f"""SELECT ?celex ?date ?title ?eli WHERE {{
 ?w cdm:work_has_resource-type rt:@RT@ ; cdm:resource_legal_in-force true ; cdm:resource_legal_id_celex ?celex ; cdm:work_date_document ?date .
 OPTIONAL {{ ?w cdm:resource_legal_eli ?eli }}
 OPTIONAL {{ ?e cdm:expression_belongs_to_work ?w ; cdm:expression_uses_language <{POR}> ; cdm:expression_title ?title }}
 FILTER(STR(?celex) > '@last@') }} ORDER BY ?celex LIMIT @limit@"""
Q_CONS = PREFIX + f"""SELECT DISTINCT ?celex ?cd WHERE {{ ?c a cdm:act_consolidated ; cdm:resource_legal_id_celex ?celex ; cdm:act_consolidated_date ?cd .
 ?e cdm:expression_belongs_to_work ?c ; cdm:expression_uses_language <{POR}> .
 ?m cdm:manifestation_manifests_expression ?e ; cdm:manifestation_type ?mt .
 FILTER(STR(?mt) = 'xhtml' && STR(?celex) > '@last@') }} ORDER BY ?celex LIMIT @limit@"""
Q_ORIG = PREFIX + f"""SELECT DISTINCT ?celex WHERE {{ ?w cdm:work_has_resource-type rt:@RT@ ; cdm:resource_legal_in-force true ; cdm:resource_legal_id_celex ?celex .
 ?e cdm:expression_belongs_to_work ?w ; cdm:expression_uses_language <{POR}> .
 ?m cdm:manifestation_manifests_expression ?e ; cdm:manifestation_type ?mt .
 FILTER(STR(?mt) = 'xhtml' && STR(?celex) > '@last@') }} ORDER BY ?celex LIMIT @limit@"""
Q_NIM = PREFIX + """SELECT ?dir ?nc ?local ?type ?date ?ojn ?eli WHERE {
 ?n cdm:measure_national_implementing_implemented_by_country <http://publications.europa.eu/resource/authority/country/PRT> ;
    cdm:measure_national_implementing_implements_resource_legal ?w ; cdm:resource_legal_id_celex ?nc .
 ?w cdm:resource_legal_id_celex ?dir .
 OPTIONAL { ?n cdm:resource_legal_id_local ?local } OPTIONAL { ?n cdm:measure_national_implementing_type_act ?type }
 OPTIONAL { ?n cdm:work_date_document ?date } OPTIONAL { ?n cdm:measure_national_implementing_number_official_journal ?ojn }
 OPTIONAL { ?n <http://publications.europa.eu/ontology/cdm#eli> ?eli }
 FILTER(STR(?nc) > '@last@') } ORDER BY ?nc LIMIT @limit@"""
Q_END = PREFIX + """SELECT ?celex ?end WHERE { ?w cdm:resource_legal_id_celex ?celex ; cdm:resource_legal_date_end-of-validity ?end .
 FILTER(STR(?celex) IN (@list@)) }"""
RESOURCE_TYPES = {"REG": "Regulamento", "DIR": "Diretiva"}
SAVE_EVERY = 25


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---- raw cache -------------------------------------------------------------------------------------

class Raw:
    def __init__(self, path):
        self.dir = Path(path)
        (self.dir / "json").mkdir(parents=True, exist_ok=True)
        self._index = None

    def rec_path(self, celex):
        return self.dir / "json" / f"{celex}.json.gz"

    def read(self, celex):
        p = self.rec_path(celex)
        if not p.exists():
            return None
        try:
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return None  # damaged file: treated as missing and fetched again

    def index(self):
        if self._index is None:
            self._index = self.read_json("index.json", {}) or {}
        return self._index

    def write(self, celex, rec):
        data = gzip.compress(json.dumps(rec, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), 6, mtime=0)
        atomic_write(self.rec_path(celex), data, binary=True)
        entry = {"wanted": rec.get("wanted"), "doc": rec.get("doc")}
        if rec.get("xhtml"):
            sc = xhtml.scan_counts(rec["xhtml"])   # counted on the raw markup, independent of the converter
            entry["counts"] = {"articles": sc["articles"], "recitals": sc["recitals"], "kind": rec.get("kind")}
        if rec.get("excluded"):
            entry["excluded"] = rec["excluded"]
        if rec.get("notes"):
            entry["notes"] = rec["notes"]
        self.index()[celex] = entry

    def flush_index(self):
        self.write_json("index.json", self.index())

    def read_json(self, name, default=None):
        p = self.dir / name
        if not p.exists():
            return default
        return json.loads(p.read_text(encoding="utf-8"))

    def write_json(self, name, obj):
        atomic_write(self.dir / name, json.dumps(obj, ensure_ascii=False, separators=(",", ":")))


# ---- lists --------------------------------------------------------------------------------------------

def list_acts(c, log=print):
    """{celex: {celex, type, date, title, eli}} of in-force regulations and directives (base CELEX numbers only)."""
    acts = {}
    for rt in RESOURCE_TYPES:
        rows = c.sparql_paged(Q_ACTS.replace("@RT@", rt), "celex")
        log(f"acts {rt}: {len(rows)} rows")
        for r in rows:
            a = acts.setdefault(r["celex"], {"celex": r["celex"], "type": rt, "date": r.get("date", "")[:10],
                                             "title": "", "eli": ""})
            a["title"] = a["title"] or r.get("title", "")
            a["eli"] = a["eli"] or r.get("eli", "")
    return acts


def list_consolidated(c, log=print):
    """{base celex: [(date, consolidated celex)] newest first} for consolidated versions with a Portuguese xhtml."""
    out = {}
    rows = c.sparql_paged(Q_CONS, "celex")
    log(f"consolidated versions with Portuguese xhtml: {len(rows)}")
    for r in rows:
        cc, cd = r["celex"], r["cd"][:10]
        if len(cc) >= 10 and cc[0] == "0":
            out.setdefault("3" + cc[1:10], set()).add((cd, cc))
    return {b: sorted(v, reverse=True) for b, v in out.items()}


def list_originals(c, log=print):
    out = set()
    for rt in RESOURCE_TYPES:
        rows = c.sparql_paged(Q_ORIG.replace("@RT@", rt), "celex")
        log(f"originals {rt} with Portuguese xhtml: {len(rows)}")
        out |= {r["celex"] for r in rows}
    return out


def list_nim(c, log=print):
    rows = c.sparql_paged(Q_NIM, "nc")
    seen, out = set(), []
    for r in rows:
        k = (r["nc"], r["dir"], r.get("local", ""), r.get("type", ""))
        if k not in seen:
            seen.add(k)
            out.append(r)
    log(f"Portuguese national measures: {len(out)}")
    return out


def build_plan(acts, cons, origs, today):
    """Selection rule eu.rule.selection. Returns {"acts": [...], "excluded": [...]}.
    Each selected act: celex, type, date, title, eli, kind, doc, cons_date, alternatives (documents to try if the
    first one has no Portuguese text)."""
    selected, excluded = [], []
    for celex in sorted(acts):
        a = acts[celex]
        if not BASE_CELEX.match(celex):
            excluded.append({"celex": celex, "reason": "CELEX fora do formato de um regulamento ou diretiva de base"})
            continue
        versions = [(d, cc) for d, cc in cons.get(celex, []) if d <= today]
        future = [cc for d, cc in cons.get(celex, []) if d > today]
        tries = [("consolidated", cc, d) for d, cc in versions[:3]]
        if celex in origs:
            tries.append(("original", celex, ""))
        if not tries:
            reason = "sem xhtml em português" + (" (só consolidações com data futura)" if future else "")
            excluded.append({"celex": celex, "reason": reason})
            continue
        kind, doc, d = tries[0]
        selected.append({"celex": celex, "type": RESOURCE_TYPES[a["type"]], "date": a["date"], "title": a["title"],
                         "eli": a["eli"], "kind": kind, "doc": doc, "cons_date": d,
                         "alternatives": [[k, dd, cdt] for k, dd, cdt in tries[1:]]})
    return {"acts": selected, "excluded": excluded}


# ---- one act ----------------------------------------------------------------------------------------------

def fetch_act(c, entry):
    """Raw record of one planned act: the first document of the plan that has a Portuguese text."""
    tries = [[entry["kind"], entry["doc"], entry["cons_date"]]] + entry.get("alternatives", [])
    for kind, doc, cdate in tries:
        text, notes = c.xhtml_with_notes(doc)
        if text is not None:
            rec = {"celex": entry["celex"], "wanted": entry["doc"], "doc": doc, "kind": kind, "cons_date": cdate,
                   "xhtml": text, "fetched": now_iso()}
            if notes:
                rec["notes"] = notes     # e.g. image items of a multi-item manifestation that were skipped
            return rec
    return {"celex": entry["celex"], "wanted": entry["doc"], "doc": None, "kind": None, "xhtml": None,
            "excluded": "sem texto em português (404 em todos os documentos)", "fetched": now_iso()}


def repo_docs(repo):
    """{celex: document used} for the acts in the repo (consolidated celex, or the act's own CELEX for originals)."""
    from convert import repo_acts
    return {k: v["doc"] for k, v in repo_acts(repo).items()}


def needs_fetch(entry, raw, have):
    idx = raw.index().get(entry["celex"])
    if idx and idx.get("wanted") == entry["doc"]:
        return False
    return not (have and have.get(entry["celex"]) == entry["doc"])


# ---- driver ----------------------------------------------------------------------------------------------------

def run_fetch(c, raw, mode, budget_seconds=None, repo=None, clock=time.monotonic, workers=1, today=None,
              log=lambda m: print(m, file=sys.stderr)):
    """Run (or resume) a fetch cycle. Returns the exit code 0, 1 or 2."""
    t0 = clock()
    today = today or date.today().isoformat()
    try:
        state = raw.read_json("cycle.json")
        plan = raw.read_json("plan.json")
        if state and not state.get("complete") and state.get("mode") == mode and plan:
            log(f"resuming the cycle started {state['started']}")
        else:
            acts = list_acts(c, log)
            cons = list_consolidated(c, log)
            origs = list_originals(c, log)
            nim = list_nim(c, log)
            plan = build_plan(acts, cons, origs, today)
            plan["mode"], plan["created"], plan["today"] = mode, now_iso(), today
            plan["in_force"] = sorted(acts)
            raw.write_json("nim.json", nim)
            raw.write_json("plan.json", plan)
            raw.write_json("excluded.json", plan["excluded"])
            state = {"mode": mode, "started": now_iso(), "complete": False}
            raw.write_json("cycle.json", state)
            log(f"plan: {len(plan['acts'])} acts selected, {len(plan['excluded'])} excluded")
        have = repo_docs(repo) if (repo and mode == "weekly") else None
        todo = [e for e in plan["acts"] if needs_fetch(e, raw, have)]
        log(f"{len(todo)} acts to download")
        n = 0
        pool = ThreadPoolExecutor(max_workers=max(1, workers))
        try:
            for b0 in range(0, len(todo), workers):
                if budget_seconds is not None and clock() - t0 >= budget_seconds:
                    raw.flush_index()
                    log(f"time budget reached after {b0} acts; run again to resume")
                    return 2
                for entry, rec in pool.map(lambda e: (e, fetch_act(c, e)), todo[b0:b0 + workers]):
                    raw.write(entry["celex"], rec)
                    n += 1
                if (b0 // workers + 1) % max(1, SAVE_EVERY // workers) == 0:
                    raw.flush_index()
                    log(f"{min(b0 + workers, len(todo))}/{len(todo)}")
        finally:
            pool.shutdown(wait=True, cancel_futures=True)
        raw.flush_index()
        raw.write_json("excluded.json", list(plan["excluded"]) + unavailable(raw, plan))
        raw.write_json("fetch-warnings.json", [{"celex": k, "doc": v.get("doc"), "notes": v["notes"]}
                                               for k, v in sorted(raw.index().items()) if v.get("notes")])
        state["complete"] = True
        raw.write_json("cycle.json", state)
        log(f"fetch done: {n} acts downloaded, {c.requests} requests this run")
        return 0
    except FetchAborted as e:
        raw.flush_index()
        log(f"FETCH ABORTED: {e}")
        return 1


def unavailable(raw, plan):
    """Planned acts whose record says there is no Portuguese text after all."""
    idx = raw.index()
    return [{"celex": e["celex"], "reason": idx[e["celex"]]["excluded"]} for e in plan["acts"]
            if idx.get(e["celex"], {}).get("excluded")]


def left_force(raw, repo):
    """(revoked, removed): CELEX numbers of acts in the repo that are no longer in the in-force list (revoked) and of
    acts still in force that are no longer selected (removed without a revocation entry)."""
    from convert import repo_acts
    plan = raw.read_json("plan.json", {"acts": [], "in_force": []})
    idx = raw.index()
    selected = {e["celex"] for e in plan["acts"] if not idx.get(e["celex"], {}).get("excluded")}
    in_force = set(plan.get("in_force", []))
    have = set(repo_acts(repo))
    revoked = sorted(have - in_force)
    removed = sorted((have & in_force) - selected)
    return revoked, removed


def fetch_revocations(c, raw, celexes, today, log=lambda m: None):
    """End-of-validity date of acts that left force (cdm:resource_legal_date_end-of-validity), else the detection date."""
    todo = [x for x in celexes if not (raw.dir / "revoked" / f"{x}.json").exists()]
    for i in range(0, len(todo), 40):
        batch = todo[i:i + 40]
        lst = ", ".join("'" + x.replace("'", "") + "'" for x in batch)
        rows = c.sparql(Q_END.replace("@list@", lst))
        ends = {}
        for r in rows:
            d = r["end"][:10]
            if d and not d.startswith("9999"):
                ends[r["celex"]] = min(d, ends.get(r["celex"], d))
        for x in batch:
            atomic_write(raw.dir / "revoked" / f"{x}.json",
                         json.dumps({"celex": x, "date": ends.get(x, today), "date_source": "sparql" if x in ends else "detected"}))
            log(f"revoked {x}: {ends.get(x, today)} ({'sparql' if x in ends else 'detected'})")


def run_revocations(c, raw, repo, today=None, log=lambda m: print(m, file=sys.stderr)):
    try:
        revoked, _ = left_force(raw, repo)
        fetch_revocations(c, raw, revoked, today or date.today().isoformat(), log)
        return 0
    except FetchAborted as e:
        log(f"FETCH ABORTED: {e}")
        return 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--mode", choices=["initial", "weekly"], required=True)
    ap.add_argument("--raw", required=True, help="raw cache directory (outside the repo)")
    ap.add_argument("--budget-seconds", type=float, default=None,
                    help="stop gracefully after this many seconds (exit code 2); a later run resumes")
    ap.add_argument("--workers", type=int, default=8,
                    help="downloads in flight at once; the total start rate stays at most 2 requests per second")
    ap.add_argument("--repo", default=None,
                    help="current repo: weekly mode skips acts it already holds; acts that left force get an end-of-validity date")
    a = ap.parse_args(argv)
    c, raw = Cellar(), Raw(a.raw)
    rc = run_fetch(c, raw, a.mode, a.budget_seconds, a.repo, workers=a.workers)
    if rc == 0 and a.repo:
        rc = run_revocations(c, raw, a.repo)
    return rc


if __name__ == "__main__":
    sys.exit(main())
