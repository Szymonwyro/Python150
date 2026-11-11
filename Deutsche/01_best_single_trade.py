"""
01 - Best Single Trade                         Easy | greedy / running minimum
-------------------------------------------------------------------------------
You are given the closing price of a stock for n consecutive days. You may make
at most ONE trade: buy on one day and sell on a strictly later day.

Return the maximum profit you can make. If no profitable trade exists, return 0.

Input (stdin)
    Line 1: n
    Line 2: n space-separated integers, the prices

Output (stdout)
    One integer: the maximum profit

Example
    Input
        6
        7 1 5 3 6 4
    Output
        5            (buy at 1, sell at 6)

Constraints
    1 <= n <= 10^5,  0 <= price <= 10^4
Target: O(n) time, O(1) space
"""
import sys


def solve(prices):
    l = 0
    r = 1
    best = 0
    
    while r < len(prices):
        if prices[r] > prices[l]:
            best = max(best, prices[r] - prices[l])
        else:
            l = r
            r = l
        r += 1
    return best


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    print(solve(prices))


if __name__ == "__main__":
    main()
