import re

def part_1():
    with open("Day 18/part_1.txt") as f:
        lines = f.read().split("\n")

    heights = sorted(tuple(int(n) for n in re.findall(r"\d+", p)) for p in lines)
    tip = max(h[1] for h in heights)

    ans = (heights[-1][0] - heights[0][0] + 1) * tip
    cur = 0

    for i in range(len(heights)):
        if heights[i][1] == tip: break
        cur = max(cur, heights[i][1])
        ans -= (tip - cur) * (heights[i + 1][0] - heights[i][0])

    cur = 0
    for i in range(len(heights) - 1, -1, -1):
        if heights[i][1] == tip: break
        cur = max(cur, heights[i][1])
        ans -= (tip - cur) * (heights[i][0] - heights[i - 1][0])

    print(ans)

def fill(input_path):
    with open(input_path) as f:
        lines = f.read().split("\n")

    heights = sorted(tuple(int(n) for n in re.findall(r"\d+", p)) for p in lines)
    tip = max(h[1] for h in heights)

    ans = (heights[-1][0] + heights[-1][2] - heights[0][0]) * tip
    cur = 0

    for i in range(len(heights)):
        if heights[i][1] == tip: break
        cur = max(cur, heights[i][1])
        ans -= (tip - cur) * (heights[i + 1][0] - heights[i][0])
    cur = 0
    for i in range(len(heights) - 1, -1, -1):
        if heights[i][1] == tip: break
        cur = max(cur, heights[i][1])
        ans -= (tip - cur) * (heights[i][0] + heights[i][2] - heights[i - 1][0] - heights[i - 1][2])

    return ans

def part_2():
    ans = fill("Day 18/part_2.txt")

    print(ans)

def part_3():
    ans = fill("Day 18/part_3.txt")

    print(ans)

part_3()