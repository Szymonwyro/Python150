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
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    print("all tests passed")
