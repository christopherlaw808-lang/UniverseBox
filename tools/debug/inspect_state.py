"""Debug utility to inspect a minimal game state."""


def inspect() -> dict:
    state = {"players": 1, "world_loaded": True}
    print(state)
    return state


if __name__ == "__main__":
    inspect()
