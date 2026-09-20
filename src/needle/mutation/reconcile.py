from __future__ import annotations

from copy import deepcopy
from typing import Any


OPERATION_MAP = {
    "REPLACED":"REPLACE",
    "REPLACEMENT":"REPLACE",
    "AMENDED":"REPLACE",
    "AMENDMENT":"REPLACE",
    "INSERTED":"INSERT",
    "INSERTION":"INSERT",
    "DELETED":"DELETE",
    "DELETION":"DELETE",
}


def normalize_operation(value: str) -> str:
    upper = value.strip().upper()
    return OPERATION_MAP.get(upper, upper)


def _target_matches(candidate: dict[str, Any], evidence: dict[str, Any]) -> bool:
    candidate_target = candidate["target"]["citation_path"].strip().lower()
    evidence_target = evidence["target_locator"].strip().lower()
    return candidate_target == evidence_target


def reconcile_candidate(
    candidate: dict[str, Any],
    evidence_items: list[dict[str, Any]],
) -> dict[str, Any]:
    """Reconcile a deterministic candidate with independent official evidence.

    Exact target matching is intentionally conservative in v0.1. Hierarchical
    or fuzzy target matching belongs to later mutation-engine slices.
    """
    result = deepcopy(candidate)
    supports = list(result.get("supporting_evidence", []))
    conflicts = list(result.get("conflicting_evidence", []))

    for evidence in evidence_items:
        if not _target_matches(candidate, evidence):
            continue
        operation = normalize_operation(evidence["operation"])
        normalized = {**evidence, "operation":operation}

        if operation == candidate["operation"]:
            supports.append(normalized)
        elif operation != "UNKNOWN":
            conflicts.append(normalized)

    # De-duplicate by source/channel/target/operation.
    def unique(items):
        seen = set()
        output = []
        for item in items:
            key = (
                item["channel"], item["source_id"], item["operation"],
                item["target_locator"], item.get("locator"),
            )
            if key in seen:
                continue
            seen.add(key)
            output.append(item)
        return output

    supports, conflicts = unique(supports), unique(conflicts)
    result["supporting_evidence"] = supports
    result["conflicting_evidence"] = conflicts

    if conflicts:
        result["reconciliation_state"] = "CONFLICTING"
        result["verification_state"] = "UNVERIFIED"
        return result

    independent_official = {
        item["channel"]
        for item in supports
        if item["channel"] not in {"DETERMINISTIC_DIFF","CONSOLIDATED_CHECKPOINT"}
    }
    if independent_official:
        result["reconciliation_state"] = "CORROBORATED"
    else:
        result["reconciliation_state"] = "DIFF_ONLY"

    # Verification requires a parsed authentic legal cause, not merely
    # relationship metadata or consolidated documentary provenance.
    has_authentic_cause = any(
        item["channel"] == "AUTHENTIC_ACT"
        and item["authority_character"] == "CANONICAL_LEGAL_CAUSE"
        for item in supports
    )
    result["verification_state"] = "VERIFIED" if has_authentic_cause else "UNVERIFIED"
    return result


def reconcile_candidates(
    candidates: list[dict[str, Any]],
    evidence_items: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [reconcile_candidate(candidate, evidence_items) for candidate in candidates]
