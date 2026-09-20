"""Machine comparison between Needle emissions and Gold Corpus expectations.

Gold expectations use partial structural matches: expected keys must be present and
equal, while emitters may attach additional provenance/debug fields. This keeps the
corpus coupled to legal invariants rather than implementation detail.
"""
from __future__ import annotations

from typing import Any


def _contains(actual: Any, expected: Any) -> bool:
    if isinstance(expected, dict):
        return isinstance(actual, dict) and all(
            key in actual and _contains(actual[key], value)
            for key, value in expected.items()
        )
    if isinstance(expected, list):
        return isinstance(actual, list) and all(
            any(_contains(candidate, wanted) for candidate in actual)
            for wanted in expected
        )
    return actual == expected


def compare_expectations(expectations: list[dict[str, Any]], emitted: list[dict[str, Any]]) -> list[str]:
    """Return violations of machine-readable Gold expectations.

    Each expectation has ``outcome`` (PRESENT or ABSENT) and a partial ``match``.
    ABSENT is deliberately first-class: a false legal inference must fail CI just as
    reliably as a missing true fact.
    """
    errors: list[str] = []
    for expectation in expectations:
        matches = [fact for fact in emitted if _contains(fact, expectation["match"])]
        outcome = expectation["outcome"]
        assertion_id = expectation["assertion_id"]
        if outcome == "PRESENT" and not matches:
            errors.append(f"{assertion_id}: required fact was not emitted")
        elif outcome == "ABSENT" and matches:
            errors.append(f"{assertion_id}: forbidden fact was emitted")
    return errors
