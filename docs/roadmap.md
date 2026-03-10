# Roadmap

This roadmap defines six implementation phases for UniverseBox.

## Phase 1 — Foundation & Contracts

- Establish repository layout for Python, Godot, and shared contracts.
- Define initial schemas for `WorldSnapshot`, `SimulationCommand`, `SimulationEvent`.
- Add developer tooling baseline (format, lint, test, docs checks).
- Implement deterministic RNG utility and seed wiring skeleton.

**Exit criteria:** contracts compile/validate, tooling runs in CI, seed tests pass.

## Phase 2 — Core Simulation Kernel

- Implement tick scheduler and system registry.
- Add canonical world state container and versioning.
- Introduce command queue and validation pipeline.
- Emit minimal snapshots/events each tick.

**Exit criteria:** simulation runs headless for N ticks with reproducible state.

## Phase 3 — Godot Integration Layer

- Build communication bridge (initial local transport).
- Parse and render world snapshot in Godot scene graph.
- Add debug overlay for tick number, seed, and key counters.
- Support basic command round-trip (pause/resume/inspect).

**Exit criteria:** live state can be visualized and controlled from Godot.

## Phase 4 — Gameplay Systems (MVP)

- Add foundational systems (terrain, ecology, population).
- Add simple event generation and event log UI.
- Implement save/load pipeline for snapshots.
- Add balancing hooks and configuration files.

**Exit criteria:** playable sandbox loop with stable save/load.

## Phase 5 — Tooling, QA, and Performance

- Add profiling harness for tick cost by subsystem.
- Expand automated tests (schema, deterministic replay, integration).
- Add startup diagnostics and troubleshooting commands.
- Optimize hot paths and data serialization.

**Exit criteria:** agreed performance targets met for baseline scenario.

## Phase 6 — Expansion & Hardening

- Add advanced systems (civilizations, diplomacy, macro events).
- Improve UX, onboarding, and mod extension points.
- Harden backward compatibility and migration tooling.
- Prepare release candidate with documentation freeze.

**Exit criteria:** release readiness checklist complete.
