import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.mutation.diff import diff_same_location
from needle.mutation.reconcile import reconcile_candidate
from needle.mutation.structural import reclassify_with_lineage


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


V2_SCHEMA = json.loads(
    Path("schemas/mutation-candidate-v0.2.schema.json").read_text(encoding="utf-8")
)
STRUCTURAL = json.loads(
    Path("fixtures/mutations/structural-lineage-reclassification-v0.1.json").read_text(encoding="utf-8")
)


def _structural_candidate(operation, path, candidate_id):
    before = None
    after = None
    if operation == "DELETE":
        before = {
            "state_id":"old",
            "node_id":f"old:{path}",
            "text_hash":"c"*64,
            "text_length":10,
        }
    elif operation == "INSERT":
        after = {
            "state_id":"new",
            "node_id":f"new:{path}",
            "text_hash":"d"*64,
            "text_length":10,
        }
    return {
        "candidate_id":candidate_id,
        "operation":operation,
        "target":{
            "kind":"ARTICLE",
            "citation_path":path,
            "parent_citation_path":None,
            "language":"ENG",
        },
        "alignment_basis":"UNALIGNED",
        "before":before,
        "after":after,
        "feature_deltas":{
            "numbers_added":[],"numbers_removed":[],
            "dates_added":[],"dates_removed":[],
            "references_added":[],"references_removed":[],
        },
        "reconciliation_state":"DIFF_ONLY",
        "verification_state":"UNVERIFIED",
        "supporting_evidence":[{
            "channel":"DETERMINISTIC_DIFF",
            "source_id":"synthetic-structural-diff",
            "operation":operation,
            "target_locator":path,
            "authority_character":"DERIVED",
            "locator":None,
        }],
        "conflicting_evidence":[],
        "notes":None,
    }


def test_asserted_official_lineage_reclassifies_renumber():
    candidates = [
        _structural_candidate("DELETE","Article 4","del-art4"),
        _structural_candidate("INSERT","Article 3","ins-art3"),
    ]
    edge = next(
        e for e in STRUCTURAL["lineage_edges"]
        if e["edge_id"] == "reg26-art4-to-reg1184-art3"
    )
    result = reclassify_with_lineage(candidates, [edge])
    assert len(result) == 1
    mutation = result[0]
    assert mutation["operation"] == "RENUMBER"
    assert mutation["alignment_basis"] == "ASSERTED_STRUCTURAL_LINEAGE"
    assert mutation["structural_alignment"] == {
        "source_paths":["Article 4"],
        "target_paths":["Article 3"],
    }
    assert set(mutation["consumed_candidate_ids"]) == {"del-art4","ins-art3"}
    assert mutation["reconciliation_state"] == "CORROBORATED"
    assert mutation["verification_state"] == "UNVERIFIED"
    assert mutation["lineage_edge_ids"] == ["reg26-art4-to-reg1184-art3"]
    assert list(Draft202012Validator(V2_SCHEMA).iter_errors(mutation)) == []


def test_asserted_lineage_preserves_one_to_many_split_cardinality():
    candidates = [
        _structural_candidate("DELETE","Article 7(2)","del-art7-2"),
        _structural_candidate("INSERT","Article 7","ins-art7"),
        _structural_candidate("INSERT","Article 8","ins-art8"),
    ]
    edge = next(
        e for e in STRUCTURAL["lineage_edges"]
        if e["edge_id"] == "dir69-art7-2-to-dir2008-arts7-8"
    )
    result = reclassify_with_lineage(candidates, [edge])
    assert len(result) == 1
    mutation = result[0]
    assert mutation["operation"] == "SPLIT"
    assert mutation["structural_alignment"]["source_paths"] == ["Article 7(2)"]
    assert mutation["structural_alignment"]["target_paths"] == ["Article 7","Article 8"]
    assert set(mutation["consumed_candidate_ids"]) == {"del-art7-2","ins-art7","ins-art8"}
    assert list(Draft202012Validator(V2_SCHEMA).iter_errors(mutation)) == []


def test_similarity_only_lineage_cannot_promote_move():
    candidates = [
        _structural_candidate("DELETE","Article 10","del-art10"),
        _structural_candidate("INSERT","Article 20","ins-art20"),
    ]
    edge = next(
        e for e in STRUCTURAL["lineage_edges"]
        if e["edge_id"] == "similarity-only-false-promotion-control"
    )
    result = reclassify_with_lineage(candidates, [edge])
    assert {candidate["operation"] for candidate in result} == {"DELETE","INSERT"}
    assert all(candidate.get("lineage_edge_ids") is None for candidate in result)


def test_derived_official_correlation_can_support_many_to_one_merge():
    candidates = [
        _structural_candidate("DELETE","Article 2(2)","del-art2-2"),
        _structural_candidate("DELETE","Article 2(3)","del-art2-3"),
        _structural_candidate("INSERT","Article 2(2)","ins-new-art2-2"),
    ]
    edge = next(
        e for e in STRUCTURAL["lineage_edges"]
        if e["edge_id"] == "reg26-art2-2-art2-3-to-reg1184-art2-2"
    )
    result = reclassify_with_lineage(candidates, [edge])
    assert len(result) == 1
    mutation = result[0]
    assert mutation["operation"] == "MERGE"
    assert mutation["structural_alignment"]["source_paths"] == ["Article 2(2)","Article 2(3)"]
    assert mutation["structural_alignment"]["target_paths"] == ["Article 2(2)"]
    assert set(mutation["consumed_candidate_ids"]) == {
        "del-art2-2","del-art2-3","ins-new-art2-2"
    }
    assert mutation["reconciliation_state"] == "CORROBORATED"
    assert mutation["verification_state"] == "UNVERIFIED"
    assert list(Draft202012Validator(V2_SCHEMA).iter_errors(mutation)) == []
