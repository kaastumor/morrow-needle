import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from needle.provenance.ledger import seal_record, validate_ledger


PROV_V1 = json.loads(
    Path("schemas/provenance-record-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
PROV_V2 = json.loads(
    Path("schemas/provenance-record-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
OLD_LEDGER = json.loads(
    Path("fixtures/provenance/reg794-article3-dag-v0.1.json").read_text(
        encoding="utf-8"
    )
)["records"]
DET_SCHEMA = json.loads(
    Path(
        "schemas/recognized-external-determination-v0.1.schema.json"
    ).read_text(encoding="utf-8")
)
DETERMINATIONS = [
    json.loads(Path(path).read_text(encoding="utf-8"))
    for path in (
        "fixtures/determinations/sp-capri-rating-2025-v0.1.json",
        "fixtures/determinations/szutest-biotrh-suspension-2023-v0.1.json",
        "fixtures/determinations/szutest-biotrh-withdrawal-2023-v0.1.json",
    )
]


def validate(schema, document):
    return list(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(document)
    )


def test_existing_official_provenance_mechanically_upgrades():
    upgraded = deepcopy(OLD_LEDGER)
    for record in upgraded:
        if record["record_type"] == "SOURCE_OBSERVATION":
            record["payload"]["source_origin"] = "PUBLIC_OFFICIAL"
            record["record_hash"] = seal_record(record)["record_hash"]

    assert all(validate(PROV_V2, record) == [] for record in upgraded)
    assert validate_ledger(upgraded) == []


def test_private_primary_source_observation_is_hashable_without_becoming_official():
    record = seal_record({
        "record_id": "src-private-sp-capri",
        "record_type": "SOURCE_OBSERVATION",
        "created_at": "2025-02-20T17:00:00Z",
        "payload": {
            "source_type": "PRIVATE_PRIMARY",
            "source_origin": "PRIVATE_PRIMARY",
            "identifier": "sp-capri-rating-2025-02-20",
            "resource_uri": "https://www.spglobal.com/ratings/",
            "language": "ENG",
            "representation_class": "HTML",
            "observed_at": "2025-02-20T17:00:00Z",
            "artifact_hash": "sha256:" + ("1" * 64),
            "retrieval": {
                "final_uri": "https://www.spglobal.com/ratings/",
                "media_type": "text/html",
                "http_status": 200
            }
        }
    })

    assert validate(PROV_V2, record) == []
    assert validate_ledger([record]) == []


def test_v0_2_rejects_private_origin_labeled_as_official_source_type():
    bad = seal_record({
        "record_id": "src-bad-private",
        "record_type": "SOURCE_OBSERVATION",
        "created_at": "2025-02-20T17:00:00Z",
        "payload": {
            "source_type": "OTHER_OFFICIAL",
            "source_origin": "PRIVATE_PRIMARY",
            "identifier": "bad",
            "resource_uri": "https://example.invalid/",
            "language": "ENG",
            "representation_class": "HTML",
            "observed_at": "2025-02-20T17:00:00Z",
            "artifact_hash": "sha256:" + ("2" * 64),
            "retrieval": {
                "final_uri": "https://example.invalid/",
                "media_type": "text/html",
                "http_status": 200
            }
        }
    })

    assert validate(PROV_V2, bad)


def test_all_private_determination_proofs_fit_same_contract():
    assert all(validate(DET_SCHEMA, item) == [] for item in DETERMINATIONS)
    assert {item["determination_kind"] for item in DETERMINATIONS} == {
        "ORDINAL_CLASSIFICATION_TRANSITION",
        "CERTIFICATE_STATUS_TRANSITION",
    }


def test_s_and_p_case_preserves_conditional_downstream_effect():
    sp = DETERMINATIONS[0]

    assert sp["evidence_state"] == "DIRECT"
    assert sp["source_refs"][0]["source_origin"] == "PRIVATE_PRIMARY"
    assert sp["transition"] == {
        "operation": "RECLASSIFY",
        "before": "BBB-",
        "after": "BB",
    }
    assert sp["legal_relevance"]["consequence_character"] == (
        "CONDITIONAL_ON_DOWNSTREAM_USE"
    )
    assert any(
        "No bank-specific" in guardrail
        for guardrail in sp["guardrails"]
    )


def test_szutest_cases_preserve_attributed_evidence_and_status_sequence():
    suspension, withdrawal = DETERMINATIONS[1:]

    assert suspension["evidence_state"] == "ATTRIBUTED"
    assert withdrawal["evidence_state"] == "ATTRIBUTED"
    assert suspension["source_refs"][0]["source_origin"] == "PUBLIC_OFFICIAL"
    assert suspension["transition"]["after"] == "SUSPENDED"
    assert withdrawal["transition"]["before"] == "SUSPENDED"
    assert withdrawal["transition"]["after"] == "WITHDRAWN"


def test_private_origin_and_legal_recognition_are_distinct_fields():
    for item in DETERMINATIONS:
        assert item["originator"]["originator_character"] == "PRIVATE_ENTITY"
        assert item["recognition"]["public_law_refs"]
        assert "source_origin" in item["source_refs"][0]
        assert "recognition_character" in item["recognition"]


def test_contract_does_not_create_actor_graph_or_trust_score():
    encoded = json.dumps(DET_SCHEMA, sort_keys=True).casefold()

    for forbidden in (
        "trust_score",
        "reputation_score",
        "actor_graph",
        "accreditation_graph",
        "precedent_weight",
    ):
        assert forbidden not in encoded


def test_v0_1_provenance_remains_official_only():
    source_types = (
        PROV_V1["$defs"]["source_observation"]["properties"]["source_type"]["enum"]
    )

    assert "PRIVATE_PRIMARY" not in source_types
