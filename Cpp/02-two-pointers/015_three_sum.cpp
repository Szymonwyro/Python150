/*
 * LeetCode #15 — 3Sum   [Medium]   topic: Sort + two pointers
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Return all unique triplets [a,b,c] from `nums` (distinct indices) with
 * a + b + c == 0. The answer must not contain duplicate triplets.
 *
 * Examples:
 * [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
 * [0,1,1]          -> []
 * [0,0,0]          -> [[0,0,0]]
 *
 * Hint: Sort first, fix one element, two-pointer the rest. Skip duplicates carefully. O(n^2).
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // TODO: your solution here
        return {};
    }
};

int main() {
    Solution s;
    auto norm = [](vector<vector<int>> v) { for (auto& t : v) sort(t.begin(), t.end()); sort(v.begin(), v.end()); return v; };
    { vector<int> a{-1,0,1,2,-1,-4}; CHECK(norm(s.threeSum(a)), (vector<vector<int>>{{-1,-1,2},{-1,0,1}})); }
    { vector<int> a{0,1,1};          CHECK(norm(s.threeSum(a)), (vector<vector<int>>{})); }
    { vector<int> a{0,0,0,0};        CHECK(norm(s.threeSum(a)), (vector<vector<int>>{{0,0,0}})); }
    SUMMARY();
}
