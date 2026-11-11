"""
02 - Matching Trade Pairs                      Easy | hash map
-------------------------------------------------------------------------------
A reconciliation system has a list of n trade amounts. Count the number of
pairs of indices (i, j) with i < j such that amounts[i] + amounts[j] == k.

Input (stdin)
    Line 1: n k
    Line 2: n space-separated integers, the amounts

Output (stdout)
    One integer: the number of pairs

Example
    Input
        5 6
        1 5 7 -1 5
    Output
        3            (1+5, 1+5, 7+-1)

Constraints
    1 <= n <= 10^5,  -10^9 <= amount, k <= 10^9
Target: O(n). An O(n^2) double loop will time out on large tests.
"""
import sys


def solve(amounts, k):
    seen = {} # we need a dict because duplicates provide more options
    count = 0
    for i in range(len(amounts)):
        complement = k - amounts[i]
        if complement in seen:
            count += seen[complement]
        seen[amounts[i]] = seen.get(amounts[i], 0) + 1
    
    return count


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    amounts = list(map(int, data[2:2 + n]))
    print(solve(amounts, k))


if __name__ == "__main__":
    main()
