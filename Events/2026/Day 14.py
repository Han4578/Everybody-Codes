from collections import defaultdict, Counter
import heapq
from itertools import combinations

def part_1():
    with open("Day 14/part_1.txt") as f:
        lines = f.read().split("\n")

    grid = [[0] * len(lines[0]) for _ in range(len(lines))]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if x < len(grid[0]) - 1 and lines[y][x] != lines[y][x + 1]: grid[y][x] += 1
            if y < len(grid) - 1 and lines[y][x] != lines[y + 1][x]: grid[y][x] += 1

    ans = (len(grid) + len(grid[0])) * 2 + sum(sum(r) for r in grid)

    print(ans)

def build_graph(file_path):
    with open(file_path) as f:
        lines = f.read().split("\n")

    graph = defaultdict(Counter)

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if x < len(lines[0]) - 1 and lines[y][x] != lines[y][x + 1]: 
                graph[lines[y][x]][lines[y][x + 1]] += 1
                graph[lines[y][x + 1]][lines[y][x]] += 1
            if y < len(lines) - 1 and lines[y][x] != lines[y + 1][x]: 
                graph[lines[y][x]][lines[y + 1][x]] += 1
                graph[lines[y + 1][x]][lines[y][x]] += 1

    for y in range(len(lines)):
        for x in (0, -1):
            graph[lines[y][x]]["FRAME"] += 1
            graph["FRAME"][lines[y][x]] += 1

    for x in range(len(lines[0])):
        for y in (0, -1):
            graph[lines[y][x]]["FRAME"] += 1
            graph["FRAME"][lines[y][x]] += 1

    return graph

def min_bindings(graph):
    queue = [(0, "FRAME")]
    seen = {"FRAME": 0}
    used = {"FRAME"}
    ans = 0

    while queue:
        c, n1 = heapq.heappop(queue)

        if seen[n1] != c: continue

        ans += c
        used.add(n1)

        for n2, c2 in graph[n1].items():
            if n2 not in seen or (seen[n2] > c2 and n2 not in used):
                seen[n2] = c2
                heapq.heappush(queue, (c2, n2))

    return ans

def part_2():
    graph = build_graph("Day 14/part_2.txt")
        
    ans = min_bindings(graph)

    print(ans)

def part_3():
    graph = build_graph("Day 14/part_3.txt")

    ans = sum(sum(c.values()) for c in graph.values())

    for combo in combinations([k for k in graph.keys() if k != "FRAME"], 2):        
        graph2 = {k: graph[k].copy() for k in graph.keys()}

        for p in combo:
            for n in graph[p].keys():
                graph2[n][p] = 0
                graph2[p][n] = 0
                
        ans = min(ans, (min_bindings(graph2)))

    print(ans)

part_1()
part_2()
part_3()