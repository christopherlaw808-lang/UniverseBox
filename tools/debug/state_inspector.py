"""State snapshot helper for quick diagnostics."""

from __future__ import annotations

from pathlib import Path


def collect_state_snapshot(project_root: Path) -> dict[str, object]:
    return {
        "project_root": str(project_root),
        "has_project_file": (project_root / "project.godot").exists(),
        "directory_count": sum(1 for p in project_root.iterdir() if p.is_dir()),
        "file_count": sum(1 for p in project_root.iterdir() if p.is_file()),
    }
