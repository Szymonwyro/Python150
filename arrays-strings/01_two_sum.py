"""
LeetCode 1 - Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return the
indices of the two numbers that add up to `target`.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]          # nums[0] + nums[1] == 9

Constraints:
    - Exactly one valid answer exists.
    - You may not use the same element twice.

Target: O(n) time, O(n) space. (The brute-force O(n^2) works, but the
point of this one is to build the "one-pass hashmap" reflex.)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]
    print("all tests passed")
