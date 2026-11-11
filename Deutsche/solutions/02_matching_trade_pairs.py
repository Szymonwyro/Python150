"""Solution 02 - count complements seen so far. O(n) time, O(n) space."""
import sys
from collections import defaultdict


def solve(amounts, k):
    seen = defaultdict(int)
    pairs = 0
    for a in amounts:
        pairs += seen[k - a]   # every earlier match pairs with this one
        seen[a] += 1
    return pairs


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    amounts = list(map(int, data[2:2 + n]))
    print(solve(amounts, k))


if __name__ == "__main__":
    main()
