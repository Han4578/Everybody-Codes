import re


def part_1():
    with open("Day 2/part_1.txt") as f:
        groups = f.read().split("\n")

    ans = 0

    for g in groups:
        count = [0] * 5

        for s in g.split(" "):
            count[int(s[0 if s[1] == ">" else 2]) - 1] += 1

        ans += int("".join(str(i + 1) for i, _ in sorted(enumerate(count), key=lambda k: k[1], reverse=True)))

    print(ans)

def part_2():
    with open("Day 2/part_2.txt") as f:
        groups = f.read().split("\n")

    ans = 0

    for g in groups:
        n = max(int(s) for s in re.findall(r"\d+", g))
        count = [0] * n
        first = [0] * n
        rules = set()

        for s in g.split(" "):
            first[int(s[0 if s[1] == ">" else 2]) - 1] += 1
            rules.add(s if s[1] == ">" else s[2] + ">" + s[0])
            count[int(s[0]) - 1] += 1
            count[int(s[2]) - 1] += 1

        a, b = [i for i, v in enumerate(count, start=1) if v != n - 1]

        for i in range(1, n + 1):
            if i == a or i == b: continue
            if f"{a}>{i}" in rules and f"{i}>{b}" in rules: 
                first[a - 1] += 1
                break
            if f"{b}>{i}" in rules and f"{i}>{a}" in rules: 
                first[b - 1] += 1
                break

        ans += int("".join(str(i + 1) for i, _ in sorted(enumerate(first), key=lambda k: k[1], reverse=True)))

    print(ans)

def part_3():
    with open("Day 2/part_3.txt") as f:
        groups = f.read().split("\n")

    ans = 0

    for g in groups:
        n = max(int(s) for s in re.findall(r"\d+", g))
        first = [0] * n
        rules = set()

        for s in g.split(" "):
            first[int(s[0 if s[1] == ">" else 2]) - 1] += 1
            rules.add(s if s[1] == ">" else s[2] + ">" + s[0])

        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if f"{a}>{b}" in rules or f"{b}>{a}" in rules: continue
                for i in range(1, n + 1):
                    if i == a or i == b: continue
                    if f"{a}>{i}" in rules and f"{i}>{b}" in rules: 
                        first[a - 1] += 1
                        rules.add(f"{a}>{b}")
                        break
                    if f"{b}>{i}" in rules and f"{i}>{a}" in rules: 
                        first[b - 1] += 1
                        rules.add(f"{b}>{a}")
                        break

        ans += int("".join(str(i + 1) for i, _ in sorted(enumerate(first), key=lambda k: k[1], reverse=True)))

    print(ans)

part_3() 