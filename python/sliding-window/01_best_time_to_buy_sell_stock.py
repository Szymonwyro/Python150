"""
LeetCode 121 - Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array `prices` where prices[i] is the price of a given
stock on day i. You want to maximize profit by choosing a single day to
buy and a different, later day to sell. Return the max profit; return 0
if no profit is possible.

Example:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5        # buy at 1, sell at 6

Target: O(n) time, O(1) space — a one-pass "shrinking window" where you
track the minimum seen so far rather than a literal two-pointer window.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0
    L = 0
    R = 1
    while R < len(prices):
        if prices[R] < prices[L]:
            L = R
        else:
            profit = max(profit, prices[R] - prices[L])

        R += 1

    return profit

        
        
        
    



if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([2, 4, 1]) == 2
    print("all tests passed")
