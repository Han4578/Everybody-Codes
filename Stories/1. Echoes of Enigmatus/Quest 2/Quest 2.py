from re import findall, search
import pyperclip

def p1():
    with open("part 1.txt", "r") as f:
        lines = f.read().splitlines()

    tree1 = [None]
    tree2 = [None]

    for line in lines:
        node1, node2 = findall(r"\[(\d+),(.)\]", line)

        for node, tree in ((node1, tree1), (node2, tree2)):
            add_to_tree((int(node[0]), node[1]), tree)

    ans = final_word(tree1) + final_word(tree2)
    print(ans)
    pyperclip.copy(ans)

def p2():
    with open("part 2.txt", "r") as f:
        lines = f.read().splitlines()

    tree1 = [None]
    tree2 = [None]
    history1 = []
    history2 = []

    for line in lines:
        if line.startswith("SWAP"):
            index = int(search(r"\d+", line).group()) - 1
            tree1[history1[index]], tree2[history2[index]] = tree2[history2[index]], tree1[history1[index]]
        else:
            node1, node2 = findall(r"\[(\d+),(.)\]", line)

            for node, tree, history in ((node1, tree1, history1), (node2, tree2, history2)):
                history.append(add_to_tree((int(node[0]), node[1]), tree))

    ans = final_word(tree1) + final_word(tree2)
    print(ans)
    pyperclip.copy(ans)

def p3():
    with open("part 3.txt", "r") as f:
        lines = f.read().splitlines()

    root1 = [(-1, ""), None, None]
    root2 = [(-1, ""), None, None]
    history1 = []
    history2 = []

    for line in lines:
        if line.startswith("SWAP"):
            index = int(search(r"\d+", line).group()) - 1
            n1, n2 = history1[index], history2[index]
            for i in range(3):
                n1[i], n2[i] = n2[i], n1[i]

        else:
            node1, node2 = findall(r"\[(\d+),(.)\]", line)

            for node, root, history in ((node1, root1, history1), (node2, root2, history2)):
                current = root
                node = (int(node[0]), node[1])

                while True:
                    i = 1 if node[0] < current[0][0] else 2
                    if current[i]: current = current[i]
                    else:
                        history.append([node, None, None])
                        current[i] = history[-1]
                        break

    ans = ""
    for root in (root1, root2):
        longest_word = ""
        level = [root]

        while level:
            new_level = []
            word = ""

            for node in level:
                word += node[0][1]
                if node[1]: new_level.append(node[1])
                if node[2]: new_level.append(node[2])

            level = new_level
            if len(word) > len(longest_word): 
                longest_word = word

        ans += longest_word

    print(ans)
    pyperclip.copy(ans)


def add_to_tree(node, tree):
    i = 1
            
    while i < len(tree) and tree[i] != None:
        if node >= tree[i]: i = i * 2 + 1
        else: i <<= 1

    while i >= len(tree): tree += [None] * len(tree)
    tree[i] = node
    return i

def final_word(tree):
    word = []

    step = 1
    i = 1
    j = 0
    while i < len(tree):
        if len(word) <= j: word.append("")
        for _ in range(step):
            if tree[i]: word[j] += tree[i][1]
            i += 1
        step <<= 1
        j += 1

    return max(word, key=len)


p3()