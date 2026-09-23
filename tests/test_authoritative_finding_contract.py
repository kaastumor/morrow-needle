import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA = json.loads(
    Path("schemas/authoritative-finding-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)
HPAI = json.loads(
    Path("fixtures/findings/hpai-woerdense-verlaat-v0.1.json").read_text(
        encoding="utf-8"
    )
)
BAHAR = json.loads(
    Path("fixtures/findings/port-state-bahar-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def validate(document):
    return list(Draft202012Validator(SCHEMA).iter_errors(document))


def test_both_orthogonal_findings_fit_same_direct_contract():
    assert validate(HPAI) == []
    assert validate(BAHAR) == []
    assert HPAI["character"] == BAHAR["character"] == "AUTHORITATIVE_FINDING"


def test_contract_distinguishes_science_from_inspection_judgment():
    assert HPAI["finding_type"] == "SCIENTIFIC_CONFIRMATION"
    assert BAHAR["finding_type"] == "INSPECTION_DETERMINATION"


def test_hpai_location_is_context_not_legal_zone_geometry():
    location = HPAI["location_ref"]
    encoded = json.dumps(HPAI, sort_keys=True)

    assert location["latitude"] == 52.16
    assert location["longitude"] == 4.89
    assert "radius_km" not in encoded
    assert "PROTECTION_ZONE" not in encoded
    assert "SURVEILLANCE_ZONE" not in encoded


def test_bahar_count_does_not_become_metric_object():
    encoded = json.dumps(BAHAR, sort_keys=True)

    assert BAHAR["proposition"]["category"] == "DETAINABLE_DEFICIENCIES"
    assert '"metric"' not in encoded
    assert '"value": 13' not in encoded


def test_findings_own_direct_truth_not_downstream_result():
    for finding in (HPAI, BAHAR):
        assert finding["evidence_state"] == "DIRECT"
        encoded = json.dumps(finding, sort_keys=True)
        assert "derived_effect" not in encoded
        assert "application_start" not in encoded
        assert "source_mutation_ids" not in encoded


def test_contract_is_not_generic_event_or_rules_engine():
    properties = set(SCHEMA["properties"])

    assert "rules" not in properties
    assert "effects" not in properties
    assert "workflow" not in properties
    assert "finding_date" in properties
    assert "proposition" in properties
