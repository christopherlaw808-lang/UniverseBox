# UniverseBox Agent Framework

This folder contains lightweight local agents that coordinate planning, coding, debugging, and review workflows without requiring external APIs.

- `planner_agent.py`: decomposes goals into task plans.
- `coder_agent.py`: applies scoped edits and reports actions.
- `debugger_agent.py`: analyzes logs/tests and reports causes.
- `reviewer_agent.py`: performs checklist-style quality review.
- `orchestrator.py`: tracks task queue status transitions.
- `task_models.py`: shared typed models.
