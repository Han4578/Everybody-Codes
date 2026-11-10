def get_branch(name, branches):
    if name in branches: return branches[name]
    else:
        branches[name] = {"next": [], "parent": None, "name": name}
        return branches[name]
    
def get_ans(path):
    branches = {}
    apples = []

    with open(path, "r") as f:
        lines = f.read().split("\n")

        for line in lines:
            name = line.split(":")[0]
            if name in ["BUG", "ANT"]: continue
            branch = get_branch(name, branches)

            for b in line.split(":")[1].split(","):
                if b == "@":
                    apples.append(branch)
                else:
                    branch["next"].append(get_branch(b, branches))
                    branches[b]["parent"] = branch

    lengths = {}

    for branch in apples:
        path = [branch["name"]]

        while (branch["name"] != "RR"):
            branch = branch["parent"]
            path.append(branch["name"])

        
        if len(path) not in lengths: lengths[len(path)] = [path] 
        else: lengths[len(path)].append(path)

    paths = sorted(lengths.keys(), key=lambda k: len(lengths[k]))

    return lengths[paths[0]][0]


def p1():  
    path = get_ans("Day 6/p1.txt")

    print("".join(reversed(path)) + "@")

def p2():  
    path = get_ans("Day 6/p2.txt")

    print("".join(b[0] for b in reversed(path)) + "@")

def p3():  
    path = get_ans("Day 6/p3.txt")

    print("".join(b[0] for b in reversed(path)) + "@")
    

p1()
p2()
p3()
        
    


