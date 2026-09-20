import importlib.util
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).parents[1] / "scripts" / "probe_cellar.py"
spec = importlib.util.spec_from_file_location("probe_cellar", SCRIPT)
probe_cellar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe_cellar)


class RepresentationSelectionTests(unittest.TestCase):
    def test_modern_prefers_fmx4_over_xhtml_and_pdf(self):
        rows = [
            {"format":"xhtml","manif":"m.03","item":"m.03/DOC_1","expr":"e","work":"w","langCode":"ENG"},
            {"format":"pdf","manif":"m.02","item":"m.02/DOC_1","expr":"e","work":"w","langCode":"ENG"},
            {"format":"fmx4","manif":"m.05","item":"m.05/DOC_132","expr":"e","work":"w","langCode":"ENG"},
        ]
        selected = probe_cellar.select_sparql_representation(rows)
        self.assertEqual(selected["format"], "fmx4")
        self.assertEqual(selected["representation_class"], "STRUCTURED_LEGAL_XML")
        self.assertEqual(selected["manifestation_uri"], "m.05")
        self.assertEqual(selected["item_uris"], ["m.05/DOC_132"])

    def test_historical_falls_back_to_html_before_pdf(self):
        rows = [
            {"format":"pdfa1b","manif":"m.01","item":"m.01/DOC_1","expr":"e","work":"w","langCode":"ENG"},
            {"format":"html","manif":"m.02","item":"m.02/DOC_1","expr":"e","work":"w","langCode":"ENG"},
        ]
        selected = probe_cellar.select_sparql_representation(rows)
        self.assertEqual(selected["format"], "html")
        self.assertEqual(selected["representation_class"], "STRUCTURED_HTML")

    def test_items_are_grouped_under_manifestation(self):
        rows = [
            {"format":"fmx4","manif":"m.05","item":"m.05/DOC_1","expr":"e","work":"w","langCode":"ENG"},
            {"format":"fmx4","manif":"m.05","item":"m.05/DOC_2","expr":"e","work":"w","langCode":"ENG"},
        ]
        selected = probe_cellar.select_sparql_representation(rows)
        self.assertEqual(selected["item_uris"], ["m.05/DOC_1", "m.05/DOC_2"])
        self.assertIsNone(selected["internal_stream_count"])

    def test_empty_inventory_abstains(self):
        self.assertIsNone(probe_cellar.select_sparql_representation([]))


if __name__ == "__main__":
    unittest.main()
