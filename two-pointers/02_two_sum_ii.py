"""
LeetCode 167 - Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers `numbers` that is already sorted in
non-decreasing order, find two numbers that add up to `target`. Return
the indices as a 1-indexed array [index1, index2] with index1 < index2.

Example:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]

Constraints:
    - Exactly one valid answer exists.
    - You may not use the same element twice.

Target: O(n) time, O(1) extra space — this is the "use the sortedness"
counterpart to plain Two Sum. Don't reach for a hashmap here.
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    # TODO: implement (two pointers, one from each end)
    raise NotImplementedError


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
    print("all tests passed")
