from collections import defaultdict

def part_1():
    with open("Day 10/part_1.txt") as f:
        lines = f.read().split("\n")

    grid = set()
    ghosts = []

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            match c:
                case "#": continue
                case ".": grid.add((x, y))
                case _:
                    grid.add((x, y))
                    match c:
                        case ">": ghosts.append([[x, y], [1, 0]])
                        case "v": ghosts.append([[x, y], [0, 1]])
                        case "<": ghosts.append([[x, y], [-1, 0]])
                        case "^": ghosts.append([[x, y], [0, -1]])

    ans = 0

    for _ in range(10):
        for pos, dir in ghosts:
            x, y = pos
            dx, dy = dir
            if (x + dx, y + dy) not in grid: 
                dir[0] = -dy
                dir[1] = dx
                ans += 1
            else:
                pos[0] += dx
                pos[1] += dy

        poses = defaultdict(list)

        for g in ghosts: poses[tuple(g[0])].append(g[1])

        for dirs in poses.values():
            if len(dirs) > 1:
                for p in dirs:
                    p[0] *= -1
                    p[1] *= -1
                ans += len(dirs)

    print(ans)

def collide(input_file, limit):
    with open(input_file) as f:
        lines = f.read().split("\n")

    grid = set()
    ghosts = []
    seen = {}

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            match c:
                case "#": continue
                case ".": grid.add((x, y))
                case _:
                    grid.add((x, y))
                    match c:
                        case ">": ghosts.append([[x, y], [1, 0], limit])
                        case "v": ghosts.append([[x, y], [0, 1], limit])
                        case "<": ghosts.append([[x, y], [-1, 0], limit])
                        case "^": ghosts.append([[x, y], [0, -1], limit])

    ans = 0
    all_ghosts = ghosts.copy()
    cur = len(ghosts)
    prev = (limit,) * len(ghosts)

    while True:
        ans += 1
        for g in ghosts:
            pos, dir, _ = g
            x, y = pos
            dx, dy = dir
            if (x + dx, y + dy) not in grid: 
                dir[0] = -dy
                dir[1] = dx
                g[2] -= 1
            else:
                pos[0] += dx
                pos[1] += dy

        poses = defaultdict(list)

        for g in ghosts: 
            if g[2] > 0: poses[tuple(g[0])].append(g)

        for dirs in poses.values():
            if len(dirs) > 1:
                for g in dirs:
                    g[1][0] *= -1
                    g[1][1] *= -1
                    g[2] -= 1

        k = tuple((*g[0], *g[1]) for g in all_ghosts)
        if any(g[2] == 0 for g in ghosts): seen = {}

        if k in seen:
            gap = ans - seen[k][0]
            diff = [a - b[2] for a, b in zip(seen[k][1], all_ghosts)]
            m = min((g[2] // d for g, d in zip(all_ghosts, diff) if g[2] > 0 and d > 0), default=0)

            for g, d in zip(all_ghosts, diff):
                if g[2] > 0:
                    g[2] -= d * m
            ans += gap * m
        l = tuple(g[2] for g in all_ghosts)

        if l != prev:
            seen[k] = (ans, l)
            prev = l
            
        if any(g[2] == 0 for g in ghosts): 
            seen = {}
            ghosts = [g for g in ghosts if g[2] > 0]
            if not ghosts: break
            
    print(ans)

def part_2():
    collide("Day 10/part_2.txt", 10000)

def part_3():
    collide("Day 10/part_3.txt", 1000000000000)

part_3()

