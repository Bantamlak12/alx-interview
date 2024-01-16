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
    if n < 2:
        return 0

    number = n + 1
    min_operation = 0

    for i in range(2, number):
        while (n % i == 0 and n != 1):
            min_operation += i
            n //= i
    return min_operation
