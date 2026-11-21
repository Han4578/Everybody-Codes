from collections import Counter
import math
from itertools import permutations

def convert(a, b):
        if a == "K" or b == "K": return "K"
        if a == b: return a
        
        match sorted([a, b]):
            case ["C", "M"]:
                return "B"
            case ["C", "Y"]:
                return "G"
            case ["M", "Y"]:
                return "R"

def part_1():
    with open("Day 19/part_1.txt") as f:
        grids = f.read().split("\n\n")

    count = Counter()

    for a, b in zip(*grids):
        if a == "\n": continue
        count[convert(a, b)] += 1


    ans = math.prod(c[1] for c in count.most_common(3))

    print(ans)

def part_2():
    with open("Day 19/part_2.txt") as f:
        grids = f.read().split("\n\n")

    ans = 0
    pairs = Counter((c1, n2) for c1, n2 in zip(*grids) if c1 != "\n")

    for p in permutations("CMYK", 4):
        count = Counter()

        for (c1, n2), freq in pairs.items():
            c2 = p[int(n2) - 1]
            count[convert(c1, c2)] += freq

        ans = max(ans, math.prod(c[1] for c in count.most_common(3)))

    print(ans)

def part_3():
    with open("Day 19/part_3.txt") as f:
        grids = f.read().replace("\n", "")

    ans = 0

    count = Counter(grids)
    c = count["C"]
    m = count["M"]
    y = count["Y"]
    k = count["K"]

    tri = sorted([c, m, y])
    gap = tri[1] - tri[0]
    tri[0] += min(gap, tri[2])
    tri[2] -= min(gap, tri[2])
    tri[0] += (tri[2] + 1) // 2
    tri[1] += tri[2] // 2

    t = c + m + y
    equal = [t // 3] * 3

    for i in range(t % 3):
        equal[i] += 1

    ans = max(math.prod(sorted([c, m, y, k], reverse=True)[:3]), k * tri[0] * tri[1], math.prod(equal))

    print(ans)

part_1()
part_2()
part_3()