"""Logging setup for UniverseBox tools and simulation services."""

from __future__ import annotations

import json
import logging
from pathlib import Path


DEFAULT_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging(config_path: str = "config/logging.json") -> None:
    """Configure console and file logging with safe defaults."""
    config_file = Path(config_path)
    level_name = "INFO"
    console_enabled = True
    file_enabled = True
    file_path = Path("logs/universebox.log")
    log_format = DEFAULT_FORMAT

    if config_file.exists():
        with config_file.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        level_name = payload.get("level", level_name)
        console_enabled = payload.get("console", console_enabled)
        file_enabled = payload.get("file", file_enabled)
        file_path = Path(payload.get("file_path", str(file_path)))
        log_format = payload.get("format", log_format)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    level = getattr(logging, level_name.upper(), logging.INFO)

    handlers: list[logging.Handler] = []
    if console_enabled:
        handlers.append(logging.StreamHandler())
    if file_enabled:
        handlers.append(logging.FileHandler(file_path, encoding="utf-8"))

    logging.basicConfig(level=level, format=log_format, handlers=handlers, force=True)
