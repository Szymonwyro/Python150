"""Solution 06 - prefix sums. A run (i, j] sums to k exactly when
prefix[j] - prefix[i] == k, so count earlier prefixes equal to prefix[j] - k.
O(n). A sliding window fails because negatives break monotonicity."""
import sys
from collections import defaultdict


def solve(pnl, k):
    seen = defaultdict(int)
    seen[0] = 1            # the empty prefix
    total = 0
    count = 0
    for x in pnl:
        total += x
        count += seen[total - k]
        seen[total] += 1
    return count


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    pnl = list(map(int, data[2:2 + n]))
    print(solve(pnl, k))


if __name__ == "__main__":
    main()
