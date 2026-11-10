import pyperclip
import math
from collections import deque

def shadow(grid, x, y, dx = 1, dy = 1):
    s = 0
    e = 0

    while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        if grid[y][x] != ".":
            h = int(grid[y][x])
            if h > s:
                e += 1
                s = h
            s -= 1
        x += dx
        y += dy
    return e

def part_1():
    with open("Day 8/part_1.txt") as f:
        grid = f.read().split("\n")

    upper_left = 0

    for c in grid[0]:
        if c != ".": break
        upper_left += 1


    ans = 0

    for i in range(upper_left, len(grid[0]), 2):
        ans += shadow(grid, i, 0)

    for i in range(1, upper_left + 1):
        ans += shadow(grid, upper_left - i, i)

    print(ans)
    pyperclip.copy(ans)

def part_2():
    with open("Day 8/part_2.txt") as f:
        grid = f.read().split("\n")

    points = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] != "."]

    upper_left = (min(x for x, y in points if y == 0), 0)
    upper_right = (max(x for x, y in points if y == 0), 0)
    lower_left = (min(x for x, y in points if y == len(grid) - 1), len(grid) - 1)
    lower_right = (max(x for x, y in points if y == len(grid) - 1), len(grid) - 1)
    left = (0, next(y for x, y in points if x == 0))
    right = (len(grid[0]) - 1, next(y for x, y in points if x == len(grid[0]) - 1))

    ans = 0
    hex_dirs = ((-1, 0, right, (-1, -1), (-1, 1)), (1, 0, left, (1, 1), (1, -1)), (1, 1, upper_left, (-1, 1), (1, 0)), (-1, -1, lower_right, (1, -1), (-1, 0)), (1, -1, lower_left, (1, 0), (-1, -1)), (-1, 1, upper_right, (-1, 0), (1, 1)))

    sin = math.sin(120)
    cos = math.cos(120)

    for dx, dy, (x, y), *dirs in hex_dirs:
        ans += shadow(grid, x, y, dx, dy)
        for dxx, dyy in dirs:
            xx = x + dxx
            yy = y + dyy
            while 0 <= xx < len(grid[0]) and 0 <= yy < len(grid):
                if grid[yy][xx] != ".": 
                    ans += shadow(grid, xx, yy, dx, dy)
                xx += dxx
                yy += dyy      

    print(ans)
    pyperclip.copy(ans)

def part_3():
    with open("Day 8/part_3.txt") as f:
        grid = f.read().split("\n")

    grid = [[int(c) if c != "." else -1 for c in row] for row in grid]

    points = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] >= 0]

    upper_left = (min(x for x, y in points if y == 0), 0)
    upper_right = (max(x for x, y in points if y == 0), 0)
    lower_left = (min(x for x, y in points if y == len(grid) - 1), len(grid) - 1)
    lower_right = (max(x for x, y in points if y == len(grid) - 1), len(grid) - 1)
    left = (0, next(y for x, y in points if x == 0))
    right = (len(grid[0]) - 1, next(y for x, y in points if x == len(grid[0]) - 1))

    ans = 0
    hex_dirs = (
        (1, 1, upper_left, (-1, 1), (1, 0)), 
        (-1, 1, upper_right, (-1, 0), (1, 1)),
        (-1, 0, right, (-1, -1), (-1, 1)), 
        (-1, -1, lower_right, (1, -1), (-1, 0)), 
        (1, -1, lower_left, (1, 0), (-1, -1)), 
        (1, 0, left, (1, 1), (1, -1)), 
        )

    growing = deque()
    r = 0
    t = 100000

    def shadow(grid, x, y, dx = 1, dy = 1):
        nonlocal t
        s = 0
        e = 0

        while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            h = int(grid[y][x])
            if h >= 0:
                if h > 0 and h > s:
                    e += 1
                    s = h
                    if h == 9:
                        grid[y][x] = 0
                        growing.append((x, y, r))
                        t -= 1
                    else: 
                        grid[y][x] += 1
                s -= 1
            x += dx
            y += dy
        return e

    while True:
        dx, dy, (x, y), *dirs = hex_dirs[r % 6]
        ans += shadow(grid, x, y, dx, dy)
        for dxx, dyy in dirs:
            xx = x + dxx
            yy = y + dyy
            while 0 <= xx < len(grid[0]) and 0 <= yy < len(grid):
                if grid[yy][xx] >= 0: 
                    ans += shadow(grid, xx, yy, dx, dy)
                xx += dxx
                yy += dyy    
        if t <= 0: break
        while growing and growing[0][2] == r - 3:
            x, y, _ = growing.popleft()
            grid[y][x] += 1
        r += 1  

    print(ans, r)
    pyperclip.copy(ans)

part_3()