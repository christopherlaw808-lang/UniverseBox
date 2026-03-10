"""Save/load helpers."""

import json
from pathlib import Path


def save_world(path: Path, world: dict) -> None:
    path.write_text(json.dumps(world, indent=2), encoding="utf-8")
