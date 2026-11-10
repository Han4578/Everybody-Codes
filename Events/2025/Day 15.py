import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def has_wall(a, b, walls):
    return any( #vertical
        w[0] <= a[0] <= w[2] and a[1] <= w[1] <= b[1] #horizontal
        if w[1] == w[3] else 
        w[0] == a[0] and not (w[3] < a[1] or w[1] > b[1]) #vertical
        for w in walls
        ) if a[0] == b[0] else any(#horizontal
        w[1] == a[1] and not (w[2] < a[0] or w[0] > b[0]) #horizontal
        if w[1] == w[3] else
        w[1] <= a[1] <= w[3] and a[0] <= w[0] <= b[0] #vertical
        for w in walls
    )

def can_connect(p1, p2, walls):
    e = (
        min(p1[0], p2[0]),
        min(p1[1], p2[1]),
        max(p1[0], p2[0]),
        max(p1[1], p2[1]),
    )
    return not ((
            has_wall((e[0], e[1]), (e[2], e[1]), walls) or has_wall((e[2], e[1]), (e[2], e[3]), walls)
        ) or (
            has_wall((e[0], e[3]), (e[2], e[3]), walls) or has_wall((e[0], e[1]), (e[0], e[3]), walls)
        )
    )

def part_1():
    with open("Day 15/part 1.txt", "r") as f:
        instructions = f.read().split(",")

    direction = (0, -1)
    goal = (0, 0)
    seen = {}

    for i in instructions:
        direction = (direction[1], -direction[0]) if i[0] == "L" else (-direction[1], direction[0])
        
        for _ in range(int(i[1:])):
            goal = (goal[0] + direction[0], goal[1] + direction[1])
            seen[goal] = 0

    del seen[goal]
    heap = [(manhattan((0, 0), goal), 0, 0, 0)]
    seen[(0, 0)] = heap[0][0]
    ans = -1

    while heap:
        h, c, x, y = heapq.heappop(heap)

        if seen[(x, y)] != h: continue
        if (x, y) == goal: 
            ans = c
            break

        c += 1

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            t = (nx, ny)
            new_h = manhattan((nx, ny), goal) + c

            if (t not in seen or seen[t] > new_h):
                seen[t] = new_h
                heapq.heappush(heap, (new_h, c, nx, ny))

    print(ans)

def part_2():
    with open("Day 15/part 2.txt", "r") as f:
        instructions = f.read().split(",")

    direction = (0, -1)
    goal = (0, 0)
    seen = {}

    for i in instructions:
        direction = (direction[1], -direction[0]) if i[0] == "L" else (-direction[1], direction[0])
        
        for _ in range(int(i[1:])):
            goal = (goal[0] + direction[0], goal[1] + direction[1])
            seen[goal] = 0

    del seen[goal]
    heap = [(manhattan((0, 0), goal), 0, 0, 0)]
    seen[(0, 0)] = heap[0][0]
    ans = -1

    while heap:
        h, c, x, y = heapq.heappop(heap)

        if seen[(x, y)] != h: continue
        if (x, y) == goal: 
            ans = c
            break

        c += 1

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            t = (nx, ny)
            new_h = manhattan((nx, ny), goal) + c

            if (t not in seen or seen[t] > new_h):
                seen[t] = new_h
                heapq.heappush(heap, (new_h, c, nx, ny))

    print(ans)

def part_3():
    with open("Day 15/part 3.txt", "r") as f:
        instructions = f.read().split(",")

    direction = (0, -1)
    goal = (0, 0)
    points = [(0, 0), (0, 0)]
    walls = []

    for i in instructions:
        new_direction = (direction[1], -direction[0]) if i[0] == "L" else (-direction[1], direction[0])

        if i[0] == "L":#move left back right front
            points[-2] = (points[-2][0] - direction[0], points[-2][1] - direction[1])
            points[-1] = (points[-1][0] + direction[0], points[-1][1] + direction[1])
        else: #move right back left front
            points[-2] = (points[-2][0] + direction[0], points[-2][1] + direction[1])
            points[-1] = (points[-1][0] - direction[0], points[-1][1] - direction[1])

        direction = new_direction
        
        m = int(i[1:])
        new_goal = (goal[0] + direction[0] * m, goal[1] + direction[1] * m)
        walls.append(
            (
                min(goal[0], new_goal[0]),
                min(goal[1], new_goal[1]),
                max(goal[0], new_goal[0]),
                max(goal[1], new_goal[1])
            )
        )
        goal = new_goal

        points.extend(
            (
                (
                    goal[0] + direction[1],#left
                    goal[1] - direction[0]
                ),
                (
                    goal[0] - direction[1],#right
                    goal[1] + direction[0]
                )
            )
        )

    heap = []
    seen = {}
    ans = -1

    for i in range(2):
        heapq.heappush(heap, (1, points[i]))
        seen[points[i]] = 1

    while heap:
        c, p = heapq.heappop(heap)

        if seen[p] != c: continue

        if p == points[-1] or p == points[-2]:
            ans = c + 1
            break

        for p2 in points:
            if p == p2: continue
            d = manhattan(p, p2) + c
            if (p2 not in seen or d < seen[p2]) and can_connect(p, p2, walls):
                seen[p2] = d
                heapq.heappush(heap, (d, p2))

    print(ans)

part_1()
part_2()
part_3()