"""Datamodels for local task orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

TaskStatus = Literal["todo", "in_progress", "blocked", "complete"]


@dataclass
class AgentTask:
    id: str
    title: str
    description: str
    status: TaskStatus = "todo"
    owner: str = "unassigned"
