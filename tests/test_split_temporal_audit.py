import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.mutation.structural import reclassify_with_lineage
from needle.temporal.resolver import resolve_boundary, status_on


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


SOURCE = load(
    "fixtures/audit/dir2008-7-split-temporal-source-v0.1.json"
)
TEMPORAL = load(
    "fixtures/temporal/dir2008-7-split-temporal-v0.1.json"
)
STRUCTURAL = load(
    "fixtures/mutations/structural-lineage-reclassification-v0.1.json"
)
TEMPORAL_SCHEMA = load("schemas/temporal-assertion-v0.1.schema.json")
MUTATION_SCHEMA = load("schemas/mutation-candidate-v0.2.schema.json")


def split_edge():
    return next(
        edge for edge in STRUCTURAL["lineage_edges"]
        if edge["edge_id"] == "dir69-art7-2-to-dir2008-arts7-8"
    )


def structural_candidate(operation, path, candidate_id):
    before = None
    after = None
    if operation == "DELETE":
        before = {
            "state_id":"CELEX:31969L0335",
            "node_id":f"old:{path}",
            "text_hash":"a"*64,
            "text_length":10,
        }
    if operation == "INSERT":
        after = {
            "state_id":"CELEX:32008L0007",
            "node_id":f"new:{path}",
            "text_hash":"b"*64,
            "text_length":10,
        }
    return {
        "candidate_id":candidate_id,
        "operation":operation,
        "target":{
            "kind":"PROVISION",
            "citation_path":path,
            "parent_citation_path":None,
            "language":"ENG",
        },
        "alignment_basis":"UNALIGNED",
        "before":before,
        "after":after,
        "feature_deltas":{
            "numbers_added":[],
            "numbers_removed":[],
            "dates_added":[],
            "dates_removed":[],
            "references_added":[],
            "references_removed":[],
        },
        "reconciliation_state":"DIFF_ONLY",
        "verification_state":"UNVERIFIED",
        "supporting_evidence":[{
            "channel":"DETERMINISTIC_DIFF",
            "source_id":"split-temporal-audit",
            "operation":operation,
            "target_locator":path,
            "authority_character":"DERIVED",
            "locator":None,
        }],
        "conflicting_evidence":[],
        "notes":None,
    }


def test_split_temporal_assertions_validate_frozen_contract():
    validator=Draft202012Validator(TEMPORAL_SCHEMA)
    errors=[
        f"{assertion['assertion_id']}: {error.message}"
        for assertion in TEMPORAL["assertions"]
        for error in validator.iter_errors(assertion)
    ]
    assert errors == []


def test_official_correlation_reclassifies_delete_plus_two_inserts_as_split():
    candidates=[
        structural_candidate("DELETE","Article 7(2)","delete-old-7-2"),
        structural_candidate("INSERT","Article 7","insert-new-7"),
        structural_candidate("INSERT","Article 8","insert-new-8"),
    ]
    result=reclassify_with_lineage(candidates,[split_edge()])
    assert len(result) == 1
    mutation=result[0]
    assert mutation["operation"] == "SPLIT"
    assert mutation["alignment_basis"] == "ASSERTED_STRUCTURAL_LINEAGE"
    assert mutation["structural_alignment"] == {
        "source_paths":["Article 7(2)"],
        "target_paths":["Article 7","Article 8"],
    }
    assert set(mutation["consumed_candidate_ids"]) == {
        "delete-old-7-2","insert-new-7","insert-new-8"
    }
    assert mutation["verification_state"] == "UNVERIFIED"
    assert list(Draft202012Validator(MUTATION_SCHEMA).iter_errors(mutation)) == []
    assert "application" not in json.dumps(mutation).casefold()


def test_split_targets_have_transposition_deadline_not_synthetic_application_start():
    assertions=TEMPORAL["assertions"]
    for target in (
        "PROVISION:32008L0007:ARTICLE7",
        "PROVISION:32008L0007:ARTICLE8",
    ):
        deadline=resolve_boundary(
            assertions,
            dimension="DEADLINE",
            boundary="POINT",
            subject_keys={target},
        )
        assert deadline == {
            "state":"RESOLVED",
            "date":"2008-12-31",
            "inclusive":True,
            "assertion_ids":["dir2008-7-arts7-8-transposition-deadline"],
        }

        application=status_on(
            assertions,
            dimension="APPLICATION",
            subject_keys={target},
            on_date="2009-01-01",
        )
        assert application["state"] == "NOT_ASSERTED"
        assert application["active"] is None


def test_article18_application_date_stays_scoped_to_enumerated_articles():
    assertions=TEMPORAL["assertions"]
    article9=status_on(
        assertions,
        dimension="APPLICATION",
        subject_keys={"PROVISION:32008L0007:ARTICLE9"},
        on_date="2009-01-01",
    )
    assert article9["state"] == "RESOLVED"
    assert article9["active"] is True
    assert article9["start"]["assertion_ids"] == [
        "dir2008-7-article18-explicit-application-set"
    ]


def test_predecessor_repeal_boundary_is_not_successor_application_boundary():
    end=resolve_boundary(
        TEMPORAL["assertions"],
        dimension="LEGAL_FORCE",
        boundary="END",
        subject_keys={"ACT:31969L0335"},
    )
    assert end == {
        "state":"RESOLVED",
        "date":"2009-01-01",
        "inclusive":False,
        "assertion_ids":["dir69-335-legal-force-end"],
    }
    assert set(split_edge()["targets"][0].keys()) == {
        "act_id","eli","version","language","structural_path","text_hash"
    }


def test_authentic_source_identifier_conflict_is_preserved_not_normalized_away():
    conflict=SOURCE["source_internal_identifier_disagreement"]
    assert conflict == {
        "literal_article16":"69/355/EEC",
        "resolved_canonical_predecessor":"69/335/EEC",
        "semantics":"PRESERVE_LITERAL_AND_RESOLVE_CANONICAL_SEPARATELY",
        "conflict_state":"SOURCE_INTERNAL_CONFLICT",
    }
    evidence=SOURCE["evidence"]
    assert evidence["repeal_clause"]["printed_predecessor"] == "69/355/EEC"
    assert evidence["repeal_clause"]["canonical_predecessor"] == "69/335/EEC"
    assert set(evidence["canonical_predecessor_support"].values()) == {
        "Council Directive 69/335/EEC",
        "Directive 69/335/EEC",
    }


def test_split_temporal_forbidden_inferences_cover_all_shortcuts():
    forbidden=" ".join(TEMPORAL["forbidden_inferences"]).casefold()
    assert "different enumerated article set" in forbidden
    assert "predecessor temporal boundary" in forbidden
    assert "transposition deadline as an application start" in forbidden
    assert "silently normalizing" in forbidden
