def part_1():
    with open("Day 11/part 1.txt", "r") as f:
        cols= [int(n) for n in f.read().splitlines()]

    first_phase = True

    for _ in range(10):
        if first_phase:
            changed = False
            for i in range(1, len(cols)):
                if cols[i] < cols[i - 1]:
                    changed = True
                    cols[i] += 1
                    cols[i - 1] -= 1
            if not changed:
                first_phase = False

        if not first_phase:
            for i in range(1, len(cols)):
                if cols[i] > cols[i - 1]:
                    cols[i] -= 1
                    cols[i - 1] += 1

    ans = sum(i * n for i, n in enumerate(cols, start=1))

    print(ans)

def part_2():
    with open("Day 11/part 2.txt", "r") as f:
        cols= [int(n) for n in f.read().splitlines()]

    rounds = 0

    while True:
        changed = False
        for i in range(1, len(cols)):
            if cols[i] < cols[i - 1]:
                changed = True
                cols[i] += 1
                cols[i - 1] -= 1
        if not changed:
            break

        rounds += 1

    s = sum(cols)

    avg = s // len(cols)
            
    rounds += sum(max(0, n - avg) for n in cols)

    print(rounds)


def part_3():
    with open("Day 11/part 3.txt", "r") as f:
        cols= [int(n) for n in f.read().splitlines()]

    s = sum(cols)

    avg = s // len(cols)
            
    ans = sum(max(0, n - avg) for n in cols)
    print(ans)

part_1()
part_2()
part_3()
