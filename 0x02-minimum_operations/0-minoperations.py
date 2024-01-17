#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Returns the minimum number of operations"""
    if not isinstance(n, int) or n <= 1:
        return 0

    num_of_ops = 0
    num_of_letters = 1

    while num_of_letters < n:
        if n % num_of_letters == 0:
            # If num_of_letters is a factor of n, we can "Copy All" and "Paste"
            num_of_ops += 2
            num_of_letters *= 2
        else:
            # If num_of_letters is not a factor of n, we can only "Paste"
            num_of_ops += 1
            num_of_letters += num_of_letters

    return num_of_ops
