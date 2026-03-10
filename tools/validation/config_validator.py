"""Configuration validation checks."""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_CONFIGS = [
    "config/project_settings.json",
    "config/simulation_defaults.json",
    "config/logging.json",
    "config/agent_settings.json",
]


def validate_config_files() -> list[str]:
    issues: list[str] = []
    for config in REQUIRED_CONFIGS:
        path = Path(config)
        if not path.exists():
            issues.append(f"Missing config: {config}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(f"Invalid JSON in {config}: {exc}")
    return issues
