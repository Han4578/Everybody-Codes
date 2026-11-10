
def get_beetles(ball, cache, stamps, depth = 0, minimum = 1e32):
    if ball in cache: return cache[ball]
    if depth > minimum: return minimum  

    for stamp in stamps:
        if stamp > ball: continue
        minimum = min(minimum, 1 + get_beetles(ball - stamp, cache, stamps, depth + 1, minimum))
        if minimum <= 2: break

    cache[ball] = minimum
    return minimum  
 
def p1():
    stamps = [10, 5, 3, 1]

    with open("Day 9/p1.txt", "r") as f:
        balls = [int(n) for n in f.read().split("\n")]

    total = 0
    cache = {s: 1 for s in stamps}

    for ball in balls:
        total += get_beetles(ball, cache, stamps)

    print(total)


def p2():
    with open("Day 9/p2.txt", "r") as f:
        balls = [int(n) for n in f.read().split("\n")]

    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    stamps.reverse()

    cache = {s: 1 for s in stamps}

    total = 0
    for ball in balls:
        total += get_beetles(ball, cache, stamps)

    print(total)

def p3():
    with open("Day 9/p3.txt", "r") as f:
        balls = [int(n) for n in f.read().split("\n")]

    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    stamps.reverse()

    cache = {s: 1 for s in stamps}

    total = 0
    for ball in balls:
        min_beetle = 1e32
        offset = 0

        if ball % 2 != 0: 
            offset += 1
            ball += 1 

        midpoint = int(ball / 2)

        for n in range(51 - offset):
            min_beetle = min(min_beetle, get_beetles(midpoint + n, cache, stamps) + get_beetles(midpoint - n - offset, cache, stamps))

        total += min_beetle

    print(total)

p3() 
