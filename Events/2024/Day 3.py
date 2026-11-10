def find_ans(path, adjacent):
    with open(path, "r") as f:
        lines = f.read().split("\n")

    spots = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (c == "#"): spots.add((x, y))

    total = 0

    while (len(spots) > 0):
        total += len(spots)
        new_spot = set(filter(lambda s: all((s[0] + dx, s[1] + dy) in spots for dx, dy in adjacent), spots))
        spots = new_spot

    return total

adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
octal = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def p1():
    print(find_ans("Day 3/p1.txt", adjacent))

def p2():
    print(find_ans("Day 3/p2.txt", adjacent))

def p3():
    print(find_ans("Day 3/p3.txt", octal))

p3()