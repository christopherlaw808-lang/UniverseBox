"""Grid-based deterministic planet generation."""

from __future__ import annotations

from python.simulation.resource_system import resources_for_terrain
from python.simulation.world_seed import seed_to_rng
from python.simulation.world_state import TileState

TERRAINS = ["water", "plains", "forest", "mountain", "desert"]


def generate_tiles(seed: int, width: int, height: int) -> list[TileState]:
    """Generate deterministic terrain/resource tiles for a map."""
    rng = seed_to_rng(seed)
    tiles: list[TileState] = []
    for y in range(height):
        for x in range(width):
            noise = rng.random() + (y / max(1, height)) * 0.15
            if noise < 0.20:
                terrain = "water"
            elif noise < 0.45:
                terrain = "plains"
            elif noise < 0.65:
                terrain = "forest"
            elif noise < 0.85:
                terrain = "mountain"
            else:
                terrain = "desert"
            tiles.append(TileState(x=x, y=y, terrain=terrain, resources=resources_for_terrain(terrain)))
    return tiles
