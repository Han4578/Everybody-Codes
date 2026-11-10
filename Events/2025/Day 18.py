import re

def get_final_energy(initial, plants, thicc):
    energy = []
    offset = len(initial)
    for branches in plants:
        energy.append(0)
        for p, t in branches:
            if p < offset: energy[-1] += initial[p] * t
            elif energy[p - offset] >= thicc[p - offset]: 
                energy[-1] += energy[p - offset] * t
   
    return energy[-1] if energy[-1] >= thicc[-1] else 0

def part_1():
    with open("Day 18/part 1.txt") as f:
        plant_inputs = f.read().split("\n\n")

    energy = []
    thicc = []

    for plant in plant_inputs:
        result = [int(n) if n.isdigit() else -1 for n in re.findall(r"(free|\d+)", plant)]

        thicc.append(result[1])

        energy.append(0)
        for i in range(2, len(result), 2):
            if result[i] == -1:
                energy[-1] += 1
            else:
                if energy[result[i] - 1] >= thicc[result[i] - 1]: energy[-1] += energy[result[i] - 1] * result[i + 1]

    ans = energy[-1]

    print(ans)

def part_2():
    with open("Day 18/part 2.txt") as f:
        input = f.read().split("\n\n\n")
        plant_inputs = input[0].split("\n\n")
        initial_inputs = input[1].splitlines()

    thicc = []
    plants = []

    for plant in plant_inputs:
        result = re.findall(r"(free|-?\d+)", plant)
        if result[-2] == "free": continue
        thicc.append(int(result[1]))

        plants.append([])
        for i in range(2, len(result), 2):
            plants[-1].append((int(result[i]) - 1, int(result[i + 1])))

    ans = sum(get_final_energy([int(n) for n in initial_line.split(" ")], plants, thicc) for initial_line in initial_inputs)

    print(ans)

def part_3():
    with open("Day 18/part 3.txt") as f:
        input = f.read().split("\n\n\n")
        plant_inputs = input[0].split("\n\n")
        initial_inputs = input[1].splitlines()

    max_input = [0] * 81
    thicc = []
    plants = []

    for i in range(81, len(plant_inputs)):
        plant = plant_inputs[i]
        result = [int(n) for n in re.findall(r"-?\d+", plant)]
        thicc.append(result[1])
        plants.append([(result[i] - 1, result[i + 1]) for i in range(2, len(result), 2)])

    for i in range(9):
        for j, t in plants[i]:
            if t >= 0:
                max_input[j] = 1

    max_energy = get_final_energy(max_input, plants, thicc)

    ans = sum(max_energy - e for initial_line in initial_inputs if (e:=get_final_energy([int(n) for n in initial_line.split(" ")], plants, thicc)) > 0)

    print(ans)

part_1()
part_2()
part_3()

    

