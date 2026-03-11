"""Sanity checks for generated world states."""

from __future__ import annotations

from python.simulation.world_state import WorldState


REQUIRED_TERRAINS = {"water", "plains", "forest", "mountain", "desert"}


def validate_world_state(state: WorldState) -> list[str]:
    issues: list[str] = []
    if state.width * state.height != len(state.tiles):
        issues.append("Tile count does not match width*height")
    terrains = {tile.terrain for tile in state.tiles}
    if terrains.isdisjoint(REQUIRED_TERRAINS):
        issues.append("No expected terrain types found")
    return issues
