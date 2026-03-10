from python.simulation.simulation_controller import SimulationController


def test_simulation_controller_tick_and_speed_changes():
    controller = SimulationController(seed=1, width=3, height=3)
    assert controller.state.tick == 0

    controller.step()
    assert controller.state.tick == 1

    controller.set_speed(4)
    controller.step()
    assert controller.state.tick == 5

    controller.set_speed(0)
    controller.step()
    assert controller.state.tick == 5
