from collections import Counter

def get_counter(lines):
    column_count = [Counter(line[i] for line in lines) for i in range(2, 6)]
    row_count = [Counter(line) for line in lines[2:6]]


    for counter in column_count: 
        for k in list(counter):
            if not k.isalpha() and k != "?": counter.pop(k)

    for counter in row_count: 
        for k in list(counter):
            if not k.isalpha() and k != "?": counter.pop(k)

    return column_count, row_count


def get_word(lines):
    column_count, row_count = get_counter(lines)
    final = ""

    for y, line in enumerate(lines[2:6]):
        for x, c in enumerate(line[2:6]):
            if c != ".": continue
            count = column_count[x] + row_count[y]
            final += count.most_common(1)[0][0]

    return final

def solve(all_lines, offset):
    lines = [line[offset[0]: offset[0] + 8] for line in all_lines[offset[1]: offset[1] + 8]]
    column_count, row_count = get_counter(lines)

    words = [" "] * 16
    filled_in = True
    add_letters = {}
    
    while " " in words and filled_in:
        filled_in = False
        
        for y in range(4):
            for x in range(4):
                if words[y * 4 + x] != " ": continue

                intersect = (column_count[x] & row_count[y]).keys()
                union = (column_count[x] | row_count[y]).keys()

                if len(intersect) == 1:
                    pair = list(intersect)[0]
                    words[y * 4 + x] = pair[0]
                    column_count[x][pair[0]] -= 1
                    row_count[y][pair[0]] -= 1
                    filled_in = True

                elif len(intersect) == 0 and len(union) == 2 and row_count[y]["?"] + column_count[x]["?"] == 1:
                    letter = list(filter(lambda k: k != "?", union))[0]
                    words[y * 4 + x] = letter

                    if "?" in row_count[y]:
                        for x1 in range(offset[0], offset[0] + 8):
                            if all_lines[offset[1] + y + 2][x1] != "?": continue
                            add_letters[(x1, offset[1] + y + 2)] = letter
                            break
                    else:
                        for y1 in range(offset[1], offset[1] + 8):
                            if all_lines[y1][offset[0] + x + 2] != "?": continue
                            add_letters[(offset[0] + x + 2, y1)] = letter
                            break

                    filled_in = True
                elif len(intersect) == 0 and "?" not in union: return chr(ord("A") - 1) * len(words)

    if " " not in words: 
        for pos, letter in add_letters.items():
            all_lines[pos[1]][pos[0]] = letter
        return "".join(words)
    else: return ""    


def p1():
    with open("Day 10/p1.txt", "r") as f:
        lines = f.read().split("\n")

    print(get_word(lines))

def p2():
    with open("Day 10/p2.txt", "r") as f:
        all_lines = f.read().split("\n")

    total = 0
    offset = ord("A") - 1

    for y in range(0, len(all_lines), 9):
        for x in range(0, len(all_lines[y]), 9):
            lines = [line[x : x + 8] for line in all_lines[y : y + 8]]
            word = get_word(lines)
            for base, c in enumerate(word):
                total += (base + 1) * (ord(c) - offset)

    print(total)

def p3():
    with open("Day 10/p3.txt", "r") as f:
        all_lines = [list(line) for line in f.read().split("\n")]

    total = 0
    offset = ord("A") - 1

    unsolved = set()

    for y in range(0, len(all_lines) - 2, 6):
        for x in range(0, len(all_lines[y]) - 2, 6):
            unsolved.add((x, y))

    solved = True

    while solved:
        solved = False

        for corner in set(unsolved): 
            if (word := solve(all_lines, corner)) != "": 
                unsolved.remove(corner)
                for base, c in enumerate(word):
                    total += (base + 1) * (ord(c) - offset)
                solved = True

    # print("\n".join("".join(line) for line in all_lines))
    print(total)


p1()
p2()
p3()