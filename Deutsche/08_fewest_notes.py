"""
08 - Fewest Notes                              Medium | 1D dynamic programming
-------------------------------------------------------------------------------
An ATM holds unlimited notes of m denominations. Find the fewest notes needed
to pay out exactly `amount`. If it cannot be done, return -1.

Greedy (always take the biggest note) does NOT always work: with notes
[1, 3, 4] and amount 6, greedy gives 4+1+1 (3 notes) but 3+3 is 2 notes.

Input (stdin)
    Line 1: m amount
    Line 2: m space-separated integers, the denominations

Output (stdout)
    One integer: the fewest notes, or -1

Example
    Input
        3 11
        1 2 5
    Output
        3            (5 + 5 + 1)

Constraints
    1 <= m <= 12,  1 <= note <= 10^4,  0 <= amount <= 10^4
Target: O(m * amount)

Note: input parsing is left to you in this one - practise it.
"""
import sys


def solve(notes, amount):
    best = {0: 0} # keep a table of the smallest amount of notes for each value
    for i in range(1, amount):
        best_note = 100000
        for note in notes:
            best_note = min(best_note, best[amount - note])
        else:

    pass


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    notes = list(map(int, data[2: n+3]))
    amount = int(data[1])
    pass


if __name__ == "__main__":
    main()
