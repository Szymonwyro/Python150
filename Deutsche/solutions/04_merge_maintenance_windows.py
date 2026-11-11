"""Solution 04 - sort by start, then extend or start a new window. O(n log n)."""
import sys


def solve(intervals):
    intervals.sort()
    merged = []
    for s, e in intervals:
        if merged and s <= merged[-1][1]:      # overlaps or touches
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    vals = list(map(int, data[1:1 + 2 * n]))
    intervals = [[vals[2 * i], vals[2 * i + 1]] for i in range(n)]
    out = solve(intervals)
    sys.stdout.write("\n".join(f"{s} {e}" for s, e in out) + "\n")


if __name__ == "__main__":
    main()
