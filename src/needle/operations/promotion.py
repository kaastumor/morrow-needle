from __future__ import annotations

from datetime import datetime


def _instant(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("operational promotion timestamps must be offset-aware")
    return parsed


def promotion_decision(
    *,
    remote_cursor: str,
    expected_cursor: str,
    generated_cursor: str,
) -> str:
    """Return the compare-and-swap decision for a generated monitor cycle.

    A cycle is derived from ``expected_cursor`` and may replace promoted state
    only while main still exposes that exact completed boundary. The cursor is
    therefore the compare-and-swap token for the complete promoted operational
    snapshot, including baselines, results, cards and provenance observations.
    """
    remote = _instant(remote_cursor)
    expected = _instant(expected_cursor)
    generated = _instant(generated_cursor)
    if remote_cursor == generated_cursor:
        return "ALREADY_PROMOTED"
    if remote_cursor != expected_cursor:
        return "STALE_REMOTE"
    if generated <= expected:
        return "INVALID_GENERATED_CURSOR"
    return "PROMOTE"
