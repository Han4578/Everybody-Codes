from re import search
from pyperclip import copy
from collections import deque

class Dice:
    def __init__(self, line: str):
        r = search(r"(\d+).*\[(.*)\] seed=(\d+)", line)
        assert r
        self.id = r.group(1)
        self.seed: int = int(r.group(3))
        self.faces = list(int(n) for n in r.group(2).split(","))
        self.pulse = self.seed
        self.on = 0
        self.roll_number = 1

    def roll(self) -> int:
        spin = self.roll_number * self.pulse
        self.on = (self.on + spin) % len(self.faces)
        self.pulse = ((self.pulse + spin) % self.seed) + 1 + self.roll_number + self.seed
        self.roll_number += 1
        return self.faces[self.on]


def part1():
    with open("input 1.txt", "r") as f:
        dices: list[Dice] = [Dice(line) for line in f.readlines()]

    total = 0

    while total < 10000:

        for dice in dices:
            total += dice.roll()

    print(dices[0].roll_number)

def part2():
    dices: list[Dice] = []

    with open("input 2.txt", "r") as f:
        line = f.readline()
        while line != "\n":
            dices.append(Dice(line))
            line = f.readline()
        track = [int(c) for c in f.readline()]

    position = [0] * len(dices)
    finish = []
    while len(finish) < len(position):
        for i in range(len(position)):
            if position[i] == len(track): continue
            if track[position[i]] == dices[i].roll():
                position[i] += 1
                if position[i] == len(track): finish.append(dices[i].id)

    ans = ",".join(finish)
    print(ans)

def part3():
    dices: list[Dice] = []
    with open("input 3.txt", "r") as f:
        line = f.readline()
        while line != "\n":
            dices.append(Dice(line))
            line = f.readline()
        grid = [line.rstrip("\n") for line in f.readlines()]

    start: list[list[tuple[int, int]]] = [[] for _ in range(9)]
    total = set()
    width = len(grid[0])
    height = len(grid)

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            start[int(c) - 1].append((x, y))


    for dice in dices:
        rolls = []
        index = dice.roll() - 1
        seen = set()
        for sx, sy in start[index]:
            queue = []
            queue.append((sx, sy, 0))

            while queue:
                x, y, r = queue.pop()
                total.add((x, y))

                while True:
                    while len(rolls) <= r: rolls += str(dice.roll())
                    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == rolls[r] and (t:=(nx, ny, r + 1)) not in seen:
                            seen.add(t)
                            queue.append(t)
                    if grid[y][x] == rolls[r]: 
                        r += 1
                        seen.add((x, y, r))
                    else: break
    
    print(len(total))

    # g = [[False] * width for _ in range(height)]

    # for x, y in total:
    #     g[y][x] = True

    # from PIL import Image

    # image = Image.fromarray(g)    
    # image = image.resize((width, height), Image.Resampling.LANCZOS)
    
    # image.save(f"part 3 output.png")

part1()
part2()
part3()