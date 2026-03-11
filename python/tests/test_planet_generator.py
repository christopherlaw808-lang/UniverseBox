from universebox.simulation.planet_generator import PlanetGenerator
from universebox.simulation.world_seed import WorldSeed


def test_planet_generator_is_deterministic_for_same_seed() -> None:
    seed = WorldSeed.from_input("my-world")
    generator = PlanetGenerator()

    a = generator.generate(seed, planet_index=0)
    b = generator.generate(seed, planet_index=0)

    assert a == b


def test_planet_generator_changes_with_index_or_seed() -> None:
    generator = PlanetGenerator()
    seed_a = WorldSeed.from_input("my-world")
    seed_b = WorldSeed.from_input("another-world")

    first = generator.generate(seed_a, planet_index=0)
    second = generator.generate(seed_a, planet_index=1)
    third = generator.generate(seed_b, planet_index=0)

    assert first != second
    assert first != third
