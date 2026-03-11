"""Planner agent for breaking goals into executable tasks."""

from __future__ import annotations

import logging

from agents.task_models import AgentTask

LOGGER = logging.getLogger(__name__)


class PlannerAgent:
    def plan(self, goal: str) -> list[AgentTask]:
        LOGGER.info("PlannerAgent planning goal: %s", goal)
        return [
            AgentTask(id="plan-1", title="Analyze goal", description=goal, owner="planner"),
            AgentTask(id="plan-2", title="Define implementation slices", description="Create actionable tasks", owner="planner"),
        ]
