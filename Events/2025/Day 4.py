import math


def part_1():
    with open("Day 4/part 1.txt", "r") as f:
        gears = f.readlines()

    ans = int(gears[0]) * 2025 // int(gears[-1])

    print(ans)

def part_2():
    with open("Day 4/part 2.txt", "r") as f:
        gears = f.readlines()

    ans = math.ceil(10000000000000 * int(gears[-1]) / int(gears[0]))
    
    print(ans)

def part_3():
    with open("Day 4/part 3.txt", "r") as f:
        gears = f.readlines()

    turns = 100
    gear = int(gears[0])

    for i in range(1, len(gears) - 1):
        a, b = tuple(int(g) for g in gears[i].split("|"))

        turns = turns * gear / a
        gear = b

    ans = int(turns * gear / int(gears[-1]))
    print(ans)

part_1()
part_2()
part_3()