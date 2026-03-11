"""Helpers for managing Godot export presets."""

from __future__ import annotations

from pathlib import Path

from tools.common.logging_utils import get_logger

logger = get_logger(__name__)


def has_export_presets(project_root: Path) -> bool:
    presets = project_root / "export_presets.cfg"
    exists = presets.exists()
    if exists:
        logger.info("Found export presets file: %s", presets)
    else:
        logger.warning("Missing export presets file: %s", presets)
    return exists


def export_preset_guidance() -> str:
    return (
        "Create export presets in Godot: Project > Export, then save. "
        "This will generate export_presets.cfg at the project root."
    )
