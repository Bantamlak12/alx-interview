#!/usr/bin/python3
""" A module that plays a prime game
"""


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
    return [p for p in range(2, limit + 1) if primes[p]]


def play_game(n, primes):
    if n == 1:
        # By default the second player wins the game
        return 'Ben'

    prime_count = 0
    for p in primes:
        if p <= n:
            prime_count += 1
        else:
            break
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
    if x <= 0:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = play_game(n, primes)
        wins[winner] += 1

    if wins['Maria'] == wins['Ben']:
        return None
    return max(wins, key=wins.get)
