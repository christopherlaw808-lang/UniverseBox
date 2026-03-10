"""Deterministic procedural planet generator."""

from __future__ import annotations

import random
from dataclasses import dataclass, asdict
from typing import Dict

from .world_seed import WorldSeed


@dataclass(frozen=True)
class PlanetProfile:
    climate: str
    gravity: float
    water_ratio: float
    size_class: str

    def to_dict(self) -> Dict[str, float | str]:
        return asdict(self)


class PlanetGenerator:
    """Generate reproducible planet data for a given seed and index."""

    CLIMATES = ("arid", "temperate", "frozen", "tropical", "rocky")
    SIZES = ("small", "medium", "large")

    def generate(self, seed: WorldSeed, planet_index: int) -> PlanetProfile:
        rng = random.Random(seed.derive(f"planet:{planet_index}"))
        return PlanetProfile(
            climate=rng.choice(self.CLIMATES),
            gravity=round(rng.uniform(0.4, 2.1), 3),
            water_ratio=round(rng.uniform(0.0, 1.0), 3),
            size_class=rng.choice(self.SIZES),
        )
