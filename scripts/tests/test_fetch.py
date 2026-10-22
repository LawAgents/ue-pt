"""eu.test.selection, rate, budget/resume and weekly change detection against a simulated Publications Office."""
import json
import unittest
from pathlib import Path

from helpers import FIX, TODAY, FakeClock, FakeEU, TmpCase, common

import convert
import fetch


def gaps(eu):
    t = [e[0] for e in eu.log]
    return [b - a for a, b in zip(t, t[1:])]


class Selection(unittest.TestCase):
    ACTS = {c: {"celex": c, "type": t, "date": "2000-01-01", "title": "T", "eli": ""} for c, t in
            (("32016R0679", "REG"), ("32019L0790", "DIR"), ("31963R0100", "REG"), ("32001R0001", "REG"), ("32016R0679R(01)", "REG"))}

    def plan(self, cons, origs):
        return fetch.build_plan(self.ACTS, cons, set(origs), TODAY)

    def test_latest_consolidation_up_to_today_wins(self):
        cons = {"32016R0679": [("2027-01-01", "02016R0679-20270101"), ("2018-05-25", "02016R0679-20180525"), ("2016-05-04", "02016R0679-20160504")]}
        e = next(a for a in self.plan(cons, [])["acts"] if a["celex"] == "32016R0679")
        self.assertEqual((e["kind"], e["doc"], e["cons_date"]), ("consolidated", "02016R0679-20180525", "2018-05-25"))
        self.assertEqual([a[1] for a in e["alternatives"]], ["02016R0679-20160504"])     # tried if the newest has no text

    def test_a_consolidation_dated_today_counts_and_tomorrow_does_not(self):
        cons = {"32016R0679": [("2026-10-23", "02016R0679-20261023"), (TODAY, "02016R0679-20261022")]}
        e = next(a for a in self.plan(cons, [])["acts"] if a["celex"] == "32016R0679")
        self.assertEqual(e["doc"], "02016R0679-20261022")

    def test_future_only_consolidations_fall_back_to_the_original(self):
        cons = {"32016R0679": [("2027-01-01", "02016R0679-20270101")]}
        e = next(a for a in self.plan(cons, ["32016R0679"])["acts"] if a["celex"] == "32016R0679")
        self.assertEqual((e["kind"], e["doc"]), ("original", "32016R0679"))

    def test_original_is_used_when_there_is_no_consolidation(self):
        e = next(a for a in self.plan({}, ["32019L0790"])["acts"] if a["celex"] == "32019L0790")
        self.assertEqual((e["kind"], e["doc"], e["type"]), ("original", "32019L0790", "Diretiva"))

    def test_acts_without_portuguese_xhtml_are_excluded_and_do_not_fail(self):
        p = self.plan({}, [])
        self.assertEqual(p["acts"], [])
        reasons = {x["celex"]: x["reason"] for x in p["excluded"]}
        self.assertIn("sem xhtml em português", reasons["31963R0100"])
        self.assertIn("fora do formato", reasons["32016R0679R(01)"])
        p = self.plan({"32001R0001": [("2030-01-01", "02001R0001-20300101")]}, [])
        self.assertIn("data futura", {x["celex"]: x["reason"] for x in p["excluded"]}["32001R0001"])


class Fetching(TmpCase):
    def setUp(self):
        super().setUp()
        self.clock = FakeClock()
        self.eu = FakeEU(self.clock)
        self.raw = fetch.Raw(self.tmp / "raw")

    def run_fetch(self, mode="initial", client=None, **kw):
        kw.setdefault("today", TODAY)
        return fetch.run_fetch(client or self.eu.client(), self.raw, mode, log=lambda m: None, clock=self.clock, **kw)

    def test_selection_end_to_end_with_future_versions_missing_text_and_exclusions(self):
        self.assertEqual(self.run_fetch(), 0)
        plan = self.raw.read_json("plan.json")
        by = {e["celex"]: e for e in plan["acts"]}
        self.assertEqual(by["32016R0679"]["doc"], "02016R0679-20160504")          # the 2027 version is ignored
        self.assertEqual(sorted(by), ["32009L0001", "32010R0265", "32016R0679", "32019L0790", "32022R1903"])
        self.assertEqual([x["celex"] for x in self.raw.read_json("excluded.json")], ["31963R0100"])
        self.assertNotIn("02016R0679-20270101", "".join(e[1] for e in self.eu.log))
        rec = self.raw.read("32019L0790")                                         # the consolidation answered 404: original text
        self.assertEqual((rec["kind"], rec["doc"], rec["wanted"]), ("original", "32019L0790", "02019L0790-20190517"))
        self.assertTrue(rec["xhtml"])

    def test_a_404_is_not_an_error_for_the_stop_rule(self):
        self.eu.acts = [dict(self.eu.act("32009L0001"), celex=f"3200{n}L000{n}", docs={}, cons=[], orig=True) for n in range(1, 6)]
        self.assertEqual(self.run_fetch(), 0)                                      # five 404 in a row: all become exclusions
        self.assertEqual(len(self.raw.read_json("excluded.json")), 5)
        self.assertTrue(all(self.raw.read(f"3200{n}L000{n}")["excluded"] for n in range(1, 6)))

    def test_at_most_two_request_starts_per_second_with_the_project_user_agent(self):
        eu = FakeEU(self.clock, latency=0.0)
        self.eu = eu
        self.assertEqual(self.run_fetch(), 0)
        self.assertGreater(len(eu.log), 10)
        self.assertGreaterEqual(min(gaps(eu)), 0.55 - 1e-6)
        self.assertGreaterEqual(min(gaps(eu)), 0.5)                               # the rule: at most 2 per second
        self.assertEqual({e[2] for e in eu.log}, {common.USER_AGENT})
        self.assertEqual(common.USER_AGENT, "LawAgents-ue/0.1 (+https://github.com/LawAgents/ue-pt)")
        docs = [e for e in eu.log if "/resource/celex/" in e[1]]
        self.assertTrue(all(e[3] == "application/xhtml+xml" for e in docs))

    def test_parallel_workers_keep_the_start_rate(self):
        eu = FakeEU(self.clock, latency=0.0)
        self.eu = eu
        self.assertEqual(self.run_fetch(workers=8), 0)
        self.assertGreaterEqual(min(gaps(eu)), 0.55 - 1e-6)

    def test_stops_after_three_consecutive_errors_and_on_429_503(self):
        self.eu.fault = lambda n, url: 500 if n >= 2 else None
        self.assertEqual(self.run_fetch(), 1)
        self.assertEqual(len(self.eu.log), 4)                                      # 1 ok + 3 failed requests, then nothing
        for status in (429, 503):
            eu = FakeEU(FakeClock())
            eu.fault = lambda n, url, s=status: s if n == 2 else None
            raw = fetch.Raw(self.tmp / f"raw{status}")
            self.assertEqual(fetch.run_fetch(eu.client(), raw, "initial", today=TODAY, log=lambda m: None), 1)
            self.assertEqual(len(eu.log), 2)
            self.assertIsNone(raw.read_json("plan.json"))                          # no partial plan

    def test_unknown_answer_shape_aborts(self):
        self.eu.fault = lambda n, url: "garbage" if n == 1 else None
        self.assertEqual(self.run_fetch(), 1)

    def test_budget_exit_2_then_resume_without_repeating_work(self):
        for i in range(12):
            self.eu.acts.append(dict(self.eu.act("32009L0001"), celex=f"320{10 + i}R00{10 + i}", rt="REG", docs={f"320{10 + i}R00{10 + i}": self.eu.act("32009L0001")["docs"]["32009L0001"]}))
        c = self.eu.client()
        self.assertEqual(self.run_fetch(client=c, budget_seconds=12), 2)
        first = len(self.eu.requests_to("/resource/celex/"))
        self.assertTrue(0 < first < 17)
        self.assertEqual(self.raw.read_json("cycle.json")["complete"], False)
        lists = len(self.eu.requests_to("/sparql"))
        self.assertEqual(self.run_fetch(client=self.eu.client(), budget_seconds=10_000), 0)
        self.assertEqual(len(self.eu.requests_to("/sparql")), lists)               # the plan was not rebuilt
        docs = [e[1] for e in self.eu.requests_to("/resource/celex/")]
        self.assertEqual(len(docs), len(set(docs)))                                # no document was asked for twice
        self.assertGreaterEqual(min(gaps(self.eu)), 0.55 - 1e-6)

    def test_finished_cycle_run_again_downloads_nothing(self):
        self.assertEqual(self.run_fetch(), 0)
        before = len(self.eu.requests_to("/resource/celex/"))
        self.assertEqual(self.run_fetch(), 0)
        self.assertEqual(len(self.eu.requests_to("/resource/celex/")), before)

    def test_raw_files_are_written_atomically_and_hold_the_text(self):
        self.run_fetch()
        names = sorted(p.name for p in (self.tmp / "raw" / "json").iterdir())
        self.assertTrue(all(n.endswith(".json.gz") for n in names))
        self.assertIn("Artigo", self.raw.read("32010R0265")["xhtml"])

    def test_index_counts_come_from_the_raw_markup(self):
        self.run_fetch()
        idx = self.raw.index()
        self.assertEqual(idx["32009L0001"]["counts"], {"articles": 5, "recitals": 4, "kind": "original"})
        self.assertEqual(idx["32016R0679"]["counts"]["articles"], 11)


class Weekly(TmpCase):
    def setUp(self):
        super().setUp()
        self.clock = FakeClock()
        self.eu = FakeEU(self.clock)
        self.raw = fetch.Raw(self.tmp / "raw")
        self.repo = self.tmp / "repo"
        self.repo.mkdir()

    def cycle(self, mode, raw=None, **kw):
        return fetch.run_fetch(self.eu.client(), raw or self.raw, mode, today=TODAY, log=lambda m: None, clock=self.clock, **kw)

    def publish(self):
        """Convert the raw cache into the repo, as a finished update would."""
        out = self.repo
        convert.convert_all(self.raw.dir, out, None, None)

    def test_only_new_or_changed_acts_are_downloaded(self):
        self.assertEqual(self.cycle("initial"), 0)
        self.publish()
        self.clock.now += 100
        before = len(self.eu.requests_to("/resource/celex/"))
        # a new consolidated version of the GDPR appears and a brand new act too
        gdpr = self.eu.act("32016R0679")
        gdpr["cons"].append(("2026-09-01", "02016R0679-20260901"))
        gdpr["docs"]["02016R0679-20260901"] = gdpr["docs"]["02016R0679-20160504"]
        self.eu.acts.append(dict(self.eu.act("32022R1903"), celex="32024R0001", docs={"32024R0001": self.eu.act("32022R1903")["docs"]["32022R1903"]}))
        self.assertEqual(self.cycle("weekly", repo=str(self.repo)), 0)
        fetched = [e[1].rsplit("/", 1)[1] for e in self.eu.requests_to("/resource/celex/")[before:]]
        self.assertEqual(sorted(fetched), ["02016R0679-20260901", "32024R0001"])     # nothing else was downloaded
        self.assertEqual(self.raw.read("32016R0679")["doc"], "02016R0679-20260901")

    def test_unchanged_acts_cost_no_document_request_even_without_a_raw_cache(self):
        self.assertEqual(self.cycle("initial"), 0)
        self.publish()
        empty = fetch.Raw(self.tmp / "other-raw")                                    # CI without a persisted cache
        before = len(self.eu.requests_to("/resource/celex/"))
        self.assertEqual(self.cycle("weekly", raw=empty, repo=str(self.repo)), 0)
        again = [e[1].rsplit("/", 1)[1] for e in self.eu.requests_to("/resource/celex/")[before:]]
        # only the act whose first choice answers 404 (the repo holds its fallback text) is asked again: 2 requests
        self.assertEqual(sorted(again), ["02019L0790-20190517", "32019L0790"])
        # acts that the repo holds are copied: the converter can still build the whole tree
        acts, errors = convert.convert_all(empty.dir, self.tmp / "stage", self.repo, None)
        self.assertEqual((len(acts), errors), (5, []))

    def test_initial_mode_ignores_the_repo(self):
        self.assertEqual(self.cycle("initial"), 0)
        self.publish()
        empty = fetch.Raw(self.tmp / "other-raw")
        self.assertEqual(self.cycle("initial", raw=empty, repo=str(self.repo)), 0)
        self.assertGreaterEqual(len(self.eu.requests_to("/resource/celex/")), 10)

    def test_acts_that_left_force_get_an_end_of_validity_date(self):
        self.assertEqual(self.cycle("initial"), 0)
        self.publish()
        self.eu.act("32022R1903")["left"] = True
        self.eu.act("32022R1903")["end"] = "2026-09-30"
        self.eu.act("32010R0265")["left"] = True                                     # no date known: detection date
        self.assertEqual(self.cycle("weekly", repo=str(self.repo)), 0)
        revoked, removed = fetch.left_force(self.raw, self.repo)
        self.assertEqual(revoked, ["32010R0265", "32022R1903"])
        c = self.eu.client()
        self.assertEqual(fetch.run_revocations(c, self.raw, self.repo, TODAY, log=lambda m: None), 0)
        self.assertEqual(self.raw.read_json("revoked/32022R1903.json")["date"], "2026-09-30")
        self.assertEqual(self.raw.read_json("revoked/32010R0265.json"), {"celex": "32010R0265", "date": TODAY, "date_source": "detected"})

    def test_act_in_force_but_no_longer_selected_is_removed_without_a_revocation(self):
        self.assertEqual(self.cycle("initial"), 0)
        self.publish()
        a = self.eu.act("32022R1903")
        a["orig"] = False                                                            # still in force, no Portuguese text now
        self.assertEqual(self.cycle("weekly", repo=str(self.repo)), 0)
        revoked, removed = fetch.left_force(self.raw, self.repo)
        self.assertEqual((revoked, removed), ([], ["32022R1903"]))


if __name__ == "__main__":
    unittest.main()


class MultiItem(TmpCase):
    """Cellar answers HTTP 300 when a manifestation has several items (text plus images)."""

    PART1 = ('<html><head><title>t</title></head><body><p class="title-article-norm">Artigo 1.<span class="superscript">o</span></p>'
             '<p class="norm">Primeira parte.</p></body></html>')
    PART2 = '<html><body><p class="title-article-norm">Artigo 2.<span class="superscript">o</span></p><p class="norm">Segunda parte.</p></body></html>'

    def setUp(self):
        super().setUp()
        self.clock = FakeClock()
        self.eu = FakeEU(self.clock)

    def multi_act(self, celex="32009R0043", doc="02009R0043-20100101"):
        a = dict(self.eu.act("32010R0265"), celex=celex, docs={}, cons=[("2010-01-01", doc)])
        a["multi"] = {doc: [("CL2009R0043PT0050020.0001.html", self.PART1.encode()), ("FOR-x.xml.jpg", b"\xff\xd8"),
                            ("L_2009022PT.01016602.tif.jpg", b"\xff"), ("part2.html", self.PART2.encode())]}
        self.eu.acts.append(a)
        return a

    def test_real_300_answer_is_parsed_in_stream_order(self):
        import cellar_client
        body = (FIX / "cellar-300-02009R0043-20100101.html").read_text(encoding="utf-8")
        items = cellar_client.parse_items(body)
        self.assertEqual(len(items), 11)
        self.assertEqual([i[0] for i in items], list(range(1, 12)))
        self.assertEqual(items[0][2], "CL2009R0043PT0050020.0001.html")
        self.assertTrue(items[0][1].endswith("/DOC_1"))
        self.assertTrue(all(not n.endswith(".html") for _, _, n in items[1:]))        # the others are images

    def test_items_are_fetched_in_order_joined_and_non_text_items_skipped(self):
        self.multi_act()
        c = self.eu.client()
        text, notes = c.xhtml_with_notes("02009R0043-20100101")
        self.assertEqual(text.count("<body"), 1)
        self.assertLess(text.index("Primeira parte."), text.index("Segunda parte."))
        self.assertEqual(len(notes), 2)
        self.assertIn("FOR-x.xml.jpg", notes[0])
        self.assertEqual([e[1].rsplit("/", 1)[1] for e in self.eu.requests_to("/resource/cellar/")], ["DOC_1", "DOC_4"])

    def test_300_is_not_an_error_for_the_three_errors_rule(self):
        for n in range(5):
            self.multi_act(f"3200{n}R000{n}", f"0200{n}R000{n}-20100101")
        raw = fetch.Raw(self.tmp / "raw")
        rc = fetch.run_fetch(self.eu.client(), raw, "initial", today=TODAY, log=lambda m: None, clock=self.clock)
        self.assertEqual(rc, 0)
        for n in range(5):
            rec = raw.read(f"3200{n}R000{n}")
            self.assertIn("Segunda parte.", rec["xhtml"])
            self.assertEqual(len(rec["notes"]), 2)
        w = raw.read_json("fetch-warnings.json")
        self.assertEqual(len(w), 5)
        self.assertEqual(w[0]["celex"], "32000R0000")

    def test_converter_reads_the_joined_document(self):
        import convert
        self.multi_act()
        raw = fetch.Raw(self.tmp / "raw")
        self.assertEqual(fetch.run_fetch(self.eu.client(), raw, "initial", today=TODAY, log=lambda m: None, clock=self.clock), 0)
        acts, errors = convert.convert_all(raw.dir, self.tmp / "out", None, None)
        self.assertEqual(errors, [])
        text = (self.tmp / "out" / "regulamentos" / "2009" / "regulamento-ue-2009-43.md").read_text(encoding="utf-8")
        self.assertIn("## Artigo 1.º", text)
        self.assertIn("## Artigo 2.º", text)
        self.assertEqual(raw.index()["32009R0043"]["counts"]["articles"], 2)

    def test_a_300_with_no_text_item_is_no_text(self):
        a = self.multi_act()
        a["multi"]["02009R0043-20100101"] = [("x.jpg", b"\xff")]
        text, notes = self.eu.client().xhtml_with_notes("02009R0043-20100101")
        self.assertIsNone(text)
        self.assertIn("300 answer without a text item", notes[-1])
