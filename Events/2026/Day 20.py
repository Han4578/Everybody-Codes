from itertools import product

def equation_to_nums(equation, digit_matches):
    nums = []
    matches = 2

    for eq in equation.split(" = "):
        n = 0
        sign = 1

        for c in eq.split(" "):
            match c:
                case "+": 
                    sign = 1
                    matches += 2
                case "-": 
                    sign = -1
                    matches += 1
                case _: 
                    n += sum((int(cc) if cc != "A" else 10) * len(digit_matches) ** i for i, cc in enumerate(reversed(c))) * sign
                    matches += sum(digit_matches[cc] for cc in c)

        nums.append(n)

    nums.append(matches)
    return nums

def base11(base10):
    ans = ""
    i = 1

    while base10 > 0:
        ans += str(base10 % 11) if base10 % 11 < 10 else "A"
        i *= 11
        base10 //= 11

    return ans[::-1]

def part_1():
    with open("Day 20/part_1.txt") as f:
        lines = f.read().split("\n")

    digit_matches = {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
    }

    ans = 0

    for line in lines:
        nums = equation_to_nums(line, digit_matches)

        if nums[0] == nums[1]: ans += nums[2]

    print(ans)

def part_2():
    with open("Day 20/part_2.txt") as f:
        lines = f.read().split("\n")

    digit_matches = {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
        "A": 6
    }
    base10 = 0

    for line in lines:
            nums = equation_to_nums(line, digit_matches)
    
            if nums[0] == nums[1]: base10 += nums[2]

    ans = base11(base10)
    print(ans)

def part_3():
    with open("Day 20/part_3.txt") as f:
        lines = f.read().split("\n")

    digits = {
        "0": 0b0111111,
        "1": 0b0000110,
        "2": 0b1011011,
        "3": 0b1001111,
        "4": 0b1100110,
        "5": 0b1101101,
        "6": 0b1111101,
        "7": 0b0000111,
        "8": 0b1111111,
        "9": 0b1101111,
        "A": 0b1110111,
    }

    digit_matches = {k: d.bit_count() for k, d in digits.items()}
    convertable = {
        "+": [["-"], [], []],
        "-": [[], ["+"], []]
    }

    for k1, d1 in digits.items():
        convertable[k1] = [[], [], []] # Remove, Add, Move

        for k2, d2 in digits.items():
            if k1 == k2: continue
            if d1.bit_count() > d2.bit_count() and (d1 ^ d2).bit_count() == 1: convertable[k1][0].append(k2)
            elif d1.bit_count() < d2.bit_count() and (d1 ^ d2).bit_count() == 1: convertable[k1][1].append(k2)
            elif d1.bit_count() == d2.bit_count() and (d1 ^ d2).bit_count() == 2: convertable[k1][2].append(k2)

    base10 = 0

    def check(chars):
        nonlocal base10
        nums = equation_to_nums("".join(chars), digit_matches)

        if nums[0] == nums[1]: 
            base10 += nums[2]
            return True
        
        return False

    for line in lines:
        chars = list(line)
        if check(chars): continue

        found = False

        for i, c in enumerate(line):
            if c not in convertable: continue

            for c2 in convertable[c][2]:
                if c == c2: continue
                chars[i] = c2

                if check(chars): 
                    found = True
                    break

            if found: break

            for j in range(i + 1, len(line)):
                if line[j] not in convertable: continue

                for a, b in list(product(convertable[c][0], convertable[line[j]][1])) + list(product(convertable[c][1], convertable[line[j]][0])):
                    chars[i] = a
                    chars[j] = b

                    if check(chars): 
                        found = True
                        break

                if found: break

                chars[j] = line[j]

            if found: break

            chars[i] = c

    ans = base11(base10)
    print(ans)

part_1()
part_2()
part_3()

