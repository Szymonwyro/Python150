"""
04 - Merge Maintenance Windows                 Medium | sorting + intervals
-------------------------------------------------------------------------------
Several teams have booked maintenance windows on a shared server. Each window
is [start, end]. Windows that overlap OR touch (e.g. [1,3] and [3,5]) should be
merged into one. Output the merged windows sorted by start time.

Input (stdin)
    Line 1: n
    Next n lines: start end

Output (stdout)
    One merged window per line: start end

Example
    Input
        4
        8 10
        1 3
        2 6
        15 18
    Output
        1 6
        8 10
        15 18

Constraints
    1 <= n <= 10^5,  0 <= start <= end <= 10^9
Target: O(n log n)

Note: input parsing is left to you in this one - practise it.
"""
import sys


def solve(intervals):
    merged = []
    intervals.sort()
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


def main():
    data = sys.stdin.read().split() # converts to ['', '', '', '', ...]
    n = int(data[0]) # first element will always be n
    intervals = []
    for i in range(n):
        start = int(data[1 + 2*i])
        end = int(data[2 + 2*i])
        intervals.append([start, end])
    result = solve(intervals)
    for start, end in result:
        print(start, end)


if __name__ == "__main__":
    main()
