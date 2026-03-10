# Module Guide

## Core
Shared services (`logging_system`, `config_loader`, `event_bus`, `service_registry`).

## Simulation
Owns world state, generation, and ticks. This is the source of truth for deterministic behavior.

## Gameplay stubs
Placeholder modules to be replaced by concrete systems incrementally.

## Persistence
JSON save/load via `SaveManager`.

## Tooling
Validation/debug/build scripts intended for local-first workflows.
