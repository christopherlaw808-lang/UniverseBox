"""Configuration loader with fallback behavior."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

LOGGER = logging.getLogger(__name__)


class ConfigLoader:
    """Load JSON configuration files with fallback defaults."""

    def __init__(self, config_dir: str = "config") -> None:
        self.config_dir = Path(config_dir)

    def load(self, name: str, fallback: dict[str, Any] | None = None) -> dict[str, Any]:
        """Load a JSON configuration by filename stem."""
        fallback = fallback or {}
        target = self.config_dir / f"{name}.json"
        if not target.exists():
            LOGGER.warning("Missing config '%s'; using fallback defaults.", target)
            return dict(fallback)

        with target.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        if not isinstance(payload, dict):
            LOGGER.warning("Config '%s' is not an object; fallback applied.", target)
            return dict(fallback)
        return {**fallback, **payload}
