/*
 * LeetCode #238 — Product of Array Except Self   [Medium]   topic: Prefix/suffix
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Return an array `answer` where answer[i] is the product of every element of
 * `nums` except nums[i]. Do it in O(n) time WITHOUT using division.
 *
 * Examples:
 * [1,2,3,4]      -> [24,12,8,6]
 * [-1,1,0,-3,3]  -> [0,0,9,0,0]
 *
 * Hint: Think prefix products from the left, suffix products from the right. Bonus: O(1) extra space (output doesn't count).
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left(nums.size(), 1); // left[i] is product of everything to the left of i
        vector<int> right(nums.size(), 1); // right[i] is product of everything to the righ of i
        int n = nums.size();
        // build left vector
        for (int i =1; i < n; i++) {
            left[i] = nums[i-1] * left[i-1];
        }

        //build right vector
        for (int i = n - 2; i >= 0; i--) {
            right[i] = nums[i+1] * right[i+1];
        }

        vector<int> answer(n);
        for (int i =0; i < n; i++) {
            answer[i] = left[i] * right[i];
        }
        return answer;
    }
};

int main() {
    Solution s;
    { vector<int> a{1,2,3,4};     CHECK(s.productExceptSelf(a), (vector<int>{24,12,8,6})); }
    { vector<int> a{-1,1,0,-3,3}; CHECK(s.productExceptSelf(a), (vector<int>{0,0,9,0,0})); }
    { vector<int> a{2,3};         CHECK(s.productExceptSelf(a), (vector<int>{3,2})); }
    SUMMARY();
}
