import re

def part_1():
    with open("part 1.txt", "r") as f:
        lines = f.readlines()

    ans = 0

    for line in lines:
        num, r, g, b = re.search(r"(\d+):([rR]+) ([gG]+) ([bB]+)", line).groups()

        r_n = int("".join("1" if s == "R" else "0" for s in r), 2)
        g_n = int("".join("1" if s == "G" else "0" for s in g), 2)
        b_n = int("".join("1" if s == "B" else "0" for s in b), 2)

        if g_n > r_n and g_n > b_n:
            ans += int(num)

    print(ans)

def part_2():
    with open("part 2.txt", "r") as f:
        lines = f.readlines()

    ans = 0
    
    highest_shine = 0
    darkest = 255

    for line in lines:
        groups = re.search(r"(\d+):([rR]+) ([gG]+) ([bB]+) ([sS]+)", line).groups()

        nums = [int("".join("1" if s.isupper() else "0" for s in g), 2) for g in groups[1:]]

        if nums[-1] > highest_shine:
            highest_shine = nums[-1]
            darkest = sum(nums[:-1])
            ans = int(groups[0])
        elif nums[-1] == highest_shine:
            d = sum(nums[:-1])
            if d < darkest:
                darkest = d
                ans = int(groups[0])
        
    print(ans)

def part_3():
    with open("part 3.txt", "r") as f:
        lines = f.readlines()

    scale_groups = [[0, 0] for _ in range(6)]

    for line in lines:
        groups = re.search(r"(\d+):([rR]+) ([gG]+) ([bB]+) ([sS]+)", line).groups()

        nums = [int("".join("1" if s.isupper() else "0" for s in g), 2) for g in groups[1:]]

        dom = max(nums[:-1])

        if nums[:-1].count(dom) > 1: continue

        shine = 0

        if 30 < nums[-1] < 33:
            continue
        elif nums[-1] >= 33:
            shine = 1

        scale_groups[nums[:-1].index(dom) * 2 + shine][0] += 1
        scale_groups[nums[:-1].index(dom) * 2 + shine][1] += int(groups[0])    

    print(scale_groups)
    ans = max(scale_groups)[1]

    print(ans)

part_3()