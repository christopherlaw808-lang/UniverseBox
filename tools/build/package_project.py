"""Build-readiness checks and packaging prep for UniverseBox."""

from __future__ import annotations

from pathlib import Path

from tools.build.export_presets_helper import export_preset_guidance, has_export_presets
from tools.common.logging_utils import get_logger

logger = get_logger(__name__)


def check_build_readiness(project_root: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []

    if not (project_root / "project.godot").exists():
        issues.append("Missing project.godot file.")

    if not has_export_presets(project_root):
        issues.append("Missing export_presets.cfg file.")

    exports_dir = project_root / "exports"
    if not exports_dir.exists():
        issues.append("Missing exports/ directory.")

    return (len(issues) == 0, issues)


def prepare_packaging(project_root: Path) -> Path:
    out_dir = project_root / "dist"
    out_dir.mkdir(parents=True, exist_ok=True)
    logger.info("Packaging output directory ready: %s", out_dir)
    return out_dir


def format_build_issues(issues: list[str]) -> str:
    base = "Build readiness checks failed:\n- " + "\n- ".join(issues)
    return base + "\n\nAction: " + export_preset_guidance()
