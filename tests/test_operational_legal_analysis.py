import pytest

from needle.operations.authentic_candidates import candidates_from_reobservation
from needle.operations.legal_analysis import OperationalLegalAnalysisError, analyze_operational_legal, apply_operational_recency_gate, collapse_evidence_candidates, derive_feed_event_relevance, derive_operational_relevance, derive_publication_recency_from_reobservation, should_attempt_legal_analysis

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


def test_recurring_reobservation_candidate_stays_out_of_change_feed_without_recency():
    reobservation={
        "celex":"32026R2104",
        "analysis_language":"eng",
        "analysis_text":(
            "ANNEX Annex V is amended as follows: in Part 1, Section B, in the "
            "entry for the United States, the following rows for the zones "
            "US-2.1405 and US-2.1406 are added after the row for the zone "
            "US-2.1404."
        ),
        "content_observation":{
            "record_id":"src-observation:live-2104",
            "payload":{
                "language":"ENG",
                "retrieval":{"final_uri":"official://reg-2104"},
            },
        },
    }
    candidates=candidates_from_reobservation(EVENT,reobservation)
    assert len(candidates)==1
    assert candidates[0]["evidence_refs"]==["src-observation:live-2104"]
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=candidates)
    assert legal["disposition"]=="LEGAL_CHANGE_VERIFIED"
    withheld=apply_operational_recency_gate(legal,recency=None)
    assert withheld["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
    assert withheld["verification_route"]=="AUTHENTIC_LEGAL_CAUSE"
    assert withheld["canonical_refs"]==legal["canonical_refs"]
    assert withheld["recency"]["state"]=="UNRESOLVED"
    assert any(
        "lacks canonical temporal/procedural evidence" in item
        for item in withheld["unknowns"]
    )


def test_reobservation_without_deterministic_text_produces_no_candidate():
    reobservation={
        "celex":"32026R2104",
        "analysis_language":"eng",
        "analysis_text":None,
        "content_observation":{
            "record_id":"src-observation:sealed-only",
            "payload":{
                "language":"ENG",
                "retrieval":{"final_uri":"official://sealed-only"},
            },
        },
    }
    assert candidates_from_reobservation(EVENT,reobservation)==[]


def test_reobservation_without_source_observation_id_produces_no_candidate():
    reobservation={
        "celex":"32026R2104",
        "analysis_language":"eng",
        "analysis_text":(
            "Annex V is amended: in Part 1, Section B, in the entry for the "
            "United States, the following rows for the zones US-2.1405 and "
            "US-2.1406 are added after the row for the zone US-2.1404."
        ),
        "content_observation":{
            "payload":{
                "language":"ENG",
                "retrieval":{"final_uri":"official://missing-record-id"},
            },
        },
    }
    assert candidates_from_reobservation(EVENT,reobservation)==[]


def test_feed_event_day_can_surface_explicit_publication_without_timestamp_laundering():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    recency=derive_feed_event_relevance(
        legal,
        temporal_assertions=[
            temporal("temporal:pub-2104","PUBLICATION","POINT","2026-09-18")
        ],
        ingestion_time="2026-09-18T10:32:20.883+02:00",
    )
    recency["evidence_refs"]=["src-operational-metadata:2104"]
    outcome=apply_operational_recency_gate(legal,recency=recency)
    assert recency["state"]=="CURRENT_RELEVANT"
    assert recency["relevant_at"]=="2026-09-18"
    assert recency["relevant_at"] != "2026-09-18T10:32:20.883+02:00"
    assert recency["novelty_basis"]=="OFFICIAL_FEED_EVENT_DAY"
    assert recency["temporal_precision"]=="DAY"
    assert outcome["disposition"]=="LEGAL_CHANGE_VERIFIED"
    assert {"kind":"TEMPORAL_ASSERTION","entity_id":"temporal:pub-2104"} in (
        outcome["canonical_refs"]
    )
    assert "src-operational-metadata:2104" in outcome["evidence_refs"]


def test_later_feed_refresh_does_not_resurrect_historical_publication():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    recency=derive_feed_event_relevance(
        legal,
        temporal_assertions=[
            temporal("temporal:pub-2104","PUBLICATION","POINT","2026-09-18")
        ],
        ingestion_time="2026-09-21T14:00:00+02:00",
    )
    recency["evidence_refs"]=["src-operational-metadata:refresh"]
    outcome=apply_operational_recency_gate(legal,recency=recency)
    assert recency["state"]=="HISTORICAL_NOT_CURRENT"
    assert outcome["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"
    assert {"kind":"TEMPORAL_ASSERTION","entity_id":"temporal:pub-2104"} in (
        outcome["canonical_refs"]
    )
    assert "src-operational-metadata:refresh" in outcome["evidence_refs"]


def test_future_publication_relative_to_feed_event_day_does_not_surface():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    recency=derive_feed_event_relevance(
        legal,
        temporal_assertions=[
            temporal("temporal:future","PUBLICATION","POINT","2026-09-19")
        ],
        ingestion_time="2026-09-18T23:30:00+02:00",
    )
    assert recency["state"]=="UNRESOLVED"
    assert apply_operational_recency_gate(
        legal,recency=recency
    )["disposition"]=="ABSTAIN_LEGAL_UNRESOLVED"


def test_feed_event_day_uses_explicit_source_offset_not_utc_reinterpretation():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    recency=derive_feed_event_relevance(
        legal,
        temporal_assertions=[
            temporal("temporal:pub","PUBLICATION","POINT","2026-09-18")
        ],
        ingestion_time="2026-09-18T00:15:00+02:00",
    )
    assert recency["event_day"]=="2026-09-18"
    assert recency["state"]=="CURRENT_RELEVANT"


def test_feed_event_relevance_rejects_naive_ingestion_time():
    legal=analyze_operational_legal(EVENT,CHANGE,candidates=[candidate()])
    with pytest.raises(
        OperationalLegalAnalysisError,match="offset-aware"
    ):
        derive_feed_event_relevance(
            legal,
            temporal_assertions=[
                temporal("temporal:pub","PUBLICATION","POINT","2026-09-18")
            ],
            ingestion_time="2026-09-18T10:32:20",
        )


def test_publication_recency_binds_same_reobserved_celex_and_metadata_evidence():
    event={
        **EVENT,
        "ingestion_time":"2026-09-18T10:32:20.883+02:00",
    }
    legal=analyze_operational_legal(event,{**CHANGE,"event_key":"evt-1"},candidates=[candidate()])
    assertion={
        **temporal(
            "temporal:pub-2104","PUBLICATION","POINT","2026-09-18"
        ),
        "subject_ref":{"identifier":"CELEX:32026R2104"},
    }
    reobservation={
        "celex":"32026R2104",
        "temporal_metadata":{
            "publication":{
                "state":"RESOLVED",
                "assertion":assertion,
                "evidence_refs":["src-operational-metadata:2104"],
            },
        },
    }
    recency=derive_publication_recency_from_reobservation(
        legal,event,reobservation
    )
    assert recency["state"]=="CURRENT_RELEVANT"
    assert recency["evidence_refs"]==["src-operational-metadata:2104"]


def test_publication_recency_refuses_cross_bound_celex():
    event={
        **EVENT,
        "ingestion_time":"2026-09-18T10:32:20.883+02:00",
    }
    legal=analyze_operational_legal(event,{**CHANGE,"event_key":"evt-1"},candidates=[candidate()])
    reobservation={
        "celex":"32026R2104",
        "temporal_metadata":{
            "publication":{
                "state":"RESOLVED",
                "assertion":{
                    **temporal(
                        "temporal:wrong","PUBLICATION","POINT","2026-09-18"
                    ),
                    "subject_ref":{"identifier":"CELEX:39999R9999"},
                },
                "evidence_refs":["src-operational-metadata:wrong"],
            },
        },
    }
    recency=derive_publication_recency_from_reobservation(
        legal,event,reobservation
    )
    assert recency["state"]=="UNRESOLVED"
    assert recency["assertion_refs"]==[]


def test_publication_recency_does_not_bind_to_source_diff_route():
    event={
        **EVENT,
        "ingestion_time":"2026-09-18T10:32:20.883+02:00",
    }
    legal=analyze_operational_legal(
        event,
        {**CHANGE,"event_key":"evt-1"},
        candidates=[candidate(verification_route="SOURCE_DIFF")],
    )
    assert derive_publication_recency_from_reobservation(
        legal,event,{
            "celex":"32026R2104",
            "temporal_metadata":{"publication":{"state":"RESOLVED"}},
        }
    ) is None
