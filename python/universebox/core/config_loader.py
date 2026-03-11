"""Configuration loader with deterministic fallback behavior."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "simulation": {
        "tick_duration": 1.0,
        "max_ticks": 10_000,
        "seed": "universebox-default",
    },
    "world": {
        "planet_count": 1,
        "resource_richness": 0.5,
    },
}


def _deep_merge(base: Dict[str, Any], override: Mapping[str, Any]) -> Dict[str, Any]:
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(base.get(key), dict):
            base[key] = _deep_merge(base[key], value)
        else:
            base[key] = value
    return base


class ConfigLoader:
    """Load JSON config files and merge with safe defaults."""

    def __init__(self, defaults: Optional[Mapping[str, Any]] = None) -> None:
        self.defaults = deepcopy(dict(defaults or DEFAULT_CONFIG))

    def load(self, path: Optional[str | Path] = None) -> Dict[str, Any]:
        config = deepcopy(self.defaults)
        if path is None:
            return config

        file_path = Path(path)
        if not file_path.exists():
            return config

        with file_path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)

        if not isinstance(loaded, Mapping):
            raise ValueError("Configuration root must be a JSON object")

        return _deep_merge(config, loaded)
