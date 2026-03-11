"""Environment validation helper."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_DIRS = ["config", "python", "godot", "docs", "logs", "saves"]


def verify() -> list[str]:
    issues: list[str] = []
    if sys.version_info < (3, 12):
        issues.append("Python 3.12+ is required.")
    for directory in REQUIRED_DIRS:
        if not Path(directory).exists():
            issues.append(f"Missing required directory: {directory}")
    return issues
