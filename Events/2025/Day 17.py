import heapq
import bisect

def part_1():
    with open("Day 17/part 1.txt") as f:
        grid = f.read().splitlines()


    volcano = (-1, -1)

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "@":
                volcano = (x, y)
                break

        if volcano[0] >= 0: break

    ans = 0

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if 0 < (x - volcano[0]) ** 2 + (y - volcano[1]) ** 2 <= 100:
                ans += int(c)

    print(ans)

def part_2():
    with open("Day 17/part 2.txt") as f:
        grid = f.read().splitlines()


    volcano = (-1, -1)

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "@":
                volcano = (x, y)
                break

        if volcano[0] >= 0: break

    points = []

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != "@": points.append(((x - volcano[0]) ** 2 + (y - volcano[1]) ** 2, int(c)))

    points.sort()
    r = 1
    ans = -1
    highest = -1

    while True:
        if (n:=sum(points[i][1] for i in range(bisect.bisect_right(points, (r - 1) ** 2, key=lambda p: p[0]), bisect.bisect_right(points, r ** 2, key=lambda p: p[0])))) > highest:
            highest = n
            ans = n * r
        if r ** 2 > points[-1][0]: break
        r += 1


    print(ans)

def move(grid, limit, r2, start, end):
    queue = [(v, i) for i, v in start.items()]
    heapq.heapify(queue)
    seen = start.copy()
    width = len(grid[0])
    height = len(grid)

    while queue:
        c, p = heapq.heappop(queue)

        if seen[p] != c: continue
        if p in end:
            if end[p] == -1:
                end[p] = c
            else:
                end[p] = min(end[p], c)
            if all(v >= 0 for v in end.values()): return end

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = p[0] + dx
            ny = p[1] + dy

            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx][0] > r2:
                t = (nx, ny)
                nc = c + grid[ny][nx][1]
                if nc <= limit and (t not in seen or seen[t] > nc): 
                    heapq.heappush(queue, (nc, t))
                    seen[t] = nc

    return {p: v for p, v in end.items() if v >= 0}






def part_3():
    with open("Day 17/part 3.txt") as f:
        grid = [list(row) for row in f.read().splitlines()]

    volcano = (-1, -1)
    start = (-1, -1)

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            match c:
                case "@":
                    volcano = (x, y)
                    break
                case "S":
                    start = (x, y)
                    break

        if volcano[0] >= 0 and start[0] >= 0: break


    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            grid[y][x] = ((x - volcano[0]) ** 2 + (y - volcano[1]) ** 2, int(c) if c.isdigit() else 0)

    ans = -1
    mid = 0

    while True:
        mid2 = mid ** 2
        limit = (mid + 1) * 30 - 1

        p1 = move(grid, limit, mid2, {start: 0}, {(x, volcano[1]): -1 for x in range(volcano[0]) if grid[volcano[1]][x][0] > mid2})
        if p1:
            p2 = move(grid, limit, mid2, p1, {(volcano[0], y): -1 for y in range(volcano[1] + 1, len(grid)) if grid[y][volcano[0]][0] > mid2})
            if p2:
                p3 = move(grid, limit, mid2, p2, {(x, volcano[1]): -1 for x in range(volcano[0] + 1, len(grid[0])) if grid[volcano[1]][x][0] > mid2})
                if p3:
                    p4 = move(grid, limit, mid2, p3, {start: -1})
                    if p4:
                        ans = mid * p4[start]
                        break        

        mid += 1

    print(ans)

part_1()
part_2()
part_3()