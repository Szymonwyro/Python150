/*
 * LeetCode #121 — Best Time to Buy and Sell Stock   [Easy]   topic: Running min
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * prices[i] is a stock's price on day i. Pick one day to buy and a LATER day
 * to sell. Return the max profit, or 0 if no profit is possible.
 *
 * Examples:
 * [7,1,5,3,6,4] -> 5   (buy at 1, sell at 6)
 * [7,6,4,3,1]   -> 0
 *
 * Hint: One pass: track the cheapest price seen so far.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // TODO: your solution here
        return 0;
    }
};

int main() {
    Solution s;
    { vector<int> a{7,1,5,3,6,4}; CHECK(s.maxProfit(a), 5); }
    { vector<int> a{7,6,4,3,1};   CHECK(s.maxProfit(a), 0); }
    { vector<int> a{2,4,1};       CHECK(s.maxProfit(a), 2); }
    { vector<int> a{1};           CHECK(s.maxProfit(a), 0); }
    SUMMARY();
}
