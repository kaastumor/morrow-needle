from __future__ import annotations

from datetime import date
from typing import Any


DEFAULT_STATE = {
    "PROCEDURE_ACTIVITY": "OPEN",
    "PROCEDURE_OUTCOME": "PENDING",
    "FORMAL_ACT_ADOPTION": "NOT_ADOPTED",
    "FINAL_ACT_PUBLICATION": "NOT_PUBLISHED",
    "PARLIAMENT_POSITION": "NONE",
    "COUNCIL_POSITION": "NONE",
    "NEGOTIATION_STATE": "NONE",
    "DELEGATED_SCRUTINY": "NOT_APPLICABLE",
}


def state_as_of(
    events: list[dict[str, Any]],
    *,
    procedure_id: str,
    on_date: str,
) -> dict[str, Any]:
    """Resolve a procedural state vector, not a single lifecycle status.

    Legal force/application are intentionally absent. They belong to the
    temporal subsystem because adoption/publication/procedure completion do not
    determine when a rule is legally in force or applicable.
    """
    cutoff = date.fromisoformat(on_date)
    selected = sorted(
        (
            event for event in events
            if event["procedure_id"] == procedure_id
            and date.fromisoformat(event["event_date"]) <= cutoff
        ),
        key=lambda event: (event["event_date"], event["event_id"]),
    )

    if not selected:
        return {
            "state":"NOT_ASSERTED",
            "procedure_id":procedure_id,
            "on_date":on_date,
            "procedure_family":None,
            "dimensions":dict(DEFAULT_STATE),
            "event_ids":[],
            "documents":[],
        }

    families = {event["procedure_family"] for event in selected}
    if len(families) != 1:
        return {
            "state":"CONFLICTING_PROCEDURE_FAMILY",
            "procedure_id":procedure_id,
            "on_date":on_date,
            "procedure_family":None,
            "families":sorted(families),
            "event_ids":[event["event_id"] for event in selected],
        }

    dimensions = dict(DEFAULT_STATE)
    documents: list[dict[str, Any]] = []
    seen_docs: set[tuple[str, str]] = set()

    for event in selected:
        for effect in event.get("effects", []):
            dimensions[effect["dimension"]] = effect["value"]
        for document in event.get("document_refs", []):
            key = (document["role"], document["identifier"])
            if key not in seen_docs:
                seen_docs.add(key)
                documents.append(document)

    return {
        "state":"RESOLVED",
        "procedure_id":procedure_id,
        "on_date":on_date,
        "procedure_family":next(iter(families)),
        "dimensions":dimensions,
        "event_ids":[event["event_id"] for event in selected],
        "documents":documents,
    }


def assert_no_collapsed_status(snapshot: dict[str, Any]) -> None:
    """Guard against reintroducing one catch-all status field."""
    forbidden = {"status", "lifecycle_status", "legal_status"}
    present = forbidden.intersection(snapshot)
    if present:
        raise AssertionError(
            f"procedural snapshot contains collapsed status field(s): {sorted(present)}"
        )
