"""
LeetCode 49 - Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings `strs`, group the anagrams together. You can
return the answer in any order.

Example:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Constraints:
    - 1 <= strs.length <= 10^4
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters.

Target: O(n * k) time where k is max string length, avoid the O(k log k)
per-string sort if you can (think: character count as a hashable key).
"""

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups.append(word)
    return list(groups.value())

    


def _normalize(groups: List[List[str]]):
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert _normalize(result) == _normalize(expected), result

    assert group_anagrams([""]) == [[""]]
    assert _normalize(group_anagrams(["a"])) == [["a"]]
    print("all tests passed")
