/*
 * LeetCode #704 — Binary Search   [Easy]   topic: Binary search
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * `nums` is sorted ascending with distinct values. Return the index of
 * `target`, or -1 if it is absent. Must be O(log n).
 *
 * Examples:
 * nums = [-1,0,3,5,9,12], target = 9 -> 4
 * nums = [-1,0,3,5,9,12], target = 2 -> -1
 *
 * Hint: Write it by hand (no std::lower_bound). Use mid = lo + (hi - lo) / 2 to avoid overflow.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // TODO: your solution here
        return -1;
    }
};

int main() {
    Solution s;
    { vector<int> a{-1,0,3,5,9,12}; CHECK(s.search(a, 9), 4); }
    { vector<int> a{-1,0,3,5,9,12}; CHECK(s.search(a, 2), -1); }
    { vector<int> a{5};             CHECK(s.search(a, 5), 0); }
    { vector<int> a{1,3};           CHECK(s.search(a, 3), 1); }
    SUMMARY();
}
