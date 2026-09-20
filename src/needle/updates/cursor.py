from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from typing import Any

from .cellar_feed import FeedPage


@dataclass(frozen=True)
class PollCursor:
    last_completed_end: str | None = None
    active_window_start: str | None = None
    active_window_end: str | None = None
    next_page: int = 1


def begin_window(
    cursor: PollCursor,
    *,
    window_start: str,
    window_end: str,
) -> PollCursor:
    if cursor.active_window_start is not None:
        raise ValueError("cannot begin a new window while another is active")
    return replace(
        cursor,
        active_window_start=window_start,
        active_window_end=window_end,
        next_page=1,
    )


def _instant(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Cellar polling windows must be offset-aware")
    return parsed


def _same_instant(left: str, right: str) -> bool:
    return _instant(left) == _instant(right)


def accept_page(cursor: PollCursor, page: FeedPage) -> PollCursor:
    if cursor.active_window_start is None or cursor.active_window_end is None:
        raise ValueError("no active polling window")
    if page.page != cursor.next_page:
        raise ValueError(
            f"expected page {cursor.next_page}, received page {page.page}"
        )

    # Feed echoes are audit signals; when present they must match the request.
    if page.window_start is not None and not _same_instant(
        page.window_start, cursor.active_window_start
    ):
        raise ValueError("feed page startDate does not match active window")
    if page.window_end is not None and not _same_instant(
        page.window_end, cursor.active_window_end
    ):
        raise ValueError("feed page endDate does not match active window")

    if page.more_entries:
        return replace(cursor, next_page=cursor.next_page + 1)

    return PollCursor(
        last_completed_end=cursor.active_window_end,
        active_window_start=None,
        active_window_end=None,
        next_page=1,
    )


def window_is_complete(cursor: PollCursor) -> bool:
    return cursor.active_window_start is None
