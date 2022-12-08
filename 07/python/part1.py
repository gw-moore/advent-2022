from __future__ import annotations

from pathlib import Path
from rich import print
from rich.pretty import pprint
from dataclasses import dataclass, field

path = Path(__file__).parents[1] / "data.txt"
lines = Path(path).read_text().split("\n")


@dataclass
class File:
    size: int
    name: str


def all_files(d: Dir) -> list[File]:
    """Return of list of all files in the dir and child dirs"""
    files = d.files
    for c in d.child_dirs.values():
        files.append(*all_files(d))


@dataclass
class Dir:
    name: str
    files: list[File] = field(default_factory=list)
    child_dirs: list[Dir] = field(default_factory=dict)
    parent: Dir | None = None

    @property
    def size(self) -> int:
        files_and_dirs = [*self.files, *self.child_dirs.values()]
        sizes = map(lambda x: x.size, files_and_dirs)
        return sum(sizes)

    def child_dirs_and_self(self) -> list[Dir]:
        result = [self]
        for d in self.child_dirs.values():
            result.extend(d.child_dirs_and_self())
        return result


root_dir = Dir(name="home", files=[], child_dirs={}, parent=None)
cur_dir = root_dir


def walk_list(lines: list[str]):
    while len(lines) > 0:
        line = lines.pop(0)
        line = line.split()

        match line:
            case ["$", "cd", "/"]:
                pprint("Starting in the home directory")
                cur_dir = root_dir
            case ["$", "cd", ".."]:
                pprint(f"Going back up a level from {cur_dir.name} to {cur_dir.parent.name}")
                cur_dir = cur_dir.parent
            case ["$", "ls"]:
                pprint(f"Listing objects in the {cur_dir.name} directory")
            case ["dir", dir_name]:
                print(f"\t[red] found dir {dir_name} in {cur_dir.name}")
                new_dir = Dir(name=dir_name, files=[], child_dirs={}, parent=cur_dir)
                # update the current dir with a child directory
                cur_dir.child_dirs[dir_name] = new_dir
            case [size, file_name]:
                print(f"\t[blue] found file {file_name} in {cur_dir.name} - size = {size}")
                cur_dir.files.append(File(size=int(size), name=file_name))
            case ["$", "cd", dir_name]:
                pprint(f"Going down a level from {cur_dir.name} to {dir_name}")
                cur_dir = cur_dir.child_dirs[dir_name]
            case _:
                print(line)
                raise ValueError("Missing a case statement")


walk_list(lines)
all_dirs = root_dir.child_dirs_and_self()
answer = 0
for d in all_dirs:
    if d.size <= 100000:
        answer += d.size

print(f"Answer: {answer}")
