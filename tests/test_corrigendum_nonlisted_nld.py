import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.multilingual.mutations import events_for_language, operation_ids_for_language


SCHEMA=json.loads(
    Path("schemas/language-scoped-mutation-v0.1.schema.json").read_text(encoding="utf-8")
)
FIXTURE=json.loads(
    Path("fixtures/audit/reg2025-905-corrigendum-nonlisted-nld-v0.1.json").read_text(
        encoding="utf-8"
    )
)
EVENT=FIXTURE["language_scoped_event"]


def observations():
    return {
        item["language"]:item
        for item in FIXTURE["independent_expression_observations"]
    }


def test_2026_corrigendum_event_validates_against_frozen_language_scope_contract():
    errors=list(Draft202012Validator(SCHEMA).iter_errors(EVENT))
    assert errors == []


def test_dutch_is_nonlisted_no_assertion_not_a_corrigendum_mutation():
    assert "NLD" not in EVENT["expression_scope"]["languages"]
    assert EVENT["expression_scope"]["nonlisted_semantics"] == "NO_ASSERTION"
    assert events_for_language([EVENT],"NLD") == []
    assert operation_ids_for_language([EVENT],"NLD") == []
    assert FIXTURE["finding"]["no_assertion_for_nld_from_corrigendum"] is True


def test_english_corrigendum_operation_remains_expression_scoped():
    selected=events_for_language([EVENT],"ENG")
    assert [event["event_id"] for event in selected] == [EVENT["event_id"]]
    assert operation_ids_for_language([EVENT],"ENG") == [
        "reg2025-905-corr-article4p1-existing-aid-scheme"
    ]
    operation=EVENT["operations"][0]
    assert "existing aid that is authorised" in operation["before_text"]
    assert "existing aid scheme that is authorised" in operation["after_text"]


def test_independent_dutch_source_already_contains_scheme_concept():
    obs=observations()
    assert obs["ENG"]["concept_marker"] == "EXISTING_AID_WITHOUT_SCHEME_NOUN"
    assert obs["NLD"]["concept_marker"] == "EXISTING_AID_SCHEME_CONCEPT_PRESENT"
    assert "bestaande steunregeling" in obs["NLD"]["observed_text"]
    assert FIXTURE["finding"]["independent_nld_state_observed"] is True


def test_independent_dutch_observation_does_not_become_cross_language_equivalence():
    assert FIXTURE["finding"]["cross_language_equivalence_asserted"] is False
    forbidden=" ".join(FIXTURE["forbidden_inferences"])
    assert "legally or semantically equivalent" in forbidden
    assert "globalized across all language expressions" in forbidden


def test_absence_from_language_list_is_not_global_negative():
    forbidden=" ".join(FIXTURE["forbidden_inferences"])
    assert "definitely unaffected by every correction" in forbidden
    assert events_for_language([EVENT],"NLD") == []
