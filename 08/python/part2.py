from pathlib import Path
from rich import print
import numpy as np

path = Path(__file__).parents[1] / "data.txt"
lines = []
for line in Path(path).read_text().split("\n"):
    lines.append([int(s) for s in line])

matrix = np.array(lines)
ex_tree_pos = [1, 2]
nrows, ncols = matrix.shape

all_viz_scores = []
for i in list(range(matrix.shape[0])):
    viz_trees = []

    if i == 0 or i == nrows - 1:
        continue
    for j in list(range(matrix.shape[1])):
        if j == 0 or j == ncols - 1:
            continue

        tree = matrix[i, j]
        ABOVE = list(range(0, i))
        ABOVE.reverse()
        LEFT = list(range(0, j))
        LEFT.reverse()
        BELOW = list(range(i + 1, nrows))
        RIGHT = list(range(j + 1, ncols))

        print()
        print(f"tree pos: {i, j}")
        print(f"tree size: {tree}")

        viz_trees_above = []
        for a in ABOVE:
            if tree > matrix[a, j]:
                viz_trees_above.append(1)
            elif tree <= matrix[a, j]:
                viz_trees_above.append(1)
                break

        viz_trees_left = []
        for l in LEFT:
            if tree > matrix[i, l]:
                viz_trees_left.append(1)
            elif tree <= matrix[i, l]:
                viz_trees_left.append(1)
                break

        viz_trees_below = []
        for b in BELOW:
            if tree > matrix[b, j]:
                viz_trees_below.append(1)
            elif tree <= matrix[b, j]:
                viz_trees_below.append(1)
                break

        viz_trees_right = []
        for r in RIGHT:
            if tree > matrix[i, r]:
                viz_trees_right.append(1)
            elif tree <= matrix[i, r]:
                viz_trees_right.append(1)
                break

        print(f"viz above: {viz_trees_above}")
        print(f"viz left: {viz_trees_left}")
        print(f"viz below: {viz_trees_below}")
        print(f"viz right: {viz_trees_right}")
        total_viz = len(viz_trees_above) * len(viz_trees_below) * len(viz_trees_left) * len(viz_trees_right)
        print(f"total viz: {total_viz}")
        all_viz_scores.append(total_viz)

print()
print(f"max score: {max(all_viz_scores)}")
