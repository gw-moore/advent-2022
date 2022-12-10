from pathlib import Path
from rich import print
import numpy as np

path = Path(__file__).parents[1] / "data.txt"
lines = []
for line in Path(path).read_text().split("\n"):
    lines.append([int(s) for s in line])

matrix = np.array(lines)

# first, count the number of trees that make up the perimeter
nrows, ncols = matrix.shape
num_viz_trees = (nrows * 2) + (ncols * 2) - 4

num_viz_trees = (nrows * 2) + (ncols * 2) - 4
print(f"starting num_viz_tree: {num_viz_trees}")

for i in list(range(matrix.shape[0])):
    if i == 0 or i == nrows - 1:
        continue
    for j in list(range(matrix.shape[1])):
        if j == 0 or j == ncols - 1:
            continue

        tree = matrix[i, j]
        ABOVE = list(range(0, i))
        BELOW = list(range(i + 1, nrows))
        LEFT = list(range(0, j))
        RIGHT = list(range(j + 1, ncols))

        print()
        print(f"tree pos: {i, j}")
        print(f"tree size: {tree}")

        hidden_above = any([tree <= matrix[a, j] for a in ABOVE])
        hidden_below = any([tree <= matrix[b, j] for b in BELOW])
        hidden_left = any([tree <= matrix[i, l] for l in LEFT])
        hidden_right = any(tree <= matrix[i, r] for r in RIGHT)
        print(f"Hidden above: {hidden_above}")
        print(f"Hidden below: {hidden_below}")
        print(f"Hidden left: {hidden_left}")
        print(f"Hidden right: {hidden_right}")

        hidden = all([hidden_above, hidden_below, hidden_left, hidden_right])
        print(f"Hidden: {hidden}")
        if hidden is False:
            num_viz_trees += 1
        print(f"num viz trees: {num_viz_trees}")

print()
print(num_viz_trees)
