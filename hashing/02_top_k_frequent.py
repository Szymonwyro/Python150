"""
LeetCode 347 - Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array `nums` and an integer `k`, return the `k` most
frequent elements. Any order of the answer is acceptable.

Example:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Target: O(n) time using bucket sort by frequency (a heap gets you
O(n log k), which is fine too and worth knowing as the fallback — but try
the O(n) bucket approach first).
"""

from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # TODO: implement
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    print("all tests passed")
