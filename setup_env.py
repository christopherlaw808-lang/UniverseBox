#!/usr/bin/env python3
"""Bootstrap a local development environment for UniverseBox."""

from pathlib import Path


def main() -> None:
    for directory in ("saves", "logs"):
        path = Path(directory)
        path.mkdir(exist_ok=True)
        print(f"[setup] ensured {path}")


if __name__ == "__main__":
    main()
