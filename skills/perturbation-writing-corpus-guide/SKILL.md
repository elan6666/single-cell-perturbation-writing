---
name: perturbation-writing-corpus-guide
description: Detailed writing guide distilled from a small corpus of single-cell perturbation and expression-prediction papers. Use with perturbation-prediction manuscript tasks to apply module structure, paragraph architecture, language style, reusable templates, and conference-vs-journal writing differences.
---

# Perturbation Writing Corpus Guide

This skill encodes the latest distilled writing guide from the user's small
corpus of single-cell perturbation/expression-prediction papers. It is a
writing-architecture guide, not a model summary.

The full latest source guide is preserved at
`references/latest-corpus-writing-guide.md` in this repository, and at
`references/latest-corpus-writing-guide.md` relative to the
`perturbation-prediction-writing` skill package when installed locally.
When a task asks for deep imitation, sentence libraries, or conference-vs-journal
style transfer, read that reference together with this skill.

Use it to make paragraphs function like strong papers: each paragraph should
have one job, a clear opening move, evidence or mechanism, interpretation, and
bounded handoff.

## Corpus Skeleton

The shared story across CMonge, Scouter, scPRAM, scDFM, SCALE, Enhanced KG,
scCADE, and PPNF-like expression-prediction papers is:

```text
single-cell perturbation experiments are valuable
-> exhaustive experiments are expensive, incomplete, unpaired, sparse, and heterogeneous
-> existing methods fail under OOD, combinations, distributional fidelity, prior coverage, or scale
-> a structured model or training framework is proposed
-> evidence spans datasets, splits, metrics, ablations, robustness, and biological interpretation
-> discussion returns to biological meaning, virtual-cell or drug-discovery potential, and limitations
```

Do not write a paragraph until its role inside this skeleton is clear.

## Full Paper Module Map

Recommended reusable structure:

1. Title: task + mechanism + capability.
2. Abstract: value, bottleneck, gap, method, mechanism, evidence, implication.
3. Introduction: domain value, experimental bottleneck, prior families, precise
   gap, method and contributions.
4. Contributions: explicit threefold list for conference papers; integrated
   contribution synthesis for journals.
5. Related Work or Background: classify existing methods and position the new
   method.
6. Problem Formulation: symbols for inputs, outputs, conditions, distributions,
   splits, and targets.
7. Method Overview: one paragraph plus a figure-level pipeline.
8. Module Details: each module follows input -> operation -> output -> why it
   works.
9. Loss or Objective: explain the role of each term before equations become
   dense.
10. Experiments Setup: datasets, preprocessing, splits, baselines, metrics,
    implementation, and fairness.
11. Results: research-question subsections, not panel lists.
12. Ablation and Robustness: verify that components are necessary.
13. Biological Interpretation: DEG, pathway, distributional, or case-level
    evidence where supported.
14. Discussion and Limitations: why it works, what it means, where evidence does
    not extend, and future work.
15. Conclusion, Availability, Ethics: short handoff, code/data, and responsible
    boundary statements.

## Paragraph-Level Architecture

Every paragraph should usually contain:

1. Opening move: question, constraint, assumption, or module purpose.
2. Setup move: dataset, split, object, condition, symbol, or prior family.
3. Evidence or mechanism move: metric, formula, baseline, module, or figure.
4. Interpretation move: what this says about model behavior or scientific
   meaning.
5. Boundary or handoff move: what remains limited, deferred, or tested next.

Avoid paragraphs that merely list papers, panels, metrics, modules, or claims.

## Abstract Pattern

Use seven compact moves:

1. Field value: perturbation prediction matters for functional genomics, drug
   discovery, precision medicine, or cellular regulation.
2. Bottleneck: exhaustive experiments are infeasible because of cost, scale,
   unpaired measurements, sparsity, heterogeneity, or poor OOD coverage.
3. Existing-method gap: name the failing assumption.
4. Method: "Here we present/propose..." with method type and task.
5. Mechanism: one sentence naming the core design.
6. Evidence: datasets/settings, baselines, metrics, hard setting.
7. Implication: what principle the evidence supports.

## Introduction Pattern

Recommended five-paragraph chain:

1. Background and value: task, assay, biological goal, application value.
2. Experimental bottleneck: scale, cost, missing combinations, destructive
   observation, unpaired cells, sparse coverage.
3. Existing method families: what each solves and what assumption remains.
4. Precise gap: one or two assumptions that fail in the target setting.
5. Method and contribution: key idea, evaluation scope, and contributions.

## Related Work Pattern

Use categories, not bibliography lists:

1. Early/direct/GRN/linear methods: effective in limited settings but assume
   simpler transitions or observed perturbations.
2. Deep generative, autoencoder, and foundation-model methods: improve
   representation but may not solve the target conditional gap.
3. Closest family: OT, flow matching, set modeling, diffusion, or prior
   knowledge methods.
4. Positioning: "Our work is most closely related to X, but differs in Y."

## Methods Pattern

The golden Methods paragraph:

1. "Given [input], our goal is to [output]."
2. "Directly modeling [space/objective] is challenging because..."
3. "We therefore introduce/formulate..."
4. "Formally, let..."
5. "This yields/allows..."

Recommended order:

1. Problem setup.
2. Method overview and architecture figure.
3. Representation or encoder.
4. Core mechanism.
5. Loss or objective.
6. Training and inference protocol.

Loss paragraphs should explain why each term exists before giving formulas.

## Experiments Pattern

Use five setup paragraphs when space allows:

1. Overall assessment goal.
2. Datasets: one sentence each for biological regime, scale, and difficulty.
3. Preprocessing and splits: normalization, HVG selection, train/val/test,
   OOD/OOS policy, held-out perturbations or controls.
4. Baselines: group by category, not random order.
5. Metrics: explain what each metric measures and which direction is better.

Perturbation papers should rarely rely on only MSE. Combine endpoint metrics
with distributional metrics and biological-response metrics when available:
MSE/MAE/R2, Wasserstein/MMD, DE-Spearman, DEG overlap, response-gene precision,
variance regression, residualized or Systema-style metrics.

## Results Pattern

Results paragraphs should start from the research question:

1. "We first sought to assess whether..."
2. Experiment setting.
3. Main quantitative result.
4. Behavior interpretation.
5. Diagnostic figure or biological evidence.
6. Handoff to the next question.

## Ablation And Robustness Pattern

Use four moves:

1. Purpose: validate whether a module is necessary.
2. Intervention: remove, replace, freeze, or change one component.
3. Result: report full model versus ablated variant.
4. Interpretation: explain what capability the component provides.

## Discussion Pattern

Recommended five paragraphs:

1. Contribution and total result.
2. Why it works.
3. Biological or application meaning.
4. Limitations.
5. Future work.

## Language Style

Use restrained, evidence-bound language:

- Verbs: enable, capture, align, condition, generalize, leverage, incorporate,
  outperform, demonstrate, suggest, reveal, preserve, improve, address,
  mitigate, formulate, instantiate, benchmark, validate.
- Transitions: however, nevertheless, despite, in contrast, unlike, to address
  this limitation, motivated by, importantly, notably, together, these results
  suggest.
- Noun phrases: population-level distributional shift, heterogeneous cellular
  responses, out-of-distribution generalization, biologically grounded metrics,
  perturbation-induced transition, conditional transport, prior biological
  knowledge, gene-gene relationships, differentially expressed genes, robust
  prediction, scalable inference.

Avoid: perfect, revolutionary, unprecedented, fully proves, guarantees,
visually proves, simply, obviously, significant improvement without a metric,
and unsupported broad application claims.

## Reusable Templates

### Expression Library By Function

Use these as abstract patterns. Adapt them to the manuscript evidence; do not
copy them mechanically.

Field value:

```text
Predicting how single cells respond to perturbations is central to
understanding cellular regulation and designing targeted interventions.
```

Experimental bottleneck:

```text
Although perturbation assays provide direct measurements of cellular responses,
their cost and combinatorial scale make exhaustive experimental screening
impractical.
```

Existing-method limitation:

```text
Despite substantial progress, current methods still struggle to capture
[heterogeneity/distributional shifts] and to generalize to
[unseen perturbations/cell types/contexts].
```

Precise gap:

```text
However, [prior/source/objective] is insufficient as the sole signal for [task],
because it fails to capture [missing biological relationship].
```

Method introduction:

```text
Here we propose [METHOD], a [framework/model] that [core operation] to
[target capability].
```

Method overview:

```text
[METHOD] consists of three components: [encoder/representation],
[transport/generation module], and [alignment/loss module].
```

Mechanism explanation:

```text
To address [limitation], we introduce [module/loss], which directly encourages
[desired property] rather than merely optimizing [weaker objective].
```

Related Work positioning:

```text
Our work is most closely related to [family of methods], but differs in
[key modeling assumption/design/evaluation protocol].
```

Experiment setup:

```text
We evaluate [METHOD] on [N] representative benchmarks spanning
[biological regimes], including [dataset A], [dataset B], and [dataset C].
```

Main result:

```text
Across [settings], [METHOD] consistently outperforms [baselines], with the
largest gains observed in [hardest setting].
```

Ablation:

```text
To assess the contribution of [component], we conduct ablation experiments by
[removing/replacing] it while keeping all other settings unchanged.
```

Robustness:

```text
To evaluate robustness, we vary [sample size/noise level/hyperparameter] and
compare the degradation of [metric] across methods.
```

Visualization:

```text
UMAP visualizations show that the predicted population overlaps with the
ground-truth perturbed distribution, suggesting that [METHOD] preserves both
central tendency and heterogeneity.
```

Biological interpretation:

```text
To assess biological relevance, we perform pathway enrichment analysis on the
predicted DEGs and compare the enriched pathways with known perturbation
mechanisms.
```

Why it works:

```text
The effectiveness of [METHOD] likely stems from the interplay of [factor A],
[factor B], and [factor C].
```

Limitations and future work:

```text
Although our results demonstrate clear potential, several challenges remain,
including [generalization/noise/batch effects/scalability].
```

Abstract:

```text
Predicting [cellular response] to [perturbations] is essential for
[biological/application goal]. However, [experimental/computational bottleneck]
makes exhaustive profiling infeasible. Existing methods often [limitation],
which restricts their ability to [OOD/generalization/heterogeneity/distribution].
Here, we present [METHOD], a [framework] that [core idea]. [METHOD] integrates
[module A] with [module B] to [mechanism]. Across [datasets/settings], [METHOD]
[outperforms/improves] [baselines] on [metrics], with particularly strong gains
in [hard setting]. Together, these results suggest that [principle] provides a
practical route toward [application].
```

Results subsection:

```text
We first asked whether [method/component] improves [capability]. To this end,
we trained [models] on [dataset] under [split] and compared them with
[baselines]. [METHOD] achieved [metric result], outperforming [baseline]. The
gain was most pronounced in [hard setting], suggesting that [mechanistic
explanation]. Qualitative analysis using [UMAP/pathway/DEG] further confirmed
that [METHOD] captures [biological property].
```

Metric-to-advantage paragraph:

```text
[Metric] evaluates [capability], which matters because [scientific or modeling
reason]. In [setting], [METHOD] improves over [strongest baseline], suggesting
that [mechanistic or biological interpretation]. We use [secondary evidence]
only as interpretive support for this primary comparison.
```

Response-gene recovery paragraph:

```text
Response-gene identity recovery links predicted expression changes to
perturbation-associated genes and downstream interpretation. [Overlap metric]
compares the strongest observed and predicted response-gene sets under the same
ranking and exclusion rules. Higher overlap for [METHOD] indicates that its
advantage extends beyond aggregate response alignment to recovery of key
response genes.
```

Discussion:

```text
We have presented [METHOD], a [framework] for [task]. Across [settings],
[METHOD] improves [accuracy/distributional fidelity/generalization] while
preserving [biological property]. These gains likely arise from [factor A],
[factor B], and [factor C]. Importantly, [METHOD] is
[scalable/flexible/lightweight/interpretable], making it suitable for
[application]. However, several challenges remain, including [limitations].
Future work should explore [extensions], which may further improve [goal].
```

## Journal Versus Conference

Journal style:

- Related Work is often integrated into Introduction.
- Results can precede Methods.
- Abstract emphasizes biological meaning and broad implications.
- Discussion must state limitations and future directions.
- Common phrasing: "Here, we present", "We found that", "Our results indicate",
  "Together, these results suggest".

Conference style:

- Related Work is often separate.
- Methods and experiments appear earlier.
- Contributions are often explicit and numbered.
- Results emphasize benchmark, table, ablation, efficiency, and fairness.
- Common phrasing: "Our contributions are threefold", "We formulate",
  "We instantiate", "We benchmark", "Compared with".

## Practical Writing Strategy

1. Define the central gap before writing any section.
2. Make the method name bind to a capability, not only a module.
3. Do not rely on one main table. Combine main results, OOD/OOS, ablation,
   robustness/scaling, and biological or distributional interpretation.
4. Keep language restrained but strong.
5. Make each paragraph perform one function.

## Anti-Template Rules

Before using any template, instantiate the evidence object inventory:

- dataset;
- split;
- held-out object;
- metric;
- metric direction;
- strongest baseline;
- numerical anchor, if available;
- mechanism interpretation;
- boundary.

Do not deliver prose that still contains placeholders such as `[METHOD]`,
`[dataset]`, `[metric]`, or `[baseline]`.

Do not write "substantially outperforms", "consistently improves", or
"generalizes to unseen perturbations" unless the tested setting, comparison,
and evidence strength are visible.

If a numerical anchor is unavailable, use a scoped qualitative claim:

```text
The comparison is consistent with improved [behavior] in [setting], but the
claim should remain qualitative until numerical anchors are inserted.
```
