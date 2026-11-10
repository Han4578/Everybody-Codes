from math import isqrt

def part_1():
    with open("Day 1/part 1.txt", "r") as f:
        nums = [int(n) for n in f.read().split(",")]

    ans = 0

    for n in nums:
        q = isqrt(n)

        if q * q == n: continue

        ans += (q + 1) ** 2 - n

    print(ans)

def part_2():
    with open("Day 1/part 2.txt", "r") as f:
        nums = [int(n) for n in f.read().split(",")]

    ans = 0

    for n in nums:
        m = max(2, (n + 4) // 4)
        if m > 2 and m * 4 - 4 == n: continue
        ans += (m + 1) * 4 - 4 - n

    print(ans)

def part_3():
    with open("Day 1/part 3.txt", "r") as f:
        nums = [int(n) for n in f.read().split(",")]

    ans = 0

    for n in nums:
        q = isqrt(n + 1)
        if q % 2 == 1 and q ** 2 - 1 == n: continue
        q += 1 if q % 2 == 0 else 2
        ans += q * q - 1 - n

    print(ans)


part_3()