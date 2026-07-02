---
name: perturbation-results
description: Write, rewrite, or review Results sections for perturbation-prediction manuscripts. Use for evidence roadmaps, main comparisons, metric interpretation, ablations, robustness, OOD/OOS settings, biological interpretation, and figure-linked paragraphs.
---

# Perturbation Results

Use after `perturbation-writing-core`, `perturbation-writing-corpus-guide`, and
when needed `perturbation-experiments`.

## Results Job

Results answers empirical questions. It should not report panels in order or
dump metrics. Each subsection should state what question is being tested and
what model behavior the evidence supports.

## Overview Story Chain

Use 1-2 paragraphs:

1. Reconnect to the Introduction and Methods central claim.
2. Explain why one dataset or one metric is insufficient.
3. State the evidence sequence.
4. Define how main and supplementary figures divide core evidence and
   diagnostics.

Avoid "if the method works, then..." proof checklists.

## Subsection Story Chain

Each Results subsection should contain:

1. Evaluated question and why it matters.
2. Exact setting: dataset, split, held-out object, benchmark, or case-selection
   rule.
3. Metric meaning and direction at first use.
4. Main comparison against the strongest relevant baseline.
5. One or two numerical anchors tied to dataset, metric, baseline, and setting.
6. Behavior interpretation.
7. Boundary or Supplement pointer only when needed.

## Paragraph Recipes

Metric setup:

```text
Because observed and predicted cells are not paired, we evaluated
distributional agreement rather than cell-wise error. [Metric] measures
[behavior]; lower/higher values indicate [direction]. We use it together with
[second metric] because [first metric] captures [aspect] but not [other aspect].
```

Main comparison:

```text
In [dataset/split], [METHOD] achieved [metric] of [value], compared with [best
baseline] at [value]. The improvement was most apparent in [failure mode],
suggesting that [mechanistic interpretation]. This conclusion is limited to
[setting].
```

Visualization:

```text
To provide a gene- or cell-level view of this trend, we examined [case]. The
observed perturbed cells [behavior], whereas [baseline] [failure mode].
[METHOD] [behavior]. This visualization is consistent with [metric trend], but
serves as diagnostic support rather than a standalone test.
```

## Ablation And Robustness

An ablation paragraph must name:

- what component is removed or replaced;
- what stays unchanged;
- which metric or setting changes;
- what capability the component contributes.

Do not interpret "full model is best" as proof of all claimed mechanisms unless
the ablation isolates those mechanisms.

## TriShift Results Chain

Default TriShift evidence order:

1. Reference transfer or held-out-control performance.
2. Systema-style or residualized diagnostics when shared systematic variation
   is a concern.
3. Response-gene identity such as `Overlap@20` where available.
4. Ablations for reference construction and conditioning input.
5. Norman or combinatorial generalization.
6. Cell-level distribution recovery.
7. Supplementary distributions, robustness, additional cases, and latent-state
   diagnostics.

## Avoid

- Starting every paragraph with "Figure X shows".
- Comparing only against weak baselines.
- Reporting many numbers without explaining behavior.
- Moving broad field-level implications into Results.
- Treating UMAP, violin, or case plots as proof.
- Hiding mixed metrics or metric conflicts.
