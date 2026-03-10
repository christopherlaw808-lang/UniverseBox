"""Basic schema checks for key config fields."""

from __future__ import annotations

import json


PROJECT_REQUIRED_KEYS = {"project_name", "default_seed", "world_width", "world_height"}


def validate_project_settings(path: str = "config/project_settings.json") -> list[str]:
    issues: list[str] = []
    payload = json.loads(open(path, encoding="utf-8").read())
    missing = PROJECT_REQUIRED_KEYS - set(payload)
    for key in sorted(missing):
        issues.append(f"project_settings missing key: {key}")
    return issues
