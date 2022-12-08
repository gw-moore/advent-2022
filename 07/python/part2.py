from __future__ import annotations

from pathlib import Path

path = Path(__file__).parents[1] / "data.txt"
lines = Path(path).read_text().split("\n")
DISK_SPACE = 70000000
