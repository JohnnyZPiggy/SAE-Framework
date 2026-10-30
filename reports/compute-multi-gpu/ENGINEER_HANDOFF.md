# ENGINEER_HANDOFF — SAE-Framework Issue #66

**OFFLINE_PASS / FIVE_TYPES_ATTEMPTED / THREE_TRANSPORT_PASS /
ONE_DEVICE_MISMATCH / ONE_BLOCKED_PROVIDER / NO_SELF_MERGE**

Repository: JohnnyZPiggy/SAE-Framework.
Branch: `feat/66-multi-gpu-controller`.
Base: `d84942e4890d9837ae0e6cbb379b85c3a95aba84`.
Clean committed original offline/live tested source:
`d4e4185d153976e7b966b7a4a1623c6cf80543cb`.
Final offline tested source (cancellation guard):
`5b8193b63e21f6066433273cbc1315d58fb4ed27`.
Final evidence-only HEAD is identified by the Draft PR/receipt, avoiding a
self-referential file hash. All three runtime script blobs are identical between
final offline-tested and final revisions; script-identity.json supplies SHA1
blobs/SHA256 and separately discloses the live-to-final controller difference.
The only post-live runtime change is a four-line stop-on-INTERRUPTED guard;
kernel_smoke/environment_preflight are also identical to live source. Existing
normal paths are unchanged. One live attempt per discovered type was preserved;
operator interruption is verified offline, not by another resource cycle.
SHA256SUMS covers all changed files except itself, canonical Git bytes.

CLAIM: https://github.com/JohnnyZPiggy/SAE-Framework/issues/66#issuecomment-6530426350

## Recovery and scope

Full Issue66, actual root AGENTS and applicable Engineer/compute contract read;
unchanged V3.3 constitution/role/COLD/WARM/task/security/lean evidence reused.
Main matched the dispatched base; no competing #66 branch/CLAIM/PR was present.
Standalone D:/sae-compute-66-20261030 checkout and independent feature branch;
no downstream worktree/pin/code/report edits. No role, merge authority or other
governance file changes. No CLI/provider patch, dependency installation or new
authentication setup. The existing CLI0.7.4/account were reused.

## What changed

- Verified canonical types T4,L4,G4,H100,A100, default T4; unsupported values fail
  UNSUPPORTED_DEVICE before any CLI operation. Existing CLI source silently
  falls back to A100 on unknown strings, so forwarding arbitrary names is unsafe.
- Kernel retains KERNEL_REACHABLE and adds strict DEVICE_OBSERVED JSON from
  nvidia-smi name/memory.total/driver_version plus optional installed torch
  version/CUDA/name/capability. No install or tensor science workload.
- Requested and observed identity remain distinct. Missing/malformed identity
  blocks work; mismatching family token sets DEVICE_MISMATCH. Only a literal
  top-level SAE_ALLOW_DEVICE_MISMATCH = True in the exact committed driver opts
  into work on mismatched hardware; classification/actual name are preserved.
- Finite bounds raised to task14400s, allocation-window10800s and work3600s;
  finite defaults unchanged. Kernel max60s, new subprocess max120s; allocation
  window bounds the full live session and reserves cleanup, not just new().
- Separate authenticated post_cleanup usage stores balance_after,
  assignments_after and observed balance_delta. Pre-allocation assignments0 and
  positive-balance guards unchanged; failed post-run readback cannot PASS.
- --devices runs finite per-type cycles sequentially. Recognized provider
  rejection stores exact trusted CLI message; loop continues after full cleanup
  and post-run zero. Unknown release/account state stops remaining allocations.
  Raw provider stderr/URLs/tokens are never published; unrecognized failure text
  is represented by scope/exit and its SHA256, not guessed as a provider refusal.
- English/Chinese compute docs and interface-message provenance updated; no
  adopted-project pin is changed automatically. Legacy adapter tuple/manifest
  schema and single-device entrypoint remain compatible.

## Discovery evidence

Read-only `colab new --help` and AST inspection of the installed CLI's
commands/session.py resolve_runtime_options GPU mapping agree on the five types.
discovery.json records exact module hashes, source lines, raw-help SHA256 and
exit codes. Runtime controller Python is WSL3.12.3; installed CLI entrypoint
uses Python3.15.0 and reports CLI0.7.4. No credential/config contents were
inspected or copied by the Engineer; authentication stayed inside the CLI.
Source assign() only selects existing runtime variant/accelerator; no pay,
purchase, top-up, subscription or billing-setting command was invoked.

Initial read-only discovery attempts encountered unavailable WSL rg and a
namespace-package origin=None. Standard-library source inspection using namespace
search locations resolved both without installing tools. One guessed local test
filename was absent; actual test inventory was read. No experiment failed here.

## Offline VALIDATE — PASS

Windows Python3.14.6 with existing pytest; no new environment/dependencies.
`python -B -m pytest tools/compute/tests -q -p no:cacheprovider
--junitxml=<TASK_ROOT>/evidence/validate/junit.xml` (180s outer bound).
Initial **46 passed,64 subtests passed,23.65s**, exit0, clean live-tested commit.
After the static cancellation finding, final **46 passed,65 subtests passed,
23.77s** at5b8193b, exit0. Its dirty flag reflects only pending README/NOTICE and
evidence metadata; all runtime/test source was committed, and the three executed
runtime files equal their Git blobs. Final revision preserves these blobs.
EXPLORE also passed46/64 on a declared dirty working tree; it is not mislabeled
as acceptance of the base revision. Raw outputs, JUnit and real commands retained.
Original test names remain present; no existing regression was dropped.

Coverage includes each supported device, unknown rejection before CLI, strict
identity with optional torch, default mismatch refusal and committed opt-in,
finite bound maxima/nonfinite values, post-run consumption/readback failure,
serial refusal-then-success, stopping on unconfirmed release, and cancellation
after cleanup without attempting another type. Existing
adapter integrity, auth/zero, output protection and real local child-timeout
tests still pass. No provider calls occur in offline tests.

## Live validation — transport and identity only

Exactly one new request per discovered type, ordered T4,L4,G4,H100,A100; four
actual allocations and one provider rejection. Parent report is deliberately
PARTIAL, not a fabricated all-PASS. All five attempts have successful stop,
authenticated cleanup zero and independent post_cleanup assignments0; timestamp
ordering and guards confirm no overlap. H100 rejection did not prevent A100.

| Requested | Observed | Result | Balance before / after | Final assignments |
|---|---|---|---|---|
| T4 | Tesla T4 | PASS | 58.90 / 58.90 | 0 |
| L4 | NVIDIA L4 | PASS | 58.90 / 58.90 | 0 |
| G4 | NVIDIA RTX PRO 6000 Blackwell Server Edition | DEVICE_MISMATCH | 58.90 / 58.90 | 0 |
| H100 | NOT_OBSERVED | BLOCKED_PROVIDER | 58.90 / 58.90 | 0 |
| A100 | NVIDIA A100-SXM4-40GB | PASS | 58.90 / 58.90 | 0 |

These are rounded compute-unit balance observations, not proof of zero monetary
cost or final settled consumption. No pricing or performance conclusions.

Observed memory/capability: T4 15360MiB/[7,5]; L4 23034MiB/[8,9];
G4 actual RTX PRO6000 97887MiB/[12,0]; A100 40960MiB/[8,0].
All observed devices: driver580.82.07,torch2.11.0+cu130,CUDA13.0.
G4 remains a mismatch under the specified family-token rule: no relabeling or
silent G4→RTX alias. Default example driver has no mismatch opt-in, so its
workload/download are NOT_RUN. This is a policy result, not failed identity.

Exact H100 safe provider message:

> [colab] Backend rejected accelerator 'H100'. You may not have quota or entitlement for this accelerator on your account. Try a different one (e.g. --gpu T4) or omit --gpu/--tpu for a CPU runtime.

The provider's text is ambiguous between quota and entitlement; no stronger
diagnosis, purchase or retry is inferred. H100 kernel/workload NOT_RUN.

Actual invocation is preserved in commands.json with private prefixes redacted:
`python3 tools/compute/colab_control.py --devices T4,L4,G4,H100,A100
--repo-path <LIVE_SOURCE> --source-sha d4e4185d153976e7b966b7a4a1623c6cf80543cb
--driver examples/compute_adapter/driver.py --artifacts examples/compute_adapter/artifacts.json
--run-id sae66-live-20261030 --out <TASK_ROOT>/evidence/live --cli <EXISTING_COLAB>
--temp-root <TASK_ROOT>/temp --task-seconds 900 --allocation-seconds 600
--cleanup-seconds 120 --kernel-timeout 60 --work-timeout 60`.
Dedicated local-only preflight passed before live execution. A clean detached
WSL Git snapshot on D avoids Windows worktree/CRLF ambiguity; runtime file bytes
match all three tested Git blobs. Driver and artifact manifest use framework's
existing trivial transport example, not a downstream repository.

Three downloaded transport-check.json artifacts are byte-identical originals;
controller verified remote announced lengths/SHA256, JSON status and source SHA.
raw-public-provenance.json records local byte counts/hash and sanitized-copy
transformations. Artifact `live_gpu: NOT_RUN` describes the trivial fixture's
lack of GPU computation; actual physical identity belongs to the separate kernel
report, not a scientific result in that fixture. No shader, math or performance
acceptance is inferred from metadata probes.

## Status, storage and next bounded action

PASS: implementation/offline regression, five real per-type attempts, requested
vs observed identity, three full transports/hashes, serial refusal continuation,
pre/post usage and authenticated-zero release. No numerical benchmark is run.
Static audit found and repaired the post-interrupt continuation bug after live
work finished; it was not exercised on real resources. The new interruption
subtest proves cleanup followed by NOT_RUN for remaining types. No extra live
attempts or repeat allocation were used to hide this source difference.

FAIL: no unexpected test or transport failure in this cycle; exact G4 mismatch
and H100 provider BLOCKED outcomes remain unchanged, not converted to PASS.
NOT_RUN: H100 kernel/workload; G4 workload without explicit opt-in; 3600s science
workload, cross-provider/other CLI-version verification, Actions, downstream pin
bump, science algorithms and releases. BLOCKED: H100 provider access; G4 work by
default mismatch policy. No new billing or self-approval/merge.

Owned root D:/sae-compute-66-20261030 holds checkout, immutable live-source,
original evidence and small helper scripts. All build/test/transport scratch is
on D; temp contains zero files after automatic owned-temp cleanup. Clones/logs
are retained for reproduction (snapshot counts in residue.json); no recursive
cleanup of shared paths and no large C:/WSL virtual-disk file. No downstream
project was modified, no pin bumped, no previous branch overwritten.

Next: Architect independently review exact final HEAD, three-script identity,
46/65 tests, strict mismatch/cancellation policy, refusal text and all five cleanup/usage
receipts. If accepted, Architect may merge; a downstream pin update is a separate
explicit PR. Any G4 alias/driver opt-in decision must preserve its actual name.
