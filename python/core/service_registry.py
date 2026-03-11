"""Service registry for shared singleton-like services."""

from __future__ import annotations

from typing import Any


class ServiceRegistry:
    """Register and resolve services by explicit names."""

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        self._services[name] = service

    def resolve(self, name: str) -> Any:
        return self._services[name]
