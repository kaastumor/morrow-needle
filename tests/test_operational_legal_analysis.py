import pytest

from needle.operations.legal_analysis import OperationalLegalAnalysisError, analyze_operational_legal, apply_operational_recency_gate, collapse_evidence_candidates, derive_operational_relevance, should_attempt_legal_analysis

EVENT={"event_key":"evt-1","action":"UPDATE"}; CHANGE={"event_key":"evt-1","change_id":"chg-1","classification":"UNRESOLVED"}
EXPLANATION={"what_changed":"An authentic act inserts two rows.","compared_with":"The placement anchor named by the authentic instruction.","when_it_matters":"As established by the authentic act.","affected":[],"evidence_character":"DIRECT"}
def candidate(**overrides):
    value={"semantic_key":"mutation:annex-v:insert:rows-a-b","outcome":"LEGAL_CHANGE_VERIFIED","verification_route":"AUTHENTIC_LEGAL_CAUSE","canonical_refs":[{"kind":"MUTATION","entity_id":"mutation-1"}],"evidence_refs":["authentic-act:1","authentic-instruction:1"],"evidence_occurrences":["formex-stream:1"],"explanation":EXPLANATION,"unknowns":[]}; value.update(overrides); return value
def bound_recency(legal,state,refs,dimension=None,relevant_at=None):
    value={"state":state,"assertion_refs":refs,"legal_analysis_identity":legal["analysis_identity"]}
    if dimension: value["relevance_dimension"]=dimension
    if relevant_at: value["relevant_at"]=relevant_at
    return value
def temporal(assertion_id,dimension,boundary,value=None,state="RESOLVED_ABSOLUTE"):
    return {"assertion_id":assertion_id,"dimension":dimension,"boundary":boundary,"normalized_date":value,"resolution_state":state}

def test_duplicate_representations_are_one_legal_candidate():
    collapsed=collapse_evidence_candidates([candidate(),candidate(evidence_occurrences=["formex-stream:2"])]); assert len(collapsed)==1; assert collapsed[0]["evidence_occurrences"]==["formex-stream:1","formex-stream:2"]
def test_same_semantic_key_with_conflicting_truth_fails_closed():
    with pytest.raises(OperationalLegalAnalysisError,match="conflicting canonical candidates"): collapse_evidence_candidates([candidate(),candidate(outcome="LEGAL_NON_IMPACT_VERIFIED")])
def test_authentic_cause_positive_is_generic_and_idempotent():
    first=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); second=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(evidence_occurrences=["formex-stream:2"])]); assert first["disposition"]=="LEGAL_CHANGE_VERIFIED"; assert first["analysis_identity"]==second["analysis_identity"]
def test_current_publication_can_surface_while_application_is_future():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); recency=derive_operational_relevance(legal,temporal_assertions=[temporal("pub","PUBLICATION","POINT","2026-09-21"),temporal("app","APPLICATION","START","2027-01-01")],window_start="2026-09-21",window_end="2026-09-22"); outcome=apply_operational_recency_gate(legal,recency=recency); assert outcome["disposition"]=="LEGAL_CHANGE_VERIFIED"; assert outcome["recency"]["relevance_dimension"]=="PUBLICATION"
def test_historical_publication_can_surface_at_current_application_start():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); recency=derive_operational_relevance(legal,temporal_assertions=[temporal("pub","PUBLICATION","POINT","2025-01-01"),temporal("app","APPLICATION","START","2026-09-21")],window_start="2026-09-21",window_end="2026-09-22"); assert recency["state"]=="CURRENT_RELEVANT"; assert recency["relevance_dimension"]=="APPLICATION_START"
def test_old_legal_events_do_not_get_resurrected_by_fresh_source_update():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); recency=derive_operational_relevance(legal,temporal_assertions=[temporal("pub","PUBLICATION","POINT","2025-01-01"),temporal("app","APPLICATION","START","2025-02-01")],window_start="2026-09-21",window_end="2026-09-22"); assert recency["state"]=="HISTORICAL_NOT_CURRENT"; assert apply_operational_recency_gate(legal,recency=recency)["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
def test_context_dependent_temporal_trigger_abstains():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); recency=derive_operational_relevance(legal,temporal_assertions=[temporal("entity-trigger","APPLICATION","START",state="CONTEXT_REQUIRED")],window_start="2026-09-21",window_end="2026-09-22"); assert recency["state"]=="CONTEXT_REQUIRED"; assert apply_operational_recency_gate(legal,recency=recency)["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
def test_multiple_current_relevance_events_fail_closed_without_precedence_rule():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); recency=derive_operational_relevance(legal,temporal_assertions=[temporal("pub","PUBLICATION","POINT","2026-09-21"),temporal("force","LEGAL_FORCE","START","2026-09-21")],window_start="2026-09-21",window_end="2026-09-22"); assert recency["state"]=="CONFLICTING"
def test_future_only_assertion_does_not_make_item_current():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); recency=derive_operational_relevance(legal,temporal_assertions=[temporal("app","APPLICATION","START","2027-01-01")],window_start="2026-09-21",window_end="2026-09-22"); assert recency["state"]=="UNRESOLVED"
def test_current_relevance_without_typed_dimension_fails_closed():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    with pytest.raises(OperationalLegalAnalysisError,match="relevance_dimension"): apply_operational_recency_gate(legal,recency=bound_recency(legal,"CURRENT_RELEVANT",["temporal:any"],relevant_at="2026-09-21"))
def test_source_timestamp_is_not_a_relevance_dimension():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    with pytest.raises(OperationalLegalAnalysisError,match="relevance_dimension"): apply_operational_recency_gate(legal,recency=bound_recency(legal,"CURRENT_RELEVANT",["source:updated"],"CELLAR_UPDATE","2026-09-21"))
def test_current_relevance_requires_evidenced_time():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    with pytest.raises(OperationalLegalAnalysisError,match="relevant_at"): apply_operational_recency_gate(legal,recency=bound_recency(legal,"CURRENT_RELEVANT",["temporal:publication"],"PUBLICATION"))
def test_recency_evidence_for_another_legal_analysis_cannot_cross_bind():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    with pytest.raises(OperationalLegalAnalysisError,match="bind to the gated legal_analysis_identity"): apply_operational_recency_gate(legal,recency={"state":"CURRENT_RELEVANT","assertion_refs":["temporal:real"],"legal_analysis_identity":"other","relevance_dimension":"PUBLICATION","relevant_at":"2026-09-21"})
def test_verified_cause_without_recency_evidence_abstains():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()]); assert apply_operational_recency_gate(legal,recency=None)["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
def test_no_supported_candidate_abstains_instead_of_inferring_from_update(): assert analyze_operational_legal(EVENT,CHANGE,candidates=[])["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
def test_cold_start_with_current_observation_reaches_legal_analysis(): assert should_attempt_legal_analysis(relevance="LEGAL_RESOURCE_CANDIDATE",source_change={"classification":"UNRESOLVED","classification_basis":["FEED_ACTION","MISSING_BASELINE"]})
def test_missing_current_observation_stays_source_unresolved(): assert not should_attempt_legal_analysis(relevance="LEGAL_RESOURCE_CANDIDATE",source_change={"classification":"UNRESOLVED","classification_basis":["MISSING_BASELINE","MISSING_OBSERVATION"]})
def test_non_legal_source_never_reaches_legal_analysis(): assert not should_attempt_legal_analysis(relevance="SOURCE_INFRASTRUCTURE",source_change={"classification":"CONTENT_CHANGED","classification_basis":["CONTENT_HASH_CHANGED"]})
def test_distinct_verified_candidates_do_not_get_arbitrarily_selected():
    other=candidate(semantic_key="mutation:other",canonical_refs=[{"kind":"MUTATION","entity_id":"mutation-2"}],evidence_refs=["authentic-act:2"]); assert analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(),other])["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
def test_change_and_non_impact_conflict_abstains(): assert analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(),candidate(semantic_key="review:scope-a",outcome="LEGAL_NON_IMPACT_VERIFIED",canonical_refs=[])])["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
def test_unknown_verification_route_is_rejected():
    with pytest.raises(OperationalLegalAnalysisError,match="allowed verification_route"): analyze_operational_legal(EVENT,CHANGE,candidates=[candidate(verification_route="MODEL")])
