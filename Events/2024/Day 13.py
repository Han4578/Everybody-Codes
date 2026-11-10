def get_ans(path):
    with open(path, "r") as f:
        lines = f.read().split("\n")

    nodes = {}
    end = (0, 0)

    current = []

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c.isnumeric(): nodes[(x, y)] = int(c)
            elif c == "S": 
                current.append(((x, y), 0, 0))
            elif c == "E": 
                end = (x, y)
                nodes[(x, y)] = 0


    adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    history = set()
    lowest = 0

    while len(current) > 0:
        smallest = current.pop(0)
        if (smallest[0] in history): continue
        history.add(smallest[0])

        if (smallest[0] == end):
            lowest = smallest[2]
            current.clear()
            break

        for (dx, dy) in adjacent:
            if (smallest[0][0] + dx, smallest[0][1] + dy) in nodes:
                if (smallest[0][0] + dx, smallest[0][1] + dy) in history: continue
                adjacent_node = nodes[(smallest[0][0] + dx, smallest[0][1] + dy)]
                if adjacent_node > smallest[1]: adjacent_node -= 10

                current.append(((smallest[0][0] + dx, smallest[0][1] + dy), adjacent_node % 10, min(abs(smallest[1] - adjacent_node), (adjacent_node - smallest[1] ) + 10) + 1 + smallest[2]))


        current.sort(key= lambda n: n[2])

    print(lowest)

def p1():
    get_ans("Day 13/p1.txt")

def p2():
    get_ans("Day 13/p2.txt")

def p3():
    get_ans("Day 13/p3.txt")



p1()
p2()
p3()