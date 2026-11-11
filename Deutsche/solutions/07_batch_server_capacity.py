"""Solution 07 - binary search on C between max(sizes) and sum(sizes).
"Can we finish in d days with capacity C?" is monotonic in C. O(n log sum)."""
import sys


def days_needed(sizes, cap):
    days, load = 1, 0
    for s in sizes:
        if load + s > cap:
            days += 1
            load = 0
        load += s
    return days


def solve(sizes, d):
    lo, hi = max(sizes), sum(sizes)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(sizes, mid) <= d:
            hi = mid           # feasible: try smaller
        else:
            lo = mid + 1
    return lo


def main():
    data = sys.stdin.read().split()
    n, d = int(data[0]), int(data[1])
    sizes = list(map(int, data[2:2 + n]))
    print(solve(sizes, d))


if __name__ == "__main__":
    main()
