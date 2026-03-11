"""Project bootstrap checks and initialization helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from tools.common.logging_utils import get_logger

logger = get_logger(__name__)


def ensure_required_paths(project_root: Path, required_paths: Iterable[str]) -> list[str]:
    """Validate required paths and return missing entries."""
    missing: list[str] = []
    for rel_path in required_paths:
        candidate = project_root / rel_path
        if not candidate.exists():
            missing.append(rel_path)

    if missing:
        logger.warning("Missing required paths: %s", ", ".join(missing))
    else:
        logger.info("All required paths are present.")
    return missing


def initialize_project_structure(project_root: Path) -> None:
    """Ensure baseline directories exist to simplify first-time setup."""
    for path in ["assets", "worlds", "configs", "exports", "logs"]:
        target = project_root / path
        target.mkdir(parents=True, exist_ok=True)
        logger.debug("Ensured directory exists: %s", target)
