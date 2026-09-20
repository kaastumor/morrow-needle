import unittest

from scripts.validate_gold_corpus import semantic_errors


class GoldCorpusSemanticContractTests(unittest.TestCase):
    def base_case(self):
        return {
            "official_sources": [{"source_id": "official"}],
            "expected": {
                "document_relationships": [],
                "provision_alignments": [],
                "textual_mutations": [],
                "change_atoms": [],
                "non_atoms": [],
                "temporal_assertions": [],
            },
            "verification": {"state": "EVIDENCED", "requirements": ["review"]},
        }

    def test_rejects_unknown_evidence_reference(self):
        case = self.base_case()
        case["expected"]["provision_alignments"] = [{
            "assertion_id": "lineage.a",
            "expectation": "x",
            "evidence_source_ids": ["missing"],
            "status": "ASSERTED",
        }]
        self.assertTrue(any("unknown evidence_source_ids" in e for e in semantic_errors(case)))

    def test_rejects_unsupported_forbidden_inference(self):
        case = self.base_case()
        case["expected"]["non_atoms"] = [{
            "assertion_id": "forbid.a",
            "expectation": "x",
            "evidence_source_ids": [],
            "status": "FORBIDDEN_INFERENCE",
        }]
        self.assertTrue(any("requires official evidence" in e for e in semantic_errors(case)))

    def test_rejects_duplicate_assertion_ids_across_buckets(self):
        case = self.base_case()
        assertion = {
            "assertion_id": "same.id",
            "expectation": "x",
            "evidence_source_ids": ["official"],
            "status": "ASSERTED",
        }
        case["expected"]["document_relationships"] = [assertion]
        case["expected"]["provision_alignments"] = [dict(assertion)]
        self.assertTrue(any("duplicate assertion_id" in e for e in semantic_errors(case)))

    def test_verified_cannot_hide_unresolved_assertions(self):
        case = self.base_case()
        case["verification"] = {"state": "VERIFIED", "requirements": ["review"], "verified_by": ["reviewer"]}
        case["expected"]["change_atoms"] = [{
            "assertion_id": "atom.uncertain",
            "expectation": "x",
            "evidence_source_ids": ["official"],
            "status": "UNRESOLVED",
        }]
        self.assertTrue(any("unsettled assertions" in e for e in semantic_errors(case)))


if __name__ == "__main__":
    unittest.main()
