"""eu.test.size, update failure leaves the repo untouched, budget/resume, end-to-end behaviour of run_update."""
import contextlib
import io
import os
import subprocess
import unittest
from unittest import mock

from helpers import TODAY, FakeClock, FakeEU, TmpCase, common

import check_size
import convert
import fetch
import run_update


def snapshot(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


class UpdateCase(TmpCase):
    def setUp(self):
        super().setUp()
        self.raw, self.repo = self.tmp / "raw", self.tmp / "repo"
        self.repo.mkdir()
        self.cfg = self.config_dir()
        self.clock = FakeClock()
        self.eu = FakeEU(self.clock)

    def run_update(self, mode="initial", **kw):
        out = io.StringIO()
        kw.setdefault("client", self.eu.client())
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = run_update.run(mode, self.raw, self.repo, config=self.cfg, count_check=False, clock=self.clock, today=TODAY, **kw)
        return rc, out.getvalue()

    def errors(self):
        import json
        return json.loads((self.raw / "errors.json").read_text(encoding="utf-8"))


class Success(UpdateCase):
    def test_initial_builds_the_repo_and_weekly_without_changes_changes_nothing(self):
        gh = self.tmp / "gh_output"
        with mock.patch.dict(os.environ, {"GITHUB_OUTPUT": str(gh)}):
            rc, out = self.run_update("initial")
        self.assertEqual(rc, 0)
        self.assertIn("CHANGED=true", out.splitlines())
        self.assertEqual(gh.read_text(encoding="utf-8").strip(), "CHANGED=true")
        for rel in ("regulamentos/2022/regulamento-ue-2022-1903.md", "diretivas/2009/diretiva-ue-2009-1.md", "indice.md",
                    "indice-regulamentos.md", "indice-diretivas.md", "nomes-comuns.md", "revogados.md"):
            self.assertTrue((self.repo / rel).exists(), rel)
        self.assertFalse((self.raw / "errors.json").exists())
        self.assertFalse(list(self.repo.rglob("*.tmp")))
        before = snapshot(self.repo)
        rc, out = self.run_update("weekly", client=self.eu.client())
        self.assertEqual(rc, 0)
        self.assertIn("CHANGED=false", out.splitlines())
        self.assertEqual(snapshot(self.repo), before)

    def test_ids_are_unique_and_follow_the_format(self):
        self.run_update("initial")
        ids = [m["id"] for m in common.main_files(self.repo)]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(i.startswith(("regulamento-ue-", "diretiva-ue-")) for i in ids))
        celexes = [m["celex"] for m in common.main_files(self.repo)]
        self.assertEqual(len(celexes), len(set(celexes)))

    def test_directive_with_a_known_portuguese_measure_lists_it_with_the_existing_id_only(self):
        self.run_update("initial")
        text = (self.repo / "diretivas/2009/diretiva-ue-2009-1.md").read_text(encoding="utf-8")
        sec = text.split("## Transposição para Portugal")[1]
        self.assertIn("(id: decreto-lei-47-2023)", sec)
        self.assertIn("(id: lei-59-2019; fonte: https://dre.pt/eli/lei/59/2019)", sec)
        self.assertNotIn("id: portaria", sec)                         # not in the Portuguese repo: no id
        self.assertEqual(sec.count("fonte:"), 1)                      # one real link, none invented

    def test_weekly_with_a_new_consolidated_version_changes_only_that_act_and_its_index_row(self):
        self.run_update("initial")
        before = snapshot(self.repo)
        gdpr = self.eu.act("32016R0679")
        gdpr["cons"].append(("2026-09-01", "02016R0679-20260901"))
        gdpr["docs"]["02016R0679-20260901"] = gdpr["docs"]["02016R0679-20160504"]
        rc, out = self.run_update("weekly", client=self.eu.client())
        self.assertEqual((rc, "CHANGED=true" in out), (0, True))
        after = snapshot(self.repo)
        changed = sorted(k for k in after if before.get(k) != after[k])
        self.assertEqual(changed, ["indice-regulamentos.md", "regulamentos/2016/regulamento-ue-2016-679/regulamento-ue-2016-679.md"]
                         if any(k.startswith("regulamentos/2016/regulamento-ue-2016-679/") for k in after) else
                         ["indice-regulamentos.md", "regulamentos/2016/regulamento-ue-2016-679.md"])
        self.assertIn(b"consolidated_celex: \"02016R0679-20260901\"", after[changed[1]])

    def test_weekly_without_a_raw_cache_copies_unchanged_acts_from_the_repo(self):
        self.run_update("initial")
        before = snapshot(self.repo)
        import shutil
        shutil.rmtree(self.raw)
        eu2 = self.eu
        n = len(eu2.requests_to("/resource/celex/"))
        rc, out = self.run_update("weekly", client=eu2.client())
        self.assertEqual(rc, 0)
        self.assertIn("CHANGED=false", out.splitlines())
        self.assertEqual(snapshot(self.repo), before)
        self.assertEqual(len(eu2.requests_to("/resource/celex/")) - n, 2)       # only the act whose first choice is a 404

    def test_act_that_left_force_is_removed_and_listed_with_its_end_of_validity(self):
        self.run_update("initial")
        (self.cfg / "nomes-comuns.txt").write_text("regulamento-ue-2016-679 | RGPD | RGPD\n", encoding="utf-8")
        a = self.eu.act("32022R1903")
        a["left"], a["end"] = True, "2026-09-30"
        rc, _ = self.run_update("weekly", client=self.eu.client())
        self.assertEqual(rc, 0)
        self.assertFalse((self.repo / "regulamentos/2022/regulamento-ue-2022-1903.md").exists())
        self.assertFalse((self.repo / "regulamentos/2022").exists())                 # empty folder pruned
        text = (self.repo / "revogados.md").read_text(encoding="utf-8")
        self.assertIn("| regulamento-ue-2022-1903 | Regulamento (UE) 2022/1903 do Conselho | 2026-09-30 | https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022R1903 |", text)
        self.assertNotIn("regulamento-ue-2022-1903", (self.repo / "indice-regulamentos.md").read_text(encoding="utf-8"))

    def test_other_files_of_the_repo_are_never_touched(self):
        keep = ("README.md", "scripts/x.py", "config/y.txt", "spec/z.xml", "plugin/a.md", "regulamentos/README.md")
        for rel in keep:
            (self.repo / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / rel).write_text("keep", encoding="utf-8")
        self.run_update("initial")
        self.run_update("weekly", client=self.eu.client())
        for rel in keep:
            self.assertEqual((self.repo / rel).read_text(encoding="utf-8"), "keep")

    def test_big_act_is_split_with_the_70_kb_default(self):
        big = self.eu.act("32016R0679")
        big["docs"]["02016R0679-20160504"] = big["docs"]["02016R0679-20160504"].replace(
            "</body>", "<p class=\"norm\">" + "Palavra repetida. " * 9000 + "</p></body>")
        self.run_update("initial")
        sizes = [p.stat().st_size for p in self.repo.rglob("*.md") if "regulamento-ue-2016-679" in p.name]
        self.assertGreater(len(sizes), 1)


class UpdateFailure(UpdateCase):
    def setUp(self):
        super().setUp()
        self.run_update("initial")
        self.before = snapshot(self.repo)

    def assertUntouched(self):
        self.assertEqual(snapshot(self.repo), self.before)

    def weekly(self, **kw):
        return self.run_update("weekly", client=self.eu.client(), **kw)

    def test_validation_error_blocks_everything(self):
        real = convert.build_items

        def lossy(events):                     # as if the converter had lost the text of one article (the heading stays)
            items = real(events)
            it = next(i for i in items if i.art)
            it.md = it.md.split("\n")[0]
            return items
        a = self.eu.act("32016R0679")
        a["cons"].append(("2026-09-01", "02016R0679-20260901"))
        a["docs"]["02016R0679-20260901"] = a["docs"]["02016R0679-20160504"]
        with mock.patch.object(convert, "build_items", lossy):
            rc, out = self.weekly()
        self.assertEqual(rc, 1)
        self.assertNotIn("CHANGED", out)
        err = self.errors()
        self.assertEqual(err["stage"], "validate")
        self.assertIn("empty_article", {e["code"] for e in err["errors"]})
        self.assertUntouched()

    def test_article_count_different_from_the_xhtml_blocks(self):
        real = convert.build_items

        def lossy(events):                     # as if the converter had lost one article
            items = real(events)
            drop = next((i for i, it in enumerate(items) if it.art), None)
            return items[:drop] + items[drop + 1:] if drop is not None else items
        gdpr = self.eu.act("32016R0679")
        gdpr["cons"].append(("2026-09-01", "02016R0679-20260901"))
        gdpr["docs"]["02016R0679-20260901"] = gdpr["docs"]["02016R0679-20160504"]
        with mock.patch.object(convert, "build_items", lossy):
            rc, _ = self.weekly()
        self.assertEqual(rc, 1)
        self.assertIn("article_count_mismatch", {e["code"] for e in self.errors()["errors"]})
        self.assertUntouched()

    def test_service_change_and_slow_down_request_block(self):
        self.eu.fault = lambda n, url: "garbage" if n > 2 else None
        rc, _ = self.weekly()
        self.assertEqual((rc, self.errors()["stage"]), (1, "fetch"))
        self.assertUntouched()
        self.eu.fault = lambda n, url: 503
        rc, _ = self.weekly()
        self.assertEqual(rc, 1)
        self.assertUntouched()

    def test_index_failure_blocks(self):
        (self.cfg / "nomes-comuns.txt").write_text("regulamento-ue-9999-1 | Nome | N\n", encoding="utf-8")
        rc, _ = self.weekly()
        err = self.errors()
        self.assertEqual((rc, err["stage"], err["errors"][0]["code"]), (1, "index", "index_error"))
        self.assertUntouched()

    def test_repo_over_the_size_limit_blocks(self):
        rc, _ = self.weekly(size_limit=1000)
        self.assertEqual((rc, self.errors()["errors"][0]["code"]), (1, "repo_too_big"))
        self.assertUntouched()

    def test_transposition_section_of_unchanged_acts_follows_the_current_list_of_portuguese_ids(self):
        (self.cfg / "pt-ids.txt").write_text("lei-34-2009\n", encoding="utf-8")        # decreto-lei-47-2023 does not exist now
        rc, _ = self.weekly()
        # weekly copies unchanged acts from the repo and refreshes their transposition section with the new id list
        self.assertEqual(rc, 0)
        text = (self.repo / "diretivas/2009/diretiva-ue-2009-1.md").read_text(encoding="utf-8")
        self.assertNotIn("id: decreto-lei-47-2023", text)

    def test_unexpected_exception_is_a_failure_not_a_half_written_repo(self):
        with mock.patch.object(convert, "convert_all", side_effect=RuntimeError("boom")):
            rc, _ = self.weekly()
        self.assertEqual((rc, self.errors()["errors"][0]["code"]), (1, "internal_error"))
        self.assertUntouched()

    def test_copy_failure_during_the_swap_is_rolled_back(self):
        gdpr = self.eu.act("32016R0679")
        gdpr["cons"].append(("2026-09-01", "02016R0679-20260901"))
        gdpr["docs"]["02016R0679-20260901"] = gdpr["docs"]["02016R0679-20160504"].replace("Objeto e objetivos", "Objeto novo")
        real = common.atomic_write
        calls = []

        def flaky(path, data, binary=False):
            calls.append(path)
            if len(calls) == 2 and "stage" not in str(path):
                raise OSError("disk full")
            return real(path, data, binary)
        with mock.patch.object(run_update, "atomic_write", flaky):
            rc, _ = self.weekly()
        self.assertEqual(rc, 1)
        self.assertUntouched()


class Budget(UpdateCase):
    def test_budget_reached_exit_2_leaves_the_repo_untouched_and_the_next_run_finishes(self):
        for i in range(10):
            self.eu.acts.append(dict(self.eu.act("32022R1903"), celex=f"320{10 + i}R00{10 + i}",
                                     docs={f"320{10 + i}R00{10 + i}": self.eu.act("32022R1903")["docs"]["32022R1903"]}))
        rc, out = self.run_update("initial", budget_seconds=8)
        self.assertEqual(rc, 2)
        self.assertEqual(snapshot(self.repo), {})
        self.assertNotIn("CHANGED", out)
        self.assertFalse((self.raw / "errors.json").exists())
        done = len(self.eu.requests_to("/resource/celex/"))
        rc, out = self.run_update("initial", client=self.eu.client(), budget_seconds=100000)
        self.assertEqual(rc, 0)
        self.assertIn("CHANGED=true", out)
        docs = [e[1] for e in self.eu.requests_to("/resource/celex/")]
        self.assertEqual(len(docs), len(set(docs)))
        self.assertGreater(len(docs), done)


class Cli(UpdateCase):
    def test_main_wires_the_arguments_and_enforces_the_30_to_50_names_rule(self):
        with mock.patch.object(run_update, "Cellar", lambda: self.eu.client()), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = run_update.main(["--mode", "initial", "--raw", str(self.raw), "--repo", str(self.repo),
                                  "--config", str(self.cfg), "--budget-seconds", "100000"])
        self.assertEqual(rc, 1)                      # the fixture list has 2 entries; the rule asks for 30 to 50
        err = self.errors()
        self.assertEqual(err["stage"], "index")
        self.assertIn("30 to 50", err["errors"][0]["message"])
        self.assertEqual(snapshot(self.repo), {})


class CheckSize(TmpCase):
    def git(self, *args):
        subprocess.run(["git", "-C", str(self.tmp), *args], check=True, capture_output=True)

    def test_prints_both_numbers_and_fails_over_the_limit(self):
        self.git("init", "-q")
        (self.tmp / "a.bin").write_bytes(b"x" * 5000)
        self.git("add", "a.bin")
        self.git("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "x")
        ok, objs, work = check_size.check(self.tmp)
        self.assertTrue(ok)
        self.assertEqual(work, 5000)
        self.assertFalse(check_size.check(self.tmp, limit=4000)[0])           # tracked tree too big
        self.assertFalse(check_size.check(self.tmp, limit=objs - 1)[0])       # git objects too big
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = check_size.main(["--repo", str(self.tmp), "--limit-bytes", "4000"])
        self.assertEqual(rc, 1)
        self.assertIn("git objects:", buf.getvalue())
        self.assertIn("working tree: 5000 bytes", buf.getvalue())
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(check_size.main(["--repo", str(self.tmp)]), 0)

    def test_untracked_files_do_not_count_but_a_given_tree_does(self):
        self.git("init", "-q")
        (self.tmp / "big.bin").write_bytes(b"x" * 9000)
        self.assertEqual(check_size.check(self.tmp)[2], 0)
        self.assertEqual(check_size.check(self.tmp, tree=self.tmp)[2], 9000)


if __name__ == "__main__":
    unittest.main()
