from collections import defaultdict
import heapq

def part_1():
    with open("Day 15/part_1.txt") as f:
            grid = f.read().split("\n")

    def solve(x, y, gap):
        heights = list(range(len(grid) // 2 - 1, 1, -2))
        upper = [0] * len(heights)
        lower = [0] * len(heights)
        w = len(heights) * 2 + (len(heights) * 2 - 1) * gap

        for dx in range(w):
            if dx % (gap + 1) == 0:
                i = dx // (gap + 1)
                if i >= len(heights): i = len(heights) - 1 - (i - len(heights))
                for dy in range(1, heights[i] + 1):
                    if grid[y - dy][x + dx] == "@": upper[i] += 1
                    if grid[y + dy][x + dx] == "@": lower[i] += 1
                for j, h in enumerate(heights):
                    if h <= heights[i]: continue
                    if grid[y - h][x + dx] == "@": upper[j] += 1
                    if grid[y + h][x + dx] == "@": lower[j] += 1
            else:
                for i, h in enumerate(heights):
                    if grid[y - h][x + dx] == "@": upper[i] += 1
                    if grid[y + h][x + dx] == "@": lower[i] += 1

        cur = 0
        x = 0

        for i, h in enumerate(heights):
            if upper[i] > 0 and lower[i] > 0:
                cur += abs(x - ((gap + 1) * (i if x < w // 2 else len(heights) * 2 - 1 - i)))
                cur += (h * 2 + (h - 1) * gap + h - 1) * 2
            elif upper[i] > 0 or lower[i] > 0:
                cur += abs(x - ((gap + 1) * (i if x < w // 2 else len(heights) * 2 - 1 - i)))
                cur += h * 3 + (h - 1) * gap - 1
                x = ((gap + 1) * (i if x > w // 2 else len(heights) * 2 - 1 - i))

        cur += w - x + 1
        return cur                

    x = 1
    H = (len(grid) // 2 - 1) // 2
    gap = 1
    ans = 1
    
    while x < len(grid[0]) - 1:
        ans += solve(x, len(grid) // 2, gap)
        x += H * 2 + (H * 2 - 1) * gap + 1
        gap += 1
        while grid[len(grid) // 2 - 1][x] == "#":
            if grid[len(grid) // 2][x] == "E": 
                break
            x += 1
            ans += 1

    print(ans)

def trace_arches(x, y, gap, graph, grid):
    heights = list(range(len(grid) // 2 - 1, 1, -2))
    upper = [0] * len(heights)
    lower = [0] * len(heights)
    w = len(heights) * 2 + (len(heights) * 2 - 1) * gap

    for dx in range(w):
        if dx % (gap + 1) == 0:
            i = dx // (gap + 1)
            if i >= len(heights): i = len(heights) - 1 - (i - len(heights))
            for dy in range(1, heights[i] + 1):
                if grid[y - dy][x + dx] == "@": upper[i] += 1
                if grid[y + dy][x + dx] == "@": lower[i] += 1
            for j, h in enumerate(heights):
                if h <= heights[i]: continue
                if grid[y - h][x + dx] == "@": upper[j] += 1
                if grid[y + h][x + dx] == "@": lower[j] += 1
        else:
            for i, h in enumerate(heights):
                if grid[y - h][x + dx] == "@": upper[i] += 1
                if grid[y + h][x + dx] == "@": lower[i] += 1

    possible = []

    for i, h in enumerate(heights):
        half_cycle = max(upper[i], lower[i])
        possible.append((((h * 2 + (h - 1) * gap - 1) * 2), half_cycle))
        possible.append(((h * 3 + (h - 1) * gap - 1) * 2, upper[i] + lower[i]))

        a = x + i * (gap + 1)
        b = x + i * (gap + 1) + h + (h - 1) * gap - 1

        for c in {upper[i], lower[i]}:
            if c == 0: continue
            graph[a].append((b, h * 3 + (h - 1) * gap - 1, c))
            graph[b].append((a, h * 3 + (h - 1) * gap - 1, c))

        if upper[i] > 0 and lower[i] > 0:
            graph[a].append((a, (h * 3 + (h - 1) * gap - 1) * 2, upper[i] + lower[i]))
            graph[b].append((b, (h * 3 + (h - 1) * gap - 1) * 2, upper[i] + lower[i]))

    return possible

def build_graph(grid):
    x = 1
    H = (len(grid) // 2 - 1) // 2
    gap = 1
    possible = []
    graph = defaultdict(list)
    
    while x < len(grid[0]) - 1:
        w = H * 2 + (H * 2 - 1) * gap
        for dx in range(0, w, gap + 1):
            graph[x + dx].append((x + dx + gap + 1, gap + 1, 0))
            if dx > 0: graph[x + dx].append((x + dx - gap - 1, gap + 1, 0))

        possible.extend(trace_arches(x, len(grid) // 2, gap, graph, grid))
        x += w - 1
        new_x = x + 2
        gap += 1
        while grid[len(grid) // 2 - 1][new_x] == "#":
            if grid[len(grid) // 2][new_x] == "E": 
                del graph[x][0]
                break
            new_x += 1
        if new_x < len(grid[0]) - 1: graph[x][0] = (new_x, new_x - x, 0)
        x = new_x

    return possible, graph

def solve(graph, target, end_x, a = 0, b = 0):
    queue = [(1, 1, 0, target, 1, False)]
    ans = 1e15
    lowest = defaultdict(lambda: 1e15)
    lowest[(1, target, 0, False)] = 1

    row_to_index = {r: i for i, r in enumerate(graph.keys())}

    while queue:
        t, cur, prev, collected, seen, vertical = heapq.heappop(queue)

        if t >= ans: break

        if lowest[(cur, collected, prev, vertical)] != t: continue


        if collected <= 0:
            if collected == 0 and ((1 << a | 1 << b) & seen) != 0:
                ans = min(ans, t + end_x - cur)
            continue

        for next, t2, c2 in graph[cur]:
            v = c2 > 0
            if (vertical == v and next == prev and next != cur): continue
            if (vertical and v and next != cur): continue
            if lowest[(next, collected - c2, cur, v)] > t + t2:
                lowest[(next, collected - c2, cur, v)] = t + t2
                heapq.heappush(queue, (t + t2, next, cur, collected - c2, seen | 1 << row_to_index[next], v))

    return ans

def part_2():
    with open("Day 15/part_2.txt") as f:
        grid = f.read().split("\n")

    _, graph = build_graph(grid)

    ans = solve(graph, 2026, len(grid[0]) - 1)

    print(ans)

def part_3():
    with open("Day 15/part_3.txt") as f:
        grid = f.read().split("\n")    

    possible, graph = build_graph(grid)
    H = (len(grid) // 2 - 1) // 2
    t = 202620261000

    i, total, time = min([(i, ((t // per_cycle) * per_cycle) if per_cycle > 0 else 1e15, (((t) // per_cycle) * cycle) if per_cycle > 0 else 1e15) for i, (cycle, per_cycle) in enumerate(possible)], key=lambda k: k[2])

    a = i // (2 * H) * H * 2 + (i // 2) % H
    b = a + (H - a % (H * 2)) * 2 - 1

    ans = solve(graph, 202620262026 - total, len(grid[0]) - 1, a, b) + time    

    print(ans)

part_1()
part_2()
part_3()