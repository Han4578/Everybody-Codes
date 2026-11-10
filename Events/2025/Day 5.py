import math
import re

def open_file(path):
    with open(path, "r") as f:
        return f.readlines()
    
def get_bone(sword):
    bone = [None, sword[0], None]

    slots = [0, 2]

    for i in range(1, len(sword)):
        n = sword[i]

        for j, s in enumerate(slots):
            match s % 3:
                case 0:
                    if n < bone[s + 1]:
                        bone[s] = n
                        del slots[j]
                        break
                case 2:
                    if n > bone[s - 1]:
                        bone[s] = n
                        del slots[j]
                        break
        else:
            bone.extend((None, n, None))
            slots.extend((len(bone) - 3, len(bone) - 1))

    return bone
    
def part_1():
    line = open_file("Day 5/part 1.txt")[0]
    nums = [int(n) for n in line[line.index(":") + 1:].split(",")]

    bone = get_bone(nums)
    ans = "".join(str(bone[i]) for i in range(1, len(bone), 3))

    print(ans)

def part_2():
    lines = open_file("Day 5/part 2.txt")
    numlist = [[int(n) for n in line[line.index(":") + 1:].split(",")] for line in lines]

    low = math.inf
    high = -math.inf

    for nums in numlist:
        bone = get_bone(nums)
        q = int("".join(str(bone[i]) for i in range(1, len(bone), 3)))
        low = min(low, q)
        high = max(high, q)


    ans = high - low
    print(ans)

def part_3():
    lines = open_file("Day 5/part 3.txt")
    numlist = [[int(n) for n in re.split(r"[:,]", line)] for line in lines]
    
    ranking = []

    for nums in numlist:
        id = nums.pop(0)
        bone = get_bone(nums)
        ranking.append((
            int("".join(str(bone[i]) for i in range(1, len(bone), 3))),
            tuple(int("".join(str(n) for n in bone[i:i + 3] if n != None)) for i in range(0, len(bone), 3)),
            id
            ))
        
    ranking.sort(reverse=True)

    ans = sum(i * r[2] for i, r in enumerate(ranking, start=1))
    print(ans)


part_1()
part_2()
part_3()


