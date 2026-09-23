import json
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/"
        "hpai-woerdense-verlaat-authoritative-finding-spatial-effect-v0.1.json"
    ).read_text(encoding="utf-8")
)
METRIC_SCHEMA = json.loads(
    Path("schemas/authoritative-metric-observation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
SET_SCHEMA = json.loads(
    Path("schemas/authoritative-dynamic-set-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def test_finding_is_categorical_not_textual_mutation():
    finding = FIXTURE["authoritative_finding"]

    assert finding["finding_character"] == "OFFICIAL_DISEASE_CONFIRMATION"
    assert finding["condition"] == "Highly pathogenic avian influenza confirmed"
    assert finding["textual_mutation"] is None
    assert finding["finding_date"] == "2026-07-17"


def test_spatial_consequence_is_derived_from_finding_location():
    spatial = FIXTURE["spatial_rule_evaluation"]
    outputs = {item["zone_kind"]: item for item in spatial["outputs"]}

    assert spatial["input_finding_id"] == (
        "finding:hpai:NL-HPAI(NON-P)-2026-00174"
    )
    assert outputs["PROTECTION_ZONE"]["radius_km"] == 3
    assert outputs["SURVEILLANCE_ZONE"]["radius_km"] == 10
    assert spatial["evaluation_state"] == (
        "DERIVED_FROM_FINDING_AND_BINDING_SPATIAL_RULE"
    )


def test_later_eu_source_preserves_same_outbreak_and_geometry():
    official = FIXTURE["official_case_confirmation"]

    assert official["eu_published_outbreak_reference"] == (
        "NL-HPAI(NON-P)-2026-00174"
    )
    assert official["eu_zone_centre"] == {
        "latitude": 52.16,
        "longitude": 4.89,
    }
    assert official["eu_protection_zone_until"] == "2026-08-08"
    assert official["eu_surveillance_zone_until"] == "2026-08-17"


def test_metric_contract_cannot_own_categorical_finding():
    assert METRIC_SCHEMA["properties"]["metric"]["required"] == [
        "name",
        "value",
        "unit",
    ]
    assert FIXTURE["architecture_probe"][
        "authoritative_metric_observation_v0_1"
    ]["fit"] == "FAILS_CAUSAL_SHAPE"


def test_dynamic_set_contract_requires_membership_semantics():
    transition_required = set(SET_SCHEMA["$defs"]["transition"]["required"])

    assert "member" in transition_required
    assert "operation" in transition_required
    assert FIXTURE["architecture_probe"]["authoritative_dynamic_set_v0_1"][
        "fit"
    ] == "FAILS_DIRECT_CAUSE"


def test_temporal_contract_has_no_geometry_ownership():
    encoded = json.dumps(TEMPORAL_SCHEMA, sort_keys=True).casefold()

    assert "radius_km" not in encoded
    assert "latitude" not in encoded
    assert "longitude" not in encoded
    assert FIXTURE["architecture_probe"]["temporal_v0_1"]["fit"] == (
        "DATES_ONLY"
    )


def test_gap_is_pinned_before_schema_design():
    probe = FIXTURE["architecture_probe"]

    assert probe["result"] == "REPRESENTATIONAL_FAILURE_PINNED"
    assert probe["provisional_missing_layers"] == [
        "AUTHORITATIVE_CATEGORICAL_FINDING",
        "SPATIAL_RULE_EVALUATION",
    ]
    assert probe["new_schema_added_in_this_probe"] is False
