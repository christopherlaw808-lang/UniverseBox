#!/usr/bin/env python3
"""Entry point for local development mode."""

from python.core.engine import Engine


def main() -> None:
    engine = Engine()
    print(engine.describe())


if __name__ == "__main__":
    main()
