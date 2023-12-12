#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """
    ops = 0

    if (n == 0) or ((n // 1) != n) or (n == 1):
        return 0

    i = 2
    while n > 1 and i <= n:
        if n % i == 0:
            n = n // i
            ops += i
        else:
            i = i + 1

    return ops
