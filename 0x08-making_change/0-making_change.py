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
    # Using Dynamic programming
    # if total == 0 or total < 0:
    #     return 0

    # dp = [float('inf')] * (total + 1)
    # dp[0] = 0

    # for coin in coins[::-1]:
    #     for amount in range(coin, total + 1):
    #         dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # if dp[-1] == float('inf'):
    #     return -1
    # return dp[-1]

    # Using Greedy algorithm
    if total == 0 or total < 0:
        return 0

    minCoins = 0

    for coin in coins[::-1]:
        while total >= coin:
            total -= coin
            minCoins += 1
    return minCoins if total == 0 else -1
