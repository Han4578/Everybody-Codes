from collections import deque

def open_file(path):
    with open(path, "r") as f:
        return list(int(n) for n in f.read().split(","))


def part_1():
    nums = open_file("Day 3/part 1.txt")

    ans = sum(set(nums))

    print(ans)

def part_2():
    nums = sorted(open_file("Day 3/part 2.txt"))

    prev = (nums[0] - 1) if nums else 0
    ans = 0
    available = 20

    for n in nums:
        if n > prev:
            ans += n
            prev = n
            available -= 1
            if available == 0: break

    print(ans)

def part_3():
    nums = sorted(open_file("Day 3/part 3.txt"))
    stacks = deque()

    for n in nums:
        if stacks and stacks[0] < n: stacks.popleft()
        stacks.append(n)

    print(len(stacks))

part_1()
part_2()
part_3()