---
name: trishift-writing-core
description: TriShift-specific overlay for perturbation-writing skills. Use only when the manuscript or user request mentions TriShift, reference-conditioned state transition, held-out-control transfer, IFNB1/PBMC, Systema-style diagnostics, reference-origin claims, or TriShift figure/caption conventions.
---

# TriShift Writing Core

This overlay keeps TriShift-specific claims out of the general perturbation
writing core. Load it only when the current manuscript, selected text, or user
request is actually about TriShift or a TriShift-style reference-conditioned
state-transition model.

## When To Load

Load this overlay when the request or text mentions:

- TriShift;
- reference-conditioned state transition;
- reference-relative shift;
- held-out-control transfer;
- target-domain-control transfer;
- IFNB1 or PBMC IFN-beta;
- Systema-style diagnostics;
- reference-centered or centroid-centered metrics;
- `Overlap@20`;
- `Module`, `GenePT`, ProtT5, or TriShift figure conventions.

Do not load this overlay for generic CMonge-like, Scouter-like, scDFM-like,
SCALE-like, or unrelated perturbation-prediction papers unless the user
explicitly asks to adapt TriShift logic.

## Central Gap

For TriShift, the central gap is normally:

```text
Unseen perturbation prediction requires both a perturbation-specific shift and a
state-compatible reference origin; perturbation identity alone does not choose
the control state from which prediction should start.
```

## Domain Contract

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

## Manuscript Order

For TriShift manuscript edits:

1. Chinese manuscript controls claim order, terminology, figure references,
   caveats, and interpretation.
2. English manuscript follows the Chinese scientific content while respecting
   venue language and page budget.
3. Supplement changes only when definitions, provenance, metrics, formulas,
   split policies, or caveats change.

## Figure And Caption Conventions

- Use `Module`, not `Stage`, for TriShift components.
- Use `perturbation prior`, not only a specific source, unless the panel is
  source-specific.
- Prior examples such as GenePT or ProtT5 must remain examples unless the
  experiment actually compares prior sources.
- Do not imply OT true cell pairing in captions or diagrams.
- Distinguish PBMC IFNB1 target-domain-control transfer from held-out-control
  genetic prediction.

## Claim Boundaries

Allowed:

- "supports reference-conditioned prediction under held-out-control transfer";
- "is consistent with improved preservation of perturbation-specific signal";
- "in the IFN-beta PBMC task...";
- "soft state-compatible reference weights";
- "diagnostic support from UMAP or distribution plots".

Forbidden unless new evidence exists:

- "solves unseen perturbation prediction";
- "handles cytokines broadly";
- "protein priors generalize across immune signaling";
- "OT recovers true cell pairs";
- "UMAP proves biological recovery";
- "the model is generally valid for all cell types, doses, or batches".

## Method Variable Scope

For TriShift Method A or Problem Formulation, keep notation minimal:

```text
X^0 = {x_i^0}_{i=1}^{n_0}, x_i^0 in R^G
Y = {y_j}_{j=1}^{n_1}, y_j in R^G
p, e(p)
\hat y_{m,p} = F_theta(x_m^0, e(p))
```

The paragraph must say that `x_m^0` is a selected reference control state, not a
factual pre-perturbation counterpart of a measured perturbed cell.

Define later:

- `z_i^0` and `z_j^1` in the encoder/latent-space subsection;
- OT coupling or Sinkhorn objective in the OT reference-pool subsection;
- shift vectors in the perturbation-shift subsection;
- residual generator formulas in the generator subsection;
- GenePT or ProtT5 details in the perturbation-prior subsection;
- PBMC/Norman splits and Systema formulas in Experiments or evaluation metrics;
- hyperparameters and baseline internals in implementation details or
  Experiments.
