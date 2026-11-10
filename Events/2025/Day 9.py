import itertools
from collections import deque

import sys
print(sys.version)
print(sys.executable)

def part_1():
    with open("Day 9/part 1.txt", "r") as f:
        parents = [s[s.index(":") + 1:] for s in f.read().splitlines()]

    ans = 0

    for p1, p2, c in itertools.combinations(parents, 3):

        if any(c[i] not in (p1[i], p2[i]) for i in range(len(c))): continue

        ans = sum(a == b for a, b in zip(p1, c)) * sum(a == b for a, b in zip(p2, c))
        break

    print(ans)

def part_2():
    with open("Day 9/part 2.txt", "r") as f:
        parents = [s[s.index(":") + 1:] for s in f.read().splitlines()]

    ans = 0

    for p1, p2, c in itertools.permutations(parents, 3):
        if p1 > p2: continue

        if any(c[i] not in (p1[i], p2[i]) for i in range(len(c))): continue

        ans += sum(a == b for a, b in zip(p1, c)) * sum(a == b for a, b in zip(p2, c))

    print(ans)

def part_3():
    with open("Day 9/part 3.txt", "r") as f:
        dnas = [s[s.index(":") + 1:] for s in f.read().splitlines()]

    parents = list(range(len(dnas)))
    sizes = [(1, i) for i in range(1, len(parents) + 1)]

    def find(i):
        while parents[i] != i:
            i = parents[i]

        return i

    for ch in range(len(parents)):
        found = False
        for p1 in range(len(parents) - 1):
            if p1 == ch: continue
            for p2 in range(p1 + 1, len(parents)):
                if p2 == ch or any(c != a and c != b for a, b, c in zip(dnas[p1], dnas[p2], dnas[ch])): continue
                gp1 = find(p1)
                gp2 = find(p2)
                gp3 = find(ch)

                found = True

                gp4 = min(gp1, gp2, gp3)
                gps = {gp1, gp2, gp3}

                sizes[gp4] = tuple(sum(sizes[gp][i] for gp in gps) for i in range(2))

                parents[gp1] = gp4
                parents[gp2] = gp4
                parents[gp3] = gp4
                parents[p1] = gp4
                parents[p2] = gp4
                parents[ch] = gp4
                break
            if found: break

    ans = max(sizes)[1]
    print(ans)

def part_4(): #part 3 but different method
    with open("Day 9/part 3.txt", "r") as f:
        dnas = [s[s.index(":") + 1:] for s in f.read().splitlines()]

    sizes = [[] for _ in range(1, len(dnas) + 1)]
    ans = (0, 0)

    for ch in range(len(dnas)):
        found = False
        for p1 in range(len(dnas) - 1):
            if p1 == ch: continue
            for p2 in range(p1 + 1, len(dnas)):
                if p2 == ch: continue
                if any(a != c and b != c for a, b, c in zip(dnas[p1], dnas[p2], dnas[ch])): continue

                sizes[p1].append(ch)
                sizes[p2].append(ch)
                sizes[ch].append(p1)
                sizes[ch].append(p2)

                found = True
                break
            if found: break

    seen = [False] * len(dnas)

    for i in range(len(dnas)):
        if seen[i]: continue
        seen[i] = True
        size = 0
        total = 0
        queue = deque((i,))

        while queue:
            j = queue.popleft()

            size += 1
            total += j
            
            for k in sizes[j]:
                if seen[k]: continue
                seen[k] = True
                queue.append(k)

        ans = max(ans, (size, total))

    print(sum(ans))
