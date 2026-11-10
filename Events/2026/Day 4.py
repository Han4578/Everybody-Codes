from collections import Counter
import re

def part_1():
    with open("Day 4/part_1.txt") as f:
        lines = f.read().split("\n")

    participants = Counter()

    for line in lines:
        id, q, p, t = re.findall(r"\d+", line)

        participants[id] += int(t)
        
    ans = sum(i * v for i, v in enumerate(sorted(participants.values()), start=1))

    print(ans)

def part_2():
    with open("Day 4/part_2.txt") as f:
        lines = f.read().split("\n")

    participants = Counter()
    parts = Counter()

    for line in lines:
        id, q, p, t = re.findall(r"\d+", line)

        participants[id] += int(t)
        parts[id] += 1

    ans = sum(i * v[1] for i, v in enumerate(sorted((-parts[id], v) for id, v in participants.items()), start=1))
    
    print(ans)

def part_3():
    with open("Day 4/part_3.txt") as f:
        lines = f.read().split("\n")
    
    time = Counter()
    points = Counter()
    completed = set()

    results = [tuple(int(s) for s in re.findall(r"\d+", line)) for line in lines]

    results.sort(key=lambda t: (t[1], t[2]))

    results.append((-1, -1, -1, -1))

    prev_p = 1
    prev_q = 1

    P = [50, 100, 150]

    for id, q, p, t in results:
        if p != prev_p or q != prev_q:
            prev_time = -1
            prev_r = -1
            r = P[prev_p - 1]
            for cur_time, cur_id in sorted((v, k) for k, v in time.items() if k in completed):
                if cur_time == prev_time: 
                    points[cur_id] += prev_r
                else:
                    if r <= 0: break
                    points[cur_id] += r
                    prev_r = r
                    prev_time = cur_time
                r -= 1

            completed.clear() 
        if prev_q != q:
            # print(sorted(points.values(), reverse=True)[-10:])
            time.clear()

        time[id] += t
        prev_p = p
        prev_q = q
        completed.add(id)

    ans = 0
    same = 0
    prev = -1

    for i, v in enumerate(sorted(points.values(), reverse=True), start=1):
        if prev == v: same += 1
        else: same = 0
        ans += v * (i - same)
        prev = v
    
    print(ans)

part_3()
