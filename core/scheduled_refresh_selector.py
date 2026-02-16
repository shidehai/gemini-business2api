from typing import List, Tuple


def select_scheduled_refresh_accounts(
    expiring_accounts: List[str],
    max_accounts: int,
    start_index: int,
) -> Tuple[List[str], int]:
    """
    Round-robin select accounts for each scheduled refresh cycle.

    Returns:
    - selected accounts for this cycle
    - next cursor index for the following cycle
    """
    if not expiring_accounts or max_accounts <= 0:
        return [], 0

    total = len(expiring_accounts)
    count = min(total, max_accounts)
    cursor = start_index % total

    end = cursor + count
    if end <= total:
        selected = expiring_accounts[cursor:end]
    else:
        selected = expiring_accounts[cursor:] + expiring_accounts[: end - total]

    next_cursor = (cursor + count) % total
    return selected, next_cursor
