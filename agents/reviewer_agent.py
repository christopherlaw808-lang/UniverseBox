"""Reviewer agent for architecture and quality checks."""

from __future__ import annotations

import logging

LOGGER = logging.getLogger(__name__)


class ReviewerAgent:
    def review(self, scope: str) -> list[str]:
        LOGGER.info("ReviewerAgent reviewing scope: %s", scope)
        return [
            "Check modular boundaries",
            "Check documentation updates",
            "Check risk and safety constraints",
        ]
