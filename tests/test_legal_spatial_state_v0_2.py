import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA_V1 = json.loads(
    Path("schemas/legal-spatial-state-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
SCHEMA_V2 = json.loads(
    Path("schemas/legal-spatial-state-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
DISCOVERY = json.loads(
    Path(
        "fixtures/discovery/legal-spatial-volume-reopen-v0.1.json"
    ).read_text(encoding="utf-8")
)
HPAI_V1 = json.loads(
    Path(
        "fixtures/spatial/hpai-woerdense-verlaat-protection-zone-v0.1.json"
    ).read_text(encoding="utf-8")
)
FISH_V1 = json.loads(
    Path(
        "fixtures/spatial/skagerrak-prawn-rtc-hvmfs-2025-4-v0.1.json"
    ).read_text(encoding="utf-8")
)
HPAI_V2 = json.loads(
    Path(
        "fixtures/spatial/hpai-woerdense-verlaat-protection-zone-v0.2.json"
    ).read_text(encoding="utf-8")
)
FISH_V2 = json.loads(
    Path(
        "fixtures/spatial/skagerrak-prawn-rtc-hvmfs-2025-4-v0.2.json"
    ).read_text(encoding="utf-8")
)


def validate(schema, document):
    return list(Draft202012Validator(schema).iter_errors(document))


def test_existing_2d_cases_mechanically_upgrade_with_null_vertical_extent():
    for old, new in ((HPAI_V1, HPAI_V2), (FISH_V1, FISH_V2)):
        assert validate(SCHEMA_V1, old) == []
        assert validate(SCHEMA_V2, new) == []

        expected = deepcopy(old)
        expected["schema_version"] = "legal-spatial-state-v0.2"
        expected["vertical_extent"] = None

        assert new["geometry"] == expected["geometry"]
        assert new["causal_input_refs"] == expected["causal_input_refs"]
        assert new["governing_rule_refs"] == expected["governing_rule_refs"]
        assert new["temporal_assertion_refs"] == expected[
            "temporal_assertion_refs"
        ]
        assert new["vertical_extent"] is None


def _base_polygon_state(case_id, legal_character):
    return {
        "schema_version": "legal-spatial-state-v0.2",
        "spatial_state_id": f"probe:{case_id}",
        "character": "LEGAL_SPATIAL_STATE",
        "legal_character": legal_character,
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
                {"latitude": 52.0, "longitude": 5.0},
                {"latitude": 52.1, "longitude": 5.0},
                {"latitude": 52.1, "longitude": 5.1},
                {"latitude": 52.0, "longitude": 5.0},
            ],
            "closed_ring": True,
        },
        "vertical_extent": None,
        "causal_input_refs": [{
            "object_type": "OTHER_OFFICIAL_CONTEXT",
            "object_id": case_id,
            "relation_character": "CAUSAL_CONTEXT",
            "evidence_state": "DIRECT",
            "notes": None,
        }],
        "governing_rule_refs": [{
            "source_type": "OTHER_OFFICIAL",
            "identifier": "Dutch official aviation source",
            "locator": case_id,
            "language": "ENG",
            "role": "GOVERNING_RULE",
            "authority_character": "BINDING_LEGAL_TEXT",
        }],
        "temporal_assertion_refs": ["temporal:source-owned-separately"],
        "evidence_state": "DIRECT",
        "source_refs": [{
            "source_type": "OTHER_OFFICIAL",
            "identifier": "Dutch official aviation source",
            "locator": case_id,
            "language": "ENG",
            "role": "GEOMETRY",
            "authority_character": "AUTHENTIC_OFFICIAL_GEOMETRY",
        }],
        "guardrails": ["Temporal validity remains externally owned."],
        "notes": None,
    }


def test_uas_agl_volume_is_representable_without_copying_operational_ceiling():
    case = DISCOVERY["cases"][0]
    candidate = _base_polygon_state(
        case["case_id"],
        "UAS_GEOGRAPHICAL_ZONE",
    )
    candidate["vertical_extent"] = {
        "definition_character": "DIRECT_OFFICIAL_VERTICAL_EXTENT",
        "lower": case["vertical_extent"]["lower"],
        "upper": case["vertical_extent"]["upper"],
        "comparison_policy": "PRESERVE_SOURCE_REFERENCE_NO_IMPLICIT_CONVERSION",
    }
    candidate["source_refs"].append({
        "source_type": "OTHER_OFFICIAL",
        "identifier": case["official_source"]["identifier"],
        "locator": "record 2.a vertical limits",
        "language": "ENG",
        "role": "VERTICAL_EXTENT",
        "authority_character": "AUTHENTIC_OFFICIAL_GEOMETRY",
    })

    assert validate(SCHEMA_V2, candidate) == []
    assert candidate["vertical_extent"]["upper"]["value"] == 120
    encoded = json.dumps(candidate)
    assert "30m" not in encoded


def test_surface_to_amsl_volume_is_representable():
    case = DISCOVERY["cases"][1]
    candidate = _base_polygon_state(
        case["case_id"],
        "PROHIBITED_AIRSPACE",
    )
    candidate["vertical_extent"] = {
        "definition_character": "DIRECT_OFFICIAL_VERTICAL_EXTENT",
        "lower": case["vertical_extent"]["lower"],
        "upper": case["vertical_extent"]["upper"],
        "comparison_policy": "PRESERVE_SOURCE_REFERENCE_NO_IMPLICIT_CONVERSION",
    }

    assert validate(SCHEMA_V2, candidate) == []
    assert candidate["vertical_extent"]["lower"]["boundary_character"] == (
        "SURFACE"
    )
    assert candidate["vertical_extent"]["upper"]["reference"] == "AMSL"


def test_amsl_to_flight_level_volume_is_representable_without_conversion():
    case = DISCOVERY["cases"][2]
    candidate = _base_polygon_state(
        case["case_id"],
        "RESTRICTED_AIRSPACE",
    )
    candidate["vertical_extent"] = {
        "definition_character": "DIRECT_OFFICIAL_VERTICAL_EXTENT",
        "lower": case["vertical_extent"]["lower"],
        "upper": case["vertical_extent"]["upper"],
        "comparison_policy": "PRESERVE_SOURCE_REFERENCE_NO_IMPLICIT_CONVERSION",
    }

    assert validate(SCHEMA_V2, candidate) == []
    assert candidate["vertical_extent"]["lower"]["reference"] == "AMSL"
    assert candidate["vertical_extent"]["upper"] == {
        "boundary_character": "FLIGHT_LEVEL",
        "value": 185,
        "unit": "FL",
        "source_expression": "FL 185",
    }


def test_null_vertical_extent_does_not_mean_unbounded():
    for document in (HPAI_V2, FISH_V2):
        assert document["vertical_extent"] is None
        assert any(
            "does not mean vertically unbounded" in item
            for item in document["guardrails"]
        )


def test_vertical_schema_contains_no_conversion_engine():
    encoded = json.dumps(SCHEMA_V2, sort_keys=True).casefold()

    for forbidden in (
        "terrain",
        "pressure_model",
        "convert_agl",
        "convert_amsl",
        "point_in_volume",
        "volume_intersection",
    ):
        assert forbidden not in encoded

    assert (
        SCHEMA_V2["$defs"]["vertical_extent"]["properties"][
            "comparison_policy"
        ]["const"]
        == "PRESERVE_SOURCE_REFERENCE_NO_IMPLICIT_CONVERSION"
    )
