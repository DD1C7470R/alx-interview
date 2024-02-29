#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins: list, total: int) -> int:
    """Defines and implementations"""

    if total < 0:
        return -1
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
