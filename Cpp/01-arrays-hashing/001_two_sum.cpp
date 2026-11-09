/*
 * LeetCode #1 — Two Sum   [Easy]   topic: Hash map
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Given an array of integers `nums` and an integer `target`, return the indices
 * of the two numbers that add up to `target`. Exactly one valid pair exists and
 * you may not use the same element twice. Return the indices in any order.
 *
 * Examples:
 * nums = [2,7,11,15], target = 9  ->  [0,1]
 * nums = [3,2,4],      target = 6  ->  [1,2]
 *
 * Hint: Aim for O(n) time.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen; // maps value -> index
        for(int i = 0; i < int(nums).size(); i++) {
            int complement = target - nums[i];
            if (seen.count(complement)) {     // checks if need in seen
                return {seen[complement], i};
            }
            seen[nums[i]] = i
        }
        return {};
    }
};

int main() {
    Solution s;
    auto sorted = [](vector<int> v) { sort(v.begin(), v.end()); return v; };
    { vector<int> a{2,7,11,15}; CHECK(sorted(s.twoSum(a, 9)), (vector<int>{0,1})); }
    { vector<int> a{3,2,4};     CHECK(sorted(s.twoSum(a, 6)), (vector<int>{1,2})); }
    { vector<int> a{3,3};       CHECK(sorted(s.twoSum(a, 6)), (vector<int>{0,1})); }
    { vector<int> a{-1,-2,-3,-4,-5}; CHECK(sorted(s.twoSum(a, -8)), (vector<int>{2,4})); }
    SUMMARY();
}
