# Scientist Protocol — Human Project Owner

The human Scientist is the **principal investigator**, final scientific decision-maker and actual Colab operator.

## Responsibilities
- Select research problems and papers; decide what is scientifically worth implementing.
- Ask GPT Mentor to teach mathematical assumptions, algorithms and GPU experimental principles.
- Decide the accuracy/performance trade-off, baseline and reporting priorities.
- Prepare a small personal Google Drive folder for Colab Notebooks and temporary files only; **no desktop sync, no GitHub/Drive result exchange**.
- Mount/import environment, install pinned repository/PR commit, run thin notebook cells.
- Check the actual device and results, run CPU/GPU experiments, and review warnings.
- Publish small, non-sensitive correctness/performance reports back to GitHub through a tested Publisher CLI (or manual PR until available).
- Approve exceptional or destructive repository actions and retain final authority.

## Scientist experiment checklist
1. Verify tested candidate SHA, installed package SHA, device, package versions and seed.
2. Execute correctness first; treat unexpected errors as blockers.
3. Run warmups, synchronized timing and appropriate repetitions; preserve precision and workload parity.
4. Confirm summary report matches observed output before authorizing publication.
5. Post report-PR/Issue link for GPT review and Codex diagnosis if necessary.
6. Ask Mentor to explain surprising results; decide next scientific direction.

The Scientist need not write the heavy Python code. The AI team should minimize required manual steps without overstating autonomous capabilities.
