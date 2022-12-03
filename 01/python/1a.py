from pathlib import Path
import sys

file = sys.argv[1]
lines = Path(file).read_text().split("\n")

elfs: list[list[str]] = []
elf: list[str] = []
for line in lines:
    if line == "":
        elfs.append(elf)
        elf = []
        continue
    elf.append(int(line))

# catch the last elf
elfs.append(elf)

total = []
for elf in elfs:
    total.append(sum(elf))

print(f"Max calories: {max(total)}")
