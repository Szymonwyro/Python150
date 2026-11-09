"""
LeetCode 125 - Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters to
lowercase and removing all non-alphanumeric characters, it reads the same
forward and backward. Given a string `s`, return True if it is a
palindrome, False otherwise.

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True

    Input: s = "race a car"
    Output: False

Target: O(n) time, O(1) extra space (two pointers walking inward, skip
non-alphanumeric chars, compare lowercase).
"""


def is_palindrome(s: str) -> bool:
    L = 0
    R = len(s) - 1
    while R > L:
        if s[L].lower().isalnum() and s[R].lower().isalnum():
            if s[L].lower() == s[R].lower():
                L += 1
                R -= 1
            else:
                return False
        elif not s[L].lower().isalnum():
            L += 1
        elif not s[R].lower().isalnum():
            R -= 1
        
    return True

    


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    print("all tests passed")
