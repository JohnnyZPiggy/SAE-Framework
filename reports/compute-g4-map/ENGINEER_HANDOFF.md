# ENGINEER_HANDOFF — SAE-Framework #68

**OFFLINE_PASS / ONE_REAL_G4_PROBE_PASS / NO_DOWNSTREAM_CHANGE / NO_SELF_MERGE**

Base: `de9833b56768a522cbc438244a941737b63293e9`.
Branch: `feat/68-g4-family-map`.
Clean offline/live tested source: `d55a5c4330f7f02dfb1ce82ca68c469d334991a2`.
Final metadata-only HEAD is recorded in the PR comment. All three final runtime
scripts equal their tested Git blobs; script-identity.json records SHA1/SHA256.
SHA256SUMS covers all changed files except itself, canonical Git bytes.

CLAIM: https://github.com/JohnnyZPiggy/SAE-Framework/issues/68#issuecomment-6531738377

## Change and verification

Full Issue68 read; inherited #66 controller contract, immutable constitution,
Engineer/security/compute policy and previous environment evidence reused.
Main/base and ownership conflicts checked. Standalone D-drive worktree, separate
from TorchOED #18. No governance, role, pin or downstream project file changed.

Replaced the literal requested-name test with an explicit case-insensitive
word-boundary family map: T4→T4, L4→L4, A100→A100, H100→H100,
G4→RTX PRO 6000. Full actual hardware name remains unchanged in device_observed.
Unknown mappings raise DEVICE_IDENTITY_UNVERIFIED before allocation; unknown
request strings still raise UNSUPPORTED_DEVICE. No permissive fallback or opt-in
needed for the documented G4 family. Mismatch policy for other names unchanged.

Source: [Google Cloud announcement](https://cloud.google.com/blog/products/compute/introducing-g4-vm-with-nvidia-rtx-pro-6000),
read in this cycle; corroborated by the actual kernel observation below.

Offline command, from checkout, existing Windows Python3.14.6:
`python -B -m pytest tools/compute/tests -q -p no:cacheprovider --junitxml=<TASK_ROOT>/evidence/validate/junit.xml`.
Outer subprocess180s; TMP/TEMP point to owned D:/sae-compute-68-20261030/temp.
**47 passed,74 subtests passed in23.06s**, exit0. Real log/JUnit retained under
validate/. Exact accepted G4 string and all other observed families pass;
L40S for L4, A10G for A100 and RTX 6000 Ada for G4 reject. Lowercase and mixed
identity disagreement checked; missing mapping rejects before any CLI call.
No old regression test was removed, no dependency installed.

## One real G4 cycle — identity/transport only

Exact-source local preflight passed, followed by one G4 allocation using the
committed controller and existing trivial framework adapter/manifest. Invocation
and exit codes in commands.json. Existing WSL Python3.12.3 / CLI0.7.4 reused;
no auth setup, provider patch, account/plan change or purchase.

Explicit bounds: task900s, whole-session window600s, cleanup reserve120s,
kernel60s, work60s. One active session; no overlapping TorchOED experiment.

Observed: **NVIDIA RTX PRO 6000 Blackwell Server Edition**,97887MiB,
driver580.82.07; torch2.11.0+cu130,CUDA13.0,capability[12,0].
Report classification TRANSPORT_ONLY_SCIENCE_UNREVIEWED, status PASS.
Artifact transport-check.json is202 bytes, downloaded and byte-count/SHA256
verified; digest `c1d331efbf230883a6c34b2ad45b6a8058be3e5155041169a3c5aded8ba8c26a`.
The artifact's live_gpu:NOT_RUN describes no tensor science in the fixture;
actual GPU identity is independently recorded by the kernel/controller.

Authenticated-zero before allocation; successful stop, authenticated-zero
cleanup and independent post_cleanup assignments0 confirmed. Pre/post balances
are recorded in summary.json as rounded compute units, not exact monetary cost.
No repeated allocation or scientific/performance experiment was performed.

## Status and next action

PASS: explicit mapping, existing regressions, live G4 identity/transport/hash,
post-run readback/cleanup and canonical source evidence. No unexpected FAIL or
repair in this cycle. NOT_RUN: tensor algorithms/performance, long-duration
work, other GPU probes, Actions, releases, downstream pin adoption.
H100's observed provider refusal from #66 remains documented, not reclassified
or retried under #68. No other compute/role/merge authority policy changed.

Owned D:/sae-compute-68-20261030 contains checkout, live-source snapshot, original
logs and small helper scripts for reproduction. Temp has zero files; residue.json
records it. No large C:/WSL virtual-disk file and no shared-path deletion.

Next: Architect independently review exact final HEAD, narrow family patterns,
47/74 tests, source identity and real G4 receipt. Leave this one Draft PR unmerged.
TorchOED adoption remains a separate explicit change after framework merge;
TorchOED's ongoing multi-GPU branch keeps its currently adopted pin and G4 gate.
