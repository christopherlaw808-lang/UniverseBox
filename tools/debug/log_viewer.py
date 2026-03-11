"""Simple log viewing utility."""

from __future__ import annotations

from pathlib import Path

from tools.common.logging_utils import get_logger

logger = get_logger(__name__)


def tail_log(log_path: Path, lines: int = 50) -> list[str]:
    if not log_path.exists():
        logger.error("Log file not found: %s", log_path)
        return []

    content = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    return content[-lines:]
