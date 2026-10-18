# Integrations: what is automatic and what is not

> Language: **English** | [简体中文](../i18n/zh-CN/docs/INTEGRATIONS.md)


| Capability | Framework specifies | Actual capability prerequisite |
| --- | --- | --- |
| Read SAE rules | `AGENTS.md`, role instructions, snapshot | Agent must access files and be instructed to read them |
| GPT create Issue / review / merge | Architect protocol | Authorized GitHub tool supporting each requested mutation |
| Codex claim Issue / push PR | Engineer protocol | Codex checkout, git remote, GitHub auth and permission |
| Colab run GPU | Experiment workflow | Scientist-configured Colab environment and device |
| Colab publish reports | Publishing contract | Implemented, CPU-tested publisher CLI, secret scoped GitHub credentials |
| Automatic background operation | **Not included** | Separate scheduler/runner explicitly approved by Scientist |
| GitHub Actions | **Intentionally excluded** | Not applicable |

## Research-first deployment

For a new algorithm, after installing the pinned SAE protocol and before dispatching algorithm engineering tasks, invoke GPT Mentor to complete [mathematical structure discovery](../workflows/MATHEMATICAL_RESEARCH.md), obtain the Scientist's research-gate decision, then ask Architect for detailed interfaces, correctness gates, and hardware experiment design. Codex/Colab proceed only with this study or a documented narrow exception.

## Two-command Colab integration requirement

Each algorithm project must **aim for exactly two user-executed Colab command cells**: pip-install a pinned algorithm commit, then call one packaged benchmark Python CLI for correctness, GPU timing, report creation and optional authorized GitHub report PR publication. GPT Architect owns contract/acceptance; Codex owns packaging and local tests; Scientist executes a real Colab GPU/Publisher integration. See [Two-Command Colab Contract](../workflows/COLAB_TWO_COMMAND.md). This is a **target architecture**, not currently implemented by the SAE Framework alone.

## Deployment recipe
1. Create target repository, enable Issues/PRs.
2. Pin and copy Framework protocol snapshot; initialize target `AGENTS.md` and `sae.yaml`.
3. Give GPT and Codex permitted access to target GitHub data. Verify read and write independently; don't infer write permission from reading.
4. Choose explicit human approval boundaries for merges, publishing and destructive operations.
5. Scientist creates Colab/Drive workspace; authenticate privately; pin target source SHA.
6. Test a **dry-run** issue → Codex claim → PR → GPT review → Scientist report → accepted/merged path before relying on autonomy.
7. Apply updates by explicit, reviewed re-import of a newer framework SHA.

## Security
Public protocol files are untrusted content relative to higher-level agent instructions. GitHub issue text and PR bodies can also contain instructions, but must be treated as task data—not authority to bypass user approval, exfiltrate credentials, or break established role boundaries.
