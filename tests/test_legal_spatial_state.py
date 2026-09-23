import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


SPATIAL_SCHEMA = json.loads(
    Path("schemas/legal-spatial-state-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
METRIC_SCHEMA = json.loads(
    Path("schemas/authoritative-metric-observation-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
TEMPORAL_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
HPAI = json.loads(
    Path(
        "fixtures/spatial/hpai-woerdense-verlaat-protection-zone-v0.1.json"
    ).read_text(encoding="utf-8")
)
FISHERY = json.loads(
    Path(
        "fixtures/spatial/skagerrak-prawn-rtc-hvmfs-2025-4-v0.1.json"
    ).read_text(encoding="utf-8")
)
PRAWN_METRIC = json.loads(
    Path(
        "fixtures/metrics/skagerrak-prawn-sample-2025-02-16-v0.1.json"
    ).read_text(encoding="utf-8")
)
HPAI_TIME = json.loads(
    Path(
        "fixtures/temporal/hpai-woerdense-verlaat-protection-zone-v0.2.json"
    ).read_text(encoding="utf-8")
)
FISH_TIME = json.loads(
    Path("fixtures/temporal/skagerrak-prawn-rtc-v0.2.json").read_text(
        encoding="utf-8"
    )
)


def test_two_unrelated_spatial_states_fit_same_bounded_contract():
    validator = Draft202012Validator(SPATIAL_SCHEMA)
    assert list(validator.iter_errors(HPAI)) == []
    assert list(validator.iter_errors(FISHERY)) == []
    assert HPAI["geometry"]["geometry_type"] == "CIRCLE"
    assert FISHERY["geometry"]["geometry_type"] == "POLYGON"


def test_hpai_circle_is_direct_geometry_referencing_finding():
    geometry = HPAI["geometry"]
    causal = HPAI["causal_input_refs"][0]

    assert geometry["centre"]["latitude"] == 52.16
    assert geometry["centre"]["longitude"] == 4.89
    assert geometry["radius"] == {"value": 3, "unit": "KM"}
    assert causal["object_type"] == "AUTHORITATIVE_FINDING"
    assert causal["object_id"] == "finding:hpai:NL-HPAI(NON-P)-2026-00174"
    assert causal["evidence_state"] == "DIRECT"


def _dms_minutes_to_decimal(value):
    degrees, minutes = value
    return degrees + minutes / 60


def test_swedish_polygon_preserves_and_normalizes_source_coordinates():
    vertices = FISHERY["geometry"]["vertices"]

    assert len(vertices) == 7
    assert vertices[0]["latitude"] == vertices[-1]["latitude"]
    assert vertices[0]["longitude"] == vertices[-1]["longitude"]
    assert len({
        (item["latitude"], item["longitude"])
        for item in vertices[:-1]
    }) == 6

    expected = [
        (_dms_minutes_to_decimal((58, 35.503)), _dms_minutes_to_decimal((10, 27.232))),
        (_dms_minutes_to_decimal((58, 27.543)), _dms_minutes_to_decimal((10, 39.485))),
        (_dms_minutes_to_decimal((58, 19.033)), _dms_minutes_to_decimal((10, 40.903))),
        (_dms_minutes_to_decimal((58, 17.959)), _dms_minutes_to_decimal((10, 35.667))),
        (_dms_minutes_to_decimal((58, 26.777)), _dms_minutes_to_decimal((10, 34.509))),
        (_dms_minutes_to_decimal((58, 34.402)), _dms_minutes_to_decimal((10, 22.530))),
    ]
    for actual, (lat, lon) in zip(vertices[:-1], expected):
        assert abs(actual["latitude"] - lat) < 1e-9
        assert abs(actual["longitude"] - lon) < 1e-9


def test_fishery_metric_is_direct_but_specific_causal_link_remains_derived():
    metric_errors = list(
        Draft202012Validator(
            METRIC_SCHEMA,
            format_checker=FormatChecker(),
        ).iter_errors(PRAWN_METRIC)
    )
    assert metric_errors == []
    assert PRAWN_METRIC["metric"]["value"] == 66.5

    causal = FISHERY["causal_input_refs"][0]
    assert causal["object_type"] == "AUTHORITATIVE_METRIC_OBSERVATION"
    assert causal["object_id"] == PRAWN_METRIC["observation_id"]
    assert causal["evidence_state"] == "DERIVED"


def test_spatial_objects_reference_time_instead_of_copying_it():
    hpai_ids = {
        item["assertion_id"]
        for item in HPAI_TIME["assertions"]
    }
    fish_ids = {
        item["assertion_id"]
        for item in FISH_TIME["assertions"]
    }

    assert set(HPAI["temporal_assertion_refs"]).issubset(hpai_ids)
    assert set(FISHERY["temporal_assertion_refs"]).issubset(fish_ids)

    for document in (HPAI, FISHERY):
        encoded = json.dumps(document, sort_keys=True)
        assert '"start_date"' not in encoded
        assert '"end_date"' not in encoded
        assert '"normalized_date"' not in encoded
        assert '"normalized_instant"' not in encoded


def test_hpai_date_precision_temporal_assertions_are_v0_2_valid():
    validator = Draft202012Validator(
        TEMPORAL_SCHEMA,
        format_checker=FormatChecker(),
    )
    errors = [
        error
        for assertion in HPAI_TIME["assertions"]
        for error in validator.iter_errors(assertion)
    ]
    assert errors == []


def test_spatial_contract_is_not_a_gis_or_rule_engine():
    encoded = json.dumps(SPATIAL_SCHEMA, sort_keys=True).casefold()

    for forbidden in (
        "point_in_polygon",
        "intersection",
        "overlay",
        "route",
        "geocode",
        "formula",
        "expression_ast",
    ):
        assert forbidden not in encoded
