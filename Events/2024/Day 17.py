from math import prod

def manhattan(s1, s2): return sum(abs(s1[i] - s2[i]) for i in range(2))

def dijkstra(path, max_dist = 1e10):
    stars = []

    with open(path, "r") as f:
        for y, row in enumerate(f.read().split("\n")):
            for x, c in enumerate(row):
                if c == "*": stars.append((x, y))

    sizes = []

    while len(stars) > 0:

        queue = [stars[0]]
        distances = {stars[0]: 0}
        size = 0
        count = 0

        while len(queue) > 0:
            star = queue.pop(0)
            stars.remove(star)
            size += distances[star]
            count += 1

            for s in stars:
                dist = manhattan(s, star)
                if dist < max_dist: 
                    if s not in distances: 
                        queue.append(s)
                        distances[s] = dist
                    else: distances[s] = min(distances[s], dist)

            queue.sort(key=lambda s: distances[s])
        
        sizes.append(size + count)

    return prod(sorted(sizes, reverse=True)[0:3])


def p1():
    print(dijkstra("Day 17/p1.txt"))

def p2():
    print(dijkstra("Day 17/p2.txt"))

def p3():
    print(dijkstra("Day 17/p3.txt", 6))

p1()
p2()
p3()





