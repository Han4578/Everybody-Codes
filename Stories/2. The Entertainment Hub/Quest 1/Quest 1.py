import pyperclip
import heapq
from collections import deque, defaultdict
import time

def drop_token(grid, token, slot):
    x = slot * 2
    y = 0
    d = 0

    while y < len(grid):
        if grid[y][x] == "*":
            if (token[d] == "L" and x > 0) or x + 1 == len(grid[y]):
                x -= 1
            else: x += 1
            d += 1
        y += 1

    return ((x // 2) + 1) * 2 - (slot + 1)

def part1():
    with open("input 1.txt", "r") as f:
        sections = f.read().split("\n\n")
        grid = sections[0].splitlines()
        tokens = sections[1].splitlines()

    ans = sum(max(0, drop_token(grid, tokens[slot], slot)) for slot in range(len(grid[0]) // 2 + 1))

    print(ans)

def part2():
    with open("input 2.txt", "r") as f:
        sections = f.read().split("\n\n")
        grid = sections[0].splitlines()
        tokens = sections[1].splitlines()

    ans = 0

    for token in tokens:
        max_amount = 0

        for slot in range(len(grid[0]) // 2 + 1):
            max_amount = max(max_amount, drop_token(grid, token, slot))

        ans += max_amount

    print(ans)

def find_min(scores):
    queue = [(0, -1, tuple())]

    while queue:
        score, i, used = heapq.heappop(queue)
        i += 1
        if i == len(scores): return score
        for j, s in enumerate(scores[i]):
            if j in used: continue
            heapq.heappush(queue, (score + s, i, used + (j,)))

def find_max(scores):
    queue = deque([(0, -1, tuple())])
    highest = 0
    seen = defaultdict(int)

    while queue:
        score, i, used = queue.popleft()
        if seen[used] != score: continue
        i += 1
        if i == len(scores): 
            highest = max(highest, score)
            continue
        for j, s in enumerate(scores[i]):
            if j in used: continue
            used2 = tuple(sorted(used + (j,)))
            if seen[used2] >= score + s: continue
            seen[used2] = score + s
            queue.append((score + s, i, used2))

    return highest



def part3():
    with open("input 3.txt", "r") as f:
        sections = f.read().split("\n\n")
        grid = sections[0].splitlines()
        tokens = sections[1].splitlines()

    scores = []

    for token in tokens:
        scores.append([max(0, drop_token(grid, token, slot)) for slot in range(len(grid[0]) // 2 + 1)])

    ans = f"{find_min(scores)} {find_max(scores)}"
    # print(ans)

part1()
part2() 
part3()

from timeit import timeit
print(timeit(part3, number=10) / 10)