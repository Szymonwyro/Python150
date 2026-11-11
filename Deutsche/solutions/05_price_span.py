"""Solution 05 - monotonic decreasing stack of indices. O(n): each index is
pushed and popped at most once."""
import sys


def solve(prices):
    spans = []
    stack = []  # indices of days with prices strictly greater than later ones
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] <= p:
            stack.pop()
        spans.append(i + 1 if not stack else i - stack[-1])
        stack.append(i)
    return spans


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    print(" ".join(map(str, solve(prices))))


if __name__ == "__main__":
    main()
