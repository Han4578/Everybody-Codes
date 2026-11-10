def open_file(path):
    with open(path, "r") as f:
        names = f.readline().split(",")
        f.readline()
        moves = f.readline().split(",")
    return names, moves


def part_1():
    names, moves = open_file("Day 1/part 1.txt")
    i = 0

    for m in moves:
        i = min(max(0, i + int(m[1:]) * (-1 if m[0] == "L" else 1)), len(names) - 1)

    print(names[i])

def part_2():
    names, moves = open_file("Day 1/part 2.txt")
    i = 0

    for m in moves:
        i += int(m[1:]) * (-1 if m[0] == "L" else 1)

    print(names[i % len(names)])

def part_3():
    names, moves = open_file("Day 1/part 3.txt")

    for m in moves:
        i = (int(m[1:]) * (-1 if m[0] == "L" else 1)) % len(names)
        names[0], names[i] = names[i], names[0]
 
    print(names[0])

part_1()
part_2()
part_3()

        