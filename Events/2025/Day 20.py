from collections import deque

def part_1():
    with open("Day 20/part 1.txt", "r") as f:
        grid = f.read().splitlines()

    width = len(grid[0])
    height = len(grid)
    ans = 0

    for y, row in enumerate(grid):
        down = False

        for x, c in enumerate(row):
            if x >= width - y: break
            if c == ".": continue
            if c == "T":
                if down:
                    if y + 1 < height and grid[y + 1][x] == "T": ans += 1
                if x + 1 < width and grid[y][x + 1] == "T": ans += 1
            down = not down

    print(ans)

def part_2():
    with open("Day 20/part 2.txt", "r") as f:
        line = f.read()
        e = line.index("E")
        s = line.index("S")
        grid = line.splitlines()

    width = len(grid[0])

    start = (s % width - s // width, s // width)
    end = (e % width - e // width, e // width)

    queue = deque([(0, start)])
    seen = {start: 0}
    ans = -1

    def check(x, y, step):
        if grid[y][x] != "#" and ((x, y) not in seen or seen[(x, y)] > step):
            seen[(x, y)] = step
            queue.append((step, (x, y)))

    while queue:
        step, pos = queue.popleft() 
        x, y = pos

        if seen[pos] != step: continue
        if pos == end:
            ans = step
            break
        step += 1

        if sum(pos) % 2 == 0:
            if y > 0: check(x, y - 1, step)
        else: check(x, y + 1, step)

        for dx in (1, -1):
            nx = x + dx
            if y <= nx < width - y: check(nx, y, step)

    print(ans)

def part_3():
    with open("Day 20/part 3.txt", "r") as f:
        line = f.read()
        e = line.index("E")
        s = line.index("S")
        grid = line.splitlines()


    width = len(grid[0])
    height = len(grid)
    grids = [grid]
    start = (s % width - s // width, s // width)
    ends = [(e % width - e // width, e // width)]

    for _ in range(2):
        new_grid = []
        for x in range(0, width, 2):
            row = [grids[-1][height - (x >> 1) - 1][x + height - (x >> 1) - 1]]
            for y in range(height - (x >> 1) - 2, -1, -1):
                for dx in range(1, -1, -1):
                    row.append(grids[-1][y][x + y + dx])
            new_grid.append("." * (x >> 1) + "".join(row) + "." * (x >> 1))
        grids.append(new_grid)
        
        found = False
        for y, row in enumerate(new_grid):
            for x, c in enumerate(row):
                if c == "E":
                    ends.append((x, y))
                    found = True
                    break
            if found: break

    queue = deque([(0, start)])
    seen = {(0, start): 0}
    ans = -1

    def check(x, y, step):
        g = step % 3
        if grids[g][y][x] != "#" and ((g, (x, y)) not in seen or seen[(g, (x, y))] > step):
            seen[(g, (x, y))] = step
            queue.append((step, (x, y)))

    while queue:
        step, pos = queue.popleft() 
        x, y = pos

        if seen[(step % 3, pos)] != step: continue
        if pos == ends[step % 3]:
            ans = step
            break
        step += 1

        check(x, y, step)

        if sum(pos) % 2 == 0:
            if y > 0: check(x, y - 1, step)
        else: check(x, y + 1, step)

        for dx in (1, -1):
            nx = x + dx
            if y <= nx < width - y: check(nx, y, step)

    print(ans)

def bonus():
    with open("Day 20/bonus.txt", "r", encoding="utf-8") as f:
        line = f.read()
        e = line.index("E")
        s = line.index("S")
        grid = line.splitlines()


    width = len(grid[0])
    height = len(grid)
    grids = [grid]

    for _ in range(2):
        new_grid = []
        for x in range(0, width, 2):
            row = [grids[-1][height - (x >> 1) - 1][x + height - (x >> 1) - 1]]
            for y in range(height - (x >> 1) - 2, -1, -1):
                for dx in range(1, -1, -1):
                    row.append(grids[-1][y][x + y + dx])
            new_grid.append("." * (x >> 1) + "".join(row) + "." * (x >> 1))
        grids.append(new_grid)

    with open("Day 20/bonus decoded.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(grids[-1]))

bonus()            

