"""
LeetCode 3 - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string `s`, find the length of the longest substring without
repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3        # "abc"

    Input: s = "bbbbb"
    Output: 1        # "b"

Target: O(n) time, O(min(n, charset)) space — classic expanding/shrinking
window with a set or last-seen-index map.
"""


def length_of_longest_substring(s: str) -> int:
    L = 0
    window = set()
    max_len = 0
    for R in range(len(s)):
        if s[R] in window:
            window.remove[s[L]]
            L += 1
        else:
            window.add(s[R])
            max_len = max(max_len, R - L + 1)

            
        
        



if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    print("all tests passed")
