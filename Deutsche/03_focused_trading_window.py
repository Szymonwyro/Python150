"""
03 - Focused Trading Window                    Medium | sliding window + hash map
-------------------------------------------------------------------------------
A trader's activity log is a sequence of n ticker symbols, one per trade.
Find the length of the longest CONTIGUOUS stretch of trades that involves at
most k distinct tickers.

Input (stdin)
    Line 1: n k
    Line 2: n space-separated ticker symbols (strings)

Output (stdout)
    One integer: the length of the longest valid window

Example
    Input
        7 2
        AAPL MSFT AAPL TSLA TSLA AAPL TSLA
    Output
        5            (AAPL TSLA TSLA AAPL TSLA)

Constraints
    1 <= n <= 10^5,  1 <= k <= n
Target: O(n)
"""
import sys


def solve(tickers, k):
    seen = {}
    best = 0
    left = 0
    for right, ticker in enumerate(tickers):
        seen[ticker] = seen.get(ticker, 0) + 1
        while len(seen) > k: # len(dict) returns number of distinct items
            out = tickers[left] # item that needs removing (where we slide the window to)
            seen[out] -= 1 # reduce item count
            if seen[out] == 0: # if item count was 1, now 0: remove it entirely 
                del seen[out] # remove item from dict
            left += 1 # slide window forward

        best = max(best, right - left + 1)

    return best





        
        

    return curr_length


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    tickers = data[2:2 + n]
    print(solve(tickers, k))


if __name__ == "__main__":
    main()
