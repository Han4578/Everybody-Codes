import pyperclip

def part1():
    with open("input 1.txt", "r") as f:
        balloons = f.read()

    bolt = 0

    for b in balloons:
        if "RGB"[bolt % 3] == b: continue
        else: bolt += 1

    print(bolt)

def part2():
    with open("input 2.txt", "r") as f:
        balloons = list(f.read()) * 100

    bolt = 0

    while balloons:
        if "RGB"[bolt % 3] == balloons.pop(0) and len(balloons) % 2 == 1: del balloons[len(balloons) // 2]
        bolt += 1

    print(bolt)

def part3():
    total = 100000
    with open("input 3.txt", "r") as f:
        sequence = list(f.read())

    left = sequence * (total // 2)
    right = []
    if total % 2 == 1: 
        left += sequence[:len(sequence) // 2]
        right += sequence[len(sequence) // 2:]
    right += sequence * (total // 2)

    i = 0
    j = 0
    bolt = 0

    while i < len(left):
        if "RGB"[bolt % 3] == left[i]:
            i += 1
            j += 1
            bolt += 1
        else:
            i += 2
            left += right[j]
            j += 1
            bolt += 2
    
    print(bolt)

part3()
    