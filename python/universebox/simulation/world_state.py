"""Serializable world-state contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping


@dataclass
class WorldState:
    """Canonical simulation state object suitable for persistence."""

    tick: int = 0
    phase: str = "initialized"
    planets: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tick": self.tick,
            "phase": self.phase,
            "planets": list(self.planets),
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "WorldState":
        tick = payload.get("tick", 0)
        phase = payload.get("phase", "initialized")
        planets = payload.get("planets", [])

        if not isinstance(tick, int) or tick < 0:
            raise ValueError("tick must be a non-negative integer")
        if not isinstance(phase, str) or not phase:
            raise ValueError("phase must be a non-empty string")
        if not isinstance(planets, list):
            raise ValueError("planets must be a list")

        return cls(tick=tick, phase=phase, planets=planets)
