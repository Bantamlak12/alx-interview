#!/usr/bin/python3
"""
File: 0-minoperations.py

Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    parameters:
    n (int): Number of characters exactly to print

    Returns:
    - The minimum number of operations to result exactly `nH`
    """
    min_operation = 0

    if not isinstance(n, int):
        return 0

    for i in range(2, n + 1):
        while (n % i == 0):
            min_operation += i
            n /= i
    return min_operation
