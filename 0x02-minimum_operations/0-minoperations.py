#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Returns the minimum number of operations"""
    num_of_ops = 3
    num_of_letters = 1
    if n <= 1 or type(n) != int:
        return 0
    else:
        if n <= 3:
            return n
        else:
            num_of_letters = 3
            while num_of_ops < n and num_of_letters < n:
                if (num_of_letters * 2) <= n:
                    num_of_ops += 2
                    num_of_letters = num_of_letters * 2
                else:
                    num_of_ops += 1
                    if n - num_of_letters < 3:
                        num_of_letters += 1
                    else:
                        num_of_letters += 3
    return num_of_ops
