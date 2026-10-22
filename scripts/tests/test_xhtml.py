"""XHTML reader tests: events, inline text, lists and tables, amendment markers, counts."""
import collections
import unittest

from helpers import xhtml_fixture

import xhtml


def doc(body):
    return f"<html><body>{body}</body></html>"


def texts(ev):
    return [e[1] for e in ev if e[0] == "text"]


class Events(unittest.TestCase):
    def test_consolidated_gdpr_structure(self):
        ev = xhtml.events(xhtml_fixture("gdpr-trimmed-consolidated.xhtml"))
        c = collections.Counter(e[0] for e in ev)
        self.assertEqual((c["article"], c["epigraph"], c["div1"], c["div2"]), (11, 11, 2, 2))
        self.assertEqual(ev[0], ("enc",))                                   # the title block, ToC and notes are dropped
        self.assertIn(("article", "Artigo 5.º"), ev)                        # superscript o -> º
        self.assertIn(("epigraph", "Princípios relativos ao tratamento de dados pessoais"), ev)
        self.assertIn(("div1", "CAPÍTULO II"), ev)
        self.assertIn(("div2", "Princípios"), ev)

    def test_list_items_and_numbered_paragraphs(self):
        t = texts(xhtml.events(xhtml_fixture("gdpr-trimmed-consolidated.xhtml")))
        self.assertIn("1. Os dados pessoais são:", t[t.index("1. Os dados pessoais são:"):][:1])
        i = t.index("1. Os dados pessoais são:")
        self.assertTrue(t[i + 1].startswith("a) Objeto de um tratamento lícito, leal e transparente"))

    def test_text_next_to_inline_elements_is_kept(self):
        # regression: "n.<sup>o</sup> 1" inside a div with direct text lost the text
        ev = xhtml.events(doc('<div id="art_1"><p class="title-article-norm">Artigo 1.<span class="superscript">o</span></p>'
                              '<div class="norm"><span class="no-parag">2. </span><div class="norm inline-element">Nos termos do n.'
                              '<span class="superscript">o</span> 1, aplica-se.</div></div></div>'))
        self.assertEqual(ev, [("article", "Artigo 1.º"), ("text", "2. Nos termos do n.º 1, aplica-se.")])

    def test_amendment_markers_are_dropped(self):
        ev = xhtml.events(doc('<p class="title-article-norm">Artigo 1.</p><p class="norm">►M1 O texto alterado ◄ continua.</p>'
                              '<p class="norm"><a href="x">▼B</a></p><p class="arrow"><a>►M2</a></p>'))
        self.assertEqual(texts(ev), ["O texto alterado continua."])

    def test_annex_and_recital_events_in_an_original(self):
        ev = xhtml.events(xhtml_fixture("dir-original-2009-1.xhtml"))
        self.assertEqual([e[0] for e in ev if e[0] in ("pbl", "recital", "enc")][:6], ["pbl", "recital", "recital", "recital", "recital", "enc"])
        self.assertEqual([e[1] for e in ev if e[0] == "recital"], ["1", "2", "3", "4"])
        self.assertTrue(all(e[2].startswith(f"({e[1]}) ") for e in ev if e[0] == "recital"))
        ev = xhtml.events(doc('<div id="anx_1"><p class="oj-doc-ti">ANEXO I</p><p class="oj-doc-ti">Lista de produtos</p>'
                              '<p class="oj-normal">Texto do anexo.</p></div>'))
        self.assertEqual(ev[:3], [("anx_start", "anx_1"), ("annex", "ANEXO I"), ("text", "ANEXO I")])


class Tables(unittest.TestCase):
    def md(self, table):
        return xhtml.table_blocks(next(n for n in xhtml.parse(table).iter() if n.tag == "table"))

    def test_marker_column_becomes_a_list(self):
        out = self.md("<table><tr><td><p>a)</p></td><td><p>primeira</p></td></tr><tr><td><p>b)</p></td><td><p>segunda</p></td></tr></table>")
        self.assertEqual(out, ["a) primeira", "b) segunda"])

    def test_plain_table_with_colspan_is_markdown(self):
        out = self.md('<table><tr><td><p>A</p></td><td colspan="2"><p>B</p></td></tr><tr><td><p>1</p></td><td><p>2</p></td><td><p>3</p></td></tr></table>')
        self.assertEqual(out, ["| A | B |  |\n|---|---|---|\n| 1 | 2 | 3 |"])

    def test_rowspan_or_nesting_falls_back_to_compact_html(self):
        out = self.md('<table><tr><td rowspan="2"><p>A</p></td><td><p>B</p></td></tr><tr><td><p>C</p></td></tr></table>')
        self.assertEqual(len(out), 1)
        self.assertTrue(out[0].startswith("<table>") and 'rowspan="2"' in out[0] and "<p>" not in out[0])

    def test_single_column_layout_table_is_flattened(self):
        self.assertEqual(self.md("<table><tr><td><p>Um</p></td></tr><tr><td><p>Dois</p></td></tr></table>"), ["Um", "Dois"])

    def test_pipes_in_cells_are_escaped(self):
        out = self.md("<table><tr><td><p>x|y</p></td><td><p>z</p></td><td><p>w</p></td></tr></table>")
        self.assertIn("x\\|y", out[0])


class SourceQuirks(unittest.TestCase):
    def test_article_headings_with_typos_are_normalised_so_none_is_dropped(self):
        for raw, want in [("Article 1.o", "Artigo 1.º"), ("Artigio 17.o A", "Artigo 17.º A"), ("Artigos 8.o", "Artigo 8.º"),
                          ("Artigo12.o", "Artigo 12.º"), ("«Artigo 7.o-D", "Artigo 7.º-D"), ("Article 66", "Artigo 66"),
                          ("ARTIGO 3.o", "Artigo 3.º")]:
            with self.subTest(raw):
                tag = raw.replace(".o", '.<span class="superscript">o</span>')
                self.assertEqual(xhtml.events(doc(f'<p class="title-article-norm">{tag}</p>')), [("article", want)])

    def test_a_table_caption_with_the_article_class_is_text_not_an_article(self):
        html = doc('<p class="title-article-norm">Artigo 1.</p><p class="title-article-norm">Quadro 6:</p>')
        self.assertEqual(xhtml.events(html), [("article", "Artigo 1."), ("text", "**Quadro 6:**")])
        self.assertEqual(xhtml.scan_counts(html)["articles"], 1)

    def test_recital_marker_printed_without_the_opening_parenthesis_is_restored(self):
        cell = '<table><tbody><tr><td><p class="oj-normal">%s</p></td><td><p class="oj-normal">Texto.</p></td></tr></tbody></table>'
        for marker in ("(5)", "5)"):
            with self.subTest(marker):
                self.assertEqual(xhtml.events(doc(f'<div id="rct_5">{cell % marker}</div>')), [("recital", "5", "(5) Texto.")])


class Counts(unittest.TestCase):
    def test_counts_are_taken_on_the_raw_markup(self):
        c = xhtml.scan_counts(xhtml_fixture("dir-original-2009-1.xhtml"))
        self.assertEqual((c["articles"], c["recitals"]), (5, 4))
        c = xhtml.scan_counts(xhtml_fixture("gdpr-trimmed-consolidated.xhtml"))
        self.assertEqual((c["articles"], c["recitals"]), (11, 0))

    def test_old_texts_without_ids_count_article_titles(self):
        c = xhtml.scan_counts(doc('<p class="title-article-norm">Artigo 1.</p><p class="title-article-norm">Artigo 2.</p>'))
        self.assertEqual((c["articles"], c["article_ids"], c["article_titles"]), (2, 0, 2))


if __name__ == "__main__":
    unittest.main()
