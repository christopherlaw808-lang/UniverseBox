"""Save/load manager for simulation state snapshots."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from python.persistence.snapshot_serializer import deserialize_state, serialize_state
from python.simulation.world_state import WorldState

LOGGER = logging.getLogger(__name__)


class SaveManager:
    """Persist simulation snapshots to local JSON files."""

    def __init__(self, save_dir: str = "saves") -> None:
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

    def save(self, state: WorldState, name: str = "last_save.json") -> Path:
        target = self.save_dir / name
        with target.open("w", encoding="utf-8") as handle:
            json.dump(serialize_state(state), handle, indent=2)
        LOGGER.info("Saved world state to %s", target)
        return target

    def load(self, name: str = "last_save.json") -> WorldState | None:
        target = self.save_dir / name
        if not target.exists():
            LOGGER.warning("Save file not found: %s", target)
            return None
        with target.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        LOGGER.info("Loaded world state from %s", target)
        return deserialize_state(payload)
