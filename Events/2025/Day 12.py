from collections import deque

def ignite(start, grid, ignited = set()):
    seen = ignited.union(start)
    queue = deque(start)
    width = len(grid[0])
    height = len(grid)

    while queue:
        x, y = queue.popleft()
        n = grid[y][x]

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] <= n and (t:=(nx, ny)) not in seen:
                seen.add(t)
                queue.append(t)

    return seen.difference(ignited)

def ignite_this(grid, remaining_bombs, ignited = set()):
    if remaining_bombs == 0: return 0

    chosen = set()

    remaining = set(t for x in range(len(grid[0])) for y in range(len(grid)) if (t:=(x, y)) not in ignited)

    while remaining:
        t = remaining.pop()
        if_ignited = ignite((t,), grid, ignited)

        chosen = max(chosen, if_ignited, key=len)
        remaining.difference_update(if_ignited)

    ans = len(chosen) + ignite_this(grid, remaining_bombs - 1, ignited.union(chosen))

    return ans

def part_1():
    with open("Day 12/part 1.txt", "r") as f:
        grid = [[int(c) for c in line] for line in f.read().splitlines()]

    ans = len(ignite(((0, 0),), grid))

    print(ans)


def part_2():
    with open("Day 12/part 2.txt", "r") as f:
        grid = [[int(c) for c in line] for line in f.read().splitlines()]

    ans = len(ignite(((0, 0), (len(grid[0]) - 1, len(grid) - 1)), grid))

    print(ans)

def part_3():
    with open("Day 12/part 3.txt", "r") as f:
        grid = [[int(c) for c in line] for line in f.read().splitlines()]

    ans = ignite_this(grid, 3)

    print(ans)
    

import timeit
# part_1()
# part_2()
print(timeit.timeit(part_3, number=1))

    
    