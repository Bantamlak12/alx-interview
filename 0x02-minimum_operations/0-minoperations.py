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

    number_ope = 2
    min_operations = 0

    while n > 1:
        while (n % number_ope == 0):
            min_operations += number_ope
            n //= number_ope
        number_ope += 1
    return min_operations
