/*
 * LeetCode #20 — Valid Parentheses   [Easy]   topic: Stack
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * `s` contains only the characters ()[]{}. Return true if every bracket is
 * closed by the same type, in the correct order.
 *
 * Examples:
 * "()[]{}" -> true
 * "(]"     -> false
 * "([])"   -> true
 *
 * Hint: std::stack<char>; watch for closing a bracket when the stack is empty.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    bool isValid(string s) {
        // TODO: your solution here
        return false;
    }
};

int main() {
    Solution s;
    CHECK(s.isValid("()"), true);
    CHECK(s.isValid("()[]{}"), true);
    CHECK(s.isValid("(]"), false);
    CHECK(s.isValid("([)]"), false);
    CHECK(s.isValid("{[]}"), true);
    CHECK(s.isValid("]"), false);
    CHECK(s.isValid("(("), false);
    SUMMARY();
}
