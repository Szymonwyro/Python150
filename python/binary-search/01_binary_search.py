"""
LeetCode 704 - Binary Search
https://leetcode.com/problems/binary-search/

Given a sorted (ascending) array of distinct integers `nums` and a
`target`, return its index, or -1 if it's not present.

Example:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4

Target: O(log n) time, O(1) space. Get the invariant right (which side is
`lo`/`hi` inclusive/exclusive of) rather than reaching for a library call.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([], 1) == -1
    print("all tests passed")
