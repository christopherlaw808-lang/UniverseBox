"""Configuration file checks for UniverseBox."""

from __future__ import annotations

import json
from pathlib import Path


def validate_json_config(config_path: Path) -> tuple[bool, str]:
    if not config_path.exists():
        return False, f"Config file is missing: {config_path}"

    try:
        json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return False, f"Invalid JSON in {config_path}: {exc}"

    return True, f"Valid JSON config: {config_path}"
