# UniverseBox

UniverseBox is a modular simulation sandbox foundation designed for emergent world development. This repository provides a first milestone prototype that combines:

- Python simulation/core tooling.
- Godot 4 starter client scenes/scripts.
- Debug-first workflows (logs, validators, test harnesses).
- AI-agent scaffolding for assisted iterative development.

## Milestone status

✅ Milestone 1 bootstrap complete:
- Deterministic seeded world generation.
- Terrain/resource layers.
- Time progression controls (pause/play/speed).
- Save/load world state stub.
- Debug overlay hooks.
- Local automation scripts and tests.

## Setup

1. Use Python 3.12+.
2. (Recommended) create a virtual environment:
   - `python -m venv .venv`
   - `source .venv/bin/activate` (Linux/macOS) or `.venv\\Scripts\\activate` (Windows)
3. Install Python dependencies:
   - `pip install -r requirements.txt`
4. Run environment validation:
   - `python setup_env.py`

## Run

- Development checks + launch guidance:
  - `python run_dev.py`
- Run Python tests:
  - `python run_tests.py`

Godot launch:
- Open `godot/project.godot` in Godot 4.x.
- Main scene is configured to `res://scenes/main.tscn`.

## Project structure overview

- `python/`: simulation, core services, persistence, tests.
- `godot/`: playable/viewable prototype scenes and scripts.
- `tools/`: bootstrap, validation, debugging, build helpers.
- `agents/`: planner/coder/debugger/reviewer/orchestrator starter agents.
- `docs/`: architecture, roadmap, coding standards, debugging guides.

## Next roadmap steps

See `docs/roadmap.md` for the full phased plan:
- Phase 2 ecosystems.
- Phase 3 civilizations.
- Phase 4 diplomacy/conflict.
- Phase 5 player scenario tools.
- Phase 6 advanced AI-driven evolution.
