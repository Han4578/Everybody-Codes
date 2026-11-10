from functools import cache
def part_1():
    with open("Day 10/part 1.txt", "r") as f:
        lines = f.read().splitlines()

    dragon = (0, 0)

    for y, line in enumerate(lines):
        try:
            dragon = (line.index("D"), y)
            break
        except:
            pass

    seen = {dragon}
    current = [dragon]
    width = len(lines[0])
    height = len(lines)

    for _ in range(4):
        next = []

        for x, y in current:
            for dx, dy in ((2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1)):
                nx = dx + x
                ny = dy + y

                if 0 <= nx < width and 0 <= ny < height and (t:=(nx, ny)) not in seen:
                    seen.add(t)
                    next.append(t)

        current = next

    ans = 0

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == "S" and (x, y) in seen:
                ans += 1

    print(ans)

def part_2():
    with open("Day 10/part 2.txt", "r") as f:
        lines = f.read().splitlines()

    dragon = (0, 0)
    sheeps = set()
    hide = set()

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            match c:
                case "S":
                    sheeps.add((x, y))
                case "#":
                    hide.add((x, y))
                case "D":
                    dragon = (x, y)

    current = {dragon}
    width = len(lines[0])
    height = len(lines)
    ans = 0

    def is_eaten(x, y, step):
        nonlocal ans

        if (x, y) not in hide and (x, y - step) in sheeps:
            sheeps.remove((x, y - step))
            ans += 1

    for step in range(20):
        next = set()

        for x, y in current:
            for dx, dy in ((2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1)):
                nx = dx + x
                ny = dy + y

                if 0 <= nx < width and 0 <= ny < height and (t:=(nx, ny)) not in next:
                    next.add(t)

        current = next

        for x, y in current:
            is_eaten(x, y, step)
            is_eaten(x, y, step + 1)


    print(ans)

def part_3():
    with open("Day 10/part 3.txt", "r") as f:
        lines = f.read().splitlines()

    dragon = (0, 0)
    sheeps = set()
    hide = []

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            match c:
                case "S":
                    sheeps.add((x, y))
                case "#":
                    hide.append((x, y))
                case "D":
                    dragon = (x, y)
                    
    hide = frozenset(hide)
    width = len(lines[0])
    height = len(lines)

    @cache
    def dfs(dragon, sheeps):
        moves = 0
        next = []
        moved = False

        for dx, dy in ((2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1)):
            nx = dragon[0] + dx
            ny = dragon[1] + dy

            if 0 <= nx < width and 0 <= ny < height:
                next.append((nx, ny))

        for s in sheeps:
            t = (s[0], s[1] + 1)
            if t == dragon and t not in hide: continue
            moved = True
            if all((t[0], y) in hide for y in range(t[1], height)) or t[1] >= height: continue

            for d in next:
                remaining = list(sh for sh in sheeps if sh != s and (sh != d or sh in hide))
                if d != t or t in hide: remaining.append(t)
                if remaining: moves += dfs(d, frozenset(remaining))
                else: moves += 1

        if not moved:
            for d in next:
                remaining = frozenset(sh for sh in sheeps if sh != d or sh in hide)
                if remaining: moves += dfs(d, remaining)
                else: moves += 1

        return moves
    
    ans = dfs(dragon, frozenset(sheeps))
    return ans

import timeit

print(timeit.timeit(part_3, number=1))
