import json
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.multilingual.mutations import (
    correction_chain_for_language,
    events_for_language,
    operation_ids_for_language,
)


SCHEMA = json.loads(
    Path("schemas/language-scoped-mutation-v0.1.schema.json").read_text(encoding="utf-8")
)
FIXTURE = json.loads(
    Path("fixtures/multilingual/reg794-2004-corrigenda-language-scope-v0.1.json").read_text(encoding="utf-8")
)


def test_language_scoped_corrigenda_validate():
    validator = Draft202012Validator(SCHEMA)
    errors = []
    for event in FIXTURE["events"]:
        errors.extend(
            f"{event['event_id']}: {error.message}"
            for error in validator.iter_errors(event)
        )
    assert errors == []


def test_expression_histories_are_not_language_neutral():
    for language, expected in FIXTURE["expected_expression_histories"].items():
        actual = [event["event_id"] for event in events_for_language(FIXTURE["events"], language)]
        assert actual == expected

    eng_ops = set(operation_ids_for_language(FIXTURE["events"], "ENG"))
    fra_ops = set(operation_ids_for_language(FIXTURE["events"], "FRA"))

    assert "group-a-annex-i-part-iii-14-heading" in eng_ops
    assert "group-b-title-number" not in eng_ops
    assert "group-b-annex-i-intro" not in eng_ops
    assert "group-b-annex-iii-c-heading" not in eng_ops

    assert "group-b-title-number" in fra_ops
    assert "group-b-annex-i-intro" in fra_ops
    assert "group-b-annex-iii-c-heading" in fra_ops
    assert "group-a-annex-i-part-iii-14-heading" not in fra_ops


def test_nonlisted_language_is_no_assertion_not_global_negative():
    assert events_for_language(FIXTURE["events"], "POL") == []


def test_corrigendum_of_corrigendum_preserves_expression_chain():
    eng = correction_chain_for_language(FIXTURE["events"], "ENG")
    fra = correction_chain_for_language(FIXTURE["events"], "FRA")

    assert eng[-1] == {
        "event_id":"corr-2005-05-25-correct-placement",
        "corrects_event_ids":["corr-2005-01-28-group-a"],
    }
    assert fra[-1] == {
        "event_id":"corr-2005-05-25-correct-placement",
        "corrects_event_ids":["corr-2005-01-28-group-b"],
    }


def test_as_of_history_excludes_later_correction_of_correction():
    eng_january = [
        event["event_id"]
        for event in events_for_language(
            FIXTURE["events"], "ENG", as_of_date="2005-02-01"
        )
    ]
    assert eng_january == ["corr-2005-01-28-group-a"]
