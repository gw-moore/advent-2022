from dataclasses import dataclass
from pathlib import Path
from rich.pretty import pprint


@dataclass
class Move:
    n_crates: int
    source: str
    destination: str

    @classmethod
    def from_str(cls, string: str):
        l = [int(s) for s in string if s.isdigit()]
        return cls(n_crates=l[0], source=f"stack{l[1]}", destination=f"stack{l[2]}")


path = Path(__file__).parents[1] / "instructions.txt"
raw_instructions = Path(path).read_text().split("\n")
raw_instructions = [i.split(" ") for i in raw_instructions]
instructions = [Move.from_str(s) for s in raw_instructions]


#     [P]                 [Q]     [T]
# [F] [N]             [P] [L]     [M]
# [H] [T] [H]         [M] [H]     [Z]
# [M] [C] [P]     [Q] [R] [C]     [J]
# [T] [J] [M] [F] [L] [G] [R]     [Q]
# [V] [G] [D] [V] [G] [D] [N] [W] [L]
# [L] [Q] [S] [B] [H] [B] [M] [L] [D]
# [D] [H] [R] [L] [N] [W] [G] [C] [R]
#  1   2   3   4   5   6   7   8   9

stacks = {
    "stack1": ["D", "L", "V", "T", "M", "H", "F"],
    "stack2": ["H", "Q", "G", "J", "C", "T", "N", "P"],
    "stack3": ["R", "S", "D", "M", "P", "H"],
    "stack4": ["L", "B", "V", "F"],
    "stack5": ["N", "H", "G", "L", "Q"],
    "stack6": ["W", "B", "D", "G", "R", "M", "P"],
    "stack7": ["G", "M", "N", "R", "C", "H", "L", "Q"],
    "stack8": ["C", "L", "W"],
    "stack9": ["R", "D", "L", "Q", "J", "Z", "M", "T"],
}

example_stacks = {
    "stack1": ["Z", "N"],
    "stack2": ["M", "C", "D"],
    "stack3": ["P"],
}


def apply_instructions(stacks: dict, instructions: list[Move]) -> dict:
    for move in instructions:
        move_stack = stacks[move.source][-move.n_crates :]
        for _ in range(int(move.n_crates)):
            _ = stacks[move.source].pop(-1)
        stacks[move.destination].extend(move_stack)
    return stacks


results = apply_instructions(stacks, instructions)
print()
print("Final result...")
pprint(results)

print("final string...")
fs = ""
for k, v in results.items():
    fs = fs + v[-1]
print(fs)
