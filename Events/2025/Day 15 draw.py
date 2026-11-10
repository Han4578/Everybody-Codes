from PIL import Image, ImageDraw

def part_3_draw():
    with open("Day 15/part 2.txt", "r") as f:
        instructions = f.read().split(",")

    direction = (0, -1)
    goal = (0, 0)
    points = [(0, 0)]
    edges = (0, 0, 0, 0)

    for i in instructions:
        direction = (direction[1], -direction[0]) if i[0] == "L" else (-direction[1], direction[0])
        
        m = int(i[1:])
        goal = (goal[0] + direction[0] * m, goal[1] + direction[1] * m)
        edges = (
            min(edges[0], goal[0]),
            min(edges[1], goal[1]),
            max(edges[2], goal[0]),
            max(edges[3], goal[1])
            )
        points.append(goal)

    img = Image.new("1", (edges[2] - edges[0] + 1, edges[3] - edges[1] + 1), 255)
    draw = ImageDraw.Draw(img)
    draw.line(tuple((p[0] - edges[0], p[1] - edges[1]) for p in points), 0)
        
    img.save("Day 15/part 2 image.png")