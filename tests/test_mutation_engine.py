import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.mutation.diff import diff_same_location
from needle.mutation.reconcile import reconcile_candidate


SCHEMA = json.loads(
    Path("schemas/mutation-candidate-v0.1.schema.json").read_text(encoding="utf-8")
)
REAL = json.loads(
    Path("fixtures/mutations/reg794-article3-replacement-evidence-v0.1.json").read_text(encoding="utf-8")
)


def _ast(state_id, paragraph_text, *, include_extra=False):
    nodes = [
        {
            "node_id":f"{state_id}:doc",
            "kind":"DOCUMENT",
            "citation_path":"Regulation X",
            "parent_id":None,
        },
        {
            "node_id":f"{state_id}:art3",
            "kind":"ARTICLE",
            "citation_path":"Article 3",
            "parent_id":f"{state_id}:doc",
        },
        {
            "node_id":f"{state_id}:art3p3",
            "kind":"PARAGRAPH",
            "citation_path":"Article 3 > 3",
            "parent_id":f"{state_id}:art3",
        },
    ]
    segments = [
        {
            "segment_id":f"{state_id}:label",
            "node_id":f"{state_id}:art3p3",
            "role":"LABEL",
            "text_source":"3.",
            "text_compare":"3.",
            "ordinal":0,
            "document_order":1,
        },
        {
            "segment_id":f"{state_id}:body",
            "node_id":f"{state_id}:art3p3",
            "role":"BODY",
            "text_source":paragraph_text,
            "text_compare":paragraph_text,
            "ordinal":1,
            "document_order":2,
        },
    ]
    if include_extra:
        nodes.append({
            "node_id":f"{state_id}:art3p4",
            "kind":"PARAGRAPH",
            "citation_path":"Article 3 > 4",
            "parent_id":f"{state_id}:art3",
        })
        segments.append({
            "segment_id":f"{state_id}:p4body",
            "node_id":f"{state_id}:art3p4",
            "role":"BODY",
            "text_source":"New paragraph inserted under Article 4.",
            "text_compare":"New paragraph inserted under Article 4.",
            "ordinal":0,
            "document_order":3,
        })
    return {"state_id":state_id,"nodes":nodes,"segments":segments}


def test_same_location_diff_detects_replacement_and_feature_deltas():
    before = _ast(
        "before",
        "From 1 January 2006 notifications use Article 2 and a threshold of 20%.",
    )
    after = _ast(
        "after",
        "From 1 July 2008 notifications use Article 3 and a threshold of 25%.",
    )
    candidates = diff_same_location(before, after, language="ENG")
    target = next(
        c for c in candidates
        if c["target"]["citation_path"] == "Article 3 > 3"
    )
    assert target["operation"] == "REPLACE"
    assert target["alignment_basis"] == "EXACT_CITATION_AND_KIND"
    assert "1 July 2008" in target["feature_deltas"]["dates_added"]
    assert "1 January 2006" in target["feature_deltas"]["dates_removed"]
    assert "Article 3" in target["feature_deltas"]["references_added"]
    assert "Article 2" in target["feature_deltas"]["references_removed"]
    assert "25%" in target["feature_deltas"]["numbers_added"]
    assert "20%" in target["feature_deltas"]["numbers_removed"]
    assert target["reconciliation_state"] == "DIFF_ONLY"
    assert target["verification_state"] == "UNVERIFIED"


def test_same_location_diff_detects_insert_without_fuzzy_identity_claim():
    before = _ast("before", "Stable paragraph.")
    after = _ast("after", "Stable paragraph.", include_extra=True)
    candidates = diff_same_location(before, after, language="ENG")
    inserted = next(
        c for c in candidates
        if c["target"]["citation_path"] == "Article 3 > 4"
    )
    assert inserted["operation"] == "INSERT"
    assert inserted["before"] is None
    assert inserted["after"] is not None
    assert inserted["alignment_basis"] == "EXACT_CITATION_AND_KIND"


def _real_article3_candidate():
    return {
        "candidate_id":"reg794-art3-replace",
        "operation":"REPLACE",
        "target":{
            "kind":"ARTICLE",
            "citation_path":"Article 3",
            "parent_citation_path":"CHAPTER II",
            "language":"ENG",
        },
        "alignment_basis":"EXACT_CITATION_AND_KIND",
        "before":{
            "state_id":"CELEX:02004R0794-20070119",
            "node_id":"art3-before",
            "text_hash":"a"*64,
            "text_length":1,
        },
        "after":{
            "state_id":"CELEX:02004R0794-20080414",
            "node_id":"art3-after",
            "text_hash":"b"*64,
            "text_length":1,
        },
        "feature_deltas":{
            "numbers_added":[],"numbers_removed":[],
            "dates_added":[],"dates_removed":[],
            "references_added":[],"references_removed":[],
        },
        "reconciliation_state":"DIFF_ONLY",
        "verification_state":"UNVERIFIED",
        "supporting_evidence":[{
            "channel":"DETERMINISTIC_DIFF",
            "source_id":"CELEX:02004R0794-20070119->CELEX:02004R0794-20080414",
            "operation":"REPLACE",
            "target_locator":"Article 3",
            "authority_character":"DERIVED",
            "locator":None,
        }],
        "conflicting_evidence":[],
        "notes":None,
    }


def test_real_article3_evidence_corroborates_but_does_not_verify():
    candidate = _real_article3_candidate()
    result = reconcile_candidate(candidate, REAL["evidence"])

    validator = Draft202012Validator(SCHEMA)
    assert list(validator.iter_errors(result)) == []
    assert result["reconciliation_state"] == "CORROBORATED"
    assert result["verification_state"] == "UNVERIFIED"

    channels = {item["channel"] for item in result["supporting_evidence"]}
    assert "DETERMINISTIC_DIFF" in channels
    assert "RELATIONSHIP_METADATA" in channels
    assert "CONSOLIDATION_PROVENANCE" in channels
    assert "CONSOLIDATED_CHECKPOINT" in channels
    assert "AUTHENTIC_ACT" not in channels


def test_conflicting_official_operation_quarantines_verification():
    candidate = _real_article3_candidate()
    conflict = {
        "channel":"RELATIONSHIP_METADATA",
        "source_id":"synthetic-conflict",
        "operation":"DELETION",
        "target_locator":"Article 3",
        "authority_character":"OFFICIAL_STRUCTURED_METADATA",
        "locator":"test-only conflict",
    }
    result = reconcile_candidate(candidate, REAL["evidence"] + [conflict])
    assert result["reconciliation_state"] == "CONFLICTING"
    assert result["verification_state"] == "UNVERIFIED"
    assert any(item["source_id"] == "synthetic-conflict" for item in result["conflicting_evidence"])
