from collections import deque


def get_within(seen, current, boundary):
    adjacent = ((1, 0), (0, 1), (-1, 0), (0, -1))
    scanned = set()
    within = set()

    for dx, dy in adjacent:
        s = (current[0] + dx, current[1] + dy)
        if s in scanned or s in seen: continue
        queue = deque([s])
        scanning = set([s])
        edge = False

        while queue and not edge:
            x, y = queue.popleft()
            for ddx, ddy in adjacent:
                s = (x + ddx, y + ddy)
                if s in scanning or s in seen: continue
                if s[0] < boundary[0] or s[0] > boundary[1] or s[1] < boundary[2] or s[1] > boundary[3] or s in scanned: 
                    scanned.update(scanning)
                    edge = True
                    break

                queue.append(s)
                scanning.add(s)

        if not edge:
            within.update(scanning)
            scanned.update(scanning)

    return within


def part_1():
    with open("part 1.txt", "r") as f:
        grid = f.readlines()

        start = None
        end = None

        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                match c:
                    case "@":
                        start = (x, y)
                    case "#":
                        end = (x, y)
                    case ".":
                        continue

                if start != None and end != None: break
            if start != None and end != None: break

    ans = 0
    seen = set()
    current = start

    d = (0, -1)

    while True:
        ans += 1

        seen.add(current)

        while True:
            next = (current[0] + d[0], current[1] + d[1])
            d = (-d[1], d[0])

            if next not in seen: break

        if next == end: break

        current = next

    print(ans)

def part_2():

    with open("part 2.txt", "r") as f:
        grid = f.readlines()

        start = None
        end = None

        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                match c:
                    case "@":
                        start = (x, y)
                    case "#":
                        end = (x, y)
                    case ".":
                        continue

                if start != None and end != None: break
            if start != None and end != None: break

    boundary = (
        min(start[0], end[0]),
        max(start[0], end[0]),
        min(start[1], end[1]),
        max(start[1], end[1]),
        )
    
    ans = 0
    seen = {start, end}
    current = start

    d = (0, -1)

    target = {(end[0] + dx, end[1] + dy) for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1))}

    while not target.issubset(seen):
        ans += 1

        while True:
            next = (current[0] + d[0], current[1] + d[1])
            d = (-d[1], d[0])

            if next not in seen: break

        current = next
        seen.add(current)

        boundary = (
            min(boundary[0], current[0]),
            max(boundary[1], current[0]),
            min(boundary[2], current[1]),
            max(boundary[3], current[1]),
            )
        
        seen.update(get_within(seen, current, boundary))


    print(ans)

def part_3():
    adjacent = ((0, -1), (1, 0), (0, 1), (-1, 0))

    with open("part 3.txt", "r") as f:
        grid = f.readlines()

        seen = set()

        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                match c:
                    case "@":
                        current = (x, y)
                    case "#":
                        seen.add((x, y))
                    case ".":
                        continue
    boundary = (
        min(s[0] for s in seen),
        max(s[0] for s in seen),
        min(s[1] for s in seen),
        max(s[1] for s in seen),
        )
    
    target = set()

    for s in seen:
        w = get_within(seen, s, boundary)

        for dx, dy in adjacent:
            t = (s[0] + dx, s[1] + dy)

            if t not in w: target.add(t)

    ans = 0
    seen.add(current)

    d = 0

    while not target.issubset(seen):
        ans += 1

        while True:
            dd = adjacent[(d % 12) // 3]
            next = (current[0] + dd[0], current[1] + dd[1])
            d += 1

            if next not in seen: break

        current = next
        seen.add(current)

        boundary = (
            min(boundary[0], current[0]),
            max(boundary[1], current[0]),
            min(boundary[2], current[1]),
            max(boundary[3], current[1]),
            )
        
        seen.update(get_within(seen, current, boundary))
        
        

    print(ans)



part_3()