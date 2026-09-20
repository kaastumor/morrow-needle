from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from typing import Any


def canonical_record_bytes(record: dict[str, Any]) -> bytes:
    material = deepcopy(record)
    material.pop("record_hash", None)
    return json.dumps(
        material,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def compute_record_hash(record: dict[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(canonical_record_bytes(record)).hexdigest()


def seal_record(record: dict[str, Any]) -> dict[str, Any]:
    sealed = deepcopy(record)
    sealed["record_hash"] = compute_record_hash(sealed)
    return sealed


def verify_record_hash(record: dict[str, Any]) -> bool:
    return record.get("record_hash") == compute_record_hash(record)


def _record_map(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {record["record_id"]:record for record in records}


def validate_ledger(records: list[dict[str, Any]]) -> list[str]:
    """Validate append-only reference and content-hash invariants.

    Ordering matters: a record may reference only records already appended.
    """
    errors: list[str] = []
    seen: dict[str, dict[str, Any]] = {}
    superseded_by: dict[str, str] = {}

    for record in records:
        record_id = record.get("record_id")
        if record_id in seen:
            errors.append(f"duplicate record_id: {record_id}")
            continue

        if not verify_record_hash(record):
            errors.append(f"record hash mismatch: {record_id}")

        payload = record.get("payload", {})
        kind = record.get("record_type")

        def require_existing(ref_id: str, expected_type: str | None = None) -> dict[str, Any] | None:
            target = seen.get(ref_id)
            if target is None:
                errors.append(
                    f"{record_id}: reference is not an earlier ledger record: {ref_id}"
                )
                return None
            if expected_type and target.get("record_type") != expected_type:
                errors.append(
                    f"{record_id}: {ref_id} must be {expected_type}, "
                    f"got {target.get('record_type')}"
                )
            return target

        if kind == "DERIVATION_RUN":
            for input_id in payload.get("input_record_ids", []):
                require_existing(input_id)

        elif kind == "CLAIM_SUPPORT":
            source = require_existing(
                payload.get("source_observation_id"),
                "SOURCE_OBSERVATION",
            )
            require_existing(
                payload.get("derivation_record_id"),
                "DERIVATION_RUN",
            )
            if source:
                expected_hash = source["payload"]["artifact_hash"]
                actual_hash = payload.get("source_span", {}).get("artifact_hash")
                if expected_hash != actual_hash:
                    errors.append(
                        f"{record_id}: source span artifact hash does not match "
                        f"source observation"
                    )

        elif kind == "SUPERSESSION":
            superseded = payload.get("superseded_record_ids", [])
            replacements = payload.get("replacement_record_ids", [])
            for ref_id in superseded + replacements:
                require_existing(ref_id)
            for ref_id in superseded:
                prior = superseded_by.get(ref_id)
                if prior is not None:
                    errors.append(
                        f"{record_id}: {ref_id} was already superseded by {prior}"
                    )
                else:
                    superseded_by[ref_id] = record_id
            if record_id in set(superseded + replacements):
                errors.append(f"{record_id}: supersession cannot reference itself")
            if set(superseded) & set(replacements):
                errors.append(
                    f"{record_id}: same record cannot be both superseded and replacement"
                )

        seen[record_id] = record

    return errors


def trace_claim_support(
    records: list[dict[str, Any]],
    *,
    entity_type: str,
    entity_id: str,
) -> list[dict[str, Any]]:
    """Return support edges for an entity with their immutable source observations."""
    by_id = _record_map(records)
    result = []
    for record in records:
        if record.get("record_type") != "CLAIM_SUPPORT":
            continue
        claim = record["payload"]["claim_ref"]
        if claim != {"entity_type":entity_type,"entity_id":entity_id}:
            continue
        source = by_id.get(record["payload"]["source_observation_id"])
        derivation = by_id.get(record["payload"]["derivation_record_id"])
        result.append({
            "support_record":record,
            "source_observation":source,
            "derivation_record":derivation,
        })
    return result



def superseded_record_ids(records: list[dict[str, Any]]) -> set[str]:
    result: set[str] = set()
    for record in records:
        if record.get("record_type") != "SUPERSESSION":
            continue
        result.update(record["payload"].get("superseded_record_ids", []))
    return result


def active_records(
    records: list[dict[str, Any]],
    *,
    include_supersession_records: bool = False,
) -> list[dict[str, Any]]:
    """Return a current provenance view without deleting historical records."""
    superseded = superseded_record_ids(records)
    return [
        record
        for record in records
        if record["record_id"] not in superseded
        and (
            include_supersession_records
            or record.get("record_type") != "SUPERSESSION"
        )
    ]
