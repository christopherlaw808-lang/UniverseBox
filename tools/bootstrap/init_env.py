"""Initialize repository runtime directories and sanity checks."""

from pathlib import Path


def init() -> None:
    for rel in ("logs", "saves"):
        Path(rel).mkdir(exist_ok=True)


if __name__ == "__main__":
    init()
    print("Bootstrap complete.")
