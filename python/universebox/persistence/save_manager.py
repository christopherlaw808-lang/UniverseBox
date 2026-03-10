"""Save manager for world snapshots."""

from __future__ import annotations

from pathlib import Path

from universebox.persistence.snapshot_serializer import SnapshotSerializer
from universebox.simulation.world_state import WorldState


class SaveManager:
    """Persist and restore world states from disk."""

    def __init__(self, serializer: SnapshotSerializer | None = None) -> None:
        self.serializer = serializer or SnapshotSerializer()

    def save(self, state: WorldState, path: str | Path) -> None:
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(self.serializer.dumps(state), encoding="utf-8")

    def load(self, path: str | Path) -> WorldState:
        file_path = Path(path)
        return self.serializer.loads(file_path.read_text(encoding="utf-8"))
