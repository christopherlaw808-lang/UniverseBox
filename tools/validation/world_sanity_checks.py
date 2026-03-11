"""Basic world data sanity checks."""

from __future__ import annotations

from pathlib import Path


def check_world_directory(worlds_dir: Path) -> tuple[bool, str]:
    if not worlds_dir.exists():
        return False, f"World directory missing: {worlds_dir}"

    world_files = list(worlds_dir.glob("*.json"))
    if not world_files:
        return False, "No world JSON files found. Add at least one file in worlds/."

    return True, f"Found {len(world_files)} world file(s)."
