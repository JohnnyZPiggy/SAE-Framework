# <PROJECT> — SAE V3.4 project entrypoint

SAE pin: `<40-CHARACTER-SAE-SHA>`. Configuration: [sae.yaml](sae.yaml). Pinned rules: [.sae/README.md](.sae/README.md).
Read the [pinned constitution](https://github.com/JohnnyZPiggy/SAE-Framework/blob/<40-CHARACTER-SAE-SHA>/AGENTS.md) and your role protocol at that SHA. Never float to `main` or silently bump the pin.

## Simplicity first (Engineer: read before writing code)

The [Simplicity Contract](https://github.com/JohnnyZPiggy/SAE-Framework/blob/<40-CHARACTER-SAE-SHA>/governance/SIMPLICITY_CONTRACT.md) overrides any older rule or habit that asks for more. The smallest change that meets the Issue's Definition of Done is the correct change.

1. **Validate only at trust boundaries** (CLI args, files, provider output), and only the fields you use. Trust internal code: let torch and Python raise.
2. **Catch an exception only if you then do something different.** No catch-and-rename, no custom error-code taxonomies.
3. **No speculative code:** no "future" abstractions, flags, fallbacks, length caps, hand-written schema validators.
4. **Tests:** one per changed behavior, plus an independent oracle for numerical claims. Test lines ≲ source lines.
5. **Evidence:** Git SHA is the integrity layer. The handoff is one PR comment, with ≤ 3 evidence files for code and ≤ 10 for a GPU run.
6. **Budget:** every Issue states S ≤ 50 / M ≤ 200 / L ≤ 500 net lines and a *Not required* list. Over 1.5× → stop, ship the Definition of Done, list extras as suggestions.

```python
# Not this
def criterion(X):
    if not isinstance(X, torch.Tensor): raise TypeError("X must be a tensor")
    if X.ndim != 2: raise ValueError(f"bad shape {X.shape}")
    try:
        return torch.linalg.slogdet(X.T @ X).logabsdet
    except RuntimeError as e:
        raise CriterionError("FAILED") from e

# This
def criterion(X):
    return torch.linalg.slogdet(X.T @ X).logabsdet
```

## Roles
- **Scientist:** sets goals, can stop any work; no routine approvals.
- **Architect / Mentor (default Claude):** research decisions, Issues with budgets, review, merges.
- **Engineer (e.g. Codex):** implements, tests, runs CPU/GPU on existing entitlements, opens PRs; never merges its own work.

## Project rules
- Production dependencies: <e.g. torch only>. Reference libraries are for tests only.
- Workspace: <designated drive / folder>; delete only task-owned scratch.
- Current state: <active Issue(s) and what is stopped>. Work starts only from an Issue or an Architect START comment.
