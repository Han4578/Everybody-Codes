from pyperclip import copy
import re
import math

def part_1():
    with open("part 1.txt", "r") as f:
        w, h, h_off, v_off = [c for c in re.findall(r"\d+", f.read())]
        w = int(w) + 1
        h = int(h) + 1

    grid = [[0] * w for _ in range(h)]

    for y in range(h):
        o = h_off[y % len(h_off)]

        for x in range(int(o), w, 2):
            if y > 0: grid[y - 1][x] += 1
            grid[y][x] += 1

    for x in range(w):
        o = v_off[x % len(v_off)]

        for y in range(int(o), h, 2):
            if x > 0: grid[y][x - 1] += 1
            grid[y][x] += 1

    return sum(n == 4 for row in grid for n in row)

def part_2():
    with open("part 2.txt", "r") as f:
        w, h, h_off, v_off = [c for c in re.findall(r"\d+", f.read())]
        w = int(w) + 1
        h = int(h) + 1

    grid = [[0] * w for _ in range(h)]
    color = [[False] * w for _ in range(h)]

    for y in range(h):
        o = int(h_off[y % len(h_off)])

        for x in range(o, w, 2):
            if y > 0: grid[y - 1][x] += 1
            grid[y][x] += 1

        
        if y > 0: color[y][0] = color[y - 1][0] ^ (o == 0)

    for x in range(w):
        o = int(v_off[x % len(v_off)])

        for y in range(h):
            if y % 2 == o:
                if x > 0: grid[y][x - 1] += 1
                grid[y][x] += 1
                if x > 0: color[y][x] = not color[y][x - 1]
            elif x > 0: color[y][x] = color[y][x - 1]

    count = [0, 0]

    for y in range(h):
        for x in range(w):
            if grid[y][x] == 4:
                count[int(color[y][x])] += 1

    return max(count)        

def part_3():
    with open("part 3.txt", "r") as f:
        w, h, h_off, v_off = [c for c in re.findall(r"\d+", f.read())]
        w = int(w)
        h = int(h)

        if len(v_off) > len(h_off):
            h, w = w, h
            h_off, v_off = v_off, h_off

    squares = [[0, 0] for _ in range(4)]
    color = [False, False]
    count = [0, 0]

    h_off += h_off

    h_mul = h // len(h_off)
    h_r = h % len(h_off)
    h_off += h_off[0]

    for y in range(1, len(h_off)):
        o = int(h_off[y % len(h_off)]) 
        if o == int(h_off[(y - 1) % len(h_off)]):
            squares[((y - 1) % 2) + o * 2][int(color[o])] += h_mul + int(h_r >= y)

        color[o] = not color[o]

    if v_off[1] == "0":
        for i in (2, 3): squares[i].reverse()

    v_off += v_off
    w_mul = w // len(v_off)
    w_r = w % len(v_off)
    v_off += v_off[0]

    if v_off[0] == v_off[1]:
        a = squares[int(v_off[0])][0]
        b = squares[int(v_off[0])][1]
        if a > 0: count[0] += a * (w_mul + int(w_r >= 1))
        if b > 0: count[1] += b * (w_mul + int(w_r >= 1))

    for x in range(2, len(v_off)):
        o = v_off[x % len(v_off)] 

        if v_off[(x - 1) % len(v_off)] == o:
            a = squares[2 + int(o)][0]
            b = squares[2 + int(o)][1]
            if a > 0: count[0] += a * (w_mul + int(w_r >= x))
            if b > 0: count[1] += b * (w_mul + int(w_r >= x))
        else:
            for i in (0, 1): squares[i].reverse()

        squares[:2], squares[2:] = squares[2:], squares[:2]


    return max(count)

ans = part_3()
print(ans)
copy(ans)
