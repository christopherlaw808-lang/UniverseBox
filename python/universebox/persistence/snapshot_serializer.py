"""Snapshot serializer for world state persistence."""

from __future__ import annotations

import json
from typing import Any, Dict

from universebox.simulation.world_state import WorldState


class SnapshotSerializer:
    """Serialize and deserialize :class:`WorldState` safely."""

    def dumps(self, state: WorldState) -> str:
        return json.dumps(state.to_dict(), sort_keys=True)

    def loads(self, payload: str) -> WorldState:
        data: Dict[str, Any] = json.loads(payload)
        return WorldState.from_dict(data)
