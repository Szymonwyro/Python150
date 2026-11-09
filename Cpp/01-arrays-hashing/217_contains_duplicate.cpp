/*
 * LeetCode #217 — Contains Duplicate   [Easy]   topic: Hash set
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Return true if any value appears at least twice in `nums`, false if every
 * element is distinct.
 *
 * Examples:
 * [1,2,3,1] -> true
 * [1,2,3,4] -> false
 *
 * Hint: O(n) time with a set, or O(n log n) with sorting — try both.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int x : nums) {
            if (seen.count(x)) {
                return true;
            }
            seen.insert(x);
        }
        return false;
    }
};

int main() {
    Solution s;
    { vector<int> a{1,2,3,1}; CHECK(s.containsDuplicate(a), true); }
    { vector<int> a{1,2,3,4}; CHECK(s.containsDuplicate(a), false); }
    { vector<int> a{1,1,1,3,3,4,3,2,4,2}; CHECK(s.containsDuplicate(a), true); }
    { vector<int> a{}; CHECK(s.containsDuplicate(a), false); }
    SUMMARY();
}
