from copy import deepcopy

from needle.operations.promotion import promotion_decision
from needle.operations.state import retain_overlap_event_keys


T0 = "2026-09-22T00:00:00+00:00"
T1 = "2026-09-22T00:10:00+00:00"
T2 = "2026-09-22T00:20:00+00:00"


def test_two_cycles_from_same_cursor_only_first_can_promote():
    assert promotion_decision(
        remote_cursor=T0, expected_cursor=T0, generated_cursor=T1
    ) == "PROMOTE"
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T0, generated_cursor=T2
    ) == "STALE_REMOTE"


def test_exact_generated_cursor_is_idempotent_already_promoted():
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T0, generated_cursor=T1
    ) == "ALREADY_PROMOTED"


def test_failure_before_completed_boundary_cannot_promote_same_cursor():
    # A failed/partial cycle has not produced a later completed boundary.  The
    # promotion guard must reject that snapshot rather than treating execution
    # time or a partially processed window as progress.
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T1, generated_cursor=T1
    ) == "INVALID_GENERATED_CURSOR"


def test_cycle_must_not_move_completed_boundary_backwards():
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T1, generated_cursor=T0
    ) == "INVALID_GENERATED_CURSOR"


def test_stale_generated_state_cannot_overwrite_newer_remote_snapshot():
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T0, generated_cursor=T2
    ) == "STALE_REMOTE"


def test_still_replayable_overlap_event_remains_deduped_after_retention():
    # The next poll begins five minutes before T1.  An already-processed event
    # inside that replayable interval must remain in the dedupe set; otherwise
    # the overlap window could emit it again.
    replayable_key = "cellar:replay_2026-09-22T00:08:00+00:00"
    expired_key = "cellar:expired_2026-09-21T23:59:00+00:00"
    state = {
        "processed_event_keys": [expired_key, replayable_key],
        "updated_at": T0,
    }
    events = [
        {"event_key": expired_key, "ingestion_time": "2026-09-21T23:59:00+00:00"},
        {"event_key": replayable_key, "ingestion_time": "2026-09-22T00:08:00+00:00"},
    ]

    compact = retain_overlap_event_keys(
        deepcopy(state),
        events,
        window_end=T1,
        overlap_seconds=300,
        updated_at=T1,
    )

    assert replayable_key in compact["processed_event_keys"]
    assert expired_key not in compact["processed_event_keys"]
    # The operational loop's existing skip predicate is membership in this set.
    assert replayable_key in set(compact["processed_event_keys"])
