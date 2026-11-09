/*
 * LeetCode #3 — Longest Substring Without Repeating Characters   [Medium]   topic: Sliding window
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Return the length of the longest contiguous substring of `s` that contains
 * no repeated character.
 *
 * Examples:
 * "abcabcbb" -> 3  ("abc")
 * "bbbbb"    -> 1
 * "pwwkew"   -> 3  ("wke")
 *
 * Hint: Grow the right edge; when you hit a repeat, jump the left edge past its last position.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // TODO: your solution here
        return 0;
    }
};

int main() {
    Solution s;
    CHECK(s.lengthOfLongestSubstring("abcabcbb"), 3);
    CHECK(s.lengthOfLongestSubstring("bbbbb"), 1);
    CHECK(s.lengthOfLongestSubstring("pwwkew"), 3);
    CHECK(s.lengthOfLongestSubstring(""), 0);
    CHECK(s.lengthOfLongestSubstring("abba"), 2);
    SUMMARY();
}
