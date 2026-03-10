"""Deterministic seed helper utilities."""

from __future__ import annotations

import random


def seed_to_rng(seed: int) -> random.Random:
    """Create a deterministic random generator for a seed."""
    return random.Random(seed)
