from __future__ import annotations

from typing import Any


def events_for_language(
    events: list[dict[str, Any]],
    language: str,
    *,
    as_of_date: str | None = None,
) -> list[dict[str, Any]]:
    """Return only events whose official expression scope includes language.

    A missing language is NO_ASSERTION, not evidence that the expression is
    globally unaffected or correct.
    """
    selected = []
    for event in events:
        if language not in event["expression_scope"]["languages"]:
            continue
        if as_of_date is not None and event["event_date"] > as_of_date:
            continue
        selected.append(event)
    return sorted(selected, key=lambda e: (e["event_date"], e["event_id"]))


def operation_ids_for_language(
    events: list[dict[str, Any]],
    language: str,
    *,
    as_of_date: str | None = None,
) -> list[str]:
    return [
        operation["operation_id"]
        for event in events_for_language(events, language, as_of_date=as_of_date)
        for operation in event["operations"]
    ]


def correction_chain_for_language(
    events: list[dict[str, Any]],
    language: str,
) -> list[dict[str, Any]]:
    """Preserve correction-of-correction ancestry inside one expression."""
    selected = events_for_language(events, language)
    ids = {event["event_id"] for event in selected}
    result = []
    for event in selected:
        corrected = [
            event_id
            for event_id in event.get("corrects_event_ids", [])
            if event_id in ids
        ]
        result.append({
            "event_id": event["event_id"],
            "corrects_event_ids": corrected,
        })
    return result
