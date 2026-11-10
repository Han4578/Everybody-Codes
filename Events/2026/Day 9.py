import re
from collections import Counter

def part_1():
    with open("Day 9/part_1.txt") as f:
        lines = f.read().split("\n")

    ans = 0

    for line in lines:
        _, growth, limit = [int(n) for n in re.findall(r"\d+", line)]
        cur = Counter()
        cur[0] += 1

        while limit > sum(k * f for k, f in cur.items()):
            ans += 1
            grow = Counter()

            for k, f in cur.items():
                if k + 1 == growth:
                    grow[growth // 2] += f << 1
                    grow[1] += f
                    limit -= f
                else:
                    grow[k + 1] += f


            cur = grow


    print(ans)

def part_2():
    with open("Day 9/part_2.txt") as f:
        lines = f.read().split("\n")

    ans = 0

    for line in lines:
        _, growth, limit = [int(n) for n in re.findall(r"\d+", line)]
        branch = Counter()
        leaf = Counter()
        leaf[0] += 1

        while limit > 1:
            ans += 1
            new_branch = Counter()
            new_leaf = Counter()

            for k, f in branch.items():
                if k + 1 == growth:
                    new_branch[growth // 2] += f << 1
                    new_leaf[1] += f
                    limit -= f
                else:
                    new_branch[k + 1] += f

            for k, f in leaf.items():
                if k + 1 == growth:
                    new_branch[growth // 2] += f
                    new_leaf[growth // 2] += f
                    new_leaf[1] += f
                    limit -= f
                else:
                    new_leaf[k + 1] += f


            branch = new_branch
            leaf = new_leaf


    print(ans)

def worker_bfs(growth, limit, factor = 1):
    g = growth // 2 + 1
    low = max(1, limit * (factor - 1))
    high = limit * factor
    lowest = -1

    while low <= high:
        t = (low + high) // 2
        total = 1
        branch = Counter()
        branch[t - growth // 2] += 1

        while total < limit and branch:
            k = max(branch)
            f = branch.pop(k)

            if k < g: break
            total += f * (k // g)
            if total >= limit: break
            for r in range(g, k + 1, g):
                branch[k - r] += f
                branch[k - r - g + 2] += f

        if total >= limit:
            lowest = t
            high = t - 1
        else:
            low = t + 1

    if lowest == -1: return worker_bfs(growth, limit, factor + 1)   
    return lowest

def part_3():
    with open("Day 9/part_3.txt") as f:
        lines = f.read().split("\n")

    ans = 0
    for line in lines:
        _, growth, limit = [int(n) for n in re.findall(r"\d+", line)]
        ans += worker_bfs(growth, limit)

    print(ans)

part_3()

