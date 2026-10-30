# Colab compute tools

> English | [简体中文](README.zh-CN.md)

Three standalone Python files: a local preflight and a bounded Colab GPU controller. They are not a package, daemon or publisher. Project drivers own the science. Provenance and license: [NOTICE](NOTICE.md).

| File | Does |
|---|---|
| `environment_preflight.py` | Checks the exact commit, dirty state and writable temp paths; exports the committed tree (standard library + Git) |
| `colab_control.py` | One GPU session per device type: zero-session check → allocate → probe device → run driver → download → stop → confirm zero |
| `kernel_smoke.py` | Remote probe: prints `KERNEL_REACHABLE` and one `DEVICE_OBSERVED` JSON line (from `nvidia-smi`, plus torch if importable) |

**Requires** Colab CLI **0.7.4**, already authenticated, in the shell that launches the run (on Windows, inside WSL). Supported requests: `T4`, `L4`, `G4`, `H100`, `A100`. G4 is matched against the observed `RTX PRO 6000`. Verified live: T4, L4, A100, G4. H100 was refused by the provider.

## Use
Local check first; this never allocates:
```sh
python tools/compute/colab_control.py --preflight-only --cli colab \
  --repo-path path/to/project --source-sha <40-hex> --run-id check-1 --out out/check-1
```
Live run with a project-committed driver and manifest:
```sh
python tools/compute/colab_control.py --cli colab --repo-path path/to/project \
  --source-sha <40-hex> --driver scripts/driver.py --artifacts experiments/artifacts.json \
  --devices T4,L4,A100,G4 --run-id m2b-1 --out out/m2b-1
```
For research-sized runs, set budgets explicitly, e.g. `--task-seconds 14400 --allocation-seconds 10800 --work-timeout 3600 --cleanup-seconds 120`. Budgets apply per device type.

## Adapter contract
- `--driver` and `--artifacts` are committed files inside `--repo-path`, read from the exact `--source-sha` (dirty copies are ignored).
- The manifest is `{"artifacts": [{"name": "result.json"}]}`. Names end in `.json` and contain no path separators. Each is downloaded from `/content/<name>` and must contain the exact `source_sha` and `"status": "PASS"`.
- The driver receives `SAE_CANDIDATE_SHA`, `SAE_DEVICE_REQUESTED` and `SAE_DEVICE_OBSERVED` (JSON).
- A device mismatch is `BLOCKED` unless you pass `--allow-device-mismatch`.

Example: [examples/compute_adapter](../../examples/compute_adapter/). It emits a transport fixture only.

## Safety behaviour
- Before allocating, an authenticated `usage` readback must show **0 active assignments and a positive balance**. Otherwise there is no allocation.
- After any allocation attempt, on success, failure or Ctrl-C: `stop`, then a fresh readback confirming 0 assignments. Unconfirmed release is `CLEANUP_FAILED` and halts a multi-device sequence.
- One session at a time; finite timeouts; no automatic retry; no purchase or billing command.
- Reports (`colab-control.json`, `colab-devices.json`) hold status, SHA, requested/observed device, assignments and balance before/after, artifact SHA-256 and command exit codes. Raw CLI output is never written: it can contain tokens or session URLs.
- `PASS` here means transport and provenance passed. It is **not** scientific acceptance; the project keeps its own numerical evidence.

## Test
```sh
python -m unittest discover -s tools/compute/tests
```
