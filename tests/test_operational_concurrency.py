from needle.operations.state import promotion_decision


T0="2026-09-22T00:00:00+00:00"
T1="2026-09-22T00:10:00+00:00"
T2="2026-09-22T00:20:00+00:00"


def test_two_cycles_from_same_cursor_only_first_can_promote():
    assert promotion_decision(
        remote_cursor=T0, expected_cursor=T0, generated_cursor=T1
    ) == "PROMOTE"
    # Cycle B was generated from T0 too. Once cycle A promoted T1, B is stale.
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T0, generated_cursor=T2
    ) == "STALE_REMOTE"


def test_exact_generated_cursor_is_idempotent_already_promoted():
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T0, generated_cursor=T1
    ) == "ALREADY_PROMOTED"


def test_cycle_cannot_move_completed_boundary_backwards_or_not_at_all():
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T1, generated_cursor=T0
    ) == "INVALID_GENERATED_CURSOR"
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T1, generated_cursor=T1
    ) == "ALREADY_PROMOTED"


def test_unrelated_newer_remote_state_blocks_stale_generated_overwrite():
    # The cursor is the compare-and-swap token for the whole promoted state.
    # A generated state based on T0 may not overwrite baselines/results on T1.
    assert promotion_decision(
        remote_cursor=T1, expected_cursor=T0, generated_cursor=T2
    ) == "STALE_REMOTE"
