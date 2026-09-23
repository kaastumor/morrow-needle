import json
from pathlib import Path

from jsonschema import Draft202012Validator


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/legal-spatial-volume-reopen-v0.1.json"
    ).read_text(encoding="utf-8")
)
SCHEMA = json.loads(
    Path("schemas/legal-spatial-state-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def test_official_cases_cover_three_vertical_boundary_semantics():
    uas, prohibited, restricted = FIXTURE["cases"]

    assert uas["vertical_extent"]["lower"]["reference"] == "AGL"
    assert uas["vertical_extent"]["upper"]["value"] == 120
    assert uas["vertical_extent"]["upper"]["reference"] == "AGL"

    assert prohibited["horizontal_extent"]["geometry_type"] == "POLYGON"
    assert prohibited["vertical_extent"]["lower"] == {
        "boundary_character": "SURFACE",
        "source_expression": "GND",
    }
    assert prohibited["vertical_extent"]["upper"]["value"] == 2000
    assert prohibited["vertical_extent"]["upper"]["reference"] == "AMSL"

    assert restricted["vertical_extent"]["lower"]["reference"] == "AMSL"
    assert restricted["vertical_extent"]["upper"] == {
        "boundary_character": "FLIGHT_LEVEL",
        "value": 185,
        "unit": "FL",
        "source_expression": "FL 185",
    }


def test_uas_zone_geometry_and_operational_ceiling_remain_distinct():
    uas = FIXTURE["cases"][0]

    assert uas["vertical_extent"]["upper"]["value"] == 120
    assert "30m" in uas["operational_condition_context"]["message"]
    assert "not the same fact" in (
        uas["operational_condition_context"]["guardrail"].casefold()
    )


def test_clean_conventional_case_isolates_vertical_failure():
    prohibited = FIXTURE["cases"][1]

    assert prohibited["horizontal_extent"]["geometry_type"] == "POLYGON"
    assert "only the vertical" in prohibited["isolation_value"].casefold()


def test_v0_1_geometry_has_no_vertical_owner():
    encoded = json.dumps(SCHEMA["$defs"], sort_keys=True).casefold()

    assert "vertical_extent" not in encoded
    assert "flight_level" not in encoded
    assert FIXTURE["v0_1_probe"]["result"] == (
        "LEGAL_SPATIAL_STATE_V0_1_REOPEN_TRIGGERED"
    )


def _minimal_v0_1_candidate_with_vertical_extent():
    return {
        "schema_version": "legal-spatial-state-v0.1",
        "spatial_state_id": "probe:ehp26-volume",
        "character": "LEGAL_SPATIAL_STATE",
        "legal_character": "OTHER_RESTRICTED_AREA",
        "authority": {
            "authority_id": "NL_AIP",
            "label": "Dutch aeronautical information authority",
            "authority_type": "MEMBER_STATE_AUTHORITY",
        },
        "geometry": {
            "geometry_type": "POLYGON",
            "coordinate_reference_system": "WGS84",
            "definition_character": "DIRECT_OFFICIAL_GEOMETRY",
            "vertices": [
                {"latitude": 52.061944, "longitude": 4.305556},
                {"latitude": 52.106944, "longitude": 4.405556},
                {"latitude": 52.126944, "longitude": 4.434167},
                {"latitude": 52.143333, "longitude": 4.397222},
                {"latitude": 52.088056, "longitude": 4.274167},
                {"latitude": 52.061944, "longitude": 4.305556},
            ],
            "closed_ring": True,
            "vertical_extent": {
                "lower": {
                    "boundary_character": "SURFACE",
                    "source_expression": "GND",
                },
                "upper": {
                    "boundary_character": "ALTITUDE",
                    "value": 2000,
                    "unit": "FT",
                    "reference": "AMSL",
                    "source_expression": "2000 FT AMSL",
                },
            },
        },
        "causal_input_refs": [{
            "object_type": "OTHER_OFFICIAL_CONTEXT",
            "object_id": "Dutch eAIP EHP26",
            "relation_character": "CAUSAL_CONTEXT",
            "evidence_state": "DIRECT",
            "notes": None,
        }],
        "governing_rule_refs": [{
            "source_type": "OTHER_OFFICIAL",
            "identifier": "Dutch eAIP ENR 5.1",
            "locator": "EHP26",
            "language": "ENG",
            "role": "GOVERNING_RULE",
            "authority_character": "BINDING_LEGAL_TEXT",
        }],
        "temporal_assertion_refs": ["temporal:ehp26:h24"],
        "evidence_state": "DIRECT",
        "source_refs": [{
            "source_type": "OTHER_OFFICIAL",
            "identifier": "Dutch eAIP ENR 5.1",
            "locator": "EHP26",
            "language": "ENG",
            "role": "GEOMETRY",
            "authority_character": "AUTHENTIC_OFFICIAL_GEOMETRY",
        }],
        "guardrails": ["Vertical extent may not be discarded."],
        "notes": None,
    }


def test_v0_1_rejects_honest_vertical_extent_field():
    candidate = _minimal_v0_1_candidate_with_vertical_extent()

    without_vertical = json.loads(json.dumps(candidate))
    without_vertical["geometry"].pop("vertical_extent")

    assert list(
        Draft202012Validator(SCHEMA).iter_errors(without_vertical)
    ) == []

    with_vertical_errors = list(
        Draft202012Validator(SCHEMA).iter_errors(candidate)
    )
    assert with_vertical_errors


def test_failure_is_pinned_before_v0_2_design():
    assert FIXTURE["v0_1_probe"]["new_schema_added_in_failure_commit"] is False
    required = FIXTURE["required_evolution"]

    assert required["add_optional_vertical_extent"] is True
    assert required["support_surface_boundary"] is True
    assert required["support_altitude_boundary"] is True
    assert required["support_flight_level_boundary"] is True
    assert required["keep_temporal_validity_in_temporal_v0_2"] is True
