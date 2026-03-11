"""Basic service registry for subsystem wiring."""

from __future__ import annotations

from typing import Any, Dict


class ServiceRegistry:
    """Store and retrieve singleton-like services by name."""

    def __init__(self) -> None:
        self._services: Dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        self._services[name] = service

    def resolve(self, name: str) -> Any:
        if name not in self._services:
            raise KeyError(f"Service '{name}' is not registered")
        return self._services[name]
