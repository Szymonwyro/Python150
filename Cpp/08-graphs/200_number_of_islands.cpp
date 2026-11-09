/*
 * LeetCode #200 — Number of Islands   [Medium]   topic: DFS/BFS grid
 * https://leetcode.com/problems/  (search the number to submit)
 *
 * `grid` is a 2-D map of '1' (land) and '0' (water). An island is a group of
 * land cells connected up/down/left/right. Count the islands.
 *
 * Examples:
 * 11000
 * 11000
 * 00100
 * 00011   -> 3
 *
 * Hint: DFS from each unvisited '1', sinking the island as you go. Then rewrite it with a BFS queue.
 *
 * Status: [ ] solved   Time: ___   Space: ___
 */
#include "../common/test.h"

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // TODO: your solution here
        return 0;
    }
};

int main() {
    Solution s;
    auto g = [](vector<string> rows) { vector<vector<char>> r; for (auto& x : rows) r.emplace_back(x.begin(), x.end()); return r; };
    { auto a = g({"11110","11010","11000","00000"}); CHECK(s.numIslands(a), 1); }
    { auto a = g({"11000","11000","00100","00011"}); CHECK(s.numIslands(a), 3); }
    { auto a = g({"101","010","101"});               CHECK(s.numIslands(a), 5); }
    { auto a = g({"0"});                             CHECK(s.numIslands(a), 0); }
    SUMMARY();
}
