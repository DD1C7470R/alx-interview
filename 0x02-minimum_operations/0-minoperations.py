#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Returns the minimum number of operations"""
    if not isinstance(n, int) or n <= 1:
        return 0

    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    num_of_ops = sum(factors)
    return num_of_ops
