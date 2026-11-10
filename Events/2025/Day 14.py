from collections import Counter

def change(active, width, height):
    count = Counter()

    for x, y in active:
        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            count[(x + dx, y + dy)] += 1    

    return frozenset(t for x in range(width) for y in range(height) if (count[t := (x, y)] % 2 == 0) ^ (t in active))

def part_1():
    with open("Day 14/part 1.txt", "r") as f:
        grid = f.read().splitlines()

    ans = 0
    width = len(grid[0])
    height = len(grid)
    active = {(x, y) for x in range(width) for y in range(height) if grid[y][x] == "#"}

    for _ in range(10):
        active = change(active, width, height)
        ans += len(active)

    print(ans)

def part_2():
    with open("Day 14/part 2.txt", "r") as f:
        grid = f.read().splitlines()

    ans = 0
    width = 34
    height = 34
    active = {(x, y) for x in range(width) for y in range(height) if grid[y][x] == "#"}

    for _ in range(2025):
        active = change(active, width, height)
        ans += len(active)

    print(ans)


def part_3():
    with open("Day 14/part 3.txt", "r") as f:
        grid = f.read().splitlines()

    ans = 0
    width = 34
    height = 34
    offset_x = (width - len(grid[0])) // 2
    offset_y = (height - len(grid)) // 2
    target = frozenset((offset_x + x, offset_y + y)  for y, row in enumerate(grid) for x, c in enumerate(row) if c == "#")
    antitarget = frozenset(t for x in range(offset_x, offset_x + len(grid[0])) for y in range(offset_y, offset_y + len(grid)) if (t:=(x, y)) not in target)
    active = set()
    seen = {}
    order = []

    for i in range(0, 1000000000):
        active = change(active, width, height)

        if target.issubset(active) and not antitarget.intersection(active): 
            ans += len(active)

        if active in seen:
            j, n = seen[active]
            gap = i - j
            ans += (ans - n) * ((1000000000 - i - 1) // gap) + order[j + (1000000000 - i - 1) % gap] - n
            break
            
        seen[(active)] = (i, ans)
        order.append(ans)
        
    print(ans)

part_1()
part_2()
part_3()


