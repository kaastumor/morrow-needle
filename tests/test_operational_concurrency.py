from needle.operations.promotion import promotion_decision


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


def test_cycle_must_advance_completed_boundary():
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T1, generated_cursor=T0
    ) == "INVALID_GENERATED_CURSOR"
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T1, generated_cursor=T1
    ) == "INVALID_GENERATED_CURSOR"


def test_stale_generated_state_cannot_overwrite_newer_remote_snapshot():
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T0, generated_cursor=T2
    ) == "STALE_REMOTE"
