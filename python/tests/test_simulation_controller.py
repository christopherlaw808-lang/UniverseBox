import pytest

from universebox.simulation.simulation_controller import SimulationController
from universebox.simulation.world_state import WorldState


def test_simulation_tick_only_advances_when_running() -> None:
    controller = SimulationController(state=WorldState())

    assert controller.tick() == 0

    controller.start()
    assert controller.tick() == 1
    assert controller.state.phase == "running"

    controller.stop()
    assert controller.tick() == 1
    assert controller.state.phase == "stopped"


def test_simulation_tick_rejects_negative_steps() -> None:
    controller = SimulationController(state=WorldState())
    controller.start()

    with pytest.raises(ValueError):
        controller.tick(-1)
