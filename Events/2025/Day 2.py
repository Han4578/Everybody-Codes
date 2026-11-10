

import re
import multiprocessing

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def div(a, b):
    return (int(a[0] / b[0]), int(a[1] / b[1]))

def loop(a1, a2):
    r1 = 0
    r2 = 0

    for _ in range(100):
        # R = add(div(mul(R, R), [100000,100000]), A)
        # R = (int((R[0] ** 2 - R[1] ** 2) / 100000) + A[0], int((R[0] * R[1]) / 50000) + A[1])
        r1, r2 = int(((r1 + r2) * (r1 - r2)) / 100000) + a1, int((r1 * r2) / 50000) + a2
        if -1000000 <= r1 <= 1000000 and -1000000 <= r2 <= 1000000: continue
        return False
    
    return True
    
def open_file(path):
    with open(path, "r") as f:
        res = re.search(r"\[(-?\d+),(-?\d+)\]", f.read())
        return (int(res.group(1)), int(res.group(2)))

def part_1():
    A = open_file("Day 2/part 1.txt")
    R = [0, 0]

    for _ in range(3):
        R = mul(R, R)
        R = div(R, [10, 10])
        R = add(R, A)

    print(str(R).replace(" ", ""))

def part_2():
    A = open_file("Day 2/part 2.txt")

    with multiprocessing.Pool() as pool:
        points = pool.starmap_async(loop, ((A[0] + x, A[1] + y) for x in range(0, 1001, 10) for y in range(0, 1001, 10))).get()
        
    # for i, v in enumerate(points, start=1):
    #     print("#" if v else ".", end= "\n" if i % 101 == 0 else "")
        
    # with open("Day 2/part 2 output.txt", "w+") as f:
    #     f.write("".join(("#" if v else ".") + ("\n" if i % 101 == 0 else "") for i, v in enumerate(points, start=1)))

    return sum(points)
    

def part_3():
    A = open_file("Day 2/part 3.txt")

    with multiprocessing.Pool() as pool:
        points = pool.starmap_async(loop, ((A[0] + x, A[1] + y) for x in range(1001) for y in range(1001))).get()
        
    # with open("Day 2/part 3 output.txt", "w+") as f:
    #     f.write("".join(("#" if v else ".") + ("\n" if i % 1001 == 0 else "") for i, v in enumerate(points, start=1)))

    print(sum(points))


    
if __name__ == "__main__":
    import time
    t = time.time()
    A = open_file("Day 2/part 3.txt")

    ans = 0
    
    for x in range(1001):
        for y in range(1001):
            a1 = A[0] + x
            a2 = A[1] + y
            r1 = 0
            r2 = 0

            for _ in range(100):
                r1, r2 = int(((r1 + r2) * (r1 - r2)) / 100000) + a1, int((r1 * r2) / 50000) + a2
                if -1000000 <= r1 <= 1000000 and -1000000 <= r2 <= 1000000: continue
                break
            else:
                ans += 1
    
    print(ans)
    print(time.time() - t)

    # part_1()
    # import timeit
    # print(timeit.timeit(part_2, number=10) / 10)
    # part_3()