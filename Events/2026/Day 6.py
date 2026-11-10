from collections import defaultdict, deque

def part_1():
    with open("Day 6/part_1.txt") as f:
        lines = f.read().split("\n")

    ingredients = defaultdict(list)

    for line in lines:
        a, b = line.split(":")
        ingredients[a] = b.split(",")

    seen = {"NULL"}
    queue = deque(["NULL"])

    while queue:
        ing = queue.popleft()

        for i in ingredients[ing]:
            if i in seen: continue
            queue.append(i)
            seen.add(i)

    ans = len(seen) - 1

    print(ans)

def part_2():
    with open("Day 6/part_2.txt") as f:
        lines = f.read().split("\n")

    ingredients = defaultdict(list)

    for line in lines:
        a, b = line.split(":")
        for i in b.split(","):
            ingredients[i].append(a)

    seen = {"NULL"}
    queue = deque(["NULL"])

    while queue:
        ing = queue.popleft()

        for i in ingredients[ing]:
            if i in seen: continue
            queue.append(i)
            seen.add(i)

    ans = len(seen) - 1

    print(ans)

def part_3():
    with open("Day 6/part_3.txt") as f:
        lines = f.read().split("\n")

    makes = defaultdict(list)
    nulls = [f"NULLv{n}" for n in range(1, 4)]

    for line in lines:
        a, b = line.split(":")
        for i in b.split(","):
            makes[i].append(a)

    nulled = defaultdict(int)

    for v, null in enumerate(nulls):
        seen = {null}
        queue = deque([null])

        while queue:
            ing = queue.popleft()

            for i in makes[ing]:
                if i in seen: continue
                queue.append(i)
                nulled[i] |= 1 << v
                seen.add(i)

    ans = sum(v.bit_count() > 1 for v in nulled.values())

    print(ans)

part_3()