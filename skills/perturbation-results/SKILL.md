---
name: perturbation-results
description: Write, rewrite, or review Results sections for perturbation-prediction manuscripts. Use for evidence roadmaps, main comparisons, metric interpretation, ablations, robustness, OOD/OOS settings, biological interpretation, and figure-linked paragraphs.
---

# Perturbation Results

Use after `perturbation-writing-core`, `perturbation-writing-corpus-guide`, and
when needed `perturbation-experiments`. For metric-heavy writing, consult
`references/metric-cards.md`; for claim-strength consistency, consult
`references/claim-ledger-template.md`.

## Results Job

Results answers empirical questions. It should not report panels in order or
dump metrics. Each subsection should state what question is being tested and
what model behavior the evidence supports.

Do not treat metrics as passive diagnostics. A strong Results section uses a
metric to explain an advantage: what biological or modeling capability the
metric measures, why that capability matters, where the method improves over
the strongest baseline, and what mechanism or boundary the result suggests.
Write the advantage first. Add a boundary only when it changes the
interpretation; do not attach a defensive caveat to every result.

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
6. Behavior interpretation: what advantage the metric shows.
7. Mechanistic or biological meaning where supported.
8. Boundary or Supplement pointer only when it materially changes the claim.

## Metric-To-Advantage Rule

Every important metric paragraph should answer four questions:

1. What capability does the metric test?
2. Why does that capability matter for perturbation prediction?
3. Where does the method improve over the strongest relevant baseline?
4. What model behavior or biological signal does the improvement support?

Weak:

```text
We also report Overlap@20. TriShift achieves the highest Overlap@20.
```

Stronger:

```text
Response-gene identity recovery connects predicted expression changes to
downstream mechanism interpretation, so condition-level correlation alone is
insufficient. Overlap@20 measures whether the strongest observed response genes
are also recovered among the strongest predicted response genes. TriShift
achieves the highest Overlap@20 in [setting], indicating that its advantage
extends from response-vector alignment to recovery of response-gene identity.
```

Do not introduce a metric and then leave it uninterpreted. If a metric is in the
main Results, it should either support a stated capability or be moved to
Supplement/provenance.

## Advantage-First Interpretation

When multiple datasets show the same qualitative trend but effect sizes differ,
do not neutralize the paragraph with defensive language. State the shared
advantage, then name where it is strongest.

Weak:

```text
Adamson and Norman show smaller differences and should be treated as
directional evidence rather than a strong ranking conclusion.
```

Stronger:

```text
Adamson and Norman show the same advantage pattern, indicating that TriShift's
reference-conditioned prediction improves recovery of perturbation-specific
response structure across genetic settings. The separation is largest in
[setting], where [metric] most clearly reflects response-gene identity recovery.
```

Use "directional evidence" only when the result is too weak or inconsistent to
support the stated advantage. Otherwise, emphasize the advantage and let the
metric, setting, and comparison define the scope.

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
showing that [mechanistic interpretation]. This advantage is most directly
supported in [setting].
```

Visualization:

```text
To provide a gene- or cell-level view of this trend, we examined [case]. The
observed perturbed cells [behavior], whereas [baseline] [failure mode].
[METHOD] [behavior]. This visualization is consistent with [metric trend], but
serves as diagnostic support rather than a standalone test.
```

Response-gene recovery:

```text
To test whether prediction accuracy extends to perturbation-relevant genes, we
evaluate response-gene identity recovery. [Metric] compares the strongest
observed and predicted response-gene sets; higher values indicate that the
model recovers genes most associated with the perturbation response. In
[setting], [METHOD] improves over [baseline], suggesting that its advantage is
not limited to aggregate expression alignment but also preserves the identity of
key response genes.
```

Extended biological evidence:

```text
We next ask whether recovered response genes also support biological
interpretation. After identifying the top predicted response genes, we examine
[expression statistics/single-gene distributions/pathway enrichment]. This
secondary evidence is used to interpret the response-gene recovery metric, not
as a replacement for the primary quantitative comparison.
```

## Response-Gene Recovery Evidence Chain

For common-DEG, DEG-overlap, or Overlap@k analyses, use the metric as an
advantage point rather than a footnote. The preferred chain is:

```text
response-gene overlap is higher
-> expression statistics on top response genes are closer to observed response
-> key response-gene distribution examples are consistent with the aggregate
   trend
-> pathway or gene-set enrichment matches the perturbation context where tested
-> the method better recovers perturbation-related biological signal
```

Keep each step scoped. Pathway enrichment and single-gene plots are
interpretive support; they do not prove the full mechanism without the primary
response-gene metric.

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
- Listing metrics without explaining what advantage each metric supports.
- Adding defensive caveats after every favorable comparison.
- Moving broad field-level implications into Results.
- Treating UMAP, violin, or case plots as proof.
- Hiding mixed metrics or metric conflicts.
