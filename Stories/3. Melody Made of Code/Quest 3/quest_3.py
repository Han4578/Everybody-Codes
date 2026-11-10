import re

class Node:
        def __init__(self, line):
            id, plug, left_socket, right_socket, self.data = re.search(r"id=(\d+), plug=(.+), leftSocket=(.+), rightSocket=(.+), data=(.+)", line).groups()
            self.left: Node = None
            self.right: Node = None
            self.id = int(id)
            self.left_socket = tuple(left_socket.split(" "))
            self.right_socket = tuple(right_socket.split(" "))
            self.plug = tuple(plug.split(" "))
        
        def sum(self, pos):
            val = 0
            if self.left != None:
                t = self.left.sum(pos)
                val += t[0]
                pos = t[1] + 1

            val += self.id * pos
            print(self.data)

            if self.right != None:
                t = self.right.sum(pos + 1)
                val += t[0]
                pos = t[1]

            return val, pos

def part_1():        
    with open("part 1.txt", "r") as f:
        nodes = [Node(line) for line in f.readlines()]

    root = nodes.pop(0)
    
    def insert(parent: Node, node: Node):

        if parent.left != None:
            if insert(parent.left, node): return True
        elif parent.left_socket == node.plug:
            parent.left = node
            return True

        if parent.right != None:
            if insert(parent.right, node): return True
        elif parent.right_socket == node.plug:
            parent.right = node
            return True
            
        return False

    for node in nodes:
        insert(root, node)

    ans = root.sum(1)[0]

    print(ans)

def part_2():
    with open("part 2.txt", "r") as f:
        nodes = [Node(line) for line in f.readlines()]

    root = nodes.pop(0)

    def insert(parent: Node, node: Node):

        if parent.left != None:
            if insert(parent.left, node): return True
        elif any(a == b for a, b in zip(parent.left_socket, node.plug)):
            parent.left = node
            return True

        if parent.right != None:
            if insert(parent.right, node): return True
        elif any(a == b for a, b in zip(parent.right_socket, node.plug)):
            parent.right = node
            return True
            
        return False

    for node in nodes:
        insert(root, node)

    ans = root.sum(1)[0]

    print(ans)

def part_3():
    with open("part 3.txt", "r") as f:
        nodes = [Node(line) for line in f.readlines()]

    root = nodes.pop(0)

    node_to_insert: Node = None

    def insert(parent: Node):
        nonlocal node_to_insert

        if parent.left != None:
            if parent.left_socket == node_to_insert.plug and parent.left_socket != parent.left.plug:
                parent.left, node_to_insert = node_to_insert, parent.left 
            elif insert(parent.left): return True
        elif any(a == b for a, b in zip(parent.left_socket, node_to_insert.plug)):
            parent.left = node_to_insert
            return True

        if parent.right != None:
            if parent.right_socket == node_to_insert.plug and parent.right_socket != parent.right.plug:
                parent.right, node_to_insert = node_to_insert, parent.right 
            elif insert(parent.right): return True
        elif any(a == b for a, b in zip(parent.right_socket, node_to_insert.plug)):
            parent.right = node_to_insert
            return True
            
        return False

    for node in nodes:
        node_to_insert = node
        while not insert(root): pass

    ans = root.sum(1)[0]

    print(ans)

part_1()
part_2()
part_3()
    