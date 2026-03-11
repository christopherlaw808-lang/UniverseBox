"""Civilization system extension hook."""

from dataclasses import dataclass


@dataclass
class CivilizationStub:
    """Stub model for future civilization logic."""

    name: str
    population: int = 0
