import json
from pathlib import Path

from needle.mutation.instructions import (
    parse_authentic_corrigendum_replacements,
    parse_authentic_instructions,
)
from needle.mutation.reconcile import reconcile_candidate


FIXTURE = json.loads(Path("fixtures/mutations/reg2015-1536-authentic-replacement-instructions-v0.1.json").read_text())


def _candidate():
    return {
        "candidate_id":"test-authentic-replace",
        "operation":"REPLACE",
        "target":{"kind":"PARAGRAPH","citation_path":"Article 4 > 1","parent_citation_path":"Article 4","language":"ENG"},
        "alignment_basis":"EXACT_CITATION_AND_KIND",
        "before":None,"after":None,
        "feature_deltas":{"numbers_added":[],"numbers_removed":[],"dates_added":[],"dates_removed":[],"references_added":[],"references_removed":[]},
        "reconciliation_state":"DIFF_ONLY","verification_state":"UNVERIFIED",
        "supporting_evidence":[],"conflicting_evidence":[],"notes":None,
    }


def test_explicit_authentic_replacement_becomes_canonical_cause():
    evidence = parse_authentic_instructions(
        FIXTURE["excerpt"], source_id="CELEX:32015R1536", locator="Article 1(4)"
    )
    assert evidence == [FIXTURE["expected_evidence"]]
    result = reconcile_candidate(_candidate(), evidence)
    assert result["reconciliation_state"] == "CORROBORATED"
    assert result["verification_state"] == "VERIFIED"


def test_ambiguous_amendment_language_abstains():
    assert parse_authentic_instructions(
        "Article 3 is amended as follows:", source_id="CELEX:test"
    ) == []


def test_bare_similarity_or_consolidation_wording_abstains():
    assert parse_authentic_instructions(
        "Article 3 now contains substantially similar text.", source_id="CELEX:test"
    ) == []



def test_explicit_corrigendum_for_read_becomes_canonical_cause():
    text = (
        "On page 21 in the second line of Article 4 (1): "
        "1.2 // for: // '. . . shall be ECU 225 . . .', // "
        "read: // '. . . shall be ECU 255 . . .'."
    )
    replacements = parse_authentic_corrigendum_replacements(
        text,
        source_id="CELEX:31990R2742R(01)",
        locator="normalized-visible-text#chars:553-683",
    )
    assert len(replacements) == 1
    replacement = replacements[0]
    assert replacement["target_locator"] == "Article 4 > 1"
    assert "ECU 225" in replacement["before_text"]
    assert "ECU 255" in replacement["after_text"]

    candidate = _candidate()
    candidate["target"]["language"] = "ENG"
    result = reconcile_candidate(candidate, [replacement["evidence"]])
    assert result["verification_state"] == "VERIFIED"
    assert result["reconciliation_state"] == "CORROBORATED"
    assert result["supporting_evidence"] == [replacement["evidence"]]


def test_corrigendum_parser_abstains_without_exact_subdivision():
    assert parse_authentic_corrigendum_replacements(
        "for: 'ECU 225', read: 'ECU 255'",
        source_id="CELEX:test",
    ) == []


def test_corrigendum_parser_abstains_without_for_read_pair():
    assert parse_authentic_corrigendum_replacements(
        "On page 21 in Article 4 (1): the amount is corrected.",
        source_id="CELEX:test",
    ) == []
