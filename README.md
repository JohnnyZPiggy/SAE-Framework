# SAE Framework V3.2

**One Project, Two Outcomes: Better Software, Better Scientist.**

SAE is a **Scientist–Architect–Engineer** workflow for mathematically grounded, portable implementations of numerical, optimization and simulation algorithms. The Scientist chooses and validates; GPT Mentor investigates mathematics, GPT Architect designs/reviews, and Codex implements and actually tests.

![SAE Framework overview](docs/figures/SAE_Framework_V3.2.en.svg)

## Start here

1. Review the shared [Agent Constitution](AGENTS.md).
2. For a new algorithm project, follow [Bootstrap](SAE_BOOTSTRAP.md) and pin an immutable SAE snapshot in `.sae/`. [Project template](examples/project/AGENTS.md).
3. Invoke `推进导师工作`, `推进架构师工作` or `推进工程师工作` with the **actual project repository**. Each agent reloads GitHub state and performs one bounded cycle.
4. Follow research → CPU engineering → Architect `GPU_READY` → Scientist Colab GPU experiment. Three linked outputs: [mathematical study, engineering report and experimental report](workflows/THREE_ARTIFACT_HANDOFF.md).

## Three-cell Colab target

```python
!pip install "git+https://github.com/OWNER/REPO.git@<EXACT_SOURCE_COMMIT_SHA>"
!python -m <package>.benchmarks.run --device cuda --out reports/gpu/<run-id>
!python -m <package>.benchmarks.publish --report-dir reports/gpu/<run-id>
```

**The third cell is optional:** inspect actual accuracy and benchmark evidence before publishing. The Secret name is **`GITHUB_TOKEN`**; a `!python` subprocess is **not guaranteed** to inherit Colab Secrets. The [GPU/Colab contract](workflows/GPU_EXPERIMENT.md) specifies a safe one-cell Python upload fallback. These CLIs remain *targets until Codex implements/tests them*; this repository currently contains policy, examples and templates, not an installed Bootstrap or Publisher runtime.

## Roles and authoritative rules

| Area | Canonical source |
| --- | --- |
| Agent identity and role tasks | [AGENTS](AGENTS.md) · [Mentor](protocols/MENTOR.md) · [Architect](protocols/ARCHITECT.md) · [Engineer](protocols/ENGINEER.md) · [Scientist](protocols/SCIENTIST.md) |
| Role recovery and next-step commands | [Role Recovery](workflows/ROLE_RECOVERY.md) |
| Research and CPU/GPU stages | [Research Pipeline](workflows/RESEARCH_PIPELINE.md) |
| Ecosystem Build-vs-Reuse check | [Ecosystem Review](workflows/ECOSYSTEM_REVIEW.md) |
| Issues, PR review and handoff | [Task Management](workflows/TASK_MANAGEMENT.md) |
| Experiment, reports and `GITHUB_TOKEN` | [GPU Experiment](workflows/GPU_EXPERIMENT.md) |
| Permanent, revocable GPT merge discretion | [Standing Authorization](governance/STANDING_AUTHORIZATION.md) |

**Principles:** CPU by default; GPU by exception. Reuse reliable PyTorch components; retain distinctive mathematics. Codex supplies real CPU evidence; only the Scientist runs Colab GPU. No GitHub Actions or forced CUDA-only implementation. No copied secrets, invented tests, automatic background agents or uncontrolled merges.

## Status, languages and license

The [roadmap](docs/ROADMAP.md) tracks **P0 Bootstrap and independent GitHub Publisher implementations, currently not verified as executable**. The [adoption smoke test](docs/ADOPTION_SMOKE_TEST.md) explains portable pinned snapshots. English files are normative; [中文版 README](README.zh-CN.md) and [language policy](docs/LANGUAGE_POLICY.md) explain mirrors.

**License:** no general license has yet been chosen for this Framework repository; public visibility alone does not authorize third-party copying or reuse.
