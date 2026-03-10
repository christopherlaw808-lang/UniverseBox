# UniverseBox
This file is the master bootstrap instruction document for an AI coding system. Its job is to generate the initial working foundation for a project called Universe Box.  Universe Box is a modular simulation sandbox and game-engine worlds, planets, ecosystems, civilizations, and player interaction. The first milestone is not a full commercial game.

UniverseBox is a **modular simulation sandbox** that combines Python-driven world simulation with Godot-based rendering and player interaction.

The project goal is to build a reusable foundation for generating worlds, ecosystems, civilizations, and emergent stories while keeping systems loosely coupled and testable.

## Milestone Status

> **Current milestone:** Bootstrap foundation and documentation complete.

- ✅ Project intent and architecture are documented.
- ✅ Core module boundaries and implementation expectations are defined.
- ✅ Phase roadmap (1–6) is documented.
- 🚧 Runtime systems are still in scaffold/prototype state.

## Setup

### Prerequisites

- Python 3.11+
- Godot 4.x
- Git

### Environment setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
# Install dependencies once requirements are added
# pip install -r requirements.txt
```

## Run / Test Commands

> Commands are the intended project interface while implementation is being built.

```bash
# Run Python simulation services/modules (example)
python -m universebox.sim

# Run Godot client/editor from project root
# (requires Godot project files)
godot --path .

# Run unit tests
pytest -q

# Run linting/format checks
ruff check .
black --check .
```

## Repository Structure Overview

```text
UniverseBox/
├── README.md
├── BOOTSTRAP_REPORT.md
└── docs/
    ├── architecture.md
    ├── roadmap.md
    ├── coding_standards.md
    ├── module_guide.md
    └── debugging_guide.md
```

As implementation is added, expected top-level folders include:

- `python/` (simulation domain logic, orchestration, tests)
- `godot/` (client scenes, scripts, UI, rendering adapters)
- `shared/` (schemas/contracts/constants used across boundaries)
- `tools/` (developer utilities, data generators, profiling scripts)

## Next Steps

1. Create initial `python/` and `godot/` skeletons with shared interfaces.
2. Implement deterministic seedable simulation tick loop in Python.
3. Define schema contracts for world snapshots and event streams.
4. Implement Godot-side ingestion and visualization of simulation snapshots.
5. Add smoke tests for startup, schema validation, and reproducibility.
6. Establish CI checks for linting, tests, and docs integrity.

For details, see:

- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Coding Standards](docs/coding_standards.md)
- [Module Guide](docs/module_guide.md)
- [Debugging Guide](docs/debugging_guide.md)
