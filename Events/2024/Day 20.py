from re import finditer

def calculate_altitude(time, altitude, max_time): return max_time - time + altitude

def calculate_time(time, altitude, min_altitude): return time + max(0, min_altitude - altitude)


def p1():
    with open("Day 20/p1.txt", "r") as f:
        rows = f.read().split("\n")

    rooms = [[]]
    for row in rows:
        rooms[-1].append(row)
        if row.count("#") > 2: rooms.append([])

    rooms[-1] = rooms[-1][:2]

    nodes = {0: {}}
    id = 1
    previous_nodes = {(rows[0].find("S"), 0): nodes[0]}

    for room in rooms:
        current_nodes = {(r.start(0), - 1): {} for r in finditer(r"[+-\.]" if room != rooms[-1] else r"\+", room[-1])}

        for pos, node in current_nodes.items():
            nodes[id] = node

            match room[-1][pos[0]]:
                case "+": extra = +2
                case ".": extra = 0
                case "-": extra = -1

            for prev_pos, n in previous_nodes.items():
                distance = len(room) - 1 - prev_pos[1] + abs(prev_pos[0] - pos[0])
                n[id] = (distance, -distance + extra)

            id += 1

        previous_nodes = current_nodes


    starting_altitude = 1000
    max_time = 100

    queue = [(0, 0, starting_altitude, calculate_altitude(0, starting_altitude, max_time))]
    history = set()


    while len(queue) > 0:
        cur_id, time, altitude = queue.pop(0)[0:3]

        if cur_id in history: continue
        history.add(cur_id)

        if len(nodes[cur_id]) == 0:
            print(calculate_altitude(time, altitude, max_time))
            break

        for id, stats in nodes[cur_id].items():
            if id not in history: queue.append((id, time + stats[0], altitude + stats[1], calculate_altitude(time + stats[0], altitude + stats[1], max_time)))

        queue.sort(key=lambda t: t[3], reverse=True)  

def p2():
    with open("Day 20/p2.txt", "r") as f:
        rows = f.read().split("\n")

    flags = {}

    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c.isalpha(): flags[c] = (x, y)

    order = ["S", "A", "B", "C", "S"]
    min_altitude = 10000

    queue = [(flags[order[0]], 0, min_altitude, (0, 1), 0)]
    for start_key in range(1, len(order)):
        history = set()

        while len(queue) > 0:
            coords, time, altitude, direction = queue.pop(0)[0:4]

            if coords == flags[order[start_key]]:
                queue.clear()
                queue.append((coords, time, altitude, direction, 0))
                break

            if coords in history: continue
            history.add(coords)


            for dir in [direction, (direction[1], -direction[0]), (-direction[1], direction[0])]:
                next_coords = tuple(coords[i] + dir[i] for i in range(2))

                if next_coords in history: continue

                match rows[next_coords[1]][next_coords[0]]:
                    case "+": cost = 0
                    case "-": cost = -3
                    case "#": continue
                    case _: cost = -2
                    

                queue.append((next_coords, time + 1, altitude + cost, dir, calculate_time(time + 1, altitude + cost + time, min_altitude)))

            queue.sort(key=lambda t: t[4])

    time, altitude = queue[0][1:3]

    print(calculate_time(time, altitude + time, min_altitude))

def p3():
    with open("Day 20/p3.txt", "r") as f:
        rows = f.read().split("\n")
        rows.append(rows[0])

    starting_altitude = 384400

    short_paths = {}

    for start_x, c in enumerate(rows[0]):
        if c == "#": continue
        short_paths[start_x] = {}
        queue = [((start_x, 0), 0, (0, 1), 0, 0, 0)]
        history = set()

        while len(queue) > 0:
            coords, altitude, direction, time = queue.pop(0)[0:4]

            if coords in history: continue
            history.add(coords)

            if coords[1] == len(rows) - 1:
                short_paths[start_x][coords[0]] = altitude + time
            
            time += 1
                

            for dir in [direction, (direction[1], -direction[0]), (-direction[1], direction[0])]:
                next_coords = tuple(coords[i] + dir[i] for i in range(2))
                if next_coords in history: continue
                if (next_coords[1] < 0 or next_coords[1] >= len(rows)): continue

                match rows[next_coords[1] % len(rows)][next_coords[0]]:
                    case "+": cost = 0
                    case "-": cost = -3
                    case "#": continue
                    case _: cost = -2
                    
                queue.append((next_coords, altitude + cost, dir, time, min(altitude + time + cost, altitude + time), altitude + time + cost))

            queue.sort(key=lambda t: t[4], reverse=True)

    queue = [(rows[0].find("S"), starting_altitude, 0, (0, 0))]
    history = {0: {}}

    while len(queue) > 0:
        coords, altitude, loop, prev_coords = queue.pop(0)

        if coords in history[loop]: continue
        history[loop][coords] = (prev_coords, altitude)

        if len(history[loop]) == len(short_paths) and all(c[0] == prev_coords for c in history[loop].values()) and loop > 1: 
            break


        loop += 1
        if loop > 5: continue

        if loop not in history: history[loop] = {}
        for new_coords, cost in short_paths[coords].items():
            if new_coords in history[loop] or altitude + cost < 0: continue
            queue.append((new_coords, altitude + cost, loop, coords))

        queue.sort(key=lambda t: t[1], reverse=True)

    looped_stats = list(history[loop].values())[0]
    
    difference = history[loop - 1][looped_stats[0]][1] - history[loop][looped_stats[0]][1]
    rows.pop()

    loops = loop + looped_stats[1] // difference - 1
    total = (len(rows)) * loops
    furthest = 0

    remaining = looped_stats[1] % difference + difference
    
    queue = [((looped_stats[0], 0), remaining, (0, 1), 0, remaining)]
    history = set()

    while len(queue) > 0:
        coords, altitude, direction, time = queue.pop(0)[0:4]

        if coords in history: continue
        history.add(coords)
        
            
        furthest = max(furthest, coords[1])
        if altitude + time == 0: continue

        time += 1

        for dir in [direction, (direction[1], -direction[0]), (-direction[1], direction[0])]:
            next_coords = tuple(coords[i] + dir[i] for i in range(2))
            if next_coords in history: continue
            if (next_coords[1] < 0): continue

            match rows[next_coords[1] % len(rows)][next_coords[0]]:
                case "+": cost = 0
                case "-": cost = -3
                case "#": continue
                case _: cost = -2

            if altitude + cost + time < 0: continue
            queue.append((next_coords, altitude + cost, dir, time, altitude + time + cost))

        queue.sort(key=lambda t: t[4], reverse=True)

    print(total + furthest)

p1()
p2()
p3()