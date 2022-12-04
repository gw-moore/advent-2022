from pathlib import Path
import sys

file = sys.argv[1]
lines = Path(file).read_text().split("\n")

elves: list[list[str]] = []
elf: list[str] = []
for line in lines:
    if line == "":
        elves.append(elf)
        elf = []
        continue
    elf.append(int(line))

# catch the last elf
elves.append(elf)
total = [sum(elf) for elf in elves]

print(f"Max calories: {max(total)}")
