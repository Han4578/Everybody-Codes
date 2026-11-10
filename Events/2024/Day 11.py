from collections import Counter

def get_category(path):
    category = {}

    with open(path, "r") as f:
        lines = f.read().split("\n")

    for line in lines:
        s = line.split(":")
        category[s[0]] = Counter(s[1].split(","))

    return category

def get_ans(category, days, starting):

    termites = Counter({starting: 1})

    for i in range(days):
        new_termites = Counter()
        for t, num in termites.items():
            for c, n in category[t].items():
                new_termites[c] += n * num
        termites = new_termites

    return sum(termites.values())
    

def p1():
    print(get_ans(get_category("Day 11/p1.txt"), 4, "A"))

def p2():
    print(get_ans(get_category("Day 11/p2.txt"), 10, "Z"))

def p3():
    category = get_category("Day 11/p3.txt")

    most = 0
    least = 1e32

    for starting in category.keys():
        total = get_ans(category, 20, starting)
        most = max(most, total)
        least = min(least, total)

    print(most - least)

p1()
p2()
p3()