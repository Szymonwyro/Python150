"""Solution 03 - variable sliding window with a frequency map. O(n)."""
import sys
from collections import defaultdict


def solve(tickers, k):
    count = defaultdict(int)
    left = 0
    best = 0
    for right, t in enumerate(tickers):
        count[t] += 1
        while len(count) > k:          # too many distinct: shrink from left
            out = tickers[left]
            count[out] -= 1
            if count[out] == 0:
                del count[out]
            left += 1
        best = max(best, right - left + 1)
    return best


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    tickers = data[2:2 + n]
    print(solve(tickers, k))


if __name__ == "__main__":
    main()
