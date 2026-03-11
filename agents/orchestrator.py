"""Orchestrator for local task queue coordination."""

from __future__ import annotations

import json
from pathlib import Path

from agents.task_models import AgentTask


class Orchestrator:
    def __init__(self, queue_path: str = "agents/tasks.json") -> None:
        self.queue_path = Path(queue_path)

    def load_tasks(self) -> list[AgentTask]:
        if not self.queue_path.exists():
            return []
        payload = json.loads(self.queue_path.read_text(encoding="utf-8"))
        return [AgentTask(**item) for item in payload]

    def save_tasks(self, tasks: list[AgentTask]) -> None:
        serialized = [task.__dict__ for task in tasks]
        self.queue_path.write_text(json.dumps(serialized, indent=2), encoding="utf-8")
