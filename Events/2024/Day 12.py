from math import floor

def get_ans(file):
    with open(file, "r") as f:
        input = f.read().split("\n")

    projectiles = {}
    targets = {}
    total = 0

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            match c:
                case ".":
                    continue
                case "T":
                    targets[(x, y)] = 1
                case "H":
                    targets[(x, y)] = 2
                case "=":
                    break
                case _:
                    projectiles[(x, y)] = ord(c) - ord("A") + 1

    while (len(targets) > 0):
        for coords, seg_value in projectiles.items():
            power = 1
            found = False

            while power < len(input[0]) / 2 and not found:
                new_x = coords[0] + power * 2
                new_y = coords[1] - power
                while (new_y < len(input)):
                    if ((new_x, new_y) in targets): 
                        found = True
                        targets[(new_x, new_y)] -= 1
                        if (targets[(new_x, new_y)] <= 0): targets.pop((new_x, new_y))
                        total += power * seg_value
                        break
                    else:
                        new_x += 1
                        new_y += 1
                power += 1

    return total

def p1():
    print(get_ans("Day 12/p1.txt"))

def p2():
    print(get_ans("Day 12/p2.txt"))

def p3():
    with open("Day 12/p3.txt", "r") as f:
        asteroids = [[int(s) for s in line.split(" ")] for line in f.read().split("\n")]

    total = 0

    for original_x, original_y in asteroids:
        lowest_power = original_y * 3

        if (original_x % 2 != 0): 
            original_x -= 1
            original_y -= 1

        time = int(original_x / 2)

        for segment in range(2, -1, -1):
            y = original_y - segment - time
 
            if (y > time): break

            if (y >= time / 2):
                lowest_power = min(y * (segment + 1), lowest_power)
                continue

            starting_power = floor(time / 2)
            starting_height = starting_power * 3 - time #starting_power - (time - starting_power * 2), 

            if ((starting_height - y) % 3 != 0): continue

            lowest_power = min((starting_power - (starting_height - y) / 3) * (segment + 1), lowest_power)
        
        total += int(lowest_power)

    print(total)

p1()
p2()
p3()