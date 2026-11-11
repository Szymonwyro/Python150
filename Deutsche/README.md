# Deutsche Bank – Technology Spring Week coding test prep

Eight HackerRank-style problems at the level a first-year coding screen is
likely to be (easy → medium). Each reads from stdin and prints to stdout,
exactly like the real platform.

| #  | Problem                    | Pattern                     | Level  |
|----|----------------------------|-----------------------------|--------|
| 01 | Best Single Trade          | greedy / running minimum    | Easy   |
| 02 | Matching Trade Pairs       | hash map                    | Easy   |
| 03 | Focused Trading Window     | sliding window              | Medium |
| 04 | Merge Maintenance Windows  | sorting + intervals         | Medium |
| 05 | Price Span                 | monotonic stack             | Medium |
| 06 | P&L Target Streaks         | prefix sums + hash map      | Medium |
| 07 | Batch Server Capacity      | binary search on the answer | Medium |
| 08 | Fewest Notes               | 1D dynamic programming      | Medium |

Problems 04–08 leave input parsing to you on purpose. Parsing stdin quickly is
where people lose time in the real thing.

## How to practise

1. Do them as mock tests: pick two, set a 50-minute timer, no hints.
2. Fill in `solve()` (and `main()` where it's a TODO) in the numbered file.
3. Run the tests:

```bash
python run_tests.py         # everything
python run_tests.py 5       # just problem 05
python run_tests.py 5 --show  # show the first failing case
```

Each problem is checked on the example, edge cases, 30 random cases, and one
large case with a 2-second limit, so a brute-force answer gets partial
credit but fails the large case (same as HackerRank).

4. Only then open `solutions/` and compare approaches.

## Real-test habits

- Read the constraints first: n ≈ 10^5 means you need O(n log n) or better.
- Submit a brute force for partial marks, then optimise.
- Check: empty/single element, duplicates, negatives, very large values.
- Clean names and a short comment on the approach. Reviewers may read it.
