---
name: perturbation-supplement-captions
description: Write or review Supplement, figure captions, provenance notes, metric definitions, and figure legends for perturbation-prediction manuscripts. Use when detailed definitions, notebook provenance, split policies, metric formulas, or caption claim boundaries matter.
---

# Perturbation Supplement And Captions

Use after `perturbation-writing-core` and the relevant section skill.

## Supplement Job

The Supplement carries definitions and provenance too detailed for the main
text. It must remain notation-compatible with the manuscript.

Required Supplement jobs:

- expand metric formulas and aggregation rules;
- define top-k reference pools and split policies;
- distinguish training-time OT pools from evaluation-time held-out references;
- document perturbation prior sources and dimensionalities;
- state figure-generation notebooks and data sources;
- define preprocessing, baseline configuration, hyperparameters, and seeds when
  needed;
- repeat vector, scalar, matrix, distribution, index, and loss definitions
  consistently when formulas recur.

## Caption Job

Captions should let the figure be interpreted without overclaiming. A caption
should contain:

1. Figure question or panel group purpose.
2. Dataset, split, held-out setting, or benchmark.
3. Metric definition and direction when not obvious.
4. Baseline group or comparison target.
5. Boundary statement when panels are diagnostic.
6. Pointer to Supplement only for extra detail, not for missing core meaning.

## Caption Style

Use figure captions to define what is plotted, not to make unsupported claims.

Good:

```text
Lower Wasserstein distance indicates closer agreement between predicted and
observed perturbed distributions under the held-out-control split.
```

Risky:

```text
The plot proves that TriShift fully recovers the perturbation response.
```

## TriShift Caption Rules

- Use `Module`, not `Stage`, when describing TriShift components.
- Use `perturbation prior`, not only a specific prior source, unless the panel
  is source-specific.
- If prior examples are shown, keep them as examples such as GenePT or ProtT5
  and do not imply all prior types were tested.
- Output endpoint should be described as predicted perturbed response or
  predicted reference-relative response depending on the figure.
- Figure captions should not imply OT true cell pairing.
- Distinguish PBMC IFNB1 target-domain-control transfer from held-out-control
  genetic prediction.

## Provenance Checks

For manuscript or supplement figure notes, record:

- notebook or script entrypoint;
- dataset/source artifact;
- split policy;
- model and baseline set;
- seed or multi-split policy;
- metric aggregation;
- generated figure/table artifact path where appropriate;
- known caveats.

For drug figures and tables, also record canonical compound identifiers,
salt/formulation and vehicle, dose units, exposure time, combination ratios,
plate/donor/replicate allocation, split key, and metric aggregation unit. A
caption that uses "synergy", "mechanism", or "therapeutic" must define the
underlying endpoint and retain its evidence boundary.

## Avoid

- Captions that merely repeat "A, B, C show".
- Captions that introduce claims absent from Results.
- Supplement definitions that drift from main-text symbols.
- Metric formulas without direction or aggregation rules.
- Provenance notes that omit the held-out policy.
