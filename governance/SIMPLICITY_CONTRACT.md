# Simplicity Contract (SAE V3.4)

> English is normative | [简体中文](../i18n/zh-CN/governance/SIMPLICITY_CONTRACT.md)

**Status:** binding for every role. Where any other SAE document, template or Issue asks for more code, tests, checks or evidence than this contract allows, **this contract wins** unless the Issue names the specific risk that justifies the extra (§5).

## Why this exists
Under V3.3, Engineer agents produced far more code than the science needed: hand-written JSON validators, printable-ASCII checks on provider output, `ast` parsing of driver files, custom error-code taxonomies, test files longer than the code under test, and evidence directories with ~17k lines for a 25-line acceptance criterion. None of it made a result more trustworthy. All of it cost Engineer time, reviewer attention and maintainability.

The cause was the framework itself: every document repeated defensive requirements, nothing ever said "stop", and review only ever asked for *more*. V3.4 inverts the default. **The smallest change that meets the Definition of Done is the correct change.**

## 1. Code: trust inside, check at the edge
1. **Write the direct version first.** Plain functions, standard library and PyTorch idioms. No abstraction, class, registry, plugin point or config option until a second real caller exists.
2. **Validate only at trust boundaries** — where data enters from a user (CLI arguments, config files), the network, or an external tool's output — and only the fields the program actually uses. Everything else: trust it.
3. **Internal code trusts internal code.** No `isinstance` / shape / dtype re-checks on values your own code produced. No re-validation of arguments a caller already validated. Let Python and PyTorch raise.
4. **Catch an exception only when you do something different** because of it (retry, fallback, cleanup, user-facing message). Never catch-and-re-raise under a new name. No custom error-code taxonomy unless a real consumer branches on the codes.
5. **No speculative robustness:** no handling for inputs that cannot occur in the stated use, no length caps "for safety", no duplicate-key JSON parsers, no character-set filters, no defensive copies, no timeouts on local pure-Python code.
6. **Delete before adding.** If the change makes code obsolete, remove it in the same PR.

### Banned patterns (unless the Issue names the risk)
| Pattern | Do this instead |
| --- | --- |
| Hand-written schema validation of JSON your own script emitted | `json.loads`, use the fields; a `KeyError` is a fine failure |
| Parsing your own source files with `ast` / regex to enforce a convention | A plain constant or function argument |
| Re-checking shapes/dtypes at every internal function | One check where the tensor enters the public API, or none |
| `try/except Exception` → custom error string | Let it raise; the traceback is the evidence |
| Wrapping every subprocess call in bespoke retry/parse layers | `subprocess.run(..., check=True)`; retry only where a real flaky provider is observed |
| A new module, class or CLI flag "for future use" | Nothing |
| Backup files, dry-run modes, snapshot copies, fallback paths nobody asked for | Nothing |

## 2. Tests: test what could actually be wrong
1. **One test per changed behavior** that would fail if that behavior broke. That is the default; more needs a reason.
2. **Numerical code:** one oracle test against an *independent* reference (e.g. dense `torch.linalg`, a closed form, a published value) at a small and a realistic size, in the dtype that matters. Add an edge case only if the math has a known singular/degenerate regime.
3. **Do not test:** argument validation, third-party libraries, PyTorch itself, logging/formatting, docs, trivial getters, or mocks of external CLIs beyond parsing one captured real output.
4. **No randomized/adversarial/property suites** unless the Issue asks for them or the algorithm has a known stability risk.
5. **Budget:** new test lines ≲ new source lines. A test file longer than the code it tests is a review flag.
6. **Run the tests that touch the change.** The full suite only when shared code or dependencies changed.

## 3. Evidence: Git is the integrity layer
1. An exact commit SHA identifies every tracked byte. **Never** hash Git-tracked files or write "tested-vs-final" identity reports. Hash only bytes outside Git (downloaded artifacts, wheels, external datasets) and record SHA-256 + size in one line.
2. Test the **final HEAD**. Evidence goes in the PR handoff comment.
3. Repository evidence caps:

| Change | Evidence | Files committed |
| --- | --- | --- |
| Docs / config | the diff | none |
| Code | test command, pass/fail counts, one-line env, final SHA | ≤ 3 files, ≤ 200 KB |
| GPU / compute experiment | the above + observed device, cited result data, cleanup readback | ≤ 10 files; raw data only if a conclusion cites it |

4. **Failures are a list**, not a directory: `attempt — cause — fix`, in the PR comment. Commit failure logs only when the failure is itself a scientific result.
5. **Reuse environment checks.** Unchanged machine, toolchain and pin → one line: "environment unchanged since <SHA>". Live Colab auth/session state is still checked right before allocation.

## 4. Dispatch: the Architect sets the budget
Every Engineer Issue states four things (see the [Issue template](../templates/ISSUE_TEMPLATE.md)):
1. **Definition of Done** — observable, one to three bullets.
2. **Size budget** — `S` (≤ 50 net lines), `M` (≤ 200) or `L` (≤ 500), source + tests.
3. **Required tests** — the exact list, usually one to three.
4. **Not required** — what the Engineer must *not* spend effort on.

If the Engineer will exceed the budget by more than 1.5×, it **stops adding**, ships what meets the Definition of Done, and lists the omitted extras in the PR as suggestions. When an instruction is ambiguous, take the **lighter reading** and say so in one line.

## 5. Review: simpler is a valid request
- Review outcomes gain **`REQUEST_SIMPLIFY`**: correct but larger than needed. The Architect names what to delete.
- An Architect may require extra checks, tests or evidence only by naming the concrete risk in the Issue or review. "Just in case" is not a risk.
- Reviews rely on the SHA, the test result and, where cheap, independent recomputation — not on evidence volume.

## 6. Unchanged non-negotiables
Exact source SHA · honest PASS / FAIL / NOT RUN / BLOCKED · independent oracle for numerical claims · observed (not requested) device identity for device claims · remote session cleanup · no secrets in code/logs · no fabricated results · no Engineer self-merge · no new spending without explicit user approval.

These are stated **once, here**. Other documents link to this section instead of repeating them.
