import re
from itertools import combinations
from math import lcm

def move_hand(x, y, dx, dy, full, c):
    if dy == dx : return 0
    ans = 0
    
    moved = (dx - dy) * c + (x - y)
    if (moved >= 0 and x - y < 0) or (moved <= 0 and x - y > 0): ans += 1
    return abs(moved) // full + ans

def simulate_clock(lines):
    limit = [int(n) for n in re.findall(r"\d+", lines[0])]
    dir = [1 if c == "CW" else -1 for c in re.findall(r"C?CW", lines[1])]
    pos = [int(n) for n in re.findall(r"\d+", lines[2])]
    move = [int(n) for n in re.findall(r"\d+", lines[3])]

    ans = 0
    full = lcm(*limit)

    for a, b in combinations(list(range(3)), 2):
        lx = limit[a]
        ly = limit[b]

        x = full // lx * pos[a]
        y = full // ly * pos[b]
        dx = full // lx * dir[a]
        dy = full // ly * dir[b]

        cx = move[a]
        cy = move[b]

        ans += move_hand(x, y, dx, dy, full, min(cx, cy))

        if cx > cy:
            ans += move_hand((x + dx * (cy % lx)) % full, (y + dy * (cy % ly)) % full, dx, 0, full, cx - cy)
        elif cx < cy:
            ans += move_hand((x + dx * (cx % lx)) % full, (y + dy * (cx % ly)) % full, 0, dy, full, cy - cx)
    return ans

def part_1():
    with open("Day 13/part_1.txt") as f:
        lines = f.read().split("\n")

    ans = simulate_clock(lines)

    print(ans)

def part_2():
    with open("Day 13/part_2.txt") as f:
        clocks = f.read().split("\n\n")

    ans = sum(simulate_clock(c.split("\n")) for c in clocks)

    print(ans)

def part_3():
    with open("Day 13/part_3.txt") as f:
        clocks = f.read().split("\n\n")

    ans = sum(simulate_clock(c.split("\n")) for c in clocks)

    print(ans)

part_1()
part_2()
part_3()