"""Minimal schema validation placeholder utilities."""

from __future__ import annotations


def validate_required_keys(payload: dict, required_keys: set[str]) -> tuple[bool, list[str]]:
    missing = sorted(k for k in required_keys if k not in payload)
    return (len(missing) == 0, missing)
