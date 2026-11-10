from collections import deque

def turn(turns, lines):
    i = 0
    ans = 1
    found = False
    target = (turns % sum((b - a + 1 for a, b in lines), start=1))
    if target == 0: return 1

    for j in range(0, len(lines), 2):
        a, b = lines[j]
        gap = b - a + 1

        if i + gap < target:
            i += gap
            continue

        ans = a + target - i - 1
        found = True
        break

    if not found:
        for j in range(len(lines) - (1 if len(lines) % 2 == 0 else 2), -1, -2):
            a, b = lines[j]
            gap = b - a + 1

            if i + gap < target:
                i += gap
                continue

            ans = b - (target - i - 1)
            break

    return ans

def part_1():
    with open("Day 13/part 1.txt", "r") as f:
        lines = [int(n) for n in f.read().splitlines()]

    wheel = deque([1])
    left = True

    for n in lines:
        if left:
            wheel.append(n)
        else:
            wheel.appendleft(n)
        left = not left

    ans = wheel[(2025 + len(lines) // 2) % len(wheel)]

    print(ans)

def part_2():
    with open("Day 13/part 2.txt", "r") as f:
        lines = [tuple(int(n) for n in line.split("-"))for line in f.read().splitlines()]

    ans = turn(20252025, lines)
    print(ans)

def part_3():
    with open("Day 13/part 3.txt", "r") as f:
        lines = [tuple(int(n) for n in line.split("-"))for line in f.read().splitlines()]

    ans = turn(202520252025, lines)
    print(ans)

part_1()
part_2()
part_3()


