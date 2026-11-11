"""Solution 01 - track the cheapest price seen so far. O(n) time, O(1) space."""
import sys


def solve(prices):
    best = 0
    lowest = float("inf")
    for p in prices:
        lowest = min(lowest, p)
        best = max(best, p - lowest)
    return best


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    print(solve(prices))


if __name__ == "__main__":
    main()
