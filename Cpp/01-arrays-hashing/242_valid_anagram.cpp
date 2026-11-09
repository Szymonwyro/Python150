/*
 * LeetCode #242 — Valid Anagram   [Easy]   topic: Counting
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * Given strings `s` and `t` of lowercase letters, return true if `t` is a
 * rearrangement of the letters of `s`.
 *
 * Examples:
 * s = "anagram", t = "nagaram" -> true
 * s = "rat",     t = "car"     -> false
 *
 * Hint: A fixed int[26] counter beats a map here.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    bool isAnagram(string s, string t) {
        // TODO: your solution here
        return false;
    }
};

int main() {
    Solution s;
    CHECK(s.isAnagram("anagram", "nagaram"), true);
    CHECK(s.isAnagram("rat", "car"), false);
    CHECK(s.isAnagram("a", "ab"), false);
    CHECK(s.isAnagram("", ""), true);
    SUMMARY();
}
