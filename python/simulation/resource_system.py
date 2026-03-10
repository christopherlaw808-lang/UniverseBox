"""Resource assignment logic for starter tiles."""

from __future__ import annotations


def resources_for_terrain(terrain: str) -> dict[str, int]:
    """Provide simple deterministic base resources by terrain."""
    table = {
        "water": {"food": 1, "water": 5, "stone": 0, "metal": 0, "energy": 1},
        "plains": {"food": 4, "water": 2, "stone": 1, "metal": 0, "energy": 1},
        "forest": {"food": 3, "water": 2, "stone": 1, "metal": 1, "energy": 2},
        "mountain": {"food": 0, "water": 1, "stone": 4, "metal": 3, "energy": 1},
        "desert": {"food": 0, "water": 0, "stone": 2, "metal": 1, "energy": 3},
    }
    return table.get(terrain, {"food": 0, "water": 0, "stone": 0, "metal": 0, "energy": 0})
