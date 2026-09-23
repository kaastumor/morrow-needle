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


def test_two_official_cases_require_vertical_legal_extent():
    uas, prohibited = FIXTURE["cases"]

    assert uas["vertical_extent"]["lower"] == {
        "value": 0,
        "unit": "M",
        "reference": "AGL",
        "source_expression": "lowerLimit 0 M AGL",
    }
    assert uas["vertical_extent"]["upper"]["value"] == 120
    assert uas["vertical_extent"]["upper"]["reference"] == "AGL"

    assert prohibited["vertical_extent"]["lower"] == {
        "boundary_character": "SURFACE",
        "source_expression": "GND",
    }
    assert prohibited["vertical_extent"]["upper"]["value"] == 2000
    assert prohibited["vertical_extent"]["upper"]["reference"] == "AMSL"


def test_uas_zone_geometry_and_operational_ceiling_remain_distinct():
    uas = FIXTURE["cases"][0]

    assert uas["vertical_extent"]["upper"]["value"] == 120
    assert "30m" in uas["operational_condition_context"]["message"]
    assert "not the same fact" in (
        uas["operational_condition_context"]["guardrail"].casefold()
    )


def test_v0_1_geometry_has_no_vertical_owner():
    encoded = json.dumps(SCHEMA["$defs"], sort_keys=True).casefold()

    assert "vertical_extent" not in encoded
    assert "upperverticalreference" not in encoded
    assert "lowerverticalreference" not in encoded
    assert FIXTURE["v0_1_probe"]["result"] == (
        "LEGAL_SPATIAL_STATE_V0_1_REOPEN_TRIGGERED"
    )


def _minimal_v0_1_candidate_with_vertical_extent():
    return {
        "schema_version": "legal-spatial-state-v0.1",
        "spatial_state_id": "probe:ehp25-volume",
        "character": "LEGAL_SPATIAL_STATE",
        "legal_character": "OTHER_RESTRICTED_AREA",
        "authority": {
            "authority_id": "NL_AIP",
            "label": "Dutch aeronautical information authority",
            "authority_type": "MEMBER_STATE_AUTHORITY",
        },
        "geometry": {
            "geometry_type": "CIRCLE",
            "coordinate_reference_system": "WGS84",
            "definition_character": "DIRECT_OFFICIAL_GEOMETRY",
            "centre": {
                "latitude": 52.17972222222222,
                "longitude": 5.227222222222222,
                "source_latitude": "521047N",
                "source_longitude": "0051338E",
            },
            "radius": {"value": 0.5, "unit": "KM"},
            "vertical_extent": {
                "lower": {"source_expression": "GND"},
                "upper": {"value": 2000, "unit": "FT", "reference": "AMSL"},
            },
        },
        "causal_input_refs": [{
            "object_type": "OTHER_OFFICIAL_CONTEXT",
            "object_id": "Dutch eAIP EHP25",
            "relation_character": "CAUSAL_CONTEXT",
            "evidence_state": "DIRECT",
            "notes": None,
        }],
        "governing_rule_refs": [{
            "source_type": "OTHER_OFFICIAL",
            "identifier": "Dutch eAIP ENR 5.1",
            "locator": "EHP25",
            "language": "ENG",
            "role": "GOVERNING_RULE",
            "authority_character": "BINDING_LEGAL_TEXT",
        }],
        "temporal_assertion_refs": ["temporal:ehp25:h24"],
        "evidence_state": "DIRECT",
        "source_refs": [{
            "source_type": "OTHER_OFFICIAL",
            "identifier": "Dutch eAIP ENR 5.1",
            "locator": "EHP25",
            "language": "ENG",
            "role": "GEOMETRY",
            "authority_character": "AUTHENTIC_OFFICIAL_GEOMETRY",
        }],
        "guardrails": ["Vertical extent may not be discarded."],
        "notes": None,
    }


def test_v0_1_rejects_honest_vertical_extent_field():
    candidate = _minimal_v0_1_candidate_with_vertical_extent()
    errors = list(Draft202012Validator(SCHEMA).iter_errors(candidate))

    assert errors
    assert any(
        error.validator == "additionalProperties"
        and "vertical_extent" in error.message
        for error in errors
    )


def test_failure_is_pinned_before_v0_2_design():
    assert FIXTURE["v0_1_probe"]["new_schema_added_in_failure_commit"] is False
    required = FIXTURE["required_evolution"]

    assert required["add_optional_vertical_extent"] is True
    assert required["preserve_vertical_reference_semantics"] is True
    assert required["keep_temporal_validity_in_temporal_v0_2"] is True
