/*
 * LeetCode #70 — Climbing Stairs   [Easy]   topic: 1-D DP
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * You climb a staircase of `n` steps taking 1 or 2 steps at a time. How many
 * distinct ways are there to reach the top?
 *
 * Examples:
 * n = 2 -> 2   (1+1, 2)
 * n = 3 -> 3   (1+1+1, 1+2, 2+1)
 *
 * Hint: Write the recurrence first. Then reduce to O(1) space.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    int climbStairs(int n) {
        // TODO: your solution here
        return 0;
    }
};

int main() {
    Solution s;
    CHECK(s.climbStairs(1), 1);
    CHECK(s.climbStairs(2), 2);
    CHECK(s.climbStairs(3), 3);
    CHECK(s.climbStairs(5), 8);
    CHECK(s.climbStairs(45), 1836311903);
    SUMMARY();
}
