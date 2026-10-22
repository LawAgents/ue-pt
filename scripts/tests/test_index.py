"""Index tests (eu.schema.index): common names, shards of at most 40 KB, manifest, revoked list."""
import re
import shutil
import unittest

from helpers import FIX, FakeClock, FakeEU, TODAY, TmpCase, common

import build_index
import convert
import fetch


class IndexCase(TmpCase):
    def build_tree(self):
        eu = FakeEU(FakeClock())
        raw = fetch.Raw(self.tmp / "raw")
        self.assertEqual(fetch.run_fetch(eu.client(), raw, "initial", today=TODAY, log=lambda m: None), 0)
        out = self.tmp / "tree"
        convert.convert_all(raw.dir, out, None, None)
        self.cfg = self.config_dir()
        return out

    def run_index(self, out, **kw):
        kw.setdefault("check_count", False)
        return build_index.build_all(out, self.cfg, **kw)


class CommonNames(IndexCase):
    def test_generator_fails_when_an_id_of_the_list_is_missing(self):
        out = self.build_tree()
        self.run_index(out)
        shutil.rmtree(out / "regulamentos" / "2016")                                  # the GDPR disappears
        with self.assertRaises(build_index.IndexError_) as cm:
            self.run_index(out)
        self.assertIn("regulamento-ue-2016-679", str(cm.exception))
        self.assertEqual(build_index.main(["--root", str(out), "--config", str(self.cfg), "--no-count-check"]), 1)

    def test_missing_file_and_wrong_number_of_entries_fail(self):
        out = self.build_tree()
        with self.assertRaises(build_index.IndexError_) as cm:
            build_index.build_all(out, self.cfg)                                      # the fixture has 2 entries
        self.assertIn("30 to 50", str(cm.exception))
        (self.cfg / "nomes-comuns.txt").unlink()
        with self.assertRaises(build_index.IndexError_):
            self.run_index(out)

    def test_names_and_acronyms_are_written_with_the_path(self):
        out = self.build_tree()
        self.run_index(out)
        text = (out / "nomes-comuns.md").read_text(encoding="utf-8")
        self.assertIn("| nome comum | siglas | id | caminho |", text)
        self.assertIn("| Regulamento Geral sobre a Proteção de Dados | RGPD, GDPR | regulamento-ue-2016-679 | regulamentos/2016/regulamento-ue-2016-679.md |", text)
        self.assertLessEqual(len(text.encode()), 10 * 1024)


class Contract(IndexCase):
    def test_files_columns_and_sizes_follow_the_schema(self):
        out = self.build_tree()
        written = self.run_index(out)
        self.assertEqual(written, ["indice-diretivas.md", "indice-regulamentos.md", "indice.md", "nomes-comuns.md", "revogados.md"])
        head = "| id | título | caminho | nome comum | siglas | sumário | source | last_amended | text_version |"
        for n in ("indice-regulamentos.md", "indice-diretivas.md"):
            text = (out / n).read_text(encoding="utf-8")
            self.assertIn(head, text.splitlines())
            self.assertLessEqual(len(text.encode()), 40 * 1024)
        self.assertIn("| id | título | data do fim de vigência | ligação oficial |", (out / "revogados.md").read_text(encoding="utf-8"))

    def test_rows_carry_source_last_amended_and_text_version(self):
        out = self.build_tree()
        self.run_index(out)
        regs = (out / "indice-regulamentos.md").read_text(encoding="utf-8").splitlines()
        gdpr = [c.strip() for c in next(ln for ln in regs if ln.startswith("| regulamento-ue-2016-679")).strip("|").split(" | ")]
        self.assertEqual(gdpr[3:5], ["Regulamento Geral sobre a Proteção de Dados", "RGPD, GDPR"])
        self.assertEqual(gdpr[6:], ["https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02016R0679-20160504", "2016-05-04", "consolidado"])
        orig = [c.strip() for c in next(ln for ln in regs if ln.startswith("| regulamento-ue-2022-1903")).strip("|").split(" | ")]
        self.assertTrue(orig[-1] == "original sem consolidação" and orig[-2] == "")

    def test_manifest_lists_every_index_file_with_type_years_and_counts(self):
        out = self.build_tree()
        written = self.run_index(out)
        manifest = (out / "indice.md").read_text(encoding="utf-8")
        self.assertIn("| ficheiro | tipo | ano inicial | ano final | n.º de atos |", manifest)
        for n in written:
            if n.startswith("indice-"):
                self.assertIn(f"| {n} |", manifest)
        self.assertIn("| indice-diretivas.md | Diretiva | 2009 | 2019 | 2 |", manifest)
        self.assertIn("| indice-regulamentos.md | Regulamento | 2010 | 2022 | 3 |", manifest)

    def test_only_overviews_are_listed_not_parts(self):
        out = self.build_tree()
        convert_dir = self.tmp / "tree2"
        raw = fetch.Raw(self.tmp / "raw")
        convert.convert_all(raw.dir, convert_dir, None, None, max_bytes=8_000)
        self.run_index(convert_dir)
        text = (convert_dir / "indice-regulamentos.md").read_text(encoding="utf-8")
        self.assertEqual(text.count("| regulamento-ue-2016-679 |"), 1)
        self.assertNotIn("regulamento-ue-2016-679-capitulo", text)
        for ln in text.splitlines():
            if ln.startswith("| regulamento-ue-2016-679 |"):
                self.assertIn("regulamentos/2016/regulamento-ue-2016-679/regulamento-ue-2016-679.md", ln)


class Sharding(TmpCase):
    def tree(self, years, per_year, summary="x" * 150):
        root = self.tmp / "tree"
        n = 0
        for y in years:
            for i in range(per_year):
                n += 1
                cel = f"3{y}R{n:04d}"
                aid = common.act_id(cel)
                self.write_act(root, f"regulamentos/{y}/{aid}.md", {"id": aid, "celex": cel, "year": y, "number": f"{y}/{n}",
                               "title": f"Regulamento (UE) {y}/{n} com um título razoavelmente comprido para ocupar espaço", "summary": summary,
                               "source": f"https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:{cel}", "consolidated_celex": f"0{cel[1:]}-{y}0101",
                               "last_amended": f"{y}-01-01"}, "# T\n\n## Artigo 1.º\n\nA.\n")
        cfg = self.tmp / "config"
        cfg.mkdir(exist_ok=True)
        first = common.act_id(f"3{years[0]}R0001")
        (cfg / "nomes-comuns.txt").write_text(f"{first} | Um | U\n", encoding="utf-8")
        return root, cfg

    def test_years_are_packed_into_shards_of_at_most_40_kb_without_splitting_a_year(self):
        root, cfg = self.tree(range(2000, 2012), 60)
        names = build_index.build_all(root, cfg, check_count=False)
        shards = sorted(n for n in names if n.startswith("indice-regulamentos"))
        self.assertGreater(len(shards), 1)
        seen = []
        for s in shards:
            self.assertRegex(s, r"^indice-regulamentos-\d{4}-\d{4}\.md$")
            text = (root / s).read_text(encoding="utf-8")
            self.assertLessEqual(len(text.encode()), 40 * 1024)
            years = {int(y) for y in re.findall(r"regulamentos/(\d{4})/", text)}
            self.assertTrue(years.isdisjoint(seen))
            seen += sorted(years)
        self.assertEqual(sorted(seen), list(range(2000, 2012)))

    def test_a_year_above_the_cap_is_cut_by_id_into_lettered_files(self):
        root, cfg = self.tree([2000, 2001], 150)
        names = build_index.build_all(root, cfg, check_count=False)
        shards = sorted(n for n in names if n.startswith("indice-regulamentos"))
        self.assertEqual(shards[:2], ["indice-regulamentos-2000-a.md", "indice-regulamentos-2000-b.md"])
        ids = []
        for s in shards:
            self.assertLessEqual((root / s).stat().st_size, 40 * 1024)
            ids += re.findall(r"(?m)^\| (regulamento-ue-\d+-\d+) ", (root / s).read_text(encoding="utf-8"))
        self.assertEqual(len(ids), 300)
        manifest = (root / "indice.md").read_text(encoding="utf-8")
        self.assertIn("| indice-regulamentos-2000-a.md | Regulamento | 2000 | 2000 |", manifest)
        self.assertIn("| indice-regulamentos-2000-b.md | Regulamento | 2000 | 2000 |", manifest)


class Revoked(IndexCase):
    def test_revoked_list_merges_old_and_new_rows_and_drops_acts_in_force_again(self):
        out = self.build_tree()
        repo = self.tmp / "repo"
        repo.mkdir()
        (repo / "revogados.md").write_text(
            "# Atos revogados\n\n| id | título | data do fim de vigência | ligação oficial |\n|---|---|---|---|\n"
            "| regulamento-ue-1999-9 | Regulamento 9/1999 | 2001-02-03 | https://example.org/a |\n"
            "| regulamento-ue-2016-679 | RGPD | 2001-02-03 | https://example.org/b |\n", encoding="utf-8")
        new = [{"id": "diretiva-ue-1980-5", "title": "Diretiva 80/5", "date": "2026-01-02", "source": "https://example.org/c"}]
        self.run_index(out, repo_dir=repo, revoked_new=new)
        rows = build_index.parse_revoked(out / "revogados.md")
        self.assertEqual([r["id"] for r in rows], ["diretiva-ue-1980-5", "regulamento-ue-1999-9"])   # the GDPR is back in force
        self.assertEqual(rows[0]["date"], "2026-01-02")


if __name__ == "__main__":
    unittest.main()
