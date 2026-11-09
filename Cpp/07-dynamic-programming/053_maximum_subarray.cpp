/*
 * LeetCode #53 — Maximum Subarray   [Medium]   topic: Kadane
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Return the largest sum of any non-empty contiguous subarray of `nums`.
 *
 * Examples:
 * [-2,1,-3,4,-1,2,1,-5,4] -> 6   ([4,-1,2,1])
 * [5,4,-1,7,8]            -> 23
 * [-3,-1,-2]              -> -1
 *
 * Hint: Kadane's algorithm: best sum ending here = max(x, x + previous best ending). Same idea as max drawdown in reverse.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // TODO: your solution here
        return 0;
    }
};

int main() {
    Solution s;
    { vector<int> a{-2,1,-3,4,-1,2,1,-5,4}; CHECK(s.maxSubArray(a), 6); }
    { vector<int> a{1};                     CHECK(s.maxSubArray(a), 1); }
    { vector<int> a{5,4,-1,7,8};            CHECK(s.maxSubArray(a), 23); }
    { vector<int> a{-3,-1,-2};              CHECK(s.maxSubArray(a), -1); }
    SUMMARY();
}
