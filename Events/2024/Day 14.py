from numpy import array

def p1():
    with open("Day 14/p1.txt", "r") as f:
        directions = f.read().split(",")

    height = 0
    highest = 0

    for d in directions:
        if (d[0] not in ["U", "D"]): continue
        height += int(d[1:]) * (1 if (d[0] == "U") else -1)
        highest = max(highest, height)

    print(highest)

def build_tree(path):
    with open(path, "r") as f:
        plans = [line.split(",") for line in f.read().split("\n")]

    segments = set()
    leaves = set()

    for plan in plans:
        pos = array([0, 0, 0])

        for d in plan:
            direction = array([0, 0, 0])
            match d[0]:
                case "U":
                    direction[2] += 1
                case "D":
                    direction[2] -= 1
                case "F":   
                    direction[1] += 1
                case "B":
                    direction[1] -= 1 
                case "L":
                    direction[0] += 1
                case "R":
                    direction[0] -= 1

            for n in range(int(d[1:])):
                pos += direction
                segments.add(tuple(int(n) for n in pos))

        leaves.add(tuple(int(n) for n in pos))

    return segments, leaves


def p2():
    segments = build_tree("Day 14/p2.txt")
    print(len(segments))

def p3():
    segments, leaves = build_tree("Day 14/p3.txt")

    main_branches = set(filter(lambda s: s[0] == 0 and s[1] == 0, segments))
    leaf_distances = []
    adjacent = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]


    for leaf in leaves:
        history = set()
        current = set([leaf])
        next = set()
        branch_distances = {}
        steps = 0

        while len(branch_distances) < len(main_branches) and len(current) > 0:
            
            for pos in current:
                if (pos in main_branches and pos not in branch_distances): branch_distances[pos] = steps
                history.add(pos)

                for dir in adjacent:
                    new_pos = tuple(pos[i] + dir[i] for i in range(3))
                    if (new_pos in segments and new_pos not in history): next.add(new_pos)

            steps += 1
            current = next
            next = set()

        leaf_distances.append(branch_distances)

    minimum = 1e64

    for segment in main_branches:
        minimum = min(sum(leaf[segment] for leaf in leaf_distances), minimum)

    print(minimum)

p3()