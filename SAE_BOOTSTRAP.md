# SAE Bootstrap V3.2 — project adoption contract

> [中文](i18n/zh-CN/SAE_BOOTSTRAP.md) · This is a **procedure**, not evidence that a Bootstrap CLI already exists.

## Preflight

Identify the **actual target** `OWNER/REPO`, its default branch, access, existing files, installed tool capabilities, intended algorithm and the exact **Framework source SHA**. Do not treat SAE Framework as the algorithm repo by default. If the target already contains files, inspect them before proposing changes.

## Create a self-contained pinned snapshot

1. Copy all policy/docs needed for the selected immutable Framework revision into the target's `.sae/`, including `AGENTS.md`, `protocols/`, `workflows/`, `governance/`, `templates/`, `docs/`, `examples/`, the Chinese `i18n/zh-CN/` mirror and the corresponding Bootstrap/README documents. **All snapshot files must come from the same SHA**; do not mix live main and pinned versions.
2. Instantiate a **target-specific root** `AGENTS.md` from [project AGENTS example](examples/project/AGENTS.md), updating paths/owner/SHA; copy [sae.yaml](examples/project/sae.yaml) and fill real values. A copied Markdown link must resolve in the new `.sae/` layout, not merely in this source repo.
3. At minimum, ensure pinned access to [Role Recovery](workflows/ROLE_RECOVERY.md), [Mathematical Research](workflows/MATHEMATICAL_RESEARCH.md), [Ecosystem Review](workflows/ECOSYSTEM_REVIEW.md), [GPU/Colab](workflows/GPU_EXPERIMENT.md), [Task Management](workflows/TASK_MANAGEMENT.md) and [three artifacts](workflows/THREE_ARTIFACT_HANDOFF.md).
4. The owner-wide [Standing Authorization](governance/STANDING_AUTHORIZATION.md) is a live, revocable human delegation; a copied policy snapshot **does not create API permissions or register a private/third-party repository**. Projects retain their pinned scientific workflows until the user explicitly adopts a newer snapshot.

## Research gate before algorithm implementation

Mentor and Scientist inspect the mathematical structure, matrix/vector operations, numerical equivalence, possible tensorization and oracle. Produce `docs/research/<algorithm>-tensorization.md` using [the study template](templates/TENSORIZATION_STUDY.md). Scientist chooses `RESEARCH_READY` / `RESEARCH_BLOCKED` / `NOT_TENSORIZABLE` or a documented narrow exception. **No substantive acceleration implementation Issue without this gate.** Repository scaffolding can be prepared independently.

## Engineering skeleton and GitHub tasks

Codex implements the project packaging and small modules (as applicable: `src/`, `tests/`, `benchmarks/`, `reports/`, `docs/`), plus an installable, deterministic CLI. Require CPU oracle/edge/regression tests, applicable CPU `torch.compile`, CPU benchmarks, clean exact-SHA pip install and CLI smoke tests. Do not invent any execution evidence.

Architect writes scoped GitHub Issues/acceptance criteria, verifies the [Ecosystem Review](workflows/ECOSYSTEM_REVIEW.md), reviews Code and phase gates, and supplies an exact pinned SHA for a later Scientist Colab run. The target [three-step workflow](workflows/GPU_EXPERIMENT.md) separates install, benchmark and optional Publisher; the Publisher must safely access the `GITHUB_TOKEN` Colab Secret and never automatically publish or merge.

## Completion and limitations

- Review the proposed PR, check all copied bilingual links and SHA consistency, project AGENTS role discovery, YAML parsing, status/Issue handoff and a fresh-chat role recovery smoke test. See [Adoption Smoke Test](docs/ADOPTION_SMOKE_TEST.md).
- Record **PASS / FAIL / NOT_RUN / BLOCKED**; report the actual GitHub PR and commit; do not call the CLI or GPU verified before actual tests. Architect's final PR merge decision is subject to the live Standing Authorization and the per-PR Merge Gate; the Scientist still owns consequential scientific/security decisions.
- Re-running Bootstrap is **idempotent**: inspect differences, never silently overwrite existing project files, delete history, leak tokens, force-push, change GitHub protections or upgrade pinned snapshots. No GitHub Actions, Drive syncing, or unattended CPU/GPU execution.

**Implementation status:** this document defines the required Bootstrap behavior; [Roadmap](docs/ROADMAP.md) tracks a separate Codex CLI implementation.
