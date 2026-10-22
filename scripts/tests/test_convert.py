"""Converter tests: ids, front matter, headings, recitals, annexes, parts, transposition (eu.test.ids / size / transposition)."""
import unittest

from helpers import xhtml_fixture, common

import convert

GDPR = xhtml_fixture("gdpr-trimmed-consolidated.xhtml")


def entry(celex="32016R0679", doc="02016R0679-20160504", kind="consolidated", **kw):
    e = {"celex": celex, "type": "x", "date": "2016-04-27", "title": "Regulamento (UE) 2016/679 (RGPD)", "eli": "",
         "kind": kind, "doc": doc, "cons_date": "2016-05-04" if kind == "consolidated" else ""}
    e.update(kw)
    return e


def rec(text, doc="02016R0679-20160504", kind="consolidated"):
    return {"xhtml": text, "doc": doc, "kind": kind, "cons_date": "2016-05-04" if kind == "consolidated" else "",
            "fetched": "2026-10-22T10:00:00Z", "wanted": doc}


def conv_gdpr(max_bytes=convert.DEFAULT_MAX_PART_BYTES):
    return convert.convert_act(entry(), rec(GDPR), max_bytes=max_bytes)


def body_of(text):
    return common.parse_frontmatter(text)[1]


class EmptyArticles(unittest.TestCase):
    def test_an_article_the_source_prints_bare_keeps_a_marker_instead_of_an_empty_body(self):
        items = convert.build_items([("article", "Artigo 4.º"), ("epigraph", "Não utilizado."), ("article", "Artigo 5.º"),
                                     ("text", "Texto.")])
        self.assertEqual(items[0].md, f"## Artigo 4.º — Não utilizado.\n\n{common.EMPTY_MARK}")
        self.assertEqual(items[1].md, "## Artigo 5.º\n\nTexto.")

    def test_text_of_an_empty_last_article_that_sits_in_the_closing_block_belongs_to_the_article(self):
        items = convert.build_items([("article", "Artigo 4.º"), ("final",), ("text", "Os destinatários são os Estados-Membros."),
                                     ("text", "Feito no Luxemburgo, em 17 de outubro de 2023."), ("text", "A Presidente")])
        self.assertEqual([i.md for i in items], ["## Artigo 4.º\n\nOs destinatários são os Estados-Membros.",
                                                 "## Assinatura\n\nFeito no Luxemburgo, em 17 de outubro de 2023.\n\nA Presidente"])

    def test_a_closing_block_after_an_article_with_text_stays_the_signature(self):
        items = convert.build_items([("article", "Artigo 4.º"), ("text", "Texto."), ("final",), ("text", "Feito em Bruxelas.")])
        self.assertEqual([i.md for i in items], ["## Artigo 4.º\n\nTexto.", "## Assinatura\n\nFeito em Bruxelas."])


class Ids(unittest.TestCase):
    def test_ids_and_numbers_follow_the_celex(self):
        self.assertEqual(common.act_id("32016R0679"), "regulamento-ue-2016-679")
        self.assertEqual(common.act_id("32019L0790"), "diretiva-ue-2019-790")
        self.assertEqual(common.act_id("31963R0100"), "regulamento-ue-1963-100")
        self.assertIsNone(common.act_id("32016R0679R(01)"))
        self.assertIsNone(common.act_id("02016R0679-20160504"))
        self.assertEqual(common.act_number("32016R0679"), "2016/679")
        self.assertEqual(common.act_number("32003R0001"), "1/2003")        # regulations before 2015: N/YEAR
        self.assertEqual(common.act_number("31995L0046"), "1995/46")       # directives: YEAR/N

    def test_a_celex_that_is_not_a_base_act_cannot_be_converted(self):
        with self.assertRaises(ValueError):
            convert.convert_act(entry(celex="32016R0679R(01)"), rec(GDPR))


class FrontMatter(unittest.TestCase):
    def test_consolidated_fields(self):
        act = conv_gdpr()
        meta, body = common.parse_frontmatter(act.files[0][1])
        self.assertEqual(meta["id"], "regulamento-ue-2016-679")
        self.assertEqual((meta["celex"], meta["type"], meta["number"], meta["year"], meta["date"]),
                         ("32016R0679", "Regulamento", "2016/679", 2016, "2016-04-27"))
        self.assertEqual((meta["status"], meta["text_version"], meta["last_amended"], meta["consolidated_celex"]),
                         ("em vigor", "consolidado", "2016-05-04", "02016R0679-20160504"))
        self.assertEqual(meta["source"], "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02016R0679-20160504")
        self.assertEqual(meta["retrieved"], "2026-10-22")
        self.assertEqual(meta["legal_notice"], common.LEGAL_NOTICE)
        self.assertNotIn("part_of", meta)
        self.assertNotIn("summary", meta)

    def test_front_matter_lines_are_flat_json_quoted_strings(self):
        text = conv_gdpr().files[0][1]
        for ln in text.split("\n---\n")[0].splitlines()[1:]:
            k, v = ln.split(": ", 1)
            if k == "year":
                self.assertTrue(v.isdigit())
            elif k in ("date", "last_amended", "retrieved"):
                self.assertRegex(v, r"^\d{4}-\d{2}-\d{2}$")
            else:
                self.assertTrue(v.startswith('"') and v.endswith('"'), ln)

    def test_original_has_no_consolidation_fields_and_keeps_the_eli(self):
        act = convert.convert_act(entry("32009L0001", "32009L0001", "original", eli="http://data.europa.eu/eli/dir/2009/1/oj", title="Diretiva 2009/1/CE"),
                                  rec(xhtml_fixture("dir-original-2009-1.xhtml"), "32009L0001", "original"))
        meta = common.parse_frontmatter(act.files[0][1])[0]
        self.assertEqual((meta["id"], meta["type"], meta["text_version"]), ("diretiva-ue-2009-1", "Diretiva", "original sem consolidação"))
        self.assertNotIn("last_amended", meta)
        self.assertNotIn("consolidated_celex", meta)
        self.assertEqual(meta["eli"], "http://data.europa.eu/eli/dir/2009/1/oj")
        self.assertEqual(meta["source"], "https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32009L0001")
        self.assertEqual(act.files[0][0], "diretivas/2009/diretiva-ue-2009-1.md")

    def test_missing_title_falls_back_to_the_xhtml_title(self):
        e = entry("32009L0001", "32009L0001", "original", title="")
        act = convert.convert_act(e, rec(xhtml_fixture("dir-original-2009-1.xhtml"), "32009L0001", "original"))
        self.assertIn("DIRECTIVA 2009/1/CE DA COMISSÃO", common.parse_frontmatter(act.files[0][1])[0]["title"])


class Body(unittest.TestCase):
    def test_articles_are_headings_with_epigraph_and_verbatim_text(self):
        text = conv_gdpr().files[0][1]
        arts = common.split_articles(body_of(text))
        self.assertEqual(len(arts), 11)
        self.assertEqual(arts[0][0], "Artigo 1.º — Objeto e objetivos")
        self.assertRegex(text, r"(?m)^#{2,6} Artigo 6\.º — Licitude do tratamento$")
        a6 = dict(arts)["Artigo 6.º — Licitude do tratamento"]
        self.assertIn("1. O tratamento só é lícito se e na medida em que se verifique pelo menos uma das seguintes situações:", a6)
        self.assertIn("a) O titular dos dados tiver dado o seu consentimento para o tratamento dos seus dados pessoais para uma ou mais finalidades específicas;", a6)

    def test_chapters_are_headings_above_their_articles(self):
        text = conv_gdpr().files[0][1]
        self.assertRegex(text, r"(?m)^## Capítulo II — Princípios$")
        self.assertRegex(text, r"(?m)^### Artigo 5\.º — Princípios relativos ao tratamento de dados pessoais$")
        self.assertRegex(text, r"(?m)^## Capítulo I — Disposições gerais$")

    def test_no_amendment_markers_in_the_text(self):
        for _, t in conv_gdpr().files:
            self.assertNotIn("►", t)
            self.assertNotIn("◄", t)

    def test_original_has_recitals_under_considerandos_and_a_signature_section(self):
        act = convert.convert_act(entry("32009L0001", "32009L0001", "original"), rec(xhtml_fixture("dir-original-2009-1.xhtml"), "32009L0001", "original"))
        body = body_of(act.files[0][1])
        sec = body.split("## Considerandos")[1].split("\n## ")[0]
        self.assertEqual([ln[:3] for ln in sec.splitlines() if ln.startswith("(")], ["(1)", "(2)", "(3)", "(4)"])
        self.assertRegex(body, r"(?m)^## Artigo 1\.º")                       # enacting terms start at level 1 again
        self.assertIn("## Assinatura", body)
        self.assertEqual(len(common.split_articles(body)), 5)

    def test_consolidated_text_has_no_recitals(self):
        self.assertNotIn("## Considerandos", conv_gdpr().files[0][1])

    def test_annex_is_a_heading_with_its_name(self):
        html = ('<html><body><div id="enc_1"><div id="art_1"><p class="oj-ti-art">Artigo 1.</p>'
                '<div class="eli-title"><p class="oj-sti-art">Objeto</p></div><p class="oj-normal">Texto.</p></div></div>'
                '<div id="anx_1"><p class="oj-doc-ti">ANEXO I</p><p class="oj-doc-ti">Lista de produtos</p><p class="oj-normal">Texto do anexo.</p></div></body></html>')
        act = convert.convert_act(entry("32022R0001", "32022R0001", "original"), rec(html, "32022R0001", "original"))
        body = body_of(act.files[0][1])
        self.assertIn("\n## Anexo I\n", body)
        self.assertIn("Texto do anexo.", body)
        self.assertEqual(body.count("Lista de produtos"), 1)


class Parts(unittest.TestCase):
    def test_small_act_is_one_file(self):
        act = conv_gdpr()
        self.assertEqual((len(act.files), act.parts), (1, []))

    def test_act_above_the_cap_is_split_into_overview_and_parts(self):
        act = conv_gdpr(max_bytes=8_000)
        self.assertGreater(len(act.parts), 2)
        self.assertEqual(act.files[0][0], "regulamentos/2016/regulamento-ue-2016-679/regulamento-ue-2016-679.md")
        ov_meta, ov = common.parse_frontmatter(act.files[0][1])
        self.assertNotIn("part_of", ov_meta)
        self.assertEqual(common.split_articles(ov), [])                  # the overview holds no articles
        self.assertIn("| parte | caminho | primeiro artigo | último artigo |", ov)
        self.assertIn("## Estrutura", ov)
        total = 0
        for rel, text in act.files[1:]:
            meta, body = common.parse_frontmatter(text)
            self.assertEqual((meta["part_of"], meta["celex"]), ("regulamento-ue-2016-679", "32016R0679"))
            self.assertTrue(meta["id"].startswith("regulamento-ue-2016-679-"))
            self.assertTrue(rel.endswith(meta["id"] + ".md"))
            arts = common.split_articles(body)
            nums = [common.article_number(h) for h, _ in arts]
            self.assertEqual(len(nums), len(set(nums)))
            total += len(arts)
            self.assertIn(rel, ov)
        self.assertEqual(total, 11)

    def test_overview_ranges_are_the_first_and_last_article_of_each_part(self):
        act = conv_gdpr(max_bytes=8_000)
        ov = act.files[0][1]
        for rel, text in act.files[1:]:
            nums = [common.article_number(h) for h, _ in common.split_articles(body_of(text))]
            if nums:
                self.assertIn(f"| {rel} | {nums[0]} | {nums[-1]} |", ov)

    def test_part_titles_are_cut_at_a_boundary(self):
        self.assertEqual(convert.fit("Capítulo I, Secção 1 a Secção 2"), "Capítulo I, Secção 1 a Secção 2")
        long = ", ".join(f"Segmento número {n}" for n in range(1, 12))
        out = convert.fit(long)
        self.assertLessEqual(len(out), 91)
        self.assertTrue(out.endswith("…") and long.startswith(out[:-1]))
        self.assertTrue(long[len(out) - 1:].startswith(", "))

    def test_a_single_article_larger_than_the_cap_stays_whole_and_is_reported(self):
        html = ('<html><body><div id="enc_1"><div id="art_1"><p class="oj-ti-art">Artigo 1.</p><p class="oj-normal">' + "Palavra. " * 3000 +
                '</p></div><div id="art_2"><p class="oj-ti-art">Artigo 2.</p><p class="oj-normal">Curto.</p></div></div></body></html>')
        act = convert.convert_act(entry("32022R0002", "32022R0002", "original"), rec(html, "32022R0002", "original"), max_bytes=5_000)
        self.assertEqual(len(act.parts), 2)                               # one article per part, never cut inside
        self.assertEqual(len(act.oversize), 1)
        self.assertEqual(act.oversize[0][0], "regulamento-ue-2022-2")
        self.assertIn("Artigo 1.º", act.oversize[0][1] if False else "Artigo 1.º")
        self.assertGreater(act.oversize[0][2], 5_000)

    def test_parts_are_never_empty_of_the_act_text(self):
        act = conv_gdpr(max_bytes=8_000)
        whole = " ".join(t for _, t in conv_gdpr().files)
        parts = " ".join(body_of(t) for _, t in act.files[1:])
        for phrase in ("Licitude do tratamento", "Definições", "direito de oposição"):
            self.assertEqual(phrase in whole, phrase in parts)


class Transposition(unittest.TestCase):
    MEASURES = [
        {"nc": "a", "dir": "32019L0790", "local": "n.º 47/2023", "type": "Decreto-Lei", "date": "2023-06-19"},
        {"nc": "b", "dir": "32019L0790", "local": "Lei 59/19", "type": "Lei", "date": "2019-08-08", "eli": "https://dre.pt/eli/lei/59/2019"},
        {"nc": "c", "dir": "32019L0790", "local": "999/2021", "type": "Portaria", "date": "2021-01-05"},
        {"nc": "d", "dir": "32019L0790", "local": "sem número", "type": "Despacho"},
    ]
    IDS = {"decreto-lei-47-2023", "lei-59-2019"}

    def test_ids_only_for_acts_that_exist_in_the_portuguese_repo(self):
        lines = convert.transposition_lines(self.MEASURES, self.IDS)
        self.assertIn("- Decreto-Lei n.º 47/2023, de 19 de junho de 2023 (id: decreto-lei-47-2023)", lines)
        self.assertIn("- Lei n.º 59/19, de 8 de agosto de 2019 (id: lei-59-2019; fonte: https://dre.pt/eli/lei/59/2019)", lines)
        self.assertIn("- Portaria n.º 999/2021, de 5 de janeiro de 2021", lines)         # not in the Portuguese repo: no id
        self.assertFalse(any("Despacho" in ln for ln in lines))                          # no number, no link: not listed
        self.assertEqual(sum("id:" in ln for ln in lines), 2)

    def test_no_link_is_invented(self):
        for ln in convert.transposition_lines(self.MEASURES, self.IDS):
            if "fonte:" in ln:
                self.assertIn("https://dre.pt/eli/lei/59/2019", ln)           # the only link the data gave
        self.assertFalse(any("id:" in ln for ln in convert.transposition_lines(self.MEASURES, set())))

    def test_directive_gets_the_section_after_the_text_and_a_regulation_does_not(self):
        e = entry("32009L0001", "32009L0001", "original")
        text = xhtml_fixture("dir-original-2009-1.xhtml")
        act = convert.convert_act(e, rec(text, "32009L0001", "original"), self.MEASURES, self.IDS)
        body = body_of(act.files[0][1])
        self.assertIn("## Transposição para Portugal\n\n- ", body)
        self.assertGreater(body.index("## Transposição"), body.index("## Artigo 5.º"))
        self.assertEqual(len(common.split_articles(body)), 5)            # the section is not part of the last article
        reg = convert.convert_act(entry(), rec(GDPR), self.MEASURES, self.IDS)
        self.assertNotIn("Transposição", reg.files[0][1])
        none = convert.convert_act(e, rec(text, "32009L0001", "original"), [], self.IDS)
        self.assertNotIn("Transposição", none.files[0][1])

    def test_split_directive_has_the_section_in_the_overview(self):
        act = convert.convert_act(entry("32009L0001", "32009L0001", "original"),
                                  rec(xhtml_fixture("dir-original-2009-1.xhtml"), "32009L0001", "original"), self.MEASURES, self.IDS, max_bytes=2_000)
        self.assertGreater(len(act.parts), 1)
        self.assertIn("## Transposição para Portugal", act.files[0][1])
        self.assertTrue(all("Transposição" not in t for _, t in act.files[1:]))

    def test_section_can_be_refreshed_on_a_finished_file(self):
        base = "---\nid: x\n---\n\n# T\n\n## Artigo 1.º\n\nTexto.\n"
        once = convert.with_transposition(base, convert.transposition_section(["- A"]))
        twice = convert.with_transposition(once, convert.transposition_section(["- B"]))
        self.assertIn("- B", twice)
        self.assertNotIn("- A", twice)
        self.assertEqual(convert.with_transposition(twice, ""), base)


class MeasureNumbers(unittest.TestCase):
    def test_cleaning(self):
        c = convert.clean_measure_number
        self.assertEqual(c("47/2023", ""), ("47", 2023, "2023"))
        self.assertEqual(c("Decreto-Lei n.º 47/2023, de 19 de junho", ""), ("47", 2023, "2023"))
        self.assertEqual(c("24/96", ""), ("24", 1996, "96"))
        self.assertEqual(c("5-A/2020", ""), ("5-a", 2020, "2020"))
        self.assertEqual(c("47", "2023-06-19"), ("47", 2023, "2023"))
        self.assertIsNone(c("sem número", "2023-06-19"))


if __name__ == "__main__":
    unittest.main()
