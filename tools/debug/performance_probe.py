"""Basic timing probe for tile generation."""

from __future__ import annotations

import time

from python.simulation.planet_generator import generate_tiles


def main() -> int:
    start = time.perf_counter()
    generate_tiles(seed=424242, width=128, height=128)
    elapsed = (time.perf_counter() - start) * 1000
    print(f"Generated 128x128 tiles in {elapsed:.2f} ms")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
