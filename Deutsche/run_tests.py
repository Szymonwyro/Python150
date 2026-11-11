"""
Test runner for the Deutsche Bank practice set.

Usage
    python run_tests.py            # test every problem you've attempted
    python run_tests.py 3          # test problem 03 only
    python run_tests.py 3 --show   # also print failing input / expected / got

Each problem is run the way HackerRank runs it: as a script, input on stdin,
answer compared against stdout. Per problem you get:
    - the worked example from the problem file
    - edge cases (single element, duplicates, negatives, etc.)
    - 30 random small cases
    - 1 large case with a 2-second limit (catches O(n^2) solutions)
Expected answers come from the reference code in solutions/.
"""
import glob
import os
import random
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TIME_LIMIT = 2.0


def arr(xs):
    return " ".join(map(str, xs))


# ---------------------------------------------------------------- case makers
def cases_01(r, big):
    if big:
        n = 100_000
        return [f"{n}\n{arr(r.randint(0, 10_000) for _ in range(n))}\n"]
    fixed = ["6\n7 1 5 3 6 4\n", "1\n5\n", "5\n9 7 5 3 1\n", "4\n2 2 2 2\n"]
    rand = []
    for _ in range(30):
        n = r.randint(1, 12)
        rand.append(f"{n}\n{arr(r.randint(0, 20) for _ in range(n))}\n")
    return fixed + rand


def cases_02(r, big):
    if big:
        n = 100_000
        return [f"{n} 0\n{arr(r.randint(-50, 50) for _ in range(n))}\n"]
    fixed = ["5 6\n1 5 7 -1 5\n", "1 2\n1\n", "4 4\n2 2 2 2\n", "3 0\n-3 3 0\n"]
    rand = []
    for _ in range(30):
        n = r.randint(1, 12)
        rand.append(f"{n} {r.randint(-6, 6)}\n{arr(r.randint(-5, 5) for _ in range(n))}\n")
    return fixed + rand


def cases_03(r, big):
    syms = ["AAPL", "MSFT", "TSLA", "NVDA", "DBK", "BARC"]
    if big:
        n = 100_000
        return [f"{n} 3\n{' '.join(r.choice(syms) for _ in range(n))}\n"]
    fixed = ["7 2\nAAPL MSFT AAPL TSLA TSLA AAPL TSLA\n", "1 1\nDBK\n",
             "4 1\nDBK DBK DBK DBK\n", "3 5\nA B C\n"]
    rand = []
    for _ in range(30):
        n = r.randint(1, 12)
        rand.append(f"{n} {r.randint(1, 4)}\n{' '.join(r.choice(syms[:4]) for _ in range(n))}\n")
    return fixed + rand


def cases_04(r, big):
    def fmt(iv):
        return f"{len(iv)}\n" + "".join(f"{s} {e}\n" for s, e in iv)

    def rand_iv(n, hi):
        out = []
        for _ in range(n):
            s = r.randint(0, hi)
            out.append((s, s + r.randint(0, hi // 10 + 1)))
        return out

    if big:
        return [fmt(rand_iv(100_000, 10**9))]
    fixed = [fmt([(8, 10), (1, 3), (2, 6), (15, 18)]), fmt([(1, 3), (3, 5)]),
             fmt([(5, 5)]), fmt([(1, 10), (2, 3), (4, 5)])]
    return fixed + [fmt(rand_iv(r.randint(1, 8), 30)) for _ in range(30)]


def cases_05(r, big):
    if big:
        n = 100_000
        # decreasing then a spike: punishes the naive backwards scan
        prices = list(range(n - 1, 0, -1)) + [n]
        return [f"{n}\n{arr(prices)}\n"]
    fixed = ["7\n100 80 60 70 60 75 85\n", "1\n42\n", "4\n5 5 5 5\n", "5\n1 2 3 4 5\n"]
    rand = []
    for _ in range(30):
        n = r.randint(1, 12)
        rand.append(f"{n}\n{arr(r.randint(1, 10) for _ in range(n))}\n")
    return fixed + rand


def cases_06(r, big):
    if big:
        n = 100_000
        return [f"{n} 0\n{arr(r.randint(-3, 3) for _ in range(n))}\n"]
    fixed = ["5 3\n1 2 1 -1 2\n", "1 0\n0\n", "4 0\n0 0 0 0\n", "3 -2\n-1 -1 2\n"]
    rand = []
    for _ in range(30):
        n = r.randint(1, 12)
        rand.append(f"{n} {r.randint(-5, 5)}\n{arr(r.randint(-4, 4) for _ in range(n))}\n")
    return fixed + rand


def cases_07(r, big):
    if big:
        n = 50_000
        return [f"{n} 37\n{arr(r.randint(1, 500) for _ in range(n))}\n"]
    fixed = ["10 5\n1 2 3 4 5 6 7 8 9 10\n", "1 1\n7\n", "3 3\n3 2 2\n", "4 1\n1 2 3 4\n"]
    rand = []
    for _ in range(30):
        n = r.randint(1, 10)
        rand.append(f"{n} {r.randint(1, n)}\n{arr(r.randint(1, 15) for _ in range(n))}\n")
    return fixed + rand


def cases_08(r, big):
    if big:
        return ["12 10000\n" + arr(r.sample(range(7, 400), 12)) + "\n"]
    fixed = ["3 11\n1 2 5\n", "1 3\n2\n", "1 0\n7\n", "3 6\n1 3 4\n"]
    rand = []
    for _ in range(30):
        m = r.randint(1, 4)
        rand.append(f"{m} {r.randint(0, 40)}\n{arr(r.sample(range(2, 15), m))}\n")
    return fixed + rand


MAKERS = {1: cases_01, 2: cases_02, 3: cases_03, 4: cases_04,
          5: cases_05, 6: cases_06, 7: cases_07, 8: cases_08}


# ---------------------------------------------------------------- runner
def run(path, inp):
    start = time.perf_counter()
    try:
        p = subprocess.run([sys.executable, path], input=inp, capture_output=True,
                           text=True, timeout=TIME_LIMIT * 3)
    except subprocess.TimeoutExpired:
        return None, "", TIME_LIMIT * 3
    return p.stdout, p.stderr, time.perf_counter() - start


def norm(s):
    return "\n".join(line.strip() for line in s.strip().splitlines())


def find(folder, num):
    hits = glob.glob(os.path.join(HERE, folder, f"{num:02d}_*.py"))
    return hits[0] if hits else None


def test_problem(num, show):
    mine, ref = find("", num), find("solutions", num)
    name = os.path.basename(mine)[:-3]
    r = random.Random(num)
    small, big = MAKERS[num](r, False), MAKERS[num](r, True)

    passed, first_fail = 0, None
    for inp in small:
        want, _, _ = run(ref, inp)
        got, err, _ = run(mine, inp)
        if got is not None and norm(got) == norm(want):
            passed += 1
        elif first_fail is None:
            first_fail = (inp, want, got if got is not None else "<timed out>", err)

    big_note = ""
    if passed == len(small):
        want, _, _ = run(ref, big[0])
        got, _, secs = run(mine, big[0])
        if got is None or secs > TIME_LIMIT:
            big_note = f"  large case TOO SLOW ({secs:.1f}s > {TIME_LIMIT}s)"
        elif norm(got) != norm(want):
            big_note = "  large case WRONG ANSWER"
        else:
            big_note = f"  large case OK ({secs:.2f}s)"
    else:
        big_note = "  large case skipped"

    status = "PASS" if passed == len(small) and "OK" in big_note else "FAIL"
    print(f"[{status}] {name}: {passed}/{len(small)} small{big_note}")
    if show and first_fail:
        inp, want, got, err = first_fail
        print("    input:\n      " + inp.strip().replace("\n", "\n      "))
        print("    expected:\n      " + want.strip().replace("\n", "\n      "))
        print("    got:\n      " + (got.strip() or "<nothing printed>").replace("\n", "\n      "))
        if err.strip():
            print("    error:\n      " + err.strip().splitlines()[-1])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show = "--show" in sys.argv
    nums = [int(a) for a in args] or sorted(MAKERS)
    for n in nums:
        test_problem(n, show)


if __name__ == "__main__":
    main()
