import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "src" / "needle" / "formex" / "modifications.py"
spec = importlib.util.spec_from_file_location("formex_modifications", MODULE)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class FormexModificationTests(unittest.TestCase):
    def test_article_3_structural_replacement(self):
        text = (
            '<?CLG.MDFO ID="O003001M001000" IDREF="C003001M001000" '
            'ACTION="REPLACED" LEVEL="STRUCTURE" COMMAND="EXPLICIT" '
            'ACTIVE.DOC="32008R0271" ACTIVE.LOC="AR:1;PT:1" MOD.LEVEL="1"?>'
            '<ARTICLE IDENTIFIER="003"><TI.ART>Article 3</TI.ART></ARTICLE>'
            '<?CLG.MDFC ID="C003001M001000" IDREF="O003001M001000"?>'
        )
        result = mod.parse_modification_markers(text, source_entry="fixture.xml")
        self.assertEqual(result.unmatched_open_ids, ())
        self.assertEqual(result.unmatched_close_ids, ())
        self.assertEqual(len(result.markers), 1)
        marker = result.markers[0]
        self.assertEqual(marker.action, "REPLACED")
        self.assertEqual(marker.level, "STRUCTURE")
        self.assertEqual(marker.active_doc, "32008R0271")
        self.assertEqual(marker.active_loc, "AR:1;PT:1")
        self.assertEqual(marker.mod_level, 1)

    def test_nested_corrigendum_is_not_flattened(self):
        text = (
            '<?CLG.MDFO ID="O011001M005000" IDREF="C011001M005000" '
            'ACTION="REPLACED" LEVEL="TEXT" COMMAND="EXPLICIT" '
            'ACTIVE.DOC="32025R0905" ACTIVE.LOC="AR:1;PT:4;PT:b" MOD.LEVEL="1"?>'
            '<?CLG.MDFO ID="O012002M001000" IDREF="C012002M001000" '
            'ACTION="REPLACED" LEVEL="TEXT" COMMAND="EXPLICIT" '
            'ACTIVE.DOC="32025R0905R(01)" ACTIVE.LOC="TO" MOD.LEVEL="2"?>'
            'However an increase in the original budget...'
            '<?CLG.MDFC ID="C012002M001000" IDREF="O012002M001000"?>'
            '<?CLG.MDFC ID="C011001M005000" IDREF="O011001M005000"?>'
        )
        result = mod.parse_modification_markers(text)
        self.assertEqual(len(result.markers), 2)
        by_doc = {m.active_doc: m for m in result.markers}
        self.assertEqual(by_doc["32025R0905"].mod_level, 1)
        self.assertEqual(by_doc["32025R0905R(01)"].mod_level, 2)
        self.assertGreater(by_doc["32025R0905"].end_offset, by_doc["32025R0905R(01)"].end_offset)

    def test_unmatched_marker_fails_visibly(self):
        result = mod.parse_modification_markers(
            '<?CLG.MDFO ID="O1" IDREF="C1" ACTION="REPLACED" LEVEL="TEXT" '
            'COMMAND="EXPLICIT" ACTIVE.DOC="32025R0905" ACTIVE.LOC="AR:1" MOD.LEVEL="1"?>x'
        )
        self.assertEqual(result.unmatched_open_ids, ("O1",))
        self.assertEqual(len(result.markers), 0)


if __name__ == "__main__":
    unittest.main()
