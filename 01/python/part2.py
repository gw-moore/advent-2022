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

total = []
for elf in elves:
    total.append(sum(elf))

total.sort(reverse=True)

print(f"Top 3 calories: {total[0:3]}")
print(f"Total of the top 3 calories: {sum(total[0:3])}")
