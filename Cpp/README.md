# LeetCode — C++

Each file has the problem as a comment, an empty `Solution`, and tests in `main()`.
Fill in the TODO, run it, and every check prints PASS or FAIL.

## Run
- **VS Code:** open a problem file, press `Cmd/Ctrl+Shift+B`.
- **Terminal:** `./run.sh 01-arrays-hashing/001_two_sum.cpp` (adds sanitizers to catch out-of-bounds / UB).

Out of the box every problem fails — that's expected until you solve it.
Once all tests pass, paste just the `class Solution` into leetcode.com to submit.

## Problems (suggested order)
| # | Problem | Difficulty | Pattern | File |
|---|---|---|---|---|
| 1 | Two Sum | Easy | Hash map | `01-arrays-hashing/001_two_sum.cpp` |
| 217 | Contains Duplicate | Easy | Hash set | `01-arrays-hashing/217_contains_duplicate.cpp` |
| 242 | Valid Anagram | Easy | Counting | `01-arrays-hashing/242_valid_anagram.cpp` |
| 238 | Product of Array Except Self | Medium | Prefix/suffix | `01-arrays-hashing/238_product_except_self.cpp` |
| 125 | Valid Palindrome | Easy | Two pointers | `02-two-pointers/125_valid_palindrome.cpp` |
| 15 | 3Sum | Medium | Sort + two pointers | `02-two-pointers/015_three_sum.cpp` |
| 121 | Best Time to Buy and Sell Stock | Easy | Running min | `03-sliding-window/121_best_time_stock.cpp` |
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding window | `03-sliding-window/003_longest_substring.cpp` |
| 20 | Valid Parentheses | Easy | Stack | `04-stack/020_valid_parentheses.cpp` |
| 704 | Binary Search | Easy | Binary search | `05-binary-search/704_binary_search.cpp` |
| 206 | Reverse Linked List | Easy | Pointers | `06-linked-list/206_reverse_linked_list.cpp` |
| 70 | Climbing Stairs | Easy | 1-D DP | `07-dynamic-programming/070_climbing_stairs.cpp` |
| 53 | Maximum Subarray | Medium | Kadane | `07-dynamic-programming/053_maximum_subarray.cpp` |
| 200 | Number of Islands | Medium | DFS/BFS grid | `08-graphs/200_number_of_islands.cpp` |

## Adding a new problem
Copy any file, swap the comment/signature, and write a few `CHECK(actual, expected)` lines —
include the edge cases (empty input, single element, negatives, duplicates).

## Habit
1. Try for 25 min without hints. 2. Note time/space in the header. 3. Commit: `git commit -m "solve 001 two sum"`.
