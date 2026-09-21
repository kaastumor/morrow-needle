import pytest

from needle.operations.legal_analysis import (
    OperationalLegalAnalysisError,
    analyze_operational_legal,
    apply_operational_recency_gate,
    collapse_evidence_candidates,
    should_attempt_legal_analysis,
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
    first=candidate(); second=candidate(evidence_occurrences=["formex-stream:2"])
    collapsed=collapse_evidence_candidates([first,second])
    assert len(collapsed) == 1
    assert collapsed[0]["evidence_occurrences"] == ["formex-stream:1","formex-stream:2"]


def test_same_semantic_key_with_conflicting_truth_fails_closed():
    with pytest.raises(OperationalLegalAnalysisError,match="conflicting canonical candidates"):
        collapse_evidence_candidates([candidate(),candidate(outcome="LEGAL_NON_IMPACT_VERIFIED")])


def test_authentic_cause_positive_is_generic_and_idempotent():
    first=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); second=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(evidence_occurrences=["formex-stream:2"])])
    assert first["disposition"] == "LEGAL_CHANGE_VERIFIED"
    assert first["verification_route"] == "AUTHENTIC_LEGAL_CAUSE"
    assert first["canonical_refs"][0]["kind"] == "MUTATION"
    assert first["analysis_identity"] == second["analysis_identity"]


def test_recent_authentic_cause_requires_canonical_recency_evidence():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    outcome=apply_operational_recency_gate(legal,recency={
        "state":"CURRENT_RELEVANT","assertion_refs":["temporal-assertion:application-start"]
    })
    assert outcome["disposition"] == "LEGAL_CHANGE_VERIFIED"
    assert outcome["recency"]["state"] == "CURRENT_RELEVANT"
    assert "temporal-assertion:application-start" in outcome["evidence_refs"]


def test_fresh_feed_update_cannot_resurrect_historical_legal_cause():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    outcome=apply_operational_recency_gate(legal,recency={
        "state":"HISTORICAL_NOT_CURRENT","assertion_refs":["temporal-assertion:historical-effect"]
    })
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert outcome["canonical_refs"] == legal["canonical_refs"]
    assert "historical rather than newly relevant" in outcome["unknowns"][-1]


def test_verified_cause_without_recency_evidence_abstains():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    outcome=apply_operational_recency_gate(legal,recency=None)
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert outcome["recency"]["state"] == "UNRESOLVED"
    assert "lacks canonical temporal/procedural evidence" in outcome["unknowns"][-1]


def test_recency_positive_without_evidence_ref_is_rejected():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    with pytest.raises(OperationalLegalAnalysisError,match="requires canonical"):
        apply_operational_recency_gate(legal,recency={"state":"CURRENT_RELEVANT","assertion_refs":[]})


def test_no_supported_candidate_abstains_instead_of_inferring_from_update():
    outcome=analyze_operational_legal(EVENT,CHANGE,candidates=[])
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert outcome["canonical_refs"] == []
    assert outcome["verification_route"] is None


def test_cold_start_with_current_observation_reaches_legal_analysis():
    change={"classification":"UNRESOLVED","classification_basis":["FEED_ACTION","MISSING_BASELINE"]}
    assert should_attempt_legal_analysis(relevance="LEGAL_RESOURCE_CANDIDATE",source_change=change)


def test_missing_current_observation_stays_source_unresolved():
    change={"classification":"UNRESOLVED","classification_basis":["MISSING_BASELINE","MISSING_OBSERVATION"]}
    assert not should_attempt_legal_analysis(relevance="LEGAL_RESOURCE_CANDIDATE",source_change=change)


def test_non_legal_source_never_reaches_legal_analysis():
    change={"classification":"CONTENT_CHANGED","classification_basis":["CONTENT_HASH_CHANGED"]}
    assert not should_attempt_legal_analysis(relevance="SOURCE_INFRASTRUCTURE",source_change=change)


def test_distinct_verified_candidates_do_not_get_arbitrarily_selected():
    other=candidate(semantic_key="mutation:other",canonical_refs=[{"kind":"MUTATION","entity_id":"mutation-2"}],evidence_refs=["authentic-act:2"])
    outcome=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(),other])
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert "automatic selection is forbidden" in outcome["unknowns"][0]


def test_change_and_non_impact_conflict_abstains():
    non_impact=candidate(semantic_key="review:scope-a",outcome="LEGAL_NON_IMPACT_VERIFIED",canonical_refs=[])
    outcome=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(),non_impact])
    assert outcome["disposition"] == "ABSTAIN_LEGAL_UNRESOLVED"
    assert "conflicting" in outcome["unknowns"][0]


def test_unknown_verification_route_is_rejected():
    with pytest.raises(OperationalLegalAnalysisError,match="allowed verification_route"):
        analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(verification_route="MODEL")])
