"""Creature simulation extension hook."""

from dataclasses import dataclass


@dataclass
class CreatureStub:
    species: str
    vitality: int = 100
