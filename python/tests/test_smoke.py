from python.core.engine import Engine
from python.gameplay.loop import next_tick
from python.simulation.world import create_world


def test_engine_description_contains_name() -> None:
    assert "UniverseBoxEngine" in Engine().describe()


def test_next_tick_increments() -> None:
    assert next_tick(4) == 5


def test_create_world_uses_seed() -> None:
    assert create_world(99)["seed"] == 99
