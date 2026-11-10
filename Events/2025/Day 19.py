import heapq
from collections import defaultdict
import math

def part_1():
    with open("Day 19/part 1.txt", "r") as f:
        cols = f.read().splitlines()

    current_height = 0
    current_x = 0
    ans = 0

    for c in cols:
        x, y, h = [int(n) for n in c.split(",")]
        current_height -= x - current_x
        current_x = x

        min_flap = max(0, y - current_height + 1) // 2
        ans += min_flap
        current_height += min_flap << 1

    print(ans)

def part_2():
    with open("Day 19/part 2.txt", "r") as f:
        col_input = f.read().splitlines()

    prev = []
    current = [(0, 1, 1)] # x, min h, max h
    current_x = 0
    cols = defaultdict(list)

    for c in col_input:
        t = tuple(int(n) for n in c.split(","))

        if t[0] != current_x:
            prev = current
            current = []
            current_x = t[0]
    
        for p in prev:
            cols[p].append(t)
        current.append(t)

    queue = [(0, (0, 1, 1), 1, 1)] # flaps, location, min height, max height
    seen = {((0, 1, 1), 1, 1): 0}
    ans = -1

    while queue:
        flaps, col, min_h, max_h = heapq.heappop(queue)

        if seen[(col, min_h, max_h)] != flaps: continue
        if not cols[col]:
            ans = flaps
            break

        for next_col in cols[col]:
            max_reachable = min(next_col[2] + next_col[1], max_h + next_col[0] - col[0])

            if max_reachable <= next_col[1]: continue

            min_reachable = min_h - next_col[0] + col[0]

            min_flap = max(0, math.ceil((next_col[1] - min_reachable + 1) / 2))
            min_reachable += min_flap << 1
            
            t = (next_col, min_reachable, max_reachable)
  
            if t in seen and seen[t] <= flaps + min_flap: continue
            heapq.heappush(queue, (flaps + min_flap, next_col, min_reachable, max_reachable))
            seen[t] = flaps + min_flap

    print(ans)

def part_3():
    with open("Day 19/part 3.txt", "r") as f:
        col_input = f.read().splitlines()

    prev = []
    current = [(0, 1, 1)] # x, min h, max h
    current_x = 0
    cols = defaultdict(list)

    for c in col_input:
        t = tuple(int(n) for n in c.split(","))

        if t[0] != current_x:
            prev = current
            current = []
            current_x = t[0]
    
        for p in prev:
            cols[p].append(t)
        current.append(t)

    queue = [(0, (0, 1, 1), 1, 1)] # flaps, location, min height, max height
    seen = {((0, 1, 1), 1, 1): 0}
    ans = -1

    while queue:
        flaps, col, min_h, max_h = heapq.heappop(queue)

        if seen[(col, min_h, max_h)] != flaps: continue
        if not cols[col]:
            ans = flaps
            break

        for next_col in cols[col]:
            max_reachable = min(next_col[2] + next_col[1], max_h + next_col[0] - col[0])

            if max_reachable <= next_col[1]: continue

            min_reachable = min_h - next_col[0] + col[0]

            min_flap = max(0, math.ceil((next_col[1] - min_reachable + 1) / 2))
            min_reachable += min_flap << 1
            
            t = (next_col, min_reachable, max_reachable)
  
            if t in seen and seen[t] <= flaps + min_flap: continue
            heapq.heappush(queue, (flaps + min_flap, next_col, min_reachable, max_reachable))
            seen[t] = flaps + min_flap

    print(ans)

part_1() # All parts can be solved using part_1() by adding a x != next_x check, since the ans is always the min of the column
part_2()
part_3()