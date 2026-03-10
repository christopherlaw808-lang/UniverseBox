"""Deterministic world seed utilities."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass


@dataclass(frozen=True)
class WorldSeed:
    """Canonical deterministic seed representation."""

    source: str
    value: int

    @classmethod
    def from_input(cls, raw_seed: int | str) -> "WorldSeed":
        if isinstance(raw_seed, int):
            normalized = str(raw_seed)
            value = raw_seed & 0xFFFFFFFF
        else:
            normalized = raw_seed.strip().lower()
            digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
            value = int(digest[:8], 16)
        return cls(source=normalized, value=value)

    def derive(self, namespace: str) -> int:
        digest = hashlib.sha256(f"{self.value}:{namespace}".encode("utf-8")).hexdigest()
        return int(digest[:8], 16)
