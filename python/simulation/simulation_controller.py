"""High-level simulation controller for world lifecycle."""

from __future__ import annotations

import logging

from python.simulation.planet_generator import generate_tiles
from python.simulation.time_system import TimeSystem
from python.simulation.world_state import WorldState

LOGGER = logging.getLogger(__name__)


class SimulationController:
    """Own world state generation and tick advancement."""

    def __init__(self, seed: int, width: int, height: int) -> None:
        self.time_system = TimeSystem()
        self.state = WorldState(
            seed=seed,
            width=width,
            height=height,
            tick=0,
            speed_multiplier=1,
            tiles=generate_tiles(seed, width, height),
        )
        LOGGER.info("Simulation created with seed=%s size=%sx%s", seed, width, height)

    def step(self) -> None:
        increment = self.time_system.tick_increment()
        self.state.tick += increment
        self.state.speed_multiplier = self.time_system.speed_multiplier

    def set_speed(self, speed_multiplier: int) -> None:
        self.time_system.set_speed(speed_multiplier)
        self.state.speed_multiplier = self.time_system.speed_multiplier
