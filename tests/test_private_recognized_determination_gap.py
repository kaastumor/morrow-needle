import json
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/capri-sp-private-rating-regulatory-input-v0.1.json"
    ).read_text(encoding="utf-8")
)
SOURCE_SCHEMA = json.loads(
    Path("schemas/source-observation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
FINDING_SCHEMA = json.loads(
    Path("schemas/authoritative-finding-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
METRIC_SCHEMA = json.loads(
    Path("schemas/authoritative-metric-observation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def test_private_rating_transition_and_public_mapping_are_pinned():
    determination = FIXTURE["private_determination"]
    chain = FIXTURE["public_law_recognition_chain"]

    assert determination["before"] == "BBB-"
    assert determination["after"] == "BB"
    assert chain[1]["mapping"] == [
        {"private_rating_band": "BBB", "credit_quality_step": 3},
        {"private_rating_band": "BB", "credit_quality_step": 4},
    ]
    assert chain[2]["mapping"] == [
        {"credit_quality_step": 3, "risk_weight_percent": 75},
        {"credit_quality_step": 4, "risk_weight_percent": 100},
    ]


def test_bank_specific_effect_is_explicitly_not_asserted():
    evaluation = FIXTURE["conditional_evaluation"]

    assert evaluation["potential_risk_weight_transition"] == "75% -> 100%"
    assert evaluation["bank_specific_effect_asserted"] is False
    assert "nominated" in evaluation["condition"].casefold()
    assert "directly applicable" in evaluation["condition"].casefold()


def test_source_observation_has_no_honest_private_primary_source_system():
    source_systems = SOURCE_SCHEMA["properties"]["source_system"]["enum"]

    assert "PRIVATE_PRIMARY" not in source_systems
    assert all("OFFICIAL" in value or value in {
        "CELLAR", "EUR_LEX", "OFFICIAL_JOURNAL", "OEIL", "COUNCIL", "COMMISSION"
    } for value in source_systems)
    assert FIXTURE["architecture_probe"]["source_observation_v0_1"]["fit"] == (
        "FAILS_SOURCE_VOCABULARY"
    )


def test_authoritative_finding_authority_types_exclude_private_recognized_actor():
    types = (
        FINDING_SCHEMA["properties"]["authority"]["properties"][
            "authority_type"
        ]["enum"]
    )

    assert "LEGALLY_RECOGNIZED_PRIVATE_ACTOR" not in types
    assert FIXTURE["architecture_probe"]["authoritative_finding_v0_1"]["fit"] == (
        "SEMANTICALLY_CLOSE_BUT_REJECTS_ORIGINATOR"
    )


def test_rating_is_not_coerced_into_numeric_metric():
    metric_value_type = METRIC_SCHEMA["properties"]["metric"]["properties"][
        "value"
    ]["type"]

    assert metric_value_type == "number"
    assert FIXTURE["architecture_probe"][
        "authoritative_metric_observation_v0_1"
    ]["fit"] == "FAILS_VALUE_SHAPE"


def test_failure_is_pinned_before_recognition_architecture():
    probe = FIXTURE["architecture_probe"]

    assert probe["result"] == "LEGALLY_RECOGNIZED_PRIVATE_ORIGIN_GAP_PINNED"
    assert probe["provisional_missing_layer"] == (
        "RECOGNITION_BASIS_FOR_NON_PUBLIC_DETERMINATIONS"
    )
    assert probe["new_schema_added_in_this_probe"] is False
