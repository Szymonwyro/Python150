"""
05 - Price Span                                Medium | monotonic stack
-------------------------------------------------------------------------------
For each day, the "span" is the number of consecutive days ending on that day
(including the day itself) on which the price was less than or equal to that
day's price.

Return the span for every day.

Input (stdin)
    Line 1: n
    Line 2: n space-separated integers, the prices

Output (stdout)
    n space-separated integers, the spans

Example
    Input
        7
        100 80 60 70 60 75 85
    Output
        1 1 1 2 1 4 6

Constraints
    1 <= n <= 10^5
Target: O(n). Checking backwards from every day is O(n^2) and will time out.

Note: input parsing is left to you in this one - practise it.
"""
import sys


def solve(prices):
    n = len(prices)
    spans = n*[0]
    stack = [] # tracks index of highest price seen at top
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            # we found a higher price
            # we need to remove from top of stack and add this one
            stack.pop()
        if not stack:
            spans[i] = i + 1 # accounts for start (0) -> 1
        else:
            spans[i] = i - stack[-1]
        stack.append(i)

    return spans


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    spans = solve(prices)
    print(" ".join(map(str, spans)))


if __name__ == "__main__":
    main()
