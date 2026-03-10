"""Biome resolution from generated terrain types."""

from __future__ import annotations


def terrain_to_biome(terrain: str) -> str:
    """Return starter biome labels based on terrain type."""
    mapping = {
        "water": "aquatic",
        "plains": "temperate_grassland",
        "forest": "woodland",
        "mountain": "alpine",
        "desert": "arid",
    }
    return mapping.get(terrain, "unknown")
