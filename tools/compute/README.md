# Local preflight and bounded Colab transport

> English | [简体中文](README.zh-CN.md)

Status for Issue #66: **OFFLINE_VALIDATED + LIVE_MULTI_GPU_PROBED**. The verified CLI0.7.4 request set is **T4, L4, G4, H100, A100**; it is not a guarantee of account entitlement or hardware availability. At tested source `d4e4185d153976e7b966b7a4a1623c6cf80543cb`, T4/L4/A100 transport passed; G4 was observed as RTX PRO6000 Blackwell and correctly blocked as DEVICE_MISMATCH, and H100 was refused by the provider. All five attempts completed authenticated-zero cleanup and post-run readback. See [per-type evidence](../../reports/compute-multi-gpu/ENGINEER_HANDOFF.md). This is three standalone Python files, not a package, daemon, bootstrap installer or publisher. Algorithms and scientific acceptance belong to the project driver; [source/license/dependency provenance](NOTICE.md).

Historical [PR #48](https://github.com/JohnnyZPiggy/SAE-Framework/pull/48) tested source `8081b6e02eee0754903898d5afe5b112f1bb23d0` with a T4 request but no observed identity. That older evidence does not establish the new multi-device interface.

| Component | Dependency | Scope |
|---|---|---|
| `environment_preflight.py` | Python standard library + installed Git | Exact commit, dirty state, blob export, writable non-synced temporary paths |
| `colab_control.py`, `kernel_smoke.py` | Standard library + existing `colab`; remote `nvidia-smi`, optional installed torch | One bounded GPU session at a time, strict observed identity, transport and cleanup |
| Explicit `--install-local` | Existing Python pip/build backend | Optional no-deps temporary project install; never default |
| Project adapter | Project chooses dependencies | Scientific code, exact-source install, real device checks and outputs |

Earlier local evidence used Windows Python3.12.14 and WSL Python3.12.3; current versions are recorded with each run. Only audited CLI0.7.4 is accepted for authenticated readback. `--device` defaults to T4; unknown types raise `UNSUPPORTED_DEVICE` before CLI invocation (the CLI itself silently falls back to A100 on unknown names). CPU/TPU/XLA runners and native compilation are not implemented here.

## Pinning and local-only use

For future projects, copy/reference only the three runtime files from an **exact SAE commit/tag** with their MIT notice. Keep them adjacent. Record that tool pin separately from the algorithm's `--source-sha`; the report records runtime-file hashes. No floating `main`, migration of existing project `.sae/`, all-document-snapshot copy, package publishing or bootstrap/publisher changes are required.

From the same shell that will launch production (an existing WSL login shell if needed):

```sh
python tools/compute/colab_control.py --preflight-only --cli colab \
  --repo-path path/to/project --source-sha CANDIDATE_40_HEX_SHA \
  --run-id local-check-1 --out local-evidence/new-run
```

Replace the path/SHA with an existing local project checkout and full immutable commit. Preflight only calls CLI `version` and local Git/filesystem operations; no credentials, sessions, usage, allocation, driver execution or login fallback. Exact export uses `ls-tree`/`cat-file` bytes independent of dirty CRLF checkout. `.sae/` is excluded from temporary project export; its immutable documentation is not copied into every command. Other regular tracked files are exported; symlinks/submodules/unsafe paths are rejected. Temporary build/cache paths must be writable, outside checkout and Dropbox; `--temp-root` overrides OS temp without global settings changes. `--install-local` is explicit and uses existing pip/build requirements with no dependency installation; default is no install.

## Project-owned adapter contract

Live execution is **not needed** to use the example or complete local validation. In a separately scoped compute task, add `--driver scripts/my_driver.py --artifacts experiments/artifacts.json` and remove `--preflight-only`. Both paths must refer to regular committed files **inside `--repo-path` at `--source-sha`**. Absolute/traversal paths and symlink adapters are rejected. Dirty local adapters are ignored; exact Git blobs are used. The self-contained driver is temporarily staged outside the checkout and its transport SHA is recorded separately. It receives `SAE_CANDIDATE_SHA` with the verified project commit, and decides how to install/run project code without GitHub writes. Generic transport does not contain repository URLs or algorithm installation logic.

The project's small manifest is:

```json
{"artifacts": [{"name": "measurement.json"}]}
```

## Requested and observed device; sequential types

The kernel first prints `KERNEL_REACHABLE`, then exactly one `DEVICE_OBSERVED`
JSON line. It reads `nvidia-smi --query-gpu=name,memory.total,driver_version
--format=csv,noheader` (10s subprocess bound). If torch imports, it also records
torch/CUDA versions, device0 name and capability. Missing/malformed identity
blocks work; no torch installation is attempted.

`device_requested` and `device_observed` are separate fields. Every observed
name must contain the requested family as a token; no automatic SKU mapping or
relabeling. A mismatch sets `classification=DEVICE_MISMATCH` and skips work by
default. Only an exact top-level `SAE_ALLOW_DEVICE_MISMATCH = True` declaration
in the committed project driver opts in. Even then the mismatch classification
is preserved. The driver receives `SAE_DEVICE_REQUESTED` and JSON
`SAE_DEVICE_OBSERVED` in addition to `SAE_CANDIDATE_SHA`.

Use either `--device T4` or `--devices T4,L4,G4,H100,A100`. The latter creates a
new root output directory with per-type subdirectories and `colab-devices.json`.
The root run ID is at most35 characters (single-type40), reserving the suffix.
Each type completes its own allocate/probe/work/download/stop/zero/consumption
cycle before the next starts. Exact recognized provider refusal messages become
`BLOCKED_PROVIDER:<type>:<reason>`; other types continue only after cleanup and
post-run authenticated zero. Unverified cleanup/readback stops the sequence and
marks remaining types NOT_RUN. No overlapping sessions, automatic retry or
purchase. CLI support does not establish billing entitlement: existing positive
balance and provider-enforced access remain mandatory; uncertain external
billing boundaries must be reported BLOCKED_BILLING_UNCERTAIN, not bypassed.
An operator interrupt stops the remaining sequence after the active cycle's cleanup.

For research-sized work explicitly select finite budgets, for example
`--task-seconds 14400 --allocation-seconds 10800 --work-timeout 3600
--cleanup-seconds 120`. Budgets apply **per type**, not to an unbounded scheduler.
Existing adopted projects keep their old pins; adopting this revision requires
a separate project pin change, not a side effect of running the controller.

Initial contract: 1–16 JSON output basenames, each at most 1 MiB, remote `/content/<name>`; no nested/absolute paths, control-report collision, Windows reserved device name or case-insensitive duplicate. Manifest is at most 64 KiB; driver at most 1 MiB. Each declared artifact must be a JSON object with exact `source_sha` and `status: "PASS"`. A non-passing required artifact fails transport. Put optional `NOT_RUN` observations inside a passing primary report rather than declaring them passing required outputs. Duplicate JSON keys are rejected. Driver emits exactly one line per required file:

```text
ARTIFACT measurement.json BYTE_COUNT SHA256_HEX
```

After bounded downloads, the controller verifies byte count/hash, JSON source identity and declared status. This is **not a numerical oracle**: `PASS` with `TRANSPORT_ONLY_SCIENCE_UNREVIEWED` means transport/provenance and declared status passed, not GPT scientific acceptance. The project must preserve independent mathematical/numerical evidence. Artifact payloads remain project-owned and are not secret-scrubbed by transport; separate publication must screen them.

The [example driver](../../examples/compute_adapter/driver.py) and [manifest](../../examples/compute_adapter/artifacts.json) only emit a transport fixture, explicitly `live_gpu/tpu/compilation: NOT_RUN`. A regression test runs it in a local temporary directory with a real local Git SHA, requiring no provider allocation or package install:

```sh
python -m unittest discover -s tools/compute/tests -v
```

## Bounds and evidence

For allocation failures, see the [offline CLI 0.7.4 call-chain diagnosis](diagnostics/README.md). HTTP request timeouts differ from the outer process bound; an outer timeout cannot identify GET versus POST. Do not poll `status` during allocation: it synchronizes remote assignments and may modify local session state. This controller has no status observer loop.

New output directory and explicit run ID are required; existing output is never overwritten. Before allocation, unknown/unrelated active sessions or unconfirmed positive entitlement block. Every fresh `new` gets `kernel_smoke.py` with a default 30-second remote/35-second external limit, capped by remaining main budget. Missing marker, error or timeout records `KERNEL_PROBE_FAILED`, skips workload and enters cleanup. Later workloads can still hang; they have separate finite external bounds. No assertion that this fixes the original pilot hang.

Finite defaults stay task5400s, allocation-window600s, cleanup reserve60s, kernel30s and work240s. Maxima are task14400s, allocation-window10800s, kernel60s and work3600s. NaN/infinity/zero and inconsistent budgets reject. The allocation window bounds the **entire live session**, reserving cleanup; the `new` subprocess remains capped at120s, kernel external bound is kernel+5s and workload external bound is work+5s. At most two stop+authenticated-zero checks share the cleanup reserve. After a confirmed stop/zero, a separate authenticated `post_cleanup` usage call records balance_after, assignments_after and observed balance_delta. Failure of this last readback is POST_RUN_READBACK_FAILED (prior stop/zero remains recorded); the multi-type loop does not advance. Unknown release is CLEANUP_FAILED, never PASS. OS termination or provider/network failure can still prevent release; mocks do not prove live cleanup.

Balances are the CLI's rounded compute-unit observations, not an invoice or a
claim of exact monetary charges. No plan/top-up/pay-as-you-go command is used.

Readback is pinned to the audited CLI **0.7.4** path: `usage` directly performs authenticated `GET /tun/m/ccu-info`, validates the response and formats balance/rate/assignment count. It does not use `sync_sessions()` or swallow authentication SystemExit. Before allocation, require exit 0, the complete three-line stdout contract, assignment count 0 and positive balance. After stop, require a fresh complete usage response with count 0 **and successful stop**; cleanup does not require positive balance. `sessions` exit 0/empty text, empty stdout, warnings, duplicates, malformed output, auth failure, unsupported CLI version and timeouts cannot establish authenticated zero. They block allocation with `READBACK_UNVERIFIED` or leave `cleanup_confirmed=false` / `CLEANUP_FAILED`; nonzero assignments also block. Raw stderr is never parsed as success evidence. A positive usage balance is existing entitlement, not proof of exact charges. This trusts the audited installed CLI/Google authenticated-response semantics, not arbitrary executables reporting that version, and does not attest concurrent account activity after the response. No new provider API, credential handling or vendor patch is introduced.

Reports contain safe codes, command operation/timing, UTC/monotonic events, source and adapter hashes. Raw output/argv, private roots, OAuth/session URLs and environment dumps are omitted. Unobserved installation/CPU/publication/human approval/handoff fields remain null; no GitHub write occurs in this tool. Issue66 establishes observed GPU identity and transport only; GPU science, TPU and compilation remain NOT_RUN. [Local evidence](../../reports/compute-issue38/summary.md) records exact tested source and observed tests; GPT reviews and decides merge independently.
