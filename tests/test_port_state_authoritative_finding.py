import json
from pathlib import Path


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/port-state-bahar-authoritative-finding-v0.1.json"
    ).read_text(encoding="utf-8")
)


def test_bahar_pins_categorical_inspection_determination():
    finding = FIXTURE["authoritative_finding"]

    assert finding["finding_character"] == "OFFICIAL_INSPECTION_DETERMINATION"
    assert finding["subject"]["identifier_scheme"] == "IMO"
    assert finding["subject"]["identifier"] == "8230156"
    assert finding["finding_date"] == "2026-07-18"
    assert finding["finding"]["category"] == "DETAINABLE_DEFICIENCIES"
    assert finding["finding"]["count"] == 13
    assert finding["textual_mutation"] is None


def test_official_outcome_is_detention_in_greece():
    outcome = FIXTURE["official_case_consequence"]

    assert outcome["result"] == "DETAINED"
    assert outcome["detention_date"] == "2026-07-18"
    assert outcome["member_state"] == "Greece"
    assert outcome["evidence_character"] == "DIRECT_OFFICIAL_OUTCOME"


def test_second_case_confirms_finding_not_scientific_specific():
    comparison = FIXTURE["comparison_to_hpai"]

    assert comparison["result"] == (
        "AUTHORITATIVE_FINDING_PATTERN_CONFIRMED_ACROSS_DOMAINS"
    )
    assert (
        "authoritative categorical determination about a concrete subject"
        in comparison["shared_shape"]
    )


def test_deficiency_count_does_not_reclassify_case_as_metric_trigger():
    finding = FIXTURE["authoritative_finding"]["finding"]
    probe = FIXTURE["architecture_probe"]

    assert finding["count"] == 13
    assert probe["metric_fit"] == "FAILS_CATEGORICAL_SEMANTICS"
    assert finding["category"] == "DETAINABLE_DEFICIENCIES"


def test_architecture_scope_is_direct_finding_only():
    probe = FIXTURE["architecture_probe"]

    assert probe["required_direct_object"] == "AUTHORITATIVE_FINDING"
    assert probe["decision"] == (
        "TWO_ORTHOGONAL_CASES_JUSTIFY_DIRECT_FINDING_CONTRACT_ONLY"
    )
    assert "derived spatial geometry" in probe["finding_should_not_own"]
    assert "generic enforcement workflow" in probe["finding_should_not_own"]
