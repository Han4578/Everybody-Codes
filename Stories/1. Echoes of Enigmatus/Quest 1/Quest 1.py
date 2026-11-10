import re
from collections import deque

def p1():
    with open("part 1.txt", "r") as f:
        params = [[int(n) for n in re.findall(r"\d+", line)] for line in f.read().splitlines()]

    print(max(sum(eni(param[i], param[i + 3], param[-1]) for i in range(3)) for param in params))

def p2():
    with open("part 2.txt", "r") as f:
        params = [[int(n) for n in re.findall(r"\d+", line)] for line in f.read().splitlines()]

    print(max(sum(eni2(param[i], param[i + 3], param[-1]) for i in range(3)) for param in params))

def p3():
    with open("part 3.txt", "r") as f:
        params = [[int(n) for n in re.findall(r"\d+", line)] for line in f.read().splitlines()]

    print(max(sum(eni3(param[i], param[i + 3], param[-1]) for i in range(3)) for param in params))

def eni(n, exp, mod):
    s = ""
    cur = 1

    for _ in range(exp):
        cur = cur * n % mod
        s = str(cur) + s

    return int(s) 

def eni2(n, exp, mod):
    s = ""
    cur = 1
    nn = n

    if exp > 5:
        exp -= 5
        while exp > 0:
            if (exp & 1) == 1: cur = cur * nn % mod
            nn = nn * nn % mod
            exp >>= 1

    for _ in range(5):
        cur = cur * n % mod
        s = str(cur) + s

    return int(s)

def eni3(n, exp, mod):
    n %= mod
    cur = n
    loop = 1
    loop_total = 0
    seen = {}

    while cur not in seen:
        seen[cur] = (loop, loop_total)
        loop_total += cur
        cur = cur * n % mod
        loop += 1

    loop -= seen[cur][0]
    exp -= seen[cur][0] - 1
    loop_total -= seen[cur][1]
    total = loop_total * (exp // loop) + seen[cur][1]

    for _ in range(exp % loop):
        total += cur
        cur = cur * n % mod

    return total



p3()



