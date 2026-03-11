"""Validate core project paths exist."""

from pathlib import Path

REQUIRED = [
    Path("python/core/engine.py"),
    Path("godot/scenes/main.tscn"),
    Path("config/settings.example.toml"),
]


def validate() -> bool:
    missing = [str(path) for path in REQUIRED if not path.exists()]
    if missing:
        print("Missing:", ", ".join(missing))
        return False
    print("Project structure validation passed.")
    return True


if __name__ == "__main__":
    raise SystemExit(0 if validate() else 1)
