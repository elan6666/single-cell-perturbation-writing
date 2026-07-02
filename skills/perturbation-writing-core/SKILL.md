---
name: perturbation-writing-core
description: Core domain rules for perturbation-prediction manuscript writing. Use with all perturbation-prediction section skills to enforce story logic, claim boundaries, TriShift terminology, notation invariants, evidence limits, and reviewer-safe scientific framing.
---

# Perturbation Writing Core

This skill contains the shared scientific contract for perturbation-prediction
manuscripts. Load it before any section-specific writing skill.

## Core Scientific Story

Strong perturbation-prediction papers usually share one hidden skeleton:

1. High-throughput single-cell perturbation experiments are biologically useful.
2. Exhaustive profiling is infeasible because perturbation spaces grow across
   genes, combinations, drugs, cytokines, doses, cell types, patients, states,
   batches, and time.
3. The data are destructive, unpaired, high-dimensional, sparse, noisy, and
   heterogeneous.
4. Existing methods fail in a precise way: weak OOD generalization, missing
   reference origins, poor distributional fidelity, limited prior coverage,
   insufficient scaling, or overreliance on mean effects.
5. A structured model or training framework is introduced to address the gap.
6. Evidence must include multiple datasets or splits, metrics with different
   failure modes, strong baselines, ablations, robustness or transfer settings,
   and biological or distributional interpretation.
7. The paper returns to biological meaning and states limitations without
   overclaiming virtual-cell, drug-discovery, or therapeutic scope.

## Central Gap Rules

Before writing any section, identify the central gap in one sentence. It should
name an assumption that fails, not merely say "existing methods are limited".

Good gap types:

- Unpaired data gap: the same cell cannot be observed before and after
  perturbation.
- Mean-effect gap: condition averages ignore cell-state heterogeneity and
  distributional shape.
- Conditional generalization gap: a model cannot condition on unseen
  perturbations, doses, cell types, contexts, or reference origins.
- Reference-origin gap: perturbation identity does not determine the control
  state from which prediction starts.
- Prior-knowledge gap: GO graphs, LLM embeddings, pathway priors, or protein
  embeddings have incomplete biological coverage.
- Scaling gap: training or inference does not fit atlas-scale datasets or large
  perturbation spaces.
- Metric gap: endpoint accuracy, response-gene identity, residualized signal,
  and distributional fidelity can disagree.

For TriShift, the central gap is normally:

```text
Unseen perturbation prediction requires both a perturbation-specific shift and a
state-compatible reference origin; perturbation identity alone does not choose
the control state from which prediction should start.
```

## TriShift Domain Contract

Use these defaults unless the current manuscript evidence says otherwise:

- TriShift is a reference-conditioned state-transition framework.
- The prediction is reference-relative, not direct endpoint regression.
- State-compatible references are prediction origins or supervision candidates.
- OT constructs soft state-compatible reference weights; it does not recover
  true biological cell pairs.
- External perturbation priors help unseen perturbation representation, but do
  not by themselves define the starting control state.
- Held-out-control genetic prediction and PBMC target-domain-control transfer
  are related but not interchangeable.
- PBMC IFN-beta evidence supports IFNB1/PBMC transfer only; do not generalize to
  all cytokines, proteins, immune contexts, or drug classes.
- Systema-style metrics, reference-centered metrics, centroid-centered metrics,
  response-gene overlap, and distributional metrics test different failure
  modes and should not be collapsed into a single "accuracy" claim.

## Non-Negotiable Notation Rules

- Define full vectors before scalar components.
- Keep generic training vectors distinct from control and perturbed cells.
- Define dimensions, indices, distributions, matrices, losses, and metrics
  before use.
- Define OT measures, marginals, cost matrix, coupling set, entropy, and
  regularization before the OT objective.
- Avoid ambiguous notation such as `z_mu`.
- Use the same notation in main text and Supplement.
- Number only equations that are referenced.
- Never imply that OT gives true biological one-to-one cell matches.
- Separate training-time reference construction from evaluation-time held-out
  reference use.

## Evidence Contract

Each empirical claim needs:

- Dataset or biological regime.
- Split or held-out policy.
- Metric and direction.
- Strongest relevant baseline.
- One or two numerical anchors when available.
- Behavior interpretation tied to the model mechanism.
- Boundary statement when the evidence is narrow, indirect, or diagnostic.

Do not use visual plots as proof. UMAP, violin, heatmap, and pathway examples
may support interpretation only after quantitative evidence has been stated.

## Venue-Aware Defaults

Journal or Bioinformatics-style paper:

- Related Work can be integrated into Introduction.
- Results may come before Methods.
- Abstract can use structured labels if required.
- Discussion should explicitly state limitations and future work.
- Language should emphasize findings, biological meaning, and boundaries.

Conference or BIBM-style paper:

- Related Work is often separate.
- Methods and experiments usually come before Results.
- Contributions can be explicit and numbered.
- Evidence should be compact, table-centric, and metric-visible.
- Limitations may be shorter but cannot disappear when they affect claims.

## Common Failure Modes

| Failure | Fix |
|---|---|
| Starting with modules instead of problem | Begin from the destructive unpaired-observation constraint |
| Literature inventory | Organize method families by solved problem and remaining assumption |
| Generic "better performance" | Name metric, setting, strongest baseline, and behavior |
| Treating OT as true pairing | Say state-compatible reference candidate or soft reference weight |
| Overbroad prior claims | Restrict to the tested prior, dataset, and perturbation type |
| Panel-by-panel Results | Start from the evaluated question and use figures as evidence |
| Generic polish first | Fix domain story and section role before style |
