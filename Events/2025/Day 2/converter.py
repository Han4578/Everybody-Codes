from PIL import Image
import numpy as np


with open("Day 2/part 2 output.txt", "r") as f:
    arr = np.array([[c == "#" for c in line] for line in f.readlines()])

img = Image.fromarray(arr)

img.save("Day 2/part 2 output.png")