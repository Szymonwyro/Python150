"""
07 - Batch Server Capacity                     Medium | binary search on answer
-------------------------------------------------------------------------------
A settlement server must process n batches of transactions IN ORDER. Batch i
has size sizes[i]. Each day, the server processes consecutive batches until
adding the next batch would exceed its daily capacity C. A batch cannot be
split across days.

Find the minimum capacity C such that all batches are processed within d days.

Input (stdin)
    Line 1: n d
    Line 2: n space-separated integers, the batch sizes

Output (stdout)
    One integer: the minimum capacity

Example
    Input
        10 5
        1 2 3 4 5 6 7 8 9 10
    Output
        15           (days: [1..5] [6,7] [8] [9] [10])

Constraints
    1 <= d <= n <= 5 * 10^4,  1 <= size <= 500
Target: O(n log(sum)). Hint: what are the smallest and largest possible C?

Note: input parsing is left to you in this one - practise it.
"""
import sys

def days_needed(sizes, capacity):
    days = 1
    load = 0
    for size in sizes:
        if load + size <= capacity:
            load += size
        else:
            load = 0
            load += size
            days += 1
    return days
        



def solve(sizes, d):
    # which value of daily capacity 
    # the least is the largest number in the list
    # the most is the sum of the array - we process all at once
    # we try middle value of C: can we process all within the days?
    #   yes: capacity is too high or right, try the next binary search down including this one
    #   no: capacity is too low try the next binary search up removing it from list
    lower = max(sizes)
    upper = sum(sizes)
    while lower < upper:
        mid = (lower + upper) // 2          # round down
        if days_needed(sizes, mid) <= d:    # capacity is too big or right
            upper = mid
        else:                               # capacity is too low (took too many days), exclude and try higher
            lower = mid + 1
    return lower
        


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    d = int(data[1])
    sizes = list(map(int, data[2:n+3]))
    print(solve(sizes, d))


if __name__ == "__main__":
    main()
