from math import sin, cos

def rotate(paths, x, y, angle):
    rotated = {}
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0: continue
            adjacent = (x + dx, y + dy)
            new_pos = (x + round(dx * cos(angle) - dy * sin(angle)), y + round(dx * sin(angle) + dy * cos(angle)))
            rotated[new_pos] = paths.pop(adjacent)

    paths |= rotated

def get_ans(path, n, is_extra = False):
    with open(path, "r", encoding="utf-8") as f:
        rows = f.read().split("\n")

    paths = {}
    numbers = {}

    for y, row in enumerate(reversed(rows[2:])):
        for x, c in enumerate(row):
            paths[(x, y)] = (x, y)
            if c.isnumeric() or c in [">", "<"] or (is_extra and c != "."): numbers[(x, y)] = c

    keys = rows[0]
    key_i = 0

    for y in range(len(rows[2:]) - 2, 0, -1):
        for x in range(1, len(rows[2]) - 1):
            angle = 45 * (1 if keys[key_i % len(keys)] == "L" else -1)
            key_i += 1
            rotate(paths, x, y, angle)

    paths = {v: k for k, v in paths.items()}

    final_pos = {}

    for pos, c in numbers.items():
        loops = 0
        current = pos
        while pos != current or loops == 0:
            current = paths[current]
            loops += 1

        for i in range(n % loops): pos = paths[pos]
        final_pos[pos] = c

    if is_extra: return final_pos
    
    start_pos = next(filter(lambda p: final_pos[p] == ">", final_pos))
    end_pos = next(filter(lambda p: final_pos[p] == "<", final_pos))
    final = ""

    for x in range(start_pos[0] + 1, end_pos[0]): 
        final += final_pos[(x, start_pos[1])]

    return final

def p1():
    print(get_ans("Day 19/p1.txt", 1))

def p2():
    print(get_ans("Day 19/p2.txt", 100))

def p3():
    print(get_ans("Day 19/p3.txt", 1048576000), True)

def extra():
    final_pos = get_ans("Day 19/extra.txt", 1024, True)

    width = max(final_pos.keys(), key=lambda k: k[0])[0] + 1
    height = max(final_pos.keys(), key=lambda k: k[1])[1] + 1

    content = ""

    for y in range(height, -1, -1):
        for x in range(width):
            content += " " if (x, y) not in final_pos else final_pos[(x, y)]
        content += "\n"

    with open("Day 19/extra decoded.txt", "w", encoding="utf-8") as f:
        f.write(content)    
        print("Result saved")

# p1()
# p2()
# p3()
extra()