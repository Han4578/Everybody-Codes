from collections import defaultdict
from functools import cache

def get_book_and_names(path):
    with open(path, "r") as f:
        lines = f.read().split("\n")

    book = defaultdict(set)

    for i in range(2, len(lines)):
        rule = lines[i]

        a, b = rule.split(" > ")

        book[a].update(b.split(","))

    return book, lines[0].split(",") #names


def part_1():
    book, names = get_book_and_names("Day 7/part 1.txt")

    ans = [name for name in names if all(name[i] in book[name[i - 1]] for i in range(1, len(name)))][0]
    print(ans)

def part_2():
    book, names = get_book_and_names("Day 7/part 2.txt")

    ans = sum(i for i, name in enumerate(names, start=1) if all(name[i] in book[name[i - 1]] for i in range(1, len(name))))
    print(ans)


def part_3():
    book, names = get_book_and_names("Day 7/part 3.txt")
    seen = set()

    @cache
    def count(chars, letter):
        if chars < 0: return 0
        chars -= 1

        return sum((count(chars, next_letter) for next_letter in book[letter]), start=1)

    def spread(prefix):
        if prefix in seen: return 0
        seen.add(prefix)

        if len(prefix) >= 7:  
            return count(11 - len(prefix), prefix[-1])

        return sum(spread(prefix + next_letter) for next_letter in book[prefix[-1]])
    
    ans = sum(spread(name) for name in names if all(name[i] in book[name[i - 1]] for i in range(1, len(name))))
    print(ans)

def part_4():
    book, names = get_book_and_names("Day 7/part 4.txt")
    seen = set()

    @cache
    def count(chars, letter):
        if chars < 0: return 0
        chars -= 1

        return sum((count(chars, next_letter) for next_letter in book[letter]), start=1)

    def spread(prefix):
        if prefix in seen: return 0
        seen.add(prefix)

        if len(prefix) >= 7:  
            return count(98 - len(prefix), prefix[-1])

        return sum(spread(prefix + next_letter) for next_letter in book[prefix[-1]])
    
    ans = sum(spread(name) for name in names if all(name[i] in book[name[i - 1]] for i in range(1, len(name))))
    print(ans)

part_1()
part_2()
part_3()
part_4()