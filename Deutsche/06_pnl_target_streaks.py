"""
06 - P&L Target Streaks                        Medium | prefix sums + hash map
-------------------------------------------------------------------------------
You have a desk's daily P&L for n days (values can be negative). Count the
number of contiguous runs of days whose total P&L is exactly k.

Input (stdin)
    Line 1: n k
    Line 2: n space-separated integers, the daily P&L

Output (stdout)
    One integer: the number of contiguous runs summing to k

Example
    Input
        5 3
        1 2 1 -1 2
    Output
        3            ([1,2], [2,1], [1,2,1,-1])

Constraints
    1 <= n <= 10^5,  -1000 <= pnl <= 1000,  -10^7 <= k <= 10^7
Target: O(n). Note that values can be negative, so a sliding window does NOT
work here - think about why.

Note: input parsing is left to you in this one - practise it.
"""
import sys


def solve(pnl, k):
    # TODO
    pass


def main():
    # TODO
    pass


if __name__ == "__main__":
    main()
