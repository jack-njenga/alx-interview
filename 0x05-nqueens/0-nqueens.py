#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""
import sys


def solve_nqueens(n):
    """solves the first part"""
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    """attack part"""
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    """attack"""
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        n_q = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n_q < 4:
        print('N must be at least 4')
        exit(1)

    for answer in reversed(solve_nqueens(n_q)):
        # print(f"\t--> {answer}")
        result = []
        for p in [list(p) for p in answer]:
            result.append([i - 1 for i in p])
        print(result)
