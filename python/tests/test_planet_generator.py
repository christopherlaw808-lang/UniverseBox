from python.simulation.planet_generator import generate_tiles


def test_planet_generation_is_deterministic_by_seed():
    first = generate_tiles(seed=99, width=4, height=3)
    second = generate_tiles(seed=99, width=4, height=3)
    assert [tile.terrain for tile in first] == [tile.terrain for tile in second]
    assert [tile.resources for tile in first] == [tile.resources for tile in second]
