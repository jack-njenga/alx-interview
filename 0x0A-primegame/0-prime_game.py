#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that number
    and its multiples from the set. The player that cannot make a
    move loses the game. They play x rounds of the game, where n may
    be different for each round. Assuming Maria always goes first
    and both players play optimally, determine who the winner
    of each game is.
    """
    marias_wins, bens_wins = 0, 0

    if (x < 1) or (not nums):
        return None

    n = max(nums)
    primes = [1 for _ in range(1, n + 1, 1)]
    primes[0] = 0
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    if marias_wins > bens_wins:
        return "Maria"
    else:
        return "Ben"


if __name__ == "__main__":
    print(isWinner(4, [2, 3, 2, 6]))
