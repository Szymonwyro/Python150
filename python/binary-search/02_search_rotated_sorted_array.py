"""
LeetCode 33 - Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array `nums` sorted in ascending order (with distinct
values), possibly rotated at an unknown pivot. Given the rotated array and
a `target`, return its index, or -1 if not present.

Example:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

Target: O(log n) time. The trick: at every step, at least one half of the
array (around mid) is guaranteed sorted — figure out which half, then
decide if target lies in it.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([5, 1, 3], 3) == 2
    print("all tests passed")
