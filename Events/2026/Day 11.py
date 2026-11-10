from re import findall
from collections import deque
from itertools import permutations

def bfs(portals):
    ans = 0

    for i in range(len(portals)):
        seen = [False] * len(portals)
        seen[i] = True
        queue = deque([(i, 0)])

        while queue:
            p, c = queue.popleft()
            ans += c

            for p2 in portals[p]:
                if seen[p2]: continue
                queue.append((p2, c + 1))
                seen[p2] = True

    return ans

def part_1():
    with open("Day 11/part_1.txt") as f:
        lines = f.read().split("\n")

        p = int(lines[0][9:])
        extra = [[int(n) for n in findall(r"\d+", line)] for line in lines[2:]]

    portals = [[(i - 1) % p, (i + 1) % p] for i in range(p)]

    before = bfs(portals)

    for a, b in extra:
        portals[a - 1].append(b - 1)
        portals[b - 1].append(a - 1)

    after = bfs(portals)

    ans = before - after

    print(ans)

def part_2():
    with open("Day 11/part_2.txt") as f:
        lines = f.read().split("\n")

        p = int(lines[0][9:])
        extra = [[int(n) for n in findall(r"\d+", line)] for line in lines[2:]]

    portals = [[] for _ in range(p)]

    for i in range(p):
        for j in range(1, 4):
            portals[i].append((i - j) % p)
            portals[i].append((i + j) % p)

    before = bfs(portals)

    for a, b in extra:
        portals[a - 1].append(b - 1)
        portals[b - 1].append(a - 1)

    ans = 0

    for i in range(p):
        for j in range(i + 1, p):
            if j in portals[i]: continue
            portals[i].append(j)
            portals[j].append(i)
            ans = max(ans, before - bfs(portals))
            del portals[i][-1]
            del portals[j][-1]

    print(ans)

def part_3():
    with open("Day 11/part_3.txt") as f:
        lines = f.read().split("\n")

        p = int(lines[0][9:])
        extra = [[int(n) for n in findall(r"\d+", line)] for line in lines[2:]]

    portals = [[] for _ in range(p)]

    for i in range(p):
        for j in range(1, 4):
            portals[i].append((i - j) % p)
            portals[i].append((i + j) % p)

    before = bfs(portals)

    for a, b in extra:
        portals[a - 1].append(b - 1)
        portals[b - 1].append(a - 1)

    ans = 0
    pairs = {tuple(sorted(tuple(sorted((arrange[i], arrange[i + 4]))) for i in range(4))) for arrange in permutations(list(range(8)), 8)}

    for i in range(p // 8):
        crystals = [(i + j) % p for j in range(0, p, p // 8)]

        for arrange in pairs:
            for i, j in arrange:
                a = crystals[i]
                b = crystals[j]
                portals[a].append(b)
                portals[b].append(a)

            ans = max(ans, before - bfs(portals))

            for i, j in arrange:
                a = crystals[i]
                b = crystals[j]
                del portals[a][-1]
                del portals[b][-1]

    print(ans)


part_3()