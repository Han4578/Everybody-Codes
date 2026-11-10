from pyperclip import copy
import re
from collections import deque

def part_1():
    with open("part 1.txt", "r") as f:
        lines = f.read().splitlines()
        x, y = [int(c) for c in re.findall(r"\d+", lines[0])]
        a = [int(c) for c in re.findall(r"\d+", lines[1])]
        b = [int(c) for c in re.findall(r"\d+", lines[2])]
        c = [int(c) for c in re.findall(r"\d+", lines[3])]
        moves = lines[4][6:]

    beacons = {
        "A": a,
        "B": b,
        "C": c
    }

    seen = {(x, y)}

    for m in moves:
        x = (beacons[m][0] + x) // 2
        y = (beacons[m][1] + y) // 2

        seen.add((x, y))

    return len(seen)

def part_2():
    with open("part 2.txt", "r") as f:
        lines = f.read().splitlines()
        x, y = [int(c) for c in re.findall(r"\d+", lines[0])]
        a = [int(c) for c in re.findall(r"\d+", lines[1])]
        b = [int(c) for c in re.findall(r"\d+", lines[2])]
        c = [int(c) for c in re.findall(r"\d+", lines[3])]
        moves = lines[4][6:]

    beacons = {
        "A": a,
        "B": b,
        "C": c
    }

    seen = {(x, y)}
    fireflies = set()

    for m in moves:
        x = (beacons[m][0] + x) // 2
        y = (beacons[m][1] + y) // 2

        seen.add((x, y))

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            fireflies.add((x + dx, y + dy))

    return len(fireflies.difference(seen))

def part_3():
    with open("part 3.txt", "r") as f:
        lines = f.read().splitlines()
        x, y = [int(c) for c in re.findall(r"\d+", lines[0])]
        beacons = [tuple(int(c) for c in re.findall(r"\d+", l)) for l in lines[1:]]

    seen = {(x, y)}
    fireflies = set()
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for b in beacons:
            nx = (b[0] + x) // 2
            ny = (b[1] + y) // 2

            if (nx, ny) in seen: continue

            seen.add((nx, ny))
            queue.append((nx, ny))

    for x, y in seen:
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            fireflies.add((x + dx, y + dy))

    return len(fireflies.difference(seen))


ans = part_3()

print(ans)
copy(ans)
