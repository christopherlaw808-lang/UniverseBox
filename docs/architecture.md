# Architecture

This document describes the intended technical boundaries and execution model for UniverseBox.

## 1. Python ↔ Godot Boundaries

UniverseBox separates responsibilities by domain:

### Python domain (authoritative simulation)

- World state and deterministic simulation logic.
- Economy/ecology/civilization rules.
- Save/load and snapshot generation.
- Event production and simulation telemetry.

### Godot domain (presentation + interaction)

- Rendering scenes and entities.
- UI/UX and player input.
- Camera, controls, overlays, debug panels.
- Playback of simulation state received from Python.

### Shared contract layer

- Typed schemas for snapshots, commands, and events.
- Versioning policy for payload compatibility.
- Optional adapters for serialization (`json`, `msgpack`, etc.).

**Principle:** Python owns truth; Godot owns experience.

## 2. Data Flow

The default data flow is unidirectional for stability:

1. Godot sends player/system commands (e.g., pause, inspect, apply action).
2. Python validates command and applies it in next simulation tick.
3. Python emits updated world snapshot + event delta.
4. Godot ingests snapshot and updates rendered state.
5. Diagnostics/metrics are emitted for logging and profiling.

### Communication options

- Local process bridge (stdin/stdout, pipes, local sockets).
- Embedded service layer (HTTP/WebSocket for tooling).
- File-based snapshot exchange for replay/testing.

## 3. Simulation Loop

The simulation loop is deterministic and seed-driven.

### Tick lifecycle

1. **Input gather:** collect queued commands.
2. **Pre-tick validation:** schema and invariants checks.
3. **System execution:** run systems in stable order.
4. **Conflict resolution:** resolve collisions/contention.
5. **State commit:** persist updated canonical state.
6. **Output publish:** emit snapshot/events/logs.

### Determinism requirements

- Fixed update order per system group.
- Seeded random generation routed through a shared RNG service.
- No direct wall-clock dependence in simulation rules.
- Versioned migration path for state schema updates.

## 4. Fault Tolerance and Recovery

- Startup performs contract compatibility checks.
- Invalid commands are rejected with explicit reason codes.
- Corrupt snapshots fail fast with actionable diagnostics.
- Optional checkpoint cadence supports rollback/replay.

## 5. Extensibility Model

- New systems are added through a registry and explicit phase ordering.
- Feature flags gate experimental modules.
- Simulation APIs are contract-first to avoid engine coupling.
