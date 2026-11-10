def get_total(path):
    with open(path, "r") as f:
        nails = [int(s) for s in f.read().split("\n")]

    total = 0
    lowest_height = 1e32
    for i, n in enumerate(nails):
        if (n < lowest_height):
            total += i * (lowest_height - n)
            lowest_height = n
        else: total += n - lowest_height

    return int(total)

def p1():
    print(get_total("Day 4/p1.txt"))

def p2():
    print(get_total("Day 4/p2.txt"))

def p3():
    with open("Day 4/p3.txt", "r") as f:
        nails = [int(s) for s in f.read().split("\n")]

    nails.sort()

    total = 0

    median = round((nails[round(len(nails) / 2)] + nails[round(len(nails) / 2)]) / 2) if len(nails) % 2 == 0 else nails[round((len(nails) + 1) / 2)]

    for n in nails:
        total += abs(median - n)

    print(total)
    


p1()
p2()
p3()