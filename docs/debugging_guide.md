# Debugging Guide

This guide covers first-line diagnostics for UniverseBox.

## 1. Logs

### Recommended log fields

- `timestamp`
- `level`
- `subsystem` (sim, bridge, client, persistence)
- `seed`
- `tick`
- `event_id` / `command_id`
- `message`

### Log usage tips

- Always correlate Godot-side visual issues with Python tick logs.
- Capture both bridge input and output when debugging desync.
- Keep a reproducible log bundle for seed-related bugs.

## 2. Seed Diagnostics

Deterministic behavior is critical for reproducibility.

### Checklist

1. Confirm seed value at startup is logged by both runtimes.
2. Verify no unseeded random source is used.
3. Re-run the same seed and compare snapshot hashes by tick.
4. Ensure system execution order has not changed.
5. Confirm schema versions match between sender and receiver.

### Typical seed bug symptoms

- Same seed produces different world layout.
- Divergence begins after specific event type.
- Replay differs from live run after load.

## 3. Startup Troubleshooting

### Symptom: Python service starts, Godot shows no world

- Verify bridge transport endpoint/port configuration.
- Confirm first `WorldSnapshot` is emitted.
- Check schema compatibility negotiation logs.
- Confirm Godot parser accepted payload.

### Symptom: Godot starts, Python fails immediately

- Validate Python environment and dependencies.
- Check config file parse errors.
- Run simulation in headless debug mode for stack trace.

### Symptom: Startup hangs on "connecting"

- Check transport reachability and firewall rules.
- Inspect timeout/retry settings.
- Use local loopback transport for baseline verification.

## 4. Minimal Triage Workflow

1. Reproduce with fixed seed.
2. Capture startup logs from both runtimes.
3. Validate command/snapshot payloads against schema.
4. Compare expected vs actual tick progression.
5. Isolate failing subsystem and disable others.
6. Create a replay artifact for regression testing.
