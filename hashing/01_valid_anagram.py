"""
LeetCode 242 - Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
and False otherwise.

Example:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False

Target: O(n) time, O(1) space if you assume a fixed 26-letter alphabet
(fixed-size count array beats a general hashmap here).
"""


def is_anagram(s: str, t: str) -> bool:
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    print("all tests passed")
