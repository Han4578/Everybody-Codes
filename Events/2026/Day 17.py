from collections import deque, defaultdict

def part_1():
    with open("Day 17/part_1.txt") as f:
        grid = f.read().split("\n")

    queue = deque([(0, (0, 0))])
    seen = [[False] * len(grid[0]) for _ in range(len(grid))]

    while queue:
        c, (x, y) = queue.popleft()

        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            print(c)
            break

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == "#" and not seen[ny][nx]:
                seen[ny][nx] = True
                queue.append((c + 1, (nx, ny)))

def part_2():
    with open("Day 17/part_2.txt") as f:
        grid = f.read().split("\n")

    queue = deque([(0, (0, 0))])
    seen = [[False] * len(grid[0]) for _ in range(len(grid))]
    seen[0][0] = True
    ans = 0

    while queue:
        c, (x, y) = queue.popleft()

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == "#":
                if not seen[ny][nx]:
                    seen[ny][nx] = True
                    queue.append((c + 1, (nx, ny)))
            else:
                ans += 1

    print(ans)

def part_3():
    with open("Day 17/part_3.txt") as f:
        grid = f.read().split("\n")

    queue = deque([(0, (0, 0))])
    seen = [[False] * len(grid[0]) for _ in range(len(grid))]
    seen[0][0] = True
    ans = 0
    chain = defaultdict(list)

    grid_to_edge = {
        (1, 0): (1, 1, 1, 0),
        (0, 1): (1, 1, 0, 1),
        (-1, 0): (0, 0, 0, 1),
        (0, -1): (0, 0, 1, 0)
    }

    while queue:
        c, (x, y) = queue.popleft()

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == "#":
                if not seen[ny][nx]:
                    seen[ny][nx] = True
                    queue.append((c + 1, (nx, ny)))
            else:
                a = (x + grid_to_edge[(dx, dy)][0], y + grid_to_edge[(dx, dy)][1])
                b = (x + grid_to_edge[(dx, dy)][2], y + grid_to_edge[(dx, dy)][3])

                chain[a].append(b)
                chain[b].append(a)

    end = (len(grid[0]), len(grid))
    ans = len(chain)
    print(chain[(11, 6)], end)

    for cur in ((0, 1), (1, 0)):
        prev = (0, 0)
        side = (1, 1)
        a = 1
        while cur != end:
            dx = cur[0] - prev[0]
            dy = cur[1] - prev[1]
            if side in chain[cur]:
                prev, cur, side = cur, side, (side[0] - dx, side[1] - dy)
            elif (cur[0] + dx, cur[1] + dy) in chain[cur]:
                prev, cur, side = cur, (cur[0] + dx, cur[1] + dy), (side[0] + dx, side[1] + dy)
            else:
                ddx = cur[0] - side[0]
                ddy = cur[1] - side[1]
                prev, cur, side = cur, (cur[0] + ddx, cur[1] + ddy), (side[0] + dx + ddx * 2, side[1] + dy + ddy * 2)

            a += 1
        ans = min(ans, a)

    print(ans)


part_3()