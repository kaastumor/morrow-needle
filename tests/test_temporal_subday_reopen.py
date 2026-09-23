import json
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

from needle.temporal.resolver import status_on


FIXTURE = json.loads(
    Path(
        "fixtures/discovery/skagerrak-prawn-rtc-subday-temporal-reopen-v0.1.json"
    ).read_text(encoding="utf-8")
)
SCHEMA = json.loads(
    Path("schemas/temporal-assertion-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)


def instant_candidate(boundary, value):
    return {
        "assertion_id": f"rtc-{boundary.lower()}",
        "subject_ref": {
            "kind": "REGIME",
            "identifier": "skagerrak-prawn-rtc-hvmfs-2025-4",
            "locator": None,
        },
        "dimension": "APPLICATION",
        "boundary": boundary,
        "inclusive": boundary == "START",
        "trigger": {
            "kind": "ABSOLUTE_DATE",
            "date": value,
            "source_expression": value,
        },
        "normalized_date": value,
        "scope": {
            "mode": "DEFAULT",
            "applies_to": ["skagerrak-prawn-rtc-hvmfs-2025-4"],
            "overrides_assertion_ids": [],
            "entity_condition": None,
        },
        "resolution_state": "RESOLVED_ABSOLUTE",
        "evidence_state": "DIRECT",
        "source_refs": [{
            "source_type": "OTHER_OFFICIAL",
            "identifier": "HVMFS 2025:4",
            "locator": "Section 2",
            "language": "SWE",
            "role": "TEMPORAL_CLAUSE",
        }],
        "notes": None,
    }


def test_v0_1_schema_rejects_exact_offset_aware_instants():
    start = instant_candidate(
        "START",
        FIXTURE["official_instance"]["normalized_start"],
    )
    end = instant_candidate(
        "END",
        FIXTURE["official_instance"]["normalized_end_exclusive"],
    )

    start_errors = list(Draft202012Validator(SCHEMA).iter_errors(start))
    end_errors = list(Draft202012Validator(SCHEMA).iter_errors(end))

    assert start_errors
    assert end_errors
    assert any(error.validator == "format" for error in start_errors)
    assert any(error.validator == "format" for error in end_errors)


def test_v0_1_resolver_cannot_accept_instant_query():
    assertions = [
        instant_candidate(
            "START",
            FIXTURE["official_instance"]["normalized_start"],
        ),
        instant_candidate(
            "END",
            FIXTURE["official_instance"]["normalized_end_exclusive"],
        ),
    ]

    with pytest.raises(ValueError):
        status_on(
            assertions,
            dimension="APPLICATION",
            subject_keys={"skagerrak-prawn-rtc-hvmfs-2025-4"},
            on_date="2025-02-18T00:30:00+01:00",
        )


def test_date_rounding_would_change_legal_answers():
    cases = {
        item["query_instant"]: item["expected_active"]
        for item in FIXTURE["boundary_adversaries"]
    }

    assert cases["2025-02-18T00:30:00+01:00"] is False
    assert cases["2025-02-18T01:00:00+01:00"] is True
    assert cases["2025-03-04T00:59:00+01:00"] is True
    assert cases["2025-03-04T01:00:00+01:00"] is False


def test_reopen_is_pinned_before_schema_change():
    assert FIXTURE["v0_1_probe"]["result"] == "TEMPORAL_V0_1_REOPEN_TRIGGERED"
    assert FIXTURE["required_evolution"]["no_schema_added_in_failure_commit"] is True
