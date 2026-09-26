import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from scripts.validate_maintenance_delta import semantic_errors


SCHEMA = json.loads(
    Path("schemas/maintenance-delta-v0.1.schema.json").read_text(encoding="utf-8")
)
FIXTURE_DIR = Path("fixtures/mvp/maintenance-delta")
FIXTURES = {
    path.stem: json.loads(path.read_text(encoding="utf-8"))
    for path in sorted(FIXTURE_DIR.glob("*.json"))
}


def schema_errors(document):
    return list(Draft202012Validator(SCHEMA).iter_errors(document))


def test_all_three_replay_fixtures_validate():
    assert set(FIXTURES) == {
        "delta-s009-activation",
        "harvey-hsr-2025",
        "harvey-v3-semantic-revision-control",
    }
    for record in FIXTURES.values():
        assert schema_errors(record) == []
        assert semantic_errors(record) == []


def test_legal_proposition_requires_evidence_and_governing_time():
    record = copy.deepcopy(FIXTURES["harvey-hsr-2025"])
    unit = record["delta_units"][0]
    unit.pop("evidence")
    unit.pop("governing_time")

    errors = semantic_errors(record)

    assert any("LEGAl_PROPOSITION".lower() in error.lower() and "evidence" in error for error in errors)
    assert any("LEGAl_PROPOSITION".lower() in error.lower() and "governing_time" in error for error in errors)


def test_owner_adopted_change_requires_candidate_contract_reference():
    record = copy.deepcopy(FIXTURES["harvey-v3-semantic-revision-control"])
    record["subject"].pop("candidate_contract_ref")

    assert any(
        "ADOPTED_BY_OWNER requires subject.candidate_contract_ref" in error
        for error in semantic_errors(record)
    )


def test_accepted_repair_requires_owner_adoption_and_candidate_reference():
    record = copy.deepcopy(FIXTURES["delta-s009-activation"])
    record["repair_status"] = "ACCEPTED"
    record["change_status"] = "OBSERVED"

    errors = semantic_errors(record)

    assert any("accepted repair requires subject.candidate_contract_ref" in error for error in errors)
    assert any("accepted repair requires change_status ADOPTED_BY_OWNER" in error for error in errors)


def test_unknown_or_noncomparable_results_cannot_silently_do_nothing():
    record = copy.deepcopy(FIXTURES["harvey-v3-semantic-revision-control"])
    record["result_impact"]["existing_outputs_action"] = "NONE"

    assert any(
        "NOT_COMPARABLE/UNKNOWN result impact cannot use existing_outputs_action NONE" in error
        for error in semantic_errors(record)
    )


def test_no_known_score_impact_is_exclusive():
    record = copy.deepcopy(FIXTURES["delta-s009-activation"])
    record["delta_units"][0]["risk"] = ["NO_KNOWN_SCORE_IMPACT", "AMBIGUOUS_GRADING"]

    assert any(
        "NO_KNOWN_SCORE_IMPACT cannot be combined with another risk" in error
        for error in semantic_errors(record)
    )


def test_schema_rejects_removed_repair_action_bucket():
    record = copy.deepcopy(FIXTURES["harvey-v3-semantic-revision-control"])
    record["repair_actions"] = ["Rewrite the rubric."]

    assert schema_errors(record)


def test_schema_rejects_needle_taxonomy_metadata():
    record = copy.deepcopy(FIXTURES["harvey-hsr-2025"])
    record["needle_failure_class"] = "STATUS_APPLICATION_SEPARATION"

    assert schema_errors(record)


def test_control_records_adopted_revision_without_calling_it_a_repair():
    record = FIXTURES["harvey-v3-semantic-revision-control"]

    assert record["change_status"] == "ADOPTED_BY_OWNER"
    assert record["repair_status"] == "NOT_REQUIRED"
    assert record["subject"]["candidate_contract_ref"]


def test_hsr_fixture_preserves_event_owned_legal_time():
    record = FIXTURES["harvey-hsr-2025"]

    assert all(
        unit["governing_time"]["kind"] == "CONTROLLING_EVENT_DATE"
        for unit in record["delta_units"]
    )


def test_delta_activation_fixture_does_not_need_legal_time_owner():
    record = FIXTURES["delta-s009-activation"]

    assert record["delta_units"][0]["kind"] == "CRITERION_ACTIVATION"
    assert record["delta_units"][0]["governing_time"]["kind"] == "NOT_APPLICABLE"
