def create_columns(path):
    columns = []

    with open(path, "r") as f:
        rows = [line.split(" ") for line in f.read().split("\n")]
        for i in range(len(rows[0])): columns.append([])

        for row in rows:
            for i, n in enumerate(row):
                columns[i].append(int(n))

    return columns

def shout(columns, i):
    clapper = columns[i % len(columns)].pop(0)
    next_column = columns[(i + 1) % len(columns)]

    count = (clapper - 1) % (len(next_column) * 2) + 1

    if count <= len(next_column): next_column.insert(count - 1, clapper)
    elif count == len(next_column) + 1: next_column.append(clapper)
    else: next_column.insert(len(next_column) - count + 1, clapper)


    total = ""

    for col in columns:
        total += str(col[0])

    return total


def p1():

    columns = create_columns("Day 5/p1.txt")


    for i in range(10):
        total = shout(columns, i)

    print(total)

def p2():
    columns = create_columns("Day 5/p2.txt")

    rounds = 0
    count = {}

    while True:
        num = int(shout(columns, rounds))

        count[num] = (count[num] + 1) if num in count else 1
        rounds += 1
        if count[num] >= 2024: break

    print(rounds * num)

def p3():
    columns = create_columns("Day 5/p3.txt")

    rounds = 0
    highest = 0
    history = []
    count = {}
    found = False

    while not found:
        num = int(shout(columns, rounds))
        highest = max(highest, num)

        history.append(num)
        if num in count: count[num].append(rounds)
        else: count[num] = [rounds]

        if (len(count[num]) > 1):
            for i in reversed(count[num]):
                if i == rounds or rounds - i > i: continue

                if all(history[i - n] == history[rounds - n] for n in range(rounds - i)):
                    found = True
                    break
                
        rounds += 1

    print(highest)

p1()
p2()
p3()