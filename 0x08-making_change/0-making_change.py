#!/usr/bin/python3
""" Change comes from within
"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet a
        given amount total

    Parameters:
    - coins: A pile of coins of different values.
    - total: Total amount to meet.
    """
    if total == 0 or total < 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if isinstance(dp[-1], int):
        return dp[-1]
    return -1