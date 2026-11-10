from re import findall
from pyperclip import copy


def p1():
    with open("part 1.txt", "r") as f:
        snails = f.read().splitlines()

    total = 0

    for snail in snails:
        x, y = (int(c) - 1 for c in findall(r"\d+", snail))
        width = x + y + 1
        total += (1 + ((x + 100) % width)) + (((y - 100) % width) + 1) * 100

    print(total)
    copy(total)

def p2():
    days = align_snails("part 2.txt")
    print(days)
    copy(days)
    

def p3():
    days = align_snails("part 3.txt")
    print(days)
    copy(days)

def align_snails(file_path):
    with open(file_path, "r") as f:
        snails = f.read().splitlines()

    remainder = 0
    mod = 0

    for snail in snails:
        x, y = (int(c) - 1 for c in findall(r"\d+", snail))
        mod2 = x + y + 1
        if mod == 0:
            mod = mod2
            remainder = y
            continue

        y = (y - remainder) * find_inverse(mod, mod2) % mod2
        remainder += y * mod
        mod *= mod2
        
    return remainder

def find_inverse(n, mod):
    return gcd(mod, n)[1] % mod

def gcd(a, b):
    if a % b == 1:
        return (1, -(a // b))
    
    c, d = gcd(b, a % b)
    return (d, -(a // b) * d + c)

print(find_inverse(9, 10))