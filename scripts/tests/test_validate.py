"""Validator tests (eu.rule.validation): blockers, warnings, parts, counts, transposition ids."""
import json
import shutil
import unittest

from helpers import TmpCase, common, xhtml_fixture

import convert
import validate

BODY = "# T\n\n## Artigo 1.º — Objeto\n\nTexto um.\n\n## Artigo 2.º — Âmbito\n\nTexto dois.\n"


def codes(issues):
    return sorted({i["code"] for i in issues})


class Blocking(TmpCase):
    def check(self, meta=None, body=BODY, expected=None, extra=None, pt_ids=None):
        root = self.tmp / "tree"
        self.write_act(root, "regulamentos/2016/regulamento-ue-2016-679.md", meta or {}, body)
        for rel, m, b in extra or []:
            self.write_act(root, rel, m, b)
        return validate.validate(root, expected, pt_ids)

    def test_control_file_is_accepted(self):
        self.assertEqual(self.check(expected={"32016R0679": {"articles": 2, "recitals": 0, "kind": "consolidated"}}), ([], []))

    def test_every_blocker_is_rejected(self):
        broken = {
            "incomplete metadata": (dict(meta={"date": None}), "incomplete_metadata"),
            "celex missing": (dict(meta={"celex": None}), "missing_celex"),
            "source missing": (dict(meta={"source": None}), "missing_source"),
            "source not EUR-Lex": (dict(meta={"source": "https://example.org/x"}), "missing_source"),
            "type outside Regulamento/Diretiva": (dict(meta={"type": "Decisão"}), "unknown_type"),
            "empty article": (dict(body="# T\n\n## Artigo 1.º\n\n## Artigo 2.º\n\nTexto.\n"), "empty_article"),
            "duplicate id": (dict(extra=[("regulamentos/2016/outra/regulamento-ue-2016-679.md", {"celex": "32016R0680"}, BODY)]), "duplicate_id"),
            "duplicate celex": (dict(extra=[("regulamentos/2016/regulamento-ue-2016-680.md", {"id": "regulamento-ue-2016-680"}, BODY)]), "duplicate_celex"),
            "article count differs from the XHTML": (dict(expected={"32016R0679": {"articles": 3, "recitals": 0, "kind": "consolidated"}}), "article_count_mismatch"),
            "recitals missing in an original": (dict(meta={"text_version": "original sem consolidação", "last_amended": None, "consolidated_celex": None},
                                                    expected={"32016R0679": {"articles": 2, "recitals": 5, "kind": "original"}}), "recitals_missing"),
            "id does not match the celex": (dict(meta={"celex": "32016R0999"}), "bad_id"),
            "consolidated without last_amended": (dict(meta={"last_amended": None}), "incomplete_metadata"),
            "original with a consolidation date": (dict(meta={"text_version": "original sem consolidação"}), "incomplete_metadata"),
        }
        for name, (case, expect) in broken.items():
            with self.subTest(name):
                shutil.rmtree(self.tmp / "tree", ignore_errors=True)
                errors, _ = self.check(**case)
                self.assertIn(expect, codes(errors))

    def test_amendment_note_lines_do_not_make_an_empty_article_non_empty(self):
        errors, _ = self.check(body="# T\n\n## Artigo 1.º\n\n- *Alterado*\n")
        self.assertIn("empty_article", codes(errors))

    def test_recitals_are_counted_inside_the_considerandos_section_only(self):
        body = "# T\n\n## Considerandos\n\n(1) Um.\n\n(2) Dois.\n\n## Artigo 1.º\n\nTexto.\n\n(3) numeração dentro do artigo.\n"
        meta = {"text_version": "original sem consolidação", "last_amended": None, "consolidated_celex": None}
        ok, _ = self.check(meta=meta, body=body, expected={"32016R0679": {"articles": 1, "recitals": 2, "kind": "original"}})
        self.assertEqual(ok, [])

    def test_file_name_and_id_must_agree(self):
        root = self.tmp / "tree"
        self.write_act(root, "regulamentos/2016/outro-nome.md", {}, BODY)
        errors, _ = validate.validate(root)
        self.assertEqual(codes(errors), ["bad_id"])

    def test_json_output_and_exit_code(self):
        root = self.tmp / "tree"
        self.write_act(root, "regulamentos/2016/regulamento-ue-2016-679.md", {"source": None}, BODY)
        out = self.tmp / "errors.json"
        self.assertEqual(validate.main(["--root", str(root), "--json", str(out)]), 1)
        data = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(data["errors"][0]["code"], "missing_source")
        self.assertEqual(set(data["errors"][0]), {"code", "file", "celex", "message"})

    def test_clean_tree_exit_code_0(self):
        root = self.tmp / "tree"
        self.write_act(root, "regulamentos/2016/regulamento-ue-2016-679.md", {}, BODY)
        self.assertEqual(validate.main(["--root", str(root)]), 0)


class Warnings(TmpCase):
    def test_gap_in_numbering_is_only_a_warning(self):
        root = self.tmp / "tree"
        self.write_act(root, "regulamentos/2016/regulamento-ue-2016-679.md", {},
                       "# T\n\n## Artigo 1.º\n\nA.\n\n## Artigo 2.º\n\nB.\n\n## Artigo 5.º\n\nC.\n")
        errors, warnings = validate.validate(root)
        self.assertEqual(errors, [])
        self.assertEqual(codes(warnings), ["numbering_gap"])

    def test_the_marker_of_a_bare_article_is_a_warning_but_a_truly_empty_article_is_an_error(self):
        root = self.tmp / "tree"
        path = "regulamentos/2016/regulamento-ue-2016-679.md"
        self.write_act(root, path, {}, f"# T\n\n## Artigo 1.º\n\n{common.EMPTY_MARK}\n\n## Artigo 2.º\n\nB.\n")
        errors, warnings = validate.validate(root)
        self.assertEqual((errors, codes(warnings)), ([], ["article_without_text"]))
        self.write_act(root, path, {}, "# T\n\n## Artigo 1.º\n\n## Artigo 2.º\n\nB.\n")
        self.assertEqual(codes(validate.validate(root)[0]), ["empty_article"])

    def test_act_without_articles_is_accepted_with_a_warning(self):
        root = self.tmp / "tree"
        self.write_act(root, "regulamentos/2016/regulamento-ue-2016-679.md", {}, "# T\n\nTexto corrido.\n")
        errors, warnings = validate.validate(root, {"32016R0679": {"articles": 0, "recitals": 0, "kind": "consolidated"}})
        self.assertEqual(errors, [])
        self.assertEqual(codes(warnings), ["no_articles"])

    def test_large_file_is_reported(self):
        root = self.tmp / "tree"
        self.write_act(root, "regulamentos/2016/regulamento-ue-2016-679.md", {}, BODY + "x" * 95_000 + "\n")
        self.assertIn("large_file", codes(validate.validate(root)[1]))


class Transposition(TmpCase):
    SECTION = "\n## Transposição para Portugal\n\n- Decreto-Lei n.º 47/2023, de 19 de junho de 2023 (id: decreto-lei-47-2023)\n- Portaria n.º 999/2021\n"

    def tree(self, ids_line):
        root = self.tmp / "tree"
        self.write_act(root, "diretivas/2019/diretiva-ue-2019-790.md",
                       {"id": "diretiva-ue-2019-790", "celex": "32019L0790", "type": "Diretiva", "number": "2019/790",
                        "year": 2019, "source": "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02019L0790-20190517"},
                       BODY + "\n## Transposição para Portugal\n\n" + ids_line)
        return root

    def test_existing_id_passes_and_invented_id_is_blocked(self):
        ids = {"decreto-lei-47-2023"}
        ok = self.tree("- Decreto-Lei n.º 47/2023 (id: decreto-lei-47-2023)\n- Portaria n.º 999/2021\n")
        self.assertEqual(validate.validate(ok, None, ids)[0], [])
        shutil.rmtree(self.tmp / "tree")
        bad = self.tree("- Decreto-Lei n.º 48/2023 (id: decreto-lei-48-2023)\n")
        self.assertEqual(codes(validate.validate(bad, None, ids)[0]), ["invented_transposition_id"])

    def test_the_section_is_not_part_of_the_last_article(self):
        root = self.tree("- Portaria n.º 999/2021\n")
        self.assertEqual(validate.validate(root, {"32019L0790": {"articles": 2, "recitals": 0, "kind": "consolidated"}}, set())[0], [])


class PartsTest(TmpCase):
    def converted(self, max_bytes=8_000):
        from test_convert import GDPR, conv_gdpr
        out = self.tmp / "out"
        for rel, text in conv_gdpr(max_bytes).files:
            p = out / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")
        return out

    def test_three_or_more_parts_sharing_a_celex_are_accepted_with_a_complete_overview(self):
        out = self.converted()
        errors, _ = validate.validate(out, {"32016R0679": {"articles": 11, "recitals": 0, "kind": "consolidated"}})
        self.assertEqual(errors, [])
        self.assertGreater(len(list(out.rglob("*.md"))), 4)

    def test_overview_missing_a_part_is_rejected(self):
        out = self.converted()
        ov = next(out.rglob("regulamento-ue-2016-679.md"))
        lines = ov.read_text(encoding="utf-8").splitlines()
        i = next(k for k, ln in enumerate(lines) if ln.startswith("| ") and ".md |" in ln)
        del lines[i]
        ov.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertIn("overview_incomplete", codes(validate.validate(out)[0]))

    def test_wrong_range_in_the_overview_is_rejected(self):
        out = self.converted()
        ov = next(out.rglob("regulamento-ue-2016-679.md"))
        t = ov.read_text(encoding="utf-8")
        i = t.index("| 1.º |")
        ov.write_text(t[:i] + "| 7.º |" + t[i + 7:], encoding="utf-8")
        self.assertIn("overview_range_mismatch", codes(validate.validate(out)[0]))

    def test_same_part_title_twice_for_one_celex_is_a_duplicate(self):
        out = self.converted()
        part = next(p for p in out.rglob("*.md") if "-capitulo-i-" in p.name)
        meta, body = common.parse_frontmatter(part.read_text(encoding="utf-8"))
        dup = part.with_name(part.name.replace("capitulo-i", "capitulo-x"))
        dup.write_text(part.read_text(encoding="utf-8").replace(meta["id"], meta["id"].replace("capitulo-i", "capitulo-x")), encoding="utf-8")
        self.assertIn("duplicate_celex", codes(validate.validate(out)[0]))


class Ids(TmpCase):
    def test_generated_ids_validate_and_are_unique(self):
        from test_convert import conv_gdpr
        out = self.tmp / "out"
        for rel, text in conv_gdpr().files:
            (out / rel).parent.mkdir(parents=True, exist_ok=True)
            (out / rel).write_text(text, encoding="utf-8")
        self.assertEqual(validate.validate(out)[0], [])
        ids = [m["id"] for m in common.main_files(out)]
        self.assertEqual(ids, ["regulamento-ue-2016-679"])


if __name__ == "__main__":
    unittest.main()
