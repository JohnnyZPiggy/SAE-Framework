# Compute Throughput Policy (SAE V3.3)

This policy applies to all SAE roles and newly adopted project revisions. It supersedes voluntary compute-conservation defaults, but not provider rules, existing billing permissions, scientific correctness or resource cleanup.

## Default: use available compute for research
- GPU-first: use suitable GPUs promptly for tensorized research; CPU numerical oracles and fair comparisons remain necessary.
- Explore all GPU types genuinely available through the user's authorized Colab plan, recording the device actually allocated rather than assuming the requested model.
- Do not introduce arbitrary SAE-imposed limits on repetitions, benchmark sizes, configurations, runtime or precision solely to conserve accelerator usage.
- Scale experiments according to the research question, observed memory/runtime and provider availability. Small diagnostic probes are a starting point, not a ceiling.
- When a GPU run fails, diagnose, adjust and retry where useful; do not require elaborate speculative preflight gates.
- Architect designs ambitious decision-relevant experiments; Mentor supplies hypotheses and numerical checks; Engineer executes and documents reproducible results. All roles follow this policy.
- When the preferred accelerator is unavailable, try other authorized available GPU options, then CPU fallback if appropriate. Do not mislabel CPU evidence as GPU evidence.

## Non-negotiable operational boundaries
- Colab does not guarantee unlimited quota, concurrent sessions, hardware types or uptime. This policy means no extra *SAE-imposed* compute-saving quota; it never authorizes circumventing provider limits.
- No new paid plan, additional billing or external resource commitment without the Scientist's explicit authorization.
- Preserve reproducibility, numerical validation, source SHA, credentials, storage safety, honest benchmark evidence and independent review.
- Release completed remote sessions and owned scratch resources; do not hold idle allocations.
- GPU absence should not block independent mathematical or CPU progress.

## Priority
Interpret prior references to “low-cost”, “bounded GPU” or “GPU gate” as efficiency and operational safety guidance, not a mandate to minimize already authorized compute or avoid useful experiments. This policy does not silently change project-pinned framework versions.
