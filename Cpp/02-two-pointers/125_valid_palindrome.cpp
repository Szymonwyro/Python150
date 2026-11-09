/*
 * LeetCode #125 — Valid Palindrome   [Easy]   topic: Two pointers
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * After lowercasing and removing every non-alphanumeric character, does the
 * string read the same forwards and backwards?
 *
 * Examples:
 * "A man, a plan, a canal: Panama" -> true
 * "race a car"                     -> false
 *
 * Hint: Do it in O(1) extra space with two indices — useful: isalnum, tolower.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    bool isPalindrome(string s) {
        // TODO: your solution here
        return false;
    }
};

int main() {
    Solution s;
    CHECK(s.isPalindrome("A man, a plan, a canal: Panama"), true);
    CHECK(s.isPalindrome("race a car"), false);
    CHECK(s.isPalindrome(" "), true);
    CHECK(s.isPalindrome("0P"), false);
    SUMMARY();
}
