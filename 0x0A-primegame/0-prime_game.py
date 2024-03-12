#!/usr/bin/python3
""" A module that plays a prime game
"""


def is_prime(num):
    """Check if a number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_game(n):
    if n == 1:
        # By default the second player wins the game
        return 'Ben'
    prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
    return 'Maria' if prime_count % 2 == 1 else 'Ben'


def isWinner(x, nums):
    """
    parameters:
    - x: number of rounds
    - nums: An array of n

    Returns:
    - name of the player that won the most rounds
    - None: if the winner cannot be determined
    """
    wins = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        winner = play_game(nums[i])
        wins[winner] += 1

    if wins['Maria'] == wins['Ben']:
        return None
    return max(wins, key=wins.get)
