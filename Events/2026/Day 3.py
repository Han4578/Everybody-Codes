import re
from concurrent import futures

def part_1():
    with open("Day 3/part_1.txt") as f:
        lines = f.read().split("\n")

    ans = 0

    for line in lines:
        a, b = re.findall(r"\d+", line)

        ans += sum(int(bb) * int(aa) ** (len(a) - i) for i, (aa, bb) in enumerate(zip(a, b), start=1))

    print(ans)

def part_2():
    with open("Day 3/part_2.txt") as f:
        lines = f.read().split("\n")

    ans = 0

    for line in lines:
        a, b = re.findall(r"\d+", line)

        ans += sum(int(bb) * int(a[(-i - 1) % len(a)]) ** (i) for i, bb in enumerate(reversed(b), start=0))

    print(ans)

def p3_worker(line):
    a, b = re.findall(r"\d+", line)[1:]

    num = sum(int(bb) * int(a[(-i - 1) % len(a)]) ** (i) for i, bb in enumerate(reversed(b), start=0))

    if all(num != sum(int(bb) * int(a[(-i - 1) % len(a)]) ** (i) for i, bb in enumerate(reversed(str(n)), start=0)) for n in range(int(b))):
        return num

    return 0

def p3_worker2(line):
    a, b = re.findall(r"\d+", line)[1:]

    num = sum(int(bb) * int(a[(-i - 1) % len(a)]) ** (i) for i, bb in enumerate(reversed(b), start=0))
    l = len(b)
    t = int(b)

    def dfs(cur, remaining, i):
        if remaining == 0: return cur < t
        if t <= cur or i >= l or remaining < 0: return False

        for n in range(10):
            if dfs(cur, remaining - n * int(a[(-i - 1) % len(a)]) ** (i), i + 1): return True
            cur += 10 ** i

        return False

    if not dfs(0, num, 0):
        return num

    return 0

def part_3():
    with open("Day 3/part_3.txt") as f:
        lines = f.read().split("\n")

    with futures.ProcessPoolExecutor() as executor:
        ans = sum(executor.map(p3_worker2, lines))

    print(ans)

if __name__ == "__main__":
    from timeit import timeit

    print(timeit(part_3, number=1))
