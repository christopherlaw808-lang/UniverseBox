from python.simulation.world_seed import seed_to_rng


def test_seed_rng_is_deterministic():
    a = seed_to_rng(12).random()
    b = seed_to_rng(12).random()
    assert a == b
