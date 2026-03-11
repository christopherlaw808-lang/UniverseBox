"""Simulation time-state management."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TimeSystem:
    """Track pause/play and speed multipliers."""

    speed_multiplier: int = 1
    paused: bool = False

    def set_speed(self, speed_multiplier: int) -> None:
        self.speed_multiplier = max(0, speed_multiplier)
        self.paused = self.speed_multiplier == 0

    def tick_increment(self) -> int:
        return 0 if self.paused else max(1, self.speed_multiplier)
