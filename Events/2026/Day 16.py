
def flip(line):
    ans = 0
    
    while True:
        last = {}

        cur = line[0]

        for i, c in enumerate(line):
            if cur not in last:
                for j in range(len(line) - 1, -1, -1):
                    if line[j] == cur:
                        last[cur] = j
                        break

            if c != cur and last[line[i - 1]] != i - 1:
                t = line[i - 1]
                right = line[len(line) - 1:last[line[i - 1]]: -1]
                d = -1
                l = last[line[i - 1]]
                r = i

                while True:
                    ans += abs(l - r) + 1
                    while line[l] == t and (l <= r if d == 1 else l >= r): 
                        l += d
                    while line[r] != t and (l <= r if d == 1 else l >= r):
                        right.append(line[r])
                        r -= d
                    if (l > r if d == 1 else l < r): break
                    l, r = r, l
                    d = -d

                line = right[::-1]
                break

            cur = c
        else:
            break

    return ans

def part_1():
    with open("Day 16/part_1.txt") as f:
        line = list(f.read())

    ans = flip(line)

    print(ans)

def part_2():
    with open("Day 16/part_2.txt") as f:
        line = list(f.read()) * 10

    ans = flip(line)


    print(ans)

def part_3():
    with open("Day 16/part_3.txt") as f:
        line = list(f.read()) * 100

    ans = flip(line)

    print(ans)
    

part_3()
