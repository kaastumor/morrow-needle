import pytest

from needle.operations.legal_analysis import (
    OperationalLegalAnalysisError,
    analyze_operational_legal,
    collapse_evidence_candidates,
)

EVENT={"event_key":"evt-1","action":"UPDATE"}
CHANGE={"event_key":"evt-1","change_id":"chg-1","classification":"UNRESOLVED"}
EXPLANATION={
    "what_changed":"An authentic act inserts two rows.",
    "compared_with":"The placement anchor named by the authentic instruction.",
    "when_it_matters":"As established by the authentic act.",
    "affected":[],
    "evidence_character":"DIRECT",
}


def candidate(**overrides):
    value={
        "semantic_key":"mutation:annex-v:insert:rows-a-b",
        "outcome":"LEGAL_CHANGE_VERIFIED",
        "verification_route":"AUTHENTIC_LEGAL_CAUSE",
        "canonical_refs":[{"kind":"MUTATION","entity_id":"mutation-1"}],
        "evidence_refs":["authentic-act:1","authentic-instruction:1"],
        "evidence_occurrences":["formex-stream:1"],
        "explanation":EXPLANATION,
        "unknowns":[],
    }
    value.update(overrides)
    return value


def test_duplicate_representations_are_one_legal_candidate():
    first=candidate()
    second=candidate(evidence_occurrences=["formex-stream:2"])
    collapsed=collapse_evidence_candidates([first,second])
    assert len(collapsed) == 1
    assert collapsed[0]["evidence_occurrences"] == ["formex-stream:1","formex-stream:2"]


def test_same_semantic_key_with_conflicting_truth_fails_closed():
    with pytest.raises(OperationalLegalAnalysisError,match="conflicting canonical candidates"):
        collapse_evidence_candidates([candidate(),candidate(outcome="LEGAL_NON_IMPACT_VERIFIED")])


def test_authentic_cause_positive_is_generic_and_idempotent():
    first=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    second=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(evidence_occurrences=["formex-stream:2"])])
    assert first["disposition"] == "LEGAL_CHANGE_VERIFIED"
    assert first["verification_route"] == "AUTHENTIC_LEGAL_CAUSE"
    assert first["canonical_refs"][0]["kind"] == "MUTATION"
    assert first["analysis_identity"] == second["analysis_identity"]


def test_no_supported_candidate_abstains_instead_of_inferring_from_update():
    outcome=analyze_operational_legal(EVENT,CHANGE,candidates=[])
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert outcome["canonical_refs"] == []
    assert outcome["verification_route"] is None


def test_distinct_verified_candidates_do_not_get_arbitrarily_selected():
    other=candidate(
        semantic_key="mutation:other",
        canonical_refs=[{"kind":"MUTATION","entity_id":"mutation-2"}],
        evidence_refs=["authentic-act:2"],
    )
    outcome=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(),other])
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert "automatic selection is forbidden" in outcome["unknowns"][0]


def test_change_and_non_impact_conflict_abstains():
    non_impact=candidate(
        semantic_key="review:scope-a",
        outcome="LEGAL_NON_IMPACT_VERIFIED",
        canonical_refs=[],
    )
    outcome=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(),non_impact])
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert "conflicting" in outcome["unknowns"][0]


def test_unknown_verification_route_is_rejected():
    with pytest.raises(OperationalLegalAnalysisError,match="allowed verification_route"):
        analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(verification_route="MODEL")])
