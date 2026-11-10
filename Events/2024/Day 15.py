def find_herb_distances(start, paths, herbs, visited_herbs):
    current = set([start])
    next = set()
    history = set()
    steps = 0
    adjacent = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited_herbs[start] = {}
    herb_distances = visited_herbs[start]
    collected = 0

    while len(current) > 0 and collected < len(herbs):
        for pos in current:
            history.add(pos)

            if pos in herbs and herbs[pos] != herbs[start] and pos != start:
                if herbs[pos] not in herb_distances: herb_distances[herbs[pos]] = {}
                herb_distances[herbs[pos]][pos] = steps
                collected += 1

            for dir in adjacent:
                new_pos = tuple(pos[i] + dir[i] for i in range(2))
                if (new_pos in paths and new_pos not in history): next.add(new_pos)

        steps += 1
        current = next.copy()
        next.clear()

    for type in herb_distances.values():
        for pos in type.keys():
            if (pos not in visited_herbs): find_herb_distances(pos, paths, herbs, visited_herbs)

def dijkstra(herb_distances, start, herbs, total_herbs):
    current = [(start, 0, set())]

    history = {}

    while len(current) > 0:
        pos, steps, picked = current.pop(0)

        tpicked = tuple(picked)
        if (pos not in history): history[pos] = {}
        if (tpicked in history[pos] and history[pos][tpicked] <= steps): continue

        history[pos][tpicked] = steps
        
        if (herbs[pos] == -1 and steps > 0):
            return steps

        for herb, pos_steps in herb_distances[pos].items():
            if herb in picked: continue
            if (herb != -1 or len(picked) == total_herbs):
                new_picked = set(picked)
                new_picked.add(herb)
                for pos, step in pos_steps.items():
                    current.append((pos, steps + step, new_picked))

        current.sort(key=lambda h: h[1])

def explore_tower(x_start, x_end, start, rows):
    paths = set()
    herbs = {}
    types = set()
    visited_herbs = {}
    start = tuple(int(n) for n in start)

    for y in range(len(rows)):
        for x in range(int(x_start), int(x_end + 1)):
            match rows[y][x]:
                case "#": pass
                case "~": pass
                case ".":
                    paths.add((x, y))
                case _:
                    paths.add((x, y))
                    herbs[(x, y)] = ord(rows[y][x])
                    types.add(rows[y][x])

    herbs[start] = -1
    find_herb_distances(start, paths, herbs, visited_herbs)
    dist =  dijkstra(visited_herbs, start, herbs, len(types))
    return dist

def p1():
    with open("Day 15/p1.txt", "r") as f:
        rows = f.read().split("\n")

    start = (rows[0].find("."), 0)

    paths = set()
    herbs = set()

    for y in range(len(rows)):
        for x in range(len(rows[0])):
            match rows[y][x]:
                case ".":
                    paths.add((x, y))
                case "H":
                    paths.add((x, y))
                    herbs.add((x, y))


    current = set([start])
    next = set()
    history = set()
    adjacent = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    steps = 0

    while len(current) > 0:
        for pos in current:
            history.add(pos)

            if (pos in herbs):
                print(steps * 2)
                next.clear()
                break

            for dir in adjacent:
                new_pos = tuple(pos[i] + dir[i] for i in range(2))
                if (new_pos in paths and new_pos not in history): next.add(new_pos)

        current = next
        next = set()
        steps += 1

def p2():
    with open("Day 15/p2.txt", "r") as f:
        rows = f.read().split("\n")

    start = (rows[0].find("."), 0)

    print(explore_tower(0, len(rows[0]) - 1, start, rows))
    

def p3():
    with open("Day 15/p3.txt", "r") as f:
        rows = f.read().split("\n")

    rows[-2] = rows[-2][0:85] + "#" + rows[-2][86:169] + "#" + rows[-2][170:]
    total = 0
    line = len(rows[0]) / 3

    total += explore_tower(0, line, (line - 1, len(rows) - 2), rows) + 4 #moving between towers
    total += explore_tower(line + 1, line * 2, (rows[0].find("."), 0), rows)
    total += explore_tower(line * 2, len(rows[0]) - 1, (line * 2, len(rows) - 2), rows) + 4 #moving between towers

    print(total)

p1()
p2()
p3()