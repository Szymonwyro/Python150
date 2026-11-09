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
    sorted_s = "".join(sorted(s))
    sorted_t = "".join(sorted(t))
    if sorted_s == sorted_t:
        return True
    else:
        return False

    ## this O(nlogn)

def is_anagram2(s: str, t: str) -> bool:
    #try for O(n) with hashmap
    count_s = {}
    count_t = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    return count_s == count_t




if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    print("all tests passed")
