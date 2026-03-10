"""Serializable world state models."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class TileState:
    x: int
    y: int
    terrain: str
    resources: dict[str, int]


@dataclass
class WorldState:
    seed: int
    width: int
    height: int
    tick: int
    speed_multiplier: int
    tiles: list[TileState]

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: dict) -> "WorldState":
        tiles = [TileState(**tile) for tile in payload["tiles"]]
        return cls(
            seed=payload["seed"],
            width=payload["width"],
            height=payload["height"],
            tick=payload.get("tick", 0),
            speed_multiplier=payload.get("speed_multiplier", 1),
            tiles=tiles,
        )
