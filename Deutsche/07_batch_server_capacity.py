"""
07 - Batch Server Capacity                     Medium | binary search on answer
-------------------------------------------------------------------------------
A settlement server must process n batches of transactions IN ORDER. Batch i
has size sizes[i]. Each day, the server processes consecutive batches until
adding the next batch would exceed its daily capacity C. A batch cannot be
split across days.

Find the minimum capacity C such that all batches are processed within d days.

Input (stdin)
    Line 1: n d
    Line 2: n space-separated integers, the batch sizes

Output (stdout)
    One integer: the minimum capacity

Example
    Input
        10 5
        1 2 3 4 5 6 7 8 9 10
    Output
        15           (days: [1..5] [6,7] [8] [9] [10])

Constraints
    1 <= d <= n <= 5 * 10^4,  1 <= size <= 500
Target: O(n log(sum)). Hint: what are the smallest and largest possible C?

Note: input parsing is left to you in this one - practise it.
"""
import sys


def solve(sizes, d):
    # TODO
    pass


def main():
    # TODO
    pass


if __name__ == "__main__":
    main()
