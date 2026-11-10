
def part_1():
    with open("Day 6/part 1.txt", "r") as f:
        line = f.readline()

    ment = 0
    ans = 0

    for c in line:
        if c == "A": ment += 1
        elif c == "a": ans += ment

    print(ans)

def part_2():
    with open("Day 6/part 2.txt", "r") as f:
        line = f.readline()

    ment = {
        "A": 0,
        "B": 0,
        "C": 0,
    }
    ans = 0

    for c in line:
        if c.isupper(): ment[c] += 1
        else: ans += ment[c.upper()]

    print(ans)

def part_3():
    with open("Day 6/part 3.txt", "r") as f:
        line = f.readline() * 1000


    ment = {
        "A": 0,
        "B": 0,
        "C": 0,
    }
    ans = 0
    limit = 1000

    print(line.count("a") + line.count("b") + line.count("c"))
    return
    
    for i in range(limit):
        if line[i] <= "Z":
            ment[line[i]] += 1

    left = -limit
    right = limit

    for i, c in enumerate(line):

        if right < len(line) and line[right] <= "Z":
            ment[line[right]] += 1

        if c >= "a": ans += ment[c.upper()]
        
        if left >= 0 and line[left] <= "Z":
            ment[line[left]] -= 1

        right += 1
        left += 1

    print(ans)

import time

t = time.time()
part_3()
print(time.time() - t)