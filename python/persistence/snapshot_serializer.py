"""Convert world state objects to/from JSON-compatible payloads."""

from __future__ import annotations

from python.simulation.world_state import WorldState


def serialize_state(state: WorldState) -> dict:
    return state.to_dict()


def deserialize_state(payload: dict) -> WorldState:
    return WorldState.from_dict(payload)
