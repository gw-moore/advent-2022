from pathlib import Path
import string

path = Path(__file__).parents[1] / "data.txt"
rucksacks: list[str] = path.read_text().split("\n")

priority_map = dict(
    zip(string.ascii_lowercase, [ord(c) % 32 for c in string.ascii_lowercase])
)
upper_priority_map = dict(
    zip(string.ascii_uppercase, [ord(c) % 32 + 26 for c in string.ascii_uppercase])
)
priority_map.update(upper_priority_map)

total_cost = 0
for ruck in rucksacks:
    # ensure that each compartment is of equal length
    assert len(ruck) % 2 == 0

    # determine the size of the compartment for the given ruck
    comp_len = int(len(ruck) / 2)
    comp1 = ruck[0:comp_len]
    comp2 = ruck[comp_len:]

    # add the cost to the running total
    shared_elements = list(set(comp1).intersection(comp2))
    for se in shared_elements:
        total_cost += priority_map[se]

print(f"Total cost: {total_cost}")
