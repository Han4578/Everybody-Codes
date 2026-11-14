
def part_1():
    with open("Day 12/part_1.txt") as f:
        grid = f.read().split("\n")

    ans = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "." or (x > 0 and grid[y][x - 1] == "#") or (y > 0 and grid[y - 1][x] == "#"): continue

            w = 1
            h = 1

            for xx in range(x + 1, len(grid[0])):
                if grid[y][xx] == ".": break
                w += 1

            for yy in range(y + 1, len(grid)):
                if grid[yy][x] == ".": break
                h += 1

            ans += min(w, h)

    print(ans)

def part_2():
    with open("Day 12/part_2.txt") as f:
        grid = f.read().split("\n")

    ans = 0
    used = [[False] * len(grid[0]) for _ in range(len(grid))]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "." or used[y][x]: continue

            points = [(x, y)]

            queue = [(x, y)]
            used[y][x] = True

            while queue:
                xx, yy = queue.pop()

                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx = xx + dx
                    ny = yy + dy

                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "." and not used[ny][nx]:
                        used[ny][nx] = True
                        points.append((nx, ny))
                        queue.append((nx, ny))
                        
            temp = min(p[1] for p in points)
            upper = sum(p[1] == temp for p in points)

            temp = max(p[1] for p in points)
            lower = sum(p[1] == temp for p in points)

            temp = min(p[0] for p in points)
            left = sum(p[0] == temp for p in points)

            temp = max(p[0] for p in points)
            right = sum(p[0] == temp for p in points)

            ans += min(min(left, right) + min(upper, lower), max(left, right), max(upper, lower))
                        
    print(ans)

def part_3():
    with open("Day 12/part_3.txt") as f:
        grid = f.read().split("\n")

    ans = 0
    used = [[False] * len(grid[0]) for _ in range(len(grid))]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "." or used[y][x]: continue

            points = [(x, y)]

            queue = [(x, y)]
            used[y][x] = True

            while queue:
                xx, yy = queue.pop()

                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx = xx + dx
                    ny = yy + dy

                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "." and not used[ny][nx]:
                        used[ny][nx] = True
                        points.append((nx, ny))
                        queue.append((nx, ny))
                        
            temp = min(p[1] for p in points)
            upper = sum(p[1] == temp for p in points)

            temp = max(p[1] for p in points)
            lower = sum(p[1] == temp for p in points)

            temp = min(p[0] for p in points)
            left = sum(p[0] == temp for p in points)

            temp = max(p[0] for p in points)
            right = sum(p[0] == temp for p in points)

            if left != right or upper != lower:
                ans += min(min(left, right) + min(upper, lower), max(left, right), max(upper, lower))
            elif upper * left == len(points): ans += min(upper, left)
            else:
                lines = []
                minimum = 0

                for xx in range(x, x + upper):
                    lines.append([0])
                    for yy in range(y, y + left):
                        if grid[yy][xx] == ".": 
                            if grid[yy - 1][xx] != ".": lines[-1].append(0)
                        else: lines[-1][-1] += 1


                h = sum(len(r) > 1 for r in lines)
                w1 = min(r[0] for r in lines if len(r) > 1)
                w2 = min(r[-1] for r in lines if len(r) > 1)
                minimum = sum(len(r) == 1 for r in lines) + min(h, w1) + min(h, w2)
                h = sum(len(r) > 1 for r in lines)

                lines = []
                for yy in range(y, y + left):
                    lines.append([0])
                    for xx in range(x, x + upper):
                        if grid[yy][xx] == ".": 
                            if grid[yy][xx - 1] != ".": lines[-1].append(0)
                        else: lines[-1][-1] += 1

                h = sum(len(r) > 1 for r in lines)
                w1 = min(r[0] for r in lines if len(r) > 1)
                w2 = min(r[-1] for r in lines if len(r) > 1)
                minimum = min(minimum, sum(len(r) == 1 for r in lines) + min(h, w1) + min(h, w2))

                for i, yy in enumerate(range(y, y + left)):
                    if len(lines[i]) <= 2: continue
                    for xx in range(x + w1, x + upper - w2):
                        used[yy][xx] = False

                ans += minimum
    print(ans)

part_3()    

