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
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s == t;
    }

    bool isAnagram2(string s, string t) {
        unordered_map<char, int> cs, ct;
        for (char c : s) cs[c]++;
        for (char c : t) ct[c]++;

        return cs == ct;
    }

    bool isAnagram3(string s, string t) {
        if (s.size() != t.size()) return false;
        // 'a' = 97, 'b' = 98 ... 'z' = 122
        // difference of two letters is alphabet position
        int count[26] = {0};
        for (char c : s) count[c - 'a']++;
        for (char c : t) count[c - 'a']--;

        for (int x : count) {
            if (x != 0) return false;
        }
        return true;

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
