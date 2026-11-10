
def part_1():
    with open("Day 16/part 1.txt", "r") as f:
        blocks = f.read().split(",")

    ans = sum(90 // int(b) for b in blocks)

    print(ans)

def part_2():
    with open("Day 16/part 2.txt", "r") as f:
        blocks = f.read().split(",")

    wall = [0] * len(blocks)
    ans = 1

    for i, b in enumerate(blocks):
        b = int(b)
        if wall[i] < b:
            ans *= i + 1
            for j in range(i * 2 + 1, len(blocks), i + 1):
                wall[j] += 1

    print(ans)

def part_3():
    with open("Day 16/part 3.txt", "r") as f:
        chunk = f.read().split(",")

    wall = [0] * len(chunk)
    ans = 1
    spell = []

    for i, b in enumerate(chunk):
        b = int(b)
        if wall[i] < b:
            ans *= i + 1
            spell.append(i + 1)
            for j in range(i * 2 + 1, len(chunk), i + 1):
                wall[j] += 1

    blocks = 202520252025000
    low = 0
    high = blocks
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if sum(mid // s for s in spell) <= blocks:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1


    print(ans)

part_1()
part_2()
part_3()