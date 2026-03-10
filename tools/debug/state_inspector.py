"""Inspect saved world state snapshots."""

import json
from pathlib import Path


def main(path: str = "saves/last_save.json") -> int:
    target = Path(path)
    if not target.exists():
        print(f"Save file not found: {path}")
        return 1
    payload = json.loads(target.read_text(encoding="utf-8"))
    print(f"Seed: {payload['seed']}")
    print(f"Size: {payload['width']}x{payload['height']}")
    print(f"Tick: {payload.get('tick', 0)}")
    print(f"Tiles: {len(payload['tiles'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
