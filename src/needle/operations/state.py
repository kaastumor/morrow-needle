from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from typing import Any

from needle.provenance.ledger import verify_record_hash
from needle.updates.classify import snapshot_from_observations
from needle.updates.reobserve import celex_from_event


class OperationalStateError(ValueError):
    pass


def _instant(value: str) -> datetime:
    parsed=datetime.fromisoformat(value.replace("Z","+00:00"))
    if parsed.tzinfo is None:
        raise OperationalStateError(
            "operational timestamps must be offset-aware"
        )
    return parsed


def baseline_key(
    identifier: str,
    language: str = "ENG",
) -> str:
    return f"{identifier.upper()}|{language.upper()}"


def _record_map(state: dict[str,Any]) -> dict[str,dict[str,Any]]:
    records={}
    for record in state.get("source_observations",[]):
        record_id=record["record_id"]
        if record_id in records:
            raise OperationalStateError(
                f"duplicate operational source observation: {record_id}"
            )
        if record.get("record_type") != "SOURCE_OBSERVATION":
            raise OperationalStateError(
                f"operational state accepts only SOURCE_OBSERVATION records: {record_id}"
            )
        if not verify_record_hash(record):
            raise OperationalStateError(
                f"invalid source observation hash: {record_id}"
            )
        records[record_id]=record
    return records


def validate_operational_state(
    state: dict[str,Any],
) -> list[str]:
    errors=[]
    try:
        records=_record_map(state)
    except OperationalStateError as exc:
        errors.append(str(exc))
        return errors

    seen=set()
    for baseline in state.get("baselines",[]):
        key=baseline["baseline_key"]
        if key in seen:
            errors.append(f"duplicate baseline_key: {key}")
        seen.add(key)

        expected=baseline_key(
            baseline["identifier"],
            baseline["language"],
        )
        if key != expected:
            errors.append(
                f"{key}: baseline_key does not match identifier/language"
            )

        for field in (
            "content_observation_id",
            "metadata_observation_id",
        ):
            record_id=baseline.get(field)
            if record_id is None:
                continue
            if record_id not in records:
                errors.append(
                    f"{key}: {field} references missing observation {record_id}"
                )

        if _instant(
            baseline["eligible_for_event_ingestion_after"]
        ) < _instant(baseline["observed_at"]):
            errors.append(
                f"{key}: eligibility cannot predate observation"
            )
    return errors


def empty_operational_state(
    *,
    state_id: str,
    updated_at: str,
) -> dict[str,Any]:
    return {
        "schema_version":"operational-state-v0.1",
        "state_id":state_id,
        "character":"OPERATIONAL_CACHE",
        "updated_at":updated_at,
        "baseline_policy":"PROSPECTIVE_ONLY",
        "processed_event_keys":[],
        "source_observations":[],
        "baselines":[],
        "poll_cursor":{
            "last_completed_end":updated_at,
            "overlap_seconds":300,
        },
    }


def _celex_identifier(event: dict[str,Any]) -> str | None:
    celex=celex_from_event(event)
    return f"CELEX:{celex}" if celex else None


def lookup_baseline(
    state: dict[str,Any],
    event: dict[str,Any],
    *,
    language: str = "ENG",
) -> dict[str,Any]:
    """Return an eligible prior snapshot or a fail-closed reason.

    A cold-start observation may only compare to feed events whose ingestion
    time is strictly later than the baseline eligibility boundary.
    """
    identifier=_celex_identifier(event)
    if identifier is None:
        return {
            "state":"NO_BASELINE_KEY",
            "baseline":None,
            "snapshot":None,
            "reason":"Feed event has no CELEX identifier for operational baseline lookup.",
        }

    key=baseline_key(identifier,language)
    matches=[
        item for item in state.get("baselines",[])
        if item["baseline_key"] == key
    ]
    if not matches:
        return {
            "state":"MISSING_BASELINE",
            "baseline":None,
            "snapshot":None,
            "reason":f"No operational baseline exists for {key}.",
        }
    if len(matches) != 1:
        raise OperationalStateError(
            f"expected one operational baseline for {key}, got {len(matches)}"
        )

    baseline=matches[0]
    event_time=_instant(event["ingestion_time"])
    eligible_after=_instant(
        baseline["eligible_for_event_ingestion_after"]
    )
    if event_time <= eligible_after:
        return {
            "state":"BASELINE_NOT_PRIOR",
            "baseline":baseline,
            "snapshot":None,
            "reason":(
                "Operational baseline was captured at or after this feed event "
                "and cannot be used retroactively."
            ),
        }

    records=_record_map(state)
    content=(
        records.get(baseline["content_observation_id"])
        if baseline["content_observation_id"] else None
    )
    metadata=(
        records.get(baseline["metadata_observation_id"])
        if baseline["metadata_observation_id"] else None
    )
    return {
        "state":"ELIGIBLE",
        "baseline":baseline,
        "snapshot":snapshot_from_observations(
            content_observation=content,
            metadata_observation=metadata,
            available=True,
        ),
        "reason":None,
    }


def baseline_seed_eligible(
    reobservation: dict[str,Any],
) -> bool:
    """Return whether an observation is safe to become the next comparator.

    Availability and comparator completeness are deliberately different.
    A content-only or metadata-only observation can prove that a source route
    remains available and can support an operational abstention, but replacing
    a complete prospective baseline with that partial snapshot would discard a
    previously known comparison dimension after a transient route failure.
    """
    snapshot=reobservation.get("snapshot")
    return bool(
        reobservation.get("state")=="OBSERVED"
        and snapshot
        and snapshot.get("available") is True
        and snapshot.get("content_observation_id")
        and snapshot.get("metadata_observation_id")
    )


def advance_baseline(
    state: dict[str,Any],
    event: dict[str,Any],
    reobservation: dict[str,Any],
    *,
    updated_at: str,
    seed_character: str,
    language: str = "ENG",
    mark_event_processed: bool = True,
    eligible_for_event_ingestion_after: str | None = None,
) -> dict[str,Any]:
    """Append observations and move one operational baseline pointer.

    Existing provenance records remain untouched. Re-running with the same
    records and event is idempotent.
    """
    if seed_character not in {
        "COLD_START_SEED","POST_EVENT_REFRESH"
    }:
        raise OperationalStateError(
            f"unsupported seed_character: {seed_character}"
        )

    identifier=_celex_identifier(event)
    if identifier is None:
        raise OperationalStateError(
            "cannot advance operational baseline without CELEX identifier"
        )
    snapshot=reobservation.get("snapshot")
    if snapshot is None or snapshot.get("available") is not True:
        raise OperationalStateError(
            "cannot advance baseline from unavailable/unresolved observation"
        )
    if (
        snapshot.get("content_observation_id") is None
        and snapshot.get("metadata_observation_id") is None
    ):
        raise OperationalStateError(
            "baseline requires at least one immutable source observation"
        )

    next_state=deepcopy(state)
    existing={
        record["record_id"]:record
        for record in next_state.get("source_observations",[])
    }
    for name in ("metadata_observation","content_observation"):
        record=reobservation.get(name)
        if record is None:
            continue
        prior=existing.get(record["record_id"])
        if prior is not None and prior != record:
            raise OperationalStateError(
                f"record_id collision with different content: {record['record_id']}"
            )
        if prior is None:
            next_state["source_observations"].append(record)
            existing[record["record_id"]]=record

    key=baseline_key(identifier,language)
    observed_at=(
        reobservation.get("content_observation")
        or reobservation.get("metadata_observation")
    )["payload"]["observed_at"]

    baseline={
        "baseline_key":key,
        "identifier":identifier,
        "language":language.upper(),
        "root_cellar_id":event["root_cellar_id"],
        "content_observation_id":snapshot.get(
            "content_observation_id"
        ),
        "metadata_observation_id":snapshot.get(
            "metadata_observation_id"
        ),
        "observed_at":observed_at,
        "eligible_for_event_ingestion_after":(
            eligible_for_event_ingestion_after or observed_at
        ),
        "seed_character":seed_character,
    }
    next_state["baselines"]=[
        item for item in next_state.get("baselines",[])
        if item["baseline_key"] != key
    ]+[baseline]
    next_state["baselines"].sort(
        key=lambda item:item["baseline_key"]
    )

    if mark_event_processed:
        next_state["processed_event_keys"]=sorted(set(
            set(next_state.get("processed_event_keys",[]))
            | {event["event_key"]}
        ))
    next_state["updated_at"]=updated_at

    errors=validate_operational_state(next_state)
    if errors:
        raise OperationalStateError("; ".join(errors))
    return next_state



def mark_event_processed(
    state: dict[str,Any],
    event_key: str,
    *,
    updated_at: str,
) -> dict[str,Any]:
    next_state=deepcopy(state)
    next_state["processed_event_keys"]=sorted(
        set(next_state.get("processed_event_keys",[]))
        | {event_key}
    )
    next_state["updated_at"]=updated_at
    return next_state


def complete_poll_window(
    state: dict[str,Any],
    *,
    window_end: str,
    updated_at: str,
) -> dict[str,Any]:
    """Advance only the last fully completed operational polling boundary."""
    _instant(window_end)
    next_state=deepcopy(state)
    next_state.setdefault("poll_cursor",{})
    next_state["poll_cursor"]["last_completed_end"]=window_end
    next_state["poll_cursor"].setdefault("overlap_seconds",300)
    next_state["updated_at"]=updated_at
    return next_state
