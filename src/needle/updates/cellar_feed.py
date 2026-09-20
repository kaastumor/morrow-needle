from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import xml.etree.ElementTree as ET
from typing import Any


WEMI_SUFFIXES = {
    "work":"WORK",
    "expression":"EXPRESSION",
    "manifestation":"MANIFESTATION",
    "item":"ITEM",
    "dossier":"DOSSIER",
    "event":"EVENT",
    "agent":"AGENT",
}


class FeedParseError(ValueError):
    """Raised when a feed page cannot be represented without losing events."""


@dataclass(frozen=True)
class FeedPage:
    window_start: str | None
    window_end: str | None
    page: int
    more_entries: bool
    format: str
    events: tuple[dict[str, Any], ...]


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def _children(element: ET.Element, local_name: str) -> list[ET.Element]:
    wanted = local_name.lower()
    return [child for child in list(element) if _local(child.tag) == wanted]


def _first_text(element: ET.Element, local_name: str) -> str | None:
    for node in element.iter():
        if _local(node.tag) == local_name.lower():
            text = (node.text or "").strip()
            if text:
                return text
    return None


def _all_text(element: ET.Element, local_name: str) -> list[str]:
    values = []
    for node in element.iter():
        if _local(node.tag) == local_name.lower():
            value = (node.text or "").strip()
            if value:
                values.append(value)
    return values


def _wemi_levels(classes: list[str]) -> list[str]:
    levels = []
    for value in classes:
        tail = value.rsplit("#", 1)[-1].rsplit("/", 1)[-1].lower()
        level = WEMI_SUFFIXES.get(tail)
        if level:
            levels.append(level)
    return sorted(set(levels))


def _parse_event(
    element: ET.Element,
    *,
    format_name: str,
    window_start: str | None,
    window_end: str | None,
    page: int,
    ordinal: int,
) -> dict[str, Any]:
    generic_id = _first_text(element, "id")
    guid = _first_text(element, "guid")
    notification_entry_id = None
    for node in element.iter():
        if _local(node.tag) != "id":
            continue
        if "notificationEntry" in node.tag:
            value = (node.text or "").strip()
            if value:
                notification_entry_id = value
                break

    if (
        format_name == "RSS"
        and notification_entry_id
        and guid
        and notification_entry_id != guid
    ):
        raise FeedParseError(
            f"feed entry {ordinal} on page {page} has conflicting "
            f"notificationEntry:id and guid"
        )

    notification_id = notification_entry_id or guid or generic_id
    cellar_id = _first_text(element, "cellarId")
    root_cellar_id = _first_text(element, "rootCellarId")
    action = _first_text(element, "type")
    ingestion_time = _first_text(element, "date")

    required = {
        "notification_id": notification_id,
        "cellar_id": cellar_id,
        "root_cellar_id": root_cellar_id,
        "action": action,
        "ingestion_time": ingestion_time,
    }
    missing = sorted(name for name, value in required.items() if not value)
    if missing:
        # Never silently discard a notification and then allow the polling
        # cursor to advance. A malformed/changed official feed shape is an
        # unresolved ingestion window that must be retried or adapted.
        raise FeedParseError(
            f"feed entry {ordinal} on page {page} missing required fields: "
            + ", ".join(missing)
        )

    action = action.upper()
    if action not in {"CREATE", "UPDATE", "DELETE"}:
        raise FeedParseError(
            f"feed entry {ordinal} on page {page} has unknown action {action!r}"
        )

    classes = sorted(set(_all_text(element, "class")))
    explicit_wemi = [
        value.upper()
        for value in _all_text(element, "wemiClass")
        if value.upper() in {
            "WORK","EXPRESSION","MANIFESTATION","ITEM",
            "DOSSIER","EVENT","AGENT"
        }
    ]
    identifiers = sorted(set(_all_text(element, "identifier")))
    priority = _first_text(element, "priority")

    return {
        "notification_id":notification_id,
        "action":action,
        "cellar_id":cellar_id,
        "root_cellar_id":root_cellar_id,
        "ingestion_time":ingestion_time,
        "priority":priority,
        "classes":classes,
        "wemi_levels":sorted(set(_wemi_levels(classes) + explicit_wemi)),
        "identifiers":identifiers,
        "feed_observation":{
            "channel":"ingestion",
            "format":format_name,
            "window_start":window_start,
            "window_end":window_end,
            "page":page,
            "entry_ordinal":ordinal,
        },
    }


def parse_feed(payload: bytes | str) -> FeedPage:
    if isinstance(payload, str):
        payload = payload.encode("utf-8")
    root = ET.fromstring(payload)
    root_name = _local(root.tag)
    if root_name not in {"rss", "feed"}:
        raise FeedParseError(f"unsupported feed root {root_name!r}")
    format_name = "RSS" if root_name == "rss" else "ATOM"

    window_start = _first_text(root, "startDate")
    window_end = _first_text(root, "endDate")
    page_text = _first_text(root, "page")
    more_text = _first_text(root, "moreEntries")
    page = int(page_text) if page_text else 1
    more_entries = (more_text or "false").strip().lower() == "true"

    if format_name == "RSS":
        entries = [node for node in root.iter() if _local(node.tag) == "item"]
    else:
        entries = [node for node in root.iter() if _local(node.tag) == "entry"]

    events = []
    for ordinal, entry in enumerate(entries):
        events.append(
            _parse_event(
                entry,
                format_name=format_name,
                window_start=window_start,
                window_end=window_end,
                page=page,
                ordinal=ordinal,
            )
        )

    return FeedPage(
        window_start=window_start,
        window_end=window_end,
        page=page,
        more_entries=more_entries,
        format=format_name,
        events=tuple(events),
    )


def dedupe_events(
    events: list[dict[str, Any]] | tuple[dict[str, Any], ...],
    processed_notification_ids: set[str],
) -> tuple[list[dict[str, Any]], set[str]]:
    emitted = []
    updated = set(processed_notification_ids)
    for event in events:
        event_id = event["notification_id"]
        if event_id in updated:
            continue
        emitted.append(event)
        updated.add(event_id)
    return emitted, updated


def overlap_window_start(
    last_completed_end: datetime,
    *,
    overlap: timedelta = timedelta(minutes=5),
) -> datetime:
    return last_completed_end - overlap


def iso_utc(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat()
