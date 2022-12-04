from pathlib import Path
import sys
import string

path = Path(__file__).parents[1] / "data.txt"
rucksacks = path.read_text().split("\n")

priority_map = dict(
    zip(string.ascii_lowercase, [ord(c) % 32 for c in string.ascii_lowercase])
)
upper_priority_map = dict(
    zip(string.ascii_uppercase, [ord(c) % 32 + 26 for c in string.ascii_uppercase])
)
priority_map.update(upper_priority_map)

total_cost = 0
for ruck in rucksacks:
    assert len(ruck) % 2 == 0
    # determine length of compartments
    comp_len = int(len(ruck) / 2)
    comp1 = ruck[0:comp_len]
    comp2 = ruck[comp_len:]
    shared_elements = list(set(comp1).intersection(comp2))
    for se in shared_elements:
        total_cost += priority_map[se]

print(f"Total cost: {total_cost}")
