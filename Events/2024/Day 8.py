from math import ceil, sqrt

def p1():
    with open("Day 8/p1.txt", "r") as f:
        total = int(f.read())

    layer = ceil(sqrt(total))

    print((layer * 2 - 1) * (layer ** 2 - total))

def p2():
    with open("Day 8/p2.txt", "r") as f:
        priests = int(f.read())
    width = 1
    thickness = 1
    current_total = 1
    total = 20240000
    mod = 1111

    while current_total < total:
        thickness = (thickness * priests) % mod
        width += 2
        current_total += width * thickness

    print((current_total - total) * width)

def p3():
    with open("Day 8/p3.txt", "r") as f:
        priests = int(f.read())

    width = 1
    thickness = 1
    total = 202400000
    current_total = 1
    mod = 10
    thicknesses = [1]

    while current_total < total:
        thickness = (thickness * priests) % mod + mod
        width += 2
        current_total += width * thickness
        thicknesses.append(thickness)

    current_thickness = sum(thicknesses)
    constant = priests * width

    current_total -= min((constant * current_thickness) % mod, current_thickness - 2)

    for i in range(1, int((width - 1) / 2)):
        current_thickness -= thicknesses[i - 1]
        empty = min((constant * current_thickness) % mod, current_thickness - thicknesses[i] - 1)
        current_total -= empty * 2

    print(current_total - total)


p1()
p2()
p3()
    

