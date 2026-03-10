from universebox.simulation.world_seed import WorldSeed


def test_world_seed_from_string_is_deterministic() -> None:
    one = WorldSeed.from_input("Alpha Sector")
    two = WorldSeed.from_input(" alpha sector ")
    assert one.value == two.value
    assert one.source == two.source == "alpha sector"


def test_world_seed_derivation_is_stable() -> None:
    seed = WorldSeed.from_input("seed-01")
    assert seed.derive("planet:0") == seed.derive("planet:0")
    assert seed.derive("planet:0") != seed.derive("planet:1")
