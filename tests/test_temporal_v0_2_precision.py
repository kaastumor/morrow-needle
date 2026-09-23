import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from needle.temporal.resolver_v0_2 import (
    TemporalPrecisionError,
    status_at,
    upgrade_v0_1_assertion,
)


ASSERTION_SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
QUERY_SCHEMA = json.loads(
    Path("schemas/temporal-query-v0.2.schema.json").read_text(
        encoding="utf-8"
    )
)
RTC = json.loads(
    Path("fixtures/temporal/skagerrak-prawn-rtc-v0.2.json").read_text(
        encoding="utf-8"
    )
)
V01 = json.loads(
    Path("fixtures/temporal/temporal-adversaries-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def test_subday_assertions_validate_with_format_checking():
    validator = Draft202012Validator(
        ASSERTION_SCHEMA,
        format_checker=FormatChecker(),
    )
    errors = [
        error
        for assertion in RTC["assertions"]
        for error in validator.iter_errors(assertion)
    ]
    assert errors == []


def test_subday_queries_hit_exact_boundaries():
    for query in RTC["queries"]:
        result = status_at(
            RTC["assertions"],
            dimension="APPLICATION",
            subject_keys={RTC["subject"]},
            precision="INSTANT",
            at_value=query["instant"],
        )
        assert result["state"] == "RESOLVED", query["query_id"]
        assert result["active"] is query["expected_active"], query["query_id"]


def test_resolver_normalizes_offset_equivalent_instants_to_same_state():
    local = status_at(
        RTC["assertions"],
        dimension="APPLICATION",
        subject_keys={RTC["subject"]},
        precision="INSTANT",
        at_value="2025-02-18T01:00:00+01:00",
    )
    utc = status_at(
        RTC["assertions"],
        dimension="APPLICATION",
        subject_keys={RTC["subject"]},
        precision="INSTANT",
        at_value="2025-02-18T00:00:00Z",
    )
    assert local["active"] is True
    assert utc["active"] is True
    assert local["valid_value"] == utc["valid_value"]


def test_naive_instant_is_rejected_without_timezone_guess():
    try:
        status_at(
            RTC["assertions"],
            dimension="APPLICATION",
            subject_keys={RTC["subject"]},
            precision="INSTANT",
            at_value="2025-02-18T01:00:00",
        )
    except TemporalPrecisionError as exc:
        assert "explicit UTC offset" in str(exc)
    else:
        raise AssertionError("naive instant unexpectedly accepted")


def test_every_v0_1_fixture_query_survives_date_precision_upgrade():
    for case in V01["cases"]:
        upgraded = [
            upgrade_v0_1_assertion(assertion)
            for assertion in case["assertions"]
        ]
        for query in case.get("queries", []):
            result = status_at(
                upgraded,
                dimension=query["dimension"],
                subject_keys=set(query["subject_keys"]),
                precision="DATE",
                at_value=query["date"],
                context=query.get("context", {}),
            )
            expected = query["expected"]
            assert result["state"] == expected["state"], query["query_id"]
            assert result["active"] == expected["active"], query["query_id"]


def test_mixed_precision_fails_closed_instead_of_inventing_midnight():
    date_assertion = upgrade_v0_1_assertion(V01["cases"][0]["assertions"][0])
    date_assertion["scope"]["applies_to"] = [RTC["subject"]]

    result = status_at(
        RTC["assertions"] + [date_assertion],
        dimension="APPLICATION",
        subject_keys={RTC["subject"]},
        precision="INSTANT",
        at_value="2025-02-18T01:00:00+01:00",
    )
    assert result["state"] == "MIXED_PRECISION_UNRESOLVED"
    assert result["active"] is None


def test_v0_2_query_contract_requires_explicit_precision():
    validator = Draft202012Validator(
        QUERY_SCHEMA,
        format_checker=FormatChecker(),
    )
    good = {
        "query_id": "rtc-at-start",
        "dimension": "APPLICATION",
        "subject_keys": [RTC["subject"]],
        "valid_time": {
            "precision": "INSTANT",
            "instant": "2025-02-18T01:00:00+01:00",
        },
        "perspective": "EX_POST_LEGAL_EFFECT",
        "source_cutoff_time": None,
        "context": {},
    }
    assert list(validator.iter_errors(good)) == []

    ambiguous = dict(good)
    ambiguous["valid_time"] = {"instant": "2025-02-18T01:00:00+01:00"}
    assert list(validator.iter_errors(ambiguous))


def test_instant_assertion_rejects_naive_datetime_via_format_checker():
    bad = json.loads(json.dumps(RTC["assertions"][0]))
    bad["trigger"]["instant"] = "2025-02-18T01:00:00"
    bad["normalized_instant"] = "2025-02-18T01:00:00"

    errors = list(
        Draft202012Validator(
            ASSERTION_SCHEMA,
            format_checker=FormatChecker(),
        ).iter_errors(bad)
    )
    assert errors
