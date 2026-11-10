def p1():
    slots = []
    current = []

    with open("Day 16/p1.txt", "r") as f:
        rows = f.read().split("\n")
    
    turns = [int(n) for n in rows[0].split(",")]

    for i in range(len(turns)):
        slots.append([])
        current.append(0)

    for row in rows[2:]:
        for i, face in enumerate(row[j: j + 3] for j in range(0, len(row), 4)):
            if face == "   ": continue
            slots[i].append(face)

    for i in range(len(turns)): turns[i] %= len(slots[i])

    for i in range(100):
        for i in range(len(current)): current[i] = (current[i] + turns[i]) % len(slots[i])

        final  = " ".join(slots[i][current[i]] for i in range(len(current)))

    print(final)

def p2():
    slots = []
    current = []

    with open("Day 16/p2.txt", "r") as f:
        rows = f.read().split("\n")
    
    turns = [int(n) for n in rows[0].split(",")]

    for i in range(len(turns)):
        slots.append([])
        current.append(0)

    for row in rows[2:]:
        for i, face in enumerate(row[j] + row[j + 2] for j in range(0, len(row), 4)):
            if face == "  ": continue
            slots[i].append({c: face.count(c) for c in set(face)})

    for i in range(len(turns)): turns[i] %= len(slots[i])

    history = []

    while len(history) == 0 or sum(current) > 0:
        for i in range(len(current)): current[i] = (current[i] + turns[i]) % len(slots[i])
        
        final = {}
        coins = 0

        for i in range(len(current)):
            for c, n in slots[i][current[i]].items():
                if c in final: final[c] += n
                else: final[c] = n


        for n in final.values():
            if n < 3: continue
            coins += n - 2

        history.append(coins)
    total_pulls = 202420242024

    loops = total_pulls // len(history)
    remaining = total_pulls % len(history)

    total = sum(history) * loops + sum(history[0:remaining])
    print(total)

def p3():
    slots = []
    current = []

    with open("Day 16/p3.txt", "r") as f:
        rows = f.read().split("\n")
    
    turns = [int(n) for n in rows[0].split(",")]

    for i in range(len(turns)):
        slots.append([])
        current.append(0)

    for row in rows[2:]:
        for i, face in enumerate(row[j] + row[j + 2] for j in range(0, len(row), 4)):
            if face == "  ": continue
            slots[i].append({c: face.count(c) for c in set(face)})

    for i in range(len(turns)): turns[i] %= len(slots[i])

    states = {tuple(current): (0, 0)}

    for p in range(256):
        new_states = {}

        for state, min_max in states.items():

            for offset in range(-1, 2):
                new_state = tuple((state[i] + turns[i] + offset) % len(slots[i]) for i in range(len(turns)))
                final = {}
                coins = 0

                for i in range(len(turns)):
                    for c, n in slots[i][new_state[i]].items():
                        if c in final: final[c] += n
                        else: final[c] = n

                for n in final.values():
                    if n < 3: continue
                    coins += n - 2

                if new_state in new_states:
                    s = new_states[new_state]
                    new_states[new_state] = (max(s[0], coins + min_max[0]), min(s[1], coins + min_max[1]))
                else: new_states[new_state] = (coins + min_max[0], coins + min_max[1])

        states = new_states


    print(max(states.values(), key=lambda m: m[0])[0], min(states.values(), key=lambda m: m[1])[1])

p1()
p2()
p3()

    