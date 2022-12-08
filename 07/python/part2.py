from __future__ import annotations

from pathlib import Path
from rich import print
from rich.pretty import pprint
from dataclasses import dataclass, field

path = Path(__file__).parents[1] / "data.txt"
lines = Path(path).read_text().split("\n")
DISK_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000


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
    child_dirs: dict[Dir] = field(default_factory=dict)
    parent: Dir | None = None

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


def get_dir_size(d: Dir) -> int:
    size = sum([f.size for f in d.files])
    for child in d.child_dirs.values():
        size += get_dir_size(child)

    return size


walk_list(lines)
all_dirs = root_dir.child_dirs_and_self()
dir_sizes = {d.name: get_dir_size(d) for d in all_dirs}
USED_SPACE = dir_sizes["home"]
AVAILABLE_SPACE = DISK_SPACE - USED_SPACE
SPACE_TO_FREE = REQUIRED_UNUSED_SPACE - AVAILABLE_SPACE
possible_dirs = {k: v for k, v in dir_sizes.items() if v > SPACE_TO_FREE}
dir_to_delete = min(possible_dirs, key=possible_dirs.get)

print(f"Answer: {dir_to_delete}: {dir_sizes[dir_to_delete]}")
