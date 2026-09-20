import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.temporal.resolver import gap_between


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


SCHEMA = load("schemas/regime-lineage-v0.2.schema.json")
TEMPORAL_SCHEMA = load("schemas/temporal-assertion-v0.1.schema.json")
LINEAGE = load(
    "fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.2.json"
)
TEMPORAL = load(
    "fixtures/temporal/eprivacy-temporary-regime-v0.1.json"
)
OLD = load(
    "fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.1.json"
)


def temporal_index(data=TEMPORAL):
    return {
        assertion["assertion_id"]:assertion
        for assertion in data["assertions"]
    }


def referenced_gap(edge=LINEAGE, temporal=TEMPORAL):
    registry = {
        assertion["assertion_id"]:assertion
        for assertion in temporal["assertions"]
    }
    end = registry["eprivacy-2021-extended-application-end"]
    start = registry["eprivacy-2026-application-start"]
    assert set(edge["temporal_assertion_refs"]) >= {
        end["assertion_id"],
        start["assertion_id"],
    }
    return gap_between(
        end["normalized_date"],
        start["normalized_date"],
        previous_end_inclusive=end.get("inclusive", True),
        next_start_inclusive=start.get("inclusive", True),
    )


def test_regime_lineage_v02_validates():
    assert list(Draft202012Validator(SCHEMA).iter_errors(LINEAGE)) == []


def test_eprivacy_temporal_assertions_validate_canonical_contract():
    validator = Draft202012Validator(TEMPORAL_SCHEMA)
    errors = [
        f"{assertion['assertion_id']}: {error.message}"
        for assertion in TEMPORAL["assertions"]
        for error in validator.iter_errors(assertion)
    ]
    assert errors == []


def test_regime_lineage_v02_contains_no_canonical_temporal_values():
    encoded = json.dumps(LINEAGE, sort_keys=True)
    forbidden = [
        "application_start",
        "application_end",
        "applicability_continuity",
        "\"gap\"",
        "2021-08-02",
        "2026-04-03",
        "2026-07-31",
        "2028-04-03",
    ]
    for value in forbidden:
        assert value not in encoded

    for ref in LINEAGE["sources"] + LINEAGE["targets"]:
        assert set(ref) <= {"regime_id", "act_ids", "scope_note"}


def test_regime_lineage_temporal_references_resolve():
    registry = temporal_index()
    assert LINEAGE["temporal_assertion_refs"]
    assert set(LINEAGE["temporal_assertion_refs"]) <= set(registry)


def test_gap_is_derived_only_from_temporal_assertions():
    assert referenced_gap() == {
        "state":"GAP",
        "start":"2026-04-04",
        "end":"2026-07-30",
    }


def test_temporal_change_updates_derived_gap_without_editing_lineage():
    changed = deepcopy(TEMPORAL)
    registry = {
        assertion["assertion_id"]:assertion
        for assertion in changed["assertions"]
    }
    registry["eprivacy-2026-application-start"]["normalized_date"] = "2026-08-10"
    registry["eprivacy-2026-application-start"]["trigger"] = {
        "kind":"ABSOLUTE_DATE",
        "date":"2026-08-10",
        "source_expression":"test-only changed canonical temporal input",
    }
    registry["eprivacy-2026-application-start"]["resolution_state"] = (
        "RESOLVED_ABSOLUTE"
    )

    assert referenced_gap(temporal=changed) == {
        "state":"GAP",
        "start":"2026-04-04",
        "end":"2026-08-09",
    }
    assert LINEAGE["edge_id"] == "eprivacy-2021-regime-reenacted-as-2026"


def test_v01_is_explicitly_noncanonical_history():
    assert OLD["status"] == "SUPERSEDED_DISCOVERY_PROVENANCE"
    assert OLD["canonical_successor"].endswith(
        "reg2021-1232-to-reg2026-1881-gap-v0.2.json"
    )
