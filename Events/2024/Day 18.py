def bfs(path):
    paths = set()
    trees = set()

    with open(path, "r") as f:
        rows = f.read().split("\n")
        for y, row in enumerate(rows):
            for x, c in enumerate(row):
                if c=="#": continue
                paths.add((x, y))
                if c == "P": trees.add((x, y))

    start = [filter(lambda p: p[0] == 0 or p[1] == 0 or p[0] == len(rows[0]) - 1 or p[1] == len(rows) - 1, paths)][0]

    current = set(start)
    steps = -1
    while len(current) > 0 and len(trees) > 0:
        next = set()
        steps += 1
        for path in current:
            if path not in paths: continue
            paths.remove(path)
            if path in trees: 
                trees.remove(path)

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_step = (path[0] + dx, path[1] + dy)
                if next_step in paths: next.add(next_step)

        current = next

    return steps

def p1():
    print(bfs("Day 18/p1.txt"))

def p2():
    print(bfs("Day 18/p2.txt"))

def p3():
    paths = set()
    trees = set()

    with open("Day 18/p3.txt", "r") as f:
        rows = f.read().split("\n")
        for y, row in enumerate(rows):
            for x, c in enumerate(row):
                if c=="#": continue
                paths.add((x, y))
                if c == "P": trees.add((x, y))

    start = list(enumerate(trees))

    current = set(start)
    steps = -1
    history = {}
    lowest_cost = 1e32

    while len(current) > 0:
        next = set()
        steps += 1
        for id, path in current:
            if path not in history: history[path] = {}
            if id in history[path]: continue
            history[path][id] = steps

            if len(history[path]) == len(trees) and path not in trees:
                lowest_cost = min(lowest_cost, sum(history[path].values()))

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_step = (path[0] + dx, path[1] + dy)
                if next_step in paths: next.add((id, next_step))

        current = next

    print(lowest_cost)

p3()