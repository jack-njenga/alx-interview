#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1
    """
    rem = total
    count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)

    if total <= 0:
        return 0

    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            count += 1
        else:
            coin_idx += 1
    return count
