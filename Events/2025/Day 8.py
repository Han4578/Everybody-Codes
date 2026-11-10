from bisect import bisect_left, bisect_right
from collections import defaultdict

def part_1():
    with open("Day 8/part 1.txt", "r") as f:
        sequence = f.read().split(",")

    nails = 32
    prev = 0

    half = nails // 2
    ans = 0

    for s in sequence:
        n = int(s)

        if abs(prev - n) == half:
            ans += 1

        prev = n

    print(ans)

def part_2():
    with open("Day 8/part 2.txt", "r") as f:
        sequence = [int(c) for c in f.read().split(",")]

    pairs = defaultdict(list) 
    ans = 0

    for i in range(1, len(sequence)):
        a, b = sorted((sequence[i - 1], sequence[i]))
            
        for k, v in pairs.items():
            if k < a:
                ans += bisect_left(v, b) - bisect_right(v, a)
            elif a < k < b:
                ans += len(v) - bisect_right(v, b)

        pairs[a].insert(bisect_right(pairs[a], b), b)

    print(ans)

def part_3():
    with open("Day 8/part 3.txt", "r") as f:
        sequence = [int(s) for s in f.read().split(",")]

    NAILS = 256
    rel = [0] * (NAILS ** 2) 
    ans = 0

    for i in range(1, len(sequence)):
        a, b = sorted((sequence[i], sequence[i - 1]))

        for i in range(a - 1):
            rel[i * NAILS + a] += 1
            rel[i * NAILS + b - 1] -= 1

        for i in range(a, b - 1):
            rel[i * NAILS + b] += 1
            rel[(i + 1) * NAILS] -= 1

    current = 0

    for r in rel:
        current += r
        ans = max(ans, current)

    print(ans)

part_1()
part_2()
part_3()   