from pyperclip import copy
from bisect import bisect_left

def part_1():
    with open("part 1.txt", "r") as f:
        lines = f.read().splitlines()

    ans = 0

    for line in lines:
        seen = {0}
        cur = 0

        for c in line.split(","):
            n = int(c)

            if cur - n < 0 or cur - n in seen:
                cur += n
            else:
                cur -= n

            seen.add(cur)
        ans += cur

    return ans

def part_2():
    with open("part 2.txt", "r") as f:
        lines = f.read().splitlines()

    ans = 0

    for line in lines:
        seen = {0}
        cur = 0

        for c in line.split(","):
            n = int(c)

            if cur - n < 0 or cur - n in seen:
                cur += n
                while cur in seen: cur += 1
            else:
                cur -= n

            seen.add(cur)
        ans += cur

    return ans

def part_3():
    with open("part 3.txt", "r") as f:
        lines = f.read().splitlines()

    ans = 0

    for line in lines:
        top = []
        bottom = []
        cur = 0
        side = bottom

        for c in line.split(","):
            n = int(c)

            if cur - n <= 0 or any(a <= cur - n <= b <= cur or cur - n <= a <= cur <= b for a, b in side):
                limit = 1e6
                jump = cur + n
                for a, b in side:
                    if a <= cur <= b: limit = min(limit, b - 1)
                    if cur < a <= jump <= b: jump = b + 1
                    if limit < jump: break
                else: 
                    side.insert(bisect_left(side, jump, key=lambda k: k[1]), (cur, jump))
                    cur = jump
                    side = top if side == bottom else bottom    
            else:
                side.insert(bisect_left(side, cur, key=lambda k: k[1]), (cur - n, cur))
                cur -= n
                side = top if side == bottom else bottom

        # print(cur, top, bottom)

        ans += cur

    return ans

ans = part_3()

print(ans)
copy(ans)