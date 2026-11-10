import re
from collections import Counter
from functools import cache


def part_1():
    with open("Day 7/part_1.txt") as f:
        lines = f.read().split("\n")

    connections = {}

    ans = 0

    for line in lines:
        id, energy, *conn = [int(n) for n in re.findall(r"\d+", line)]

        connections[id] = conn
        ans += energy

    queue = [(max(connections.keys(), key=lambda k: len(connections[k])), 5)]
    
    while queue:
        cloud, remaining = queue.pop()

        ans += remaining

        if remaining == 1: continue
        for c in connections[cloud]:
            queue.append((c, remaining - 1))

    print(ans)

def part_2():
    with open("Day 7/part_2.txt") as f:
        lines = f.read().split("\n")

    ans = 0

    connections = {}

    for line in lines:
        id, energy, *conn = [int(n) for n in re.findall(r"\d+", line)]

        connections[id] = conn
        ans += energy

    @cache
    def dfs(cloud, remaining):
        ans = remaining

        if remaining > 1:
            for c in connections[cloud]:
                ans += dfs(c, remaining - 1)

        return ans


    ans += dfs(max(connections.keys(), key=lambda k: len(connections[k])), 10)

    print(ans)

def part_3():
    with open("Day 7/part_3.txt") as f:
        lines = f.read().split("\n")

    connections = {}
    energies = {}

    for line in lines:
        id, e, *conn = [int(n) for n in re.findall(r"\d+", line)]

        connections[id] = conn
        energies[id] = e

    ans = 0

    for starting in connections.keys():
        exploded = set()
        total = energies.copy()

        energy = Counter()

        energy[(starting, 10)] += 1

        while energy:
            new_energy = Counter()

            for (c, e), f in energy.items():
                if c in exploded: continue
                total[c] += e * f
                if e > 1:
                    for c2 in connections[c]:
                        if c2 in exploded: continue
                        new_energy[(c2, e - 1)] += f

            for c, e in total.items():
                if e >= 1000000:
                    exploded.add(c)
                    total[c] = 0

                    for c2 in connections[c]:
                        new_energy[(c2, 10)] += 1
            energy = new_energy

        ans = max(ans, sum(total.values()))

    print(ans)

part_3()