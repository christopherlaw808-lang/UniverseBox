"""Simulation loop coordination."""

from __future__ import annotations

from dataclasses import dataclass

from .world_state import WorldState


@dataclass
class SimulationController:
    """Control simulation lifecycle and deterministic tick progression."""

    state: WorldState
    running: bool = False

    def start(self) -> None:
        self.running = True
        self.state.phase = "running"

    def stop(self) -> None:
        self.running = False
        self.state.phase = "stopped"

    def tick(self, steps: int = 1) -> int:
        if steps < 0:
            raise ValueError("steps must be non-negative")
        if not self.running:
            return self.state.tick
        self.state.tick += steps
        return self.state.tick
