import pyperclip
from collections import deque

SQUARE_MASK = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if dx | dy != 0]

def to_land(grid, min_condition = 5, min_type = 1, becomes = 2, starting = []):
    added = [[False] * len(grid[0]) for _ in range(len(grid))]
    added[len(grid) // 2][len(grid[0]) // 2] = True

    for x, y in starting: added[y][x] = True

    queue = deque(starting)

    cannot = None

    while queue:
        x, y = queue.popleft()

        if cannot == (x, y): break

        condition = 0
        surround = []

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == dy == 0: continue
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)): continue

                if not added[ny][nx]: surround.append((nx, ny))
                if grid[ny][nx] >= min_type: condition += 1

        if condition >= min_condition or grid[y][x] == becomes:
            grid[y][x] = becomes
            cannot = None

            for nx, ny in surround:
                queue.append((nx, ny))
                cannot = None
                added[ny][nx] = True
                
        else: 
            queue.append((x, y))
            if cannot == None: cannot = (x, y)

def to_sand(grid):
    lands = deque()
    added = [[False] * len(grid[0]) for _ in range(len(grid))]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 2: continue
            surround = []
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == dy == 0: continue
                    nx = x + dx
                    ny = y + dy
                    if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)): 
                        grid[y][x] = 3
                        continue

                    if grid[ny][nx] < 2:
                        grid[y][x] = 3
                    else: 
                        surround.append((nx, ny))

            if grid[y][x] == 3:
                for nx, ny in surround:
                    if not added[ny][nx]:
                        lands.append((nx, ny))
                        added[ny][nx] = True

    to_land(grid, min_type=3, becomes=3, starting=[(x, y) for x, y in lands if grid[y][x] != 3])

def convo(grid, from_type, to_type, surround_type, mask, minimum):
    changed = []
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != from_type: continue

            surround = 0

            for dx, dy in mask:
                nx = x + dx
                ny = y + dy
                if (grid[ny][nx] if (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)) else 0) in surround_type: 
                    surround += 1

            if surround >= minimum:
                changed.append((x, y))

    for x, y in changed:
        grid[y][x] = to_type

    return len(changed) > 0

            

def part_1():
    with open("Day 5/part_1.txt") as f:
        grid = [[int(c) for c in line] for line in f.read().split("\n")]

    grid[len(grid) // 2][len(grid[0]) // 2] = 2

    to_land(grid, starting=[(len(grid[0]) // 2, len(grid) // 2)])

    print("\n".join("".join("#" if n == 2 else"." for n in row) for row in grid))

    ans = sum(n == 2 for row in grid for n in row)

    print(ans)
    pyperclip.copy(ans)

def part_2():
    with open("Day 5/part_2.txt") as f:
        grid = [[int(c) for c in line] for line in f.read().split("\n")]

    grid[len(grid) // 2][len(grid[0]) // 2] = 2

    to_land(grid, starting=[(len(grid[0]) // 2, len(grid) // 2)])
    to_sand(grid)

    print("\n".join("".join("#" if n == 3 else"." for n in row) for row in grid))

    ans = sum(n == 3 for row in grid for n in row)

    print(ans)
    pyperclip.copy(ans)

def part_3():
    with open("Day 5/part_3.txt") as f:
        grid = [[int(c) for c in line] for line in f.read().split("\n")]

    grid[len(grid) // 2][len(grid[0]) // 2] = 2

    to_land(grid, starting=[(len(grid[0]) // 2, len(grid) // 2)])
    to_sand(grid)

    convo(grid, 2, 4, (2, 4), [(dx, dy) for dy in range(-2, 3) for dx in range(-2, 3) if abs(dx) + abs(dy) != 4 and dx | dy != 0], 20)

    for _ in range(2):
        convo(grid, 2, 4, [4], SQUARE_MASK, 4)
        convo(grid, 4, 2, [3], SQUARE_MASK, 1)

    # print("\n".join("".join("#" if n == 4 else"." for n in row) for row in grid))
        

    ans = sum(n == 4 for row in grid for n in row)

    print(ans)
    pyperclip.copy(ans)
    

part_3()
    
