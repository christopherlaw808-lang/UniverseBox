"""Core engine model."""


class Engine:
    """Minimal engine stub for dev startup."""

    def __init__(self) -> None:
        self.name = "UniverseBoxEngine"
        self.version = "0.1.0"

    def describe(self) -> str:
        return f"{self.name} v{self.version} ready"
