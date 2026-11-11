"""Solution 08 - bottom-up DP. dp[a] = fewest notes to make a.
dp[a] = 1 + min(dp[a - note]) over notes <= a. O(m * amount)."""
import sys


def solve(notes, amount):
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in notes:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1


def main():
    data = sys.stdin.read().split()
    m, amount = int(data[0]), int(data[1])
    notes = list(map(int, data[2:2 + m]))
    print(solve(notes, amount))


if __name__ == "__main__":
    main()
