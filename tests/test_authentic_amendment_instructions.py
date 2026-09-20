import json
from pathlib import Path

from needle.mutation.instructions import parse_authentic_instructions
from needle.mutation.reconcile import reconcile_candidate


FIXTURE = json.loads(Path("fixtures/mutations/reg312-2008-authentic-replacement-instructions-v0.1.json").read_text())


def _candidate():
    return {
        "candidate_id":"test-authentic-replace",
        "operation":"REPLACE",
        "target":{"kind":"PARAGRAPH","citation_path":"Article 3 > 1","parent_citation_path":"Article 3","language":"ENG"},
        "alignment_basis":"EXACT_CITATION_AND_KIND",
        "before":None,"after":None,
        "feature_deltas":{"numbers_added":[],"numbers_removed":[],"dates_added":[],"dates_removed":[],"references_added":[],"references_removed":[]},
        "reconciliation_state":"DIFF_ONLY","verification_state":"UNVERIFIED",
        "supporting_evidence":[],"conflicting_evidence":[],"notes":None,
    }


def test_explicit_authentic_replacement_becomes_canonical_cause():
    evidence = parse_authentic_instructions(
        FIXTURE["parser_case"], source_id="CELEX:32008R0312", locator="Article 1(1)(a)"
    )
    assert evidence == [FIXTURE["expected_evidence"]]
    result = reconcile_candidate(_candidate(), evidence)
    assert result["reconciliation_state"] == "CORROBORATED"
    assert result["verification_state"] == "VERIFIED"


def test_ambiguous_amendment_language_abstains():
    # 'amended as follows' identifies a container but does not itself say which
    # mutation operation applies; nested instructions must provide that cause.
    assert parse_authentic_instructions(
        "Article 3 is amended as follows:", source_id="CELEX:test"
    ) == []


def test_bare_similarity_or_consolidation_wording_abstains():
    assert parse_authentic_instructions(
        "Article 3 now contains substantially similar text.", source_id="CELEX:test"
    ) == []
