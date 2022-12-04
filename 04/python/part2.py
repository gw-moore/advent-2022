from dataclasses import dataclass
from pathlib import Path

path = Path(__file__).parents[1] / "data.txt"
section_pairs = [p.split(",") for p in Path(path).read_text().split("\n")]


@dataclass
class Section:
    section_ids: str

    def convert_to_set(self):
        section_range = self.section_ids.split("-")
        start = int(section_range[0])
        end = int(section_range[1])
        return set(list(range(start, end + 1)))


@dataclass
class SectionPair:
    section1: set
    section2: set

    @classmethod
    def from_list(cls, lst: list[str]):
        return cls(Section(lst[0]).convert_to_set(), Section(lst[1]).convert_to_set())

    def test_overlap(self) -> bool:
        overlap = self.section1.intersection(self.section2)
        return len(overlap) > 0


running_total = 0
for section_pair in section_pairs:
    elf_pair = SectionPair.from_list(section_pair)
    if elf_pair.test_overlap():
        running_total += 1

print(f"Total assignment paris that overlap at all: {running_total}")
