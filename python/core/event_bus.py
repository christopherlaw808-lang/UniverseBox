"""Simple event bus for decoupled communication."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any


class EventBus:
    """Publish/subscribe event dispatcher."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[dict[str, Any]], None]]] = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable[[dict[str, Any]], None]) -> None:
        self._subscribers[event_name].append(callback)

    def publish(self, event_name: str, payload: dict[str, Any]) -> None:
        for callback in self._subscribers.get(event_name, []):
            callback(payload)
