import json
from pathlib import Path

from jsonschema import Draft202012Validator


DISCOVERY = json.loads(
    Path(
        "fixtures/discovery/air-passenger-compensation-near-mutation-v0.1.json"
    ).read_text(encoding="utf-8")
)
PROCEDURE = json.loads(
    Path(
        "fixtures/procedure/air-passenger-rights-2013-0072-near-mutation-v0.1.json"
    ).read_text(encoding="utf-8")
)
PROCEDURE_SCHEMA = json.loads(
    Path("schemas/procedure-state-event-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def test_procedure_events_fit_existing_contract():
    errors = [
        error.message
        for event in PROCEDURE["events"]
        for error in Draft202012Validator(PROCEDURE_SCHEMA).iter_errors(event)
    ]
    assert errors == []


def test_final_adopted_amount_component_returns_to_2004_baseline():
    baseline = DISCOVERY["baseline"]["amount_schedule_eur"]
    stages = {item["stage"]: item for item in DISCOVERY["procedural_rule_states"]}
    final = stages["CONCILIATION_AND_FINAL_ADOPTION_2026"]

    assert baseline == [250, 400, 600]
    assert final["amount_schedule_eur"] == baseline
    assert final["amount_component_relation_to_2004"] == (
        "NOMINAL_AMOUNT_SCHEDULE_UNCHANGED"
    )


def test_real_intermediate_variants_are_preserved_without_becoming_law():
    stages = {item["stage"]: item for item in DISCOVERY["procedural_rule_states"]}
    baseline = DISCOVERY["baseline"]["amount_schedule_eur"]

    council = stages["COUNCIL_FIRST_READING_2025"]
    parliament = stages["PARLIAMENT_SECOND_READING_2026"]

    assert council["amount_schedule_eur"] != baseline
    assert parliament["amount_schedule_eur"] != baseline
    assert council["canonical_legal_mutation"] is False
    assert parliament["canonical_legal_mutation"] is False


def test_inflation_context_does_not_mutate_the_legal_amounts():
    context = DISCOVERY["contextual_drift"]

    assert context["classification"] == "EXTERNAL_CONTEXT_NOT_LEGAL_MUTATION"
    assert context["eca_2018_theoretical_inflation_equivalents_eur"] == [
        313,
        500,
        751,
    ]
    assert context["legal_amount_schedule_after_observation_eur"] == [
        250,
        400,
        600,
    ]


def test_amount_stasis_does_not_imply_whole_rule_stasis():
    finding = DISCOVERY["finding"]
    final = {
        item["stage"]: item for item in DISCOVERY["procedural_rule_states"]
    }["CONCILIATION_AND_FINAL_ADOPTION_2026"]

    assert finding["amount_component_changed_in_final_adopted_text"] is False
    assert finding["whole_compensation_rule_unchanged"] is False
    assert final["whole_rule_relation_to_2004"] == "NOT_IDENTICAL"
    assert final["delay_trigger_hours"] == [3]


def test_formal_adoption_is_not_promoted_to_application():
    final_event = PROCEDURE["events"][-1]
    encoded = json.dumps(final_event, sort_keys=True)

    assert final_event["event_kind"] == "FORMAL_ACT_ADOPTED"
    assert {"dimension": "FORMAL_ACT_ADOPTION", "value": "ADOPTED"} in (
        final_event["effects"]
    )
    assert "FINAL_ACT_PUBLICATION" not in encoded
    assert "APPLICATION" not in encoded


def test_discovery_does_not_require_a_new_change_type():
    result = DISCOVERY["architecture_result"]

    assert result["decision"] == "SURVIVES_WITH_STRICT_LAYER_SEPARATION"
    assert result["new_schema_required"] is False
    assert set(result["layers"]) == {
        "applicable/adopted legal rule state",
        "procedure-stage institutional position",
        "external contextual observation",
    }
