from pathlib import Path
import string

path = Path(__file__).parents[1] / "data.txt"
rucksacks: list[str] = path.read_text().split("\n")
groups: list[list[str]] = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

priority_map = dict(
    zip(string.ascii_lowercase, [ord(c) % 32 for c in string.ascii_lowercase])
)
upper_priority_map = dict(
    zip(string.ascii_uppercase, [ord(c) % 32 + 26 for c in string.ascii_uppercase])
)
priority_map.update(upper_priority_map)

total_cost = 0
for grp in groups:
    unique_value = list(set(set(grp[0]) & set(grp[1]) & set(grp[2])))
    total_cost += priority_map[unique_value[0]]
print(f"Total cost: {total_cost}")
