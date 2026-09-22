from __future__ import annotations

from copy import deepcopy
from typing import Any

from needle.operations.state import OperationalStateError, validate_operational_state


def retain_operational_observations(
    state: dict[str, Any],
    *,
    latest_results: list[dict[str, Any]],
    updated_at: str,
) -> dict[str, Any]:
    """Bound the hot observation cache to live baseline/latest-output references.

    ``operational-state`` is a prospective comparison cache, not the append-only
    provenance ledger.  Keeping every historical re-observation here duplicates
    provenance ownership and grows the checked-in state forever.  We retain only
    immutable Source Observations needed by current baselines or the latest
    promoted Operational Results.  Older durable provenance belongs in the
    canonical provenance ledger/artifacts, not this hot cache.
    """
    keep: set[str] = set()
    for baseline in state.get("baselines", []):
        for field in ("content_observation_id", "metadata_observation_id"):
            value = baseline.get(field)
            if value:
                keep.add(value)

    for result in latest_results:
        for value in result.get("evidence_refs", []):
            if isinstance(value, str) and value.startswith("src-operational-"):
                keep.add(value)

    records = {record["record_id"]: record for record in state.get("source_observations", [])}
    missing = sorted(keep - records.keys())
    if missing:
        raise OperationalStateError(
            "cannot retain operational evidence because referenced Source Observations are missing: "
            + ", ".join(missing)
        )

    next_state = deepcopy(state)
    next_state["source_observations"] = [records[key] for key in sorted(keep)]
    next_state["updated_at"] = updated_at
    errors = validate_operational_state(next_state)
    if errors:
        raise OperationalStateError("; ".join(errors))
    return next_state
