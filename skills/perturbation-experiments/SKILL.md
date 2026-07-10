---
name: perturbation-experiments
description: Write or review experiment setup sections for perturbation-prediction manuscripts. Use for datasets, preprocessing, splits, baselines, metrics, fairness, implementation details, provenance, and conference table setup.
---

# Perturbation Experiments

Use after `perturbation-writing-core` and `perturbation-writing-corpus-guide`.
When metrics are central to the task, also consult `references/metric-cards.md`.

## Experiments Job

Experiments setup is not administrative filler. It defines whether the Results
can support the paper's central claim.

The section should make clear:

- what capability is being assessed;
- which biological regimes are covered;
- what is held out;
- why baselines are fair;
- what metrics test;
- how implementation and provenance support reproducibility.

## Required Structure

1. Overall experimental goal:
   - "To comprehensively assess [capability], we evaluate [method] on
     [datasets/settings]."
2. Datasets:
   - one sentence per dataset for biological regime, scale, perturbation type,
     and difficulty.
3. Preprocessing and splits:
   - normalization, HVG selection, train/val/test policy, OOD/OOS setting,
     held-out perturbations, held-out controls, target-domain controls, or
     combinations.
4. Baselines:
   - group by category: identity/mean/linear, domain-specific methods,
     generative models, prior-based models, OT/distributional models,
     foundation models.
5. Metrics:
   - define each metric's target behavior and direction.
6. Implementation and fairness:
   - same splits, same preprocessing, same available inputs, same test-time
     controls, no leakage, reproducible code/data provenance.

## Metric Guidance

Use metric families, not a single endpoint score:

- Endpoint or expression error: MSE, MAE, nMSE, R2, Pearson.
- Distributional fidelity: Wasserstein, MMD, density overlap, mean/variance
  correlation.
- Biological response identity: DE-Spearman, DEG overlap, Overlap@k, response
  gene precision.
- Residualized or systematic metrics: Systema-style Pearson or residual
  agreement when shared systematic variation is a concern.
- Reference-specific metrics: reference-centered or centroid-centered metrics
  when reference origin matters.

Explain direction at first use.

## Split Guidance

Name the held-out object:

- unseen perturbation;
- unseen gene;
- unseen combination;
- held-out control origin;
- target-domain control;
- unseen cell type;
- unseen drug/dose;
- leave-one-condition-out;
- cross-dataset or cross-batch transfer.

Never blur held-out-control genetic prediction with PBMC target-domain-control
transfer.

## TriShift Experiment Contract

- Reuse existing baseline outputs unless missing or incompatible.
- State when CellOT or another OT baseline is only defined for PBMC or a
  specific held-out-control path.
- `Overlap@20` should be framed as response-gene identity recovery, not a DEG
  classifier unless a classifier is actually trained.
- Systema-style diagnostics test perturbation-specific residual signal and
  should not replace endpoint or distributional metrics.
- Distribution recovery and UMAP evidence should be connected to quantitative
  metrics.

## Fairness Checklist

- Are train/validation/test perturbations disjoint where claimed?
- Are test controls unavailable during training when the protocol says so?
- Do baselines receive the same information type at inference?
- Are hyperparameters selected without test leakage?
- Are datasets and preprocessing named precisely?
- Are missing baselines explained rather than ignored?
- Could a no-effect, mean-response, or matched nonparametric baseline exploit
  shared systematic variation under this split?
- Is the statistical unit matched to the claim rather than inflated by cells
  from the same exposure, donor, or plate?

## Drug-Perturbation Experiment Contract

Report canonical drug identity, salt/formulation, vehicle, dose unit/range,
exposure time, replicate/plate/batch policy, and the count of unique exposure
conditions. State whether the split holds out drug, scaffold, target/MoA, dose,
time, combination, donor, cell model, or dataset; random cell splits do not
justify unseen-drug generalization. Assess viability, cell-cycle, apoptosis, and
composition shifts when they can explain a response. For combinations, state
the endpoint and Bliss, Loewe, HSA, ZIP, or other declared null before using
"synergy".
