"""Packaging utility for build preparation."""

from pathlib import Path


REQUIRED_BUILD_PATHS = ["godot/project.godot", "config/project_settings.json", "README.md"]


def verify_build_ready() -> list[str]:
    issues: list[str] = []
    for item in REQUIRED_BUILD_PATHS:
        if not Path(item).exists():
            issues.append(f"Missing required build file: {item}")
    return issues
