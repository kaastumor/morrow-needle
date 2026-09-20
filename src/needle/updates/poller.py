from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

from .cellar_feed import FeedPage, dedupe_events
from .classify import refresh_scope
from .cursor import PollCursor, accept_page, begin_window


@dataclass(frozen=True)
class PollState:
    cursor: PollCursor
    processed_notification_ids: frozenset[str]


@dataclass(frozen=True)
class PollEmission:
    event: dict[str, Any]
    refresh_plan: dict[str, Any]


def begin_poll(
    state: PollState,
    *,
    window_start: str,
    window_end: str,
) -> PollState:
    return PollState(
        cursor=begin_window(
            state.cursor,
            window_start=window_start,
            window_end=window_end,
        ),
        processed_notification_ids=state.processed_notification_ids,
    )


def accept_poll_page(
    state: PollState,
    page: FeedPage,
) -> tuple[PollState, tuple[PollEmission, ...]]:
    """Atomically accept one fully parsed page.

    If parsing happened earlier and raised, this function is never called.
    The cursor advances only after the page shape is accepted. Notification
    dedupe state advances for successfully accepted entries only.
    """
    emitted, seen = dedupe_events(
        page.events,
        set(state.processed_notification_ids),
    )
    next_cursor = accept_page(state.cursor, page)
    emissions = tuple(
        PollEmission(
            event=event,
            refresh_plan=refresh_scope(event),
        )
        for event in emitted
    )
    return (
        PollState(
            cursor=next_cursor,
            processed_notification_ids=frozenset(seen),
        ),
        emissions,
    )


def new_poll_state(
    *,
    last_completed_end: str | None = None,
    processed_notification_ids: Iterable[str] = (),
) -> PollState:
    return PollState(
        cursor=PollCursor(last_completed_end=last_completed_end),
        processed_notification_ids=frozenset(processed_notification_ids),
    )
