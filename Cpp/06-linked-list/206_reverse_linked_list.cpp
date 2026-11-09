/*
 * LeetCode #206 — Reverse Linked List   [Easy]   topic: Pointers
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Given the head of a singly linked list, reverse it in place and return the
 * new head. (ListNode is defined in common/test.h.)
 *
 * Examples:
 * [1,2,3,4,5] -> [5,4,3,2,1]
 * []          -> []
 *
 * Hint: Iterative with prev/curr/next first; then try recursion.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // TODO: your solution here
        return nullptr;
    }
};

int main() {
    Solution s;
    CHECK(toVec(s.reverseList(makeList({1,2,3,4,5}))), (vector<int>{5,4,3,2,1}));
    CHECK(toVec(s.reverseList(makeList({1,2}))), (vector<int>{2,1}));
    CHECK(toVec(s.reverseList(makeList({}))), (vector<int>{}));
    SUMMARY();
}
