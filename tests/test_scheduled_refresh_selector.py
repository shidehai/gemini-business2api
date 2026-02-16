from core.scheduled_refresh_selector import select_scheduled_refresh_accounts


def test_round_robin_selection_wraps_across_tail_and_head():
    accounts = ["a", "b", "c", "d", "e"]

    selected1, cursor1 = select_scheduled_refresh_accounts(accounts, 2, 0)
    selected2, cursor2 = select_scheduled_refresh_accounts(accounts, 2, cursor1)
    selected3, cursor3 = select_scheduled_refresh_accounts(accounts, 2, cursor2)

    assert selected1 == ["a", "b"]
    assert selected2 == ["c", "d"]
    assert selected3 == ["e", "a"]
    assert cursor1 == 2
    assert cursor2 == 4
    assert cursor3 == 1


def test_cursor_is_normalized_with_modulo():
    accounts = ["x", "y", "z"]
    selected, cursor = select_scheduled_refresh_accounts(accounts, 2, 8)
    assert selected == ["z", "x"]
    assert cursor == 1


def test_selects_all_when_below_limit():
    accounts = ["x", "y"]
    selected, cursor = select_scheduled_refresh_accounts(accounts, 10, 1)
    assert selected == ["y", "x"]
    assert cursor == 1


def test_empty_or_invalid_max_returns_empty():
    assert select_scheduled_refresh_accounts([], 3, 0) == ([], 0)
    assert select_scheduled_refresh_accounts(["a"], 0, 0) == ([], 0)
