# Metric Cards

Use these cards before writing Experiments, Results, captions, or reviewer
findings. A metric card defines what the metric can support and what it cannot.

## Endpoint Error: MSE, MAE, nMSE

Use when:

- measuring expression-level prediction error;
- comparing endpoint reconstruction under the same split and preprocessing.

Measures:

- average discrepancy between predicted and observed expression summaries or
  vectors, depending on implementation.

Direction:

- lower is better.

Common misuse:

- treating low endpoint error as proof of response-gene identity recovery;
- ignoring cell-state heterogeneity or distributional shape.

Required wording:

- "Lower nMSE indicates smaller endpoint expression error under this split."

## Pearson Or R2

Use when:

- evaluating correlation or explained variance in expression profiles;
- comparing aggregate response trends.

Measures:

- Pearson: linear association;
- R2: explained variance relative to a baseline or target.

Direction:

- higher is better.

Common misuse:

- reporting correlation without saying whether it is gene-level, condition-level,
  cell-level, mean response, residualized response, or another aggregation.

Required wording:

- "Higher Pearson correlation indicates stronger agreement in [specified
  aggregation]."

## DE-Spearman, DE Overlap, DE Precision, Overlap@20

Use when:

- evaluating recovery of perturbation-responsive genes;
- checking whether the predicted response identifies relevant gene changes.
- connecting expression prediction to downstream mechanism interpretation.

Measures:

- rank or set agreement between observed and predicted response-gene signals.

Direction:

- higher is better.

Common misuse:

- implying a trained DEG classifier when the score is computed from response
  magnitude;
- treating DEG overlap as distributional fidelity.

Required wording:

- "Overlap@20 measures whether the top predicted response genes recover the
  observed top response genes; higher values indicate stronger response-gene
  identity recovery."

Results interpretation:

- Do not present response-gene overlap as a small auxiliary metric when it is
  central to the claim. Use it to state an advantage: recovery of response-gene
  identity, not only response-vector alignment.
- A strong Results paragraph should explain why response-gene recovery matters:
  it links prediction to perturbation-associated genes and downstream
  biological interpretation.
- When evidence exists, extend the metric with top-gene expression statistics,
  single-gene distribution examples, and pathway enrichment. These are
  interpretive supports, not replacements for the primary overlap metric.

CommonDEG@k / Overlap@k definition pattern:

```text
Overlap@k = |TopK_true_response_genes intersect TopK_pred_response_genes|
```

Where `TopK_true_response_genes` is derived from observed perturbed versus
control response and `TopK_pred_response_genes` is derived from predicted
response under the same exclusion and ranking rules.

Required advantage wording:

- "This result indicates that the method's advantage extends from aggregate
  response alignment to recovery of response-gene identity."

Boundary:

- If the metric is computed from response magnitude rather than a formal DEG
  test, do not call it a DEG test. Use "response-gene identity recovery" unless
  true differential-expression testing was performed.

## Wasserstein Distance

Use when:

- observed and predicted cells are unpaired;
- distributional agreement matters.

Measures:

- distance between predicted and observed perturbed distributions under the
  chosen feature space and aggregation.

Direction:

- lower is better.

Common misuse:

- treating lower Wasserstein as proof of true cell-wise matching;
- reporting UMAP without a quantitative distribution metric.

Required wording:

- "Lower Wasserstein distance indicates closer distributional agreement between
  predicted and observed perturbed populations."

## MMD

Use when:

- comparing two sample distributions with a kernel-based statistic;
- checking terminal distribution alignment in flow or generative settings.

Measures:

- kernel discrepancy between predicted and observed distributions.

Direction:

- lower is better.

Common misuse:

- failing to state kernel, feature space, or aggregation level when it matters;
- interpreting MMD as a cell-pair metric.

Required wording:

- "Lower MMD indicates smaller kernel discrepancy between predicted and observed
  distributions."

## Mean And Variance Correlation

Use when:

- separating central tendency from heterogeneity;
- evaluating population-level response summaries.

Measures:

- agreement in per-gene means or variances across predicted and observed
  perturbed populations.

Direction:

- higher is better.

Common misuse:

- claiming full distribution recovery from mean correlation alone.

Required wording:

- "Mean correlation evaluates central response agreement, whereas variance
  correlation probes whether heterogeneity is preserved."

## Systema-Style Residual Metrics

Use when:

- shared systematic variation may inflate endpoint metrics;
- perturbation-specific residual signal is the target.

Measures:

- agreement after accounting for shared or systematic components according to
  the stated residualization protocol.

Direction:

- depends on the defined score; state it explicitly.

Common misuse:

- replacing endpoint or distributional metrics with residual diagnostics;
- failing to explain what was residualized.

Required wording:

- "Systema-style residual metrics evaluate perturbation-specific agreement after
  accounting for shared systematic variation."

## Reference-Centered And Centroid-Centered Metrics

Use when:

- the prediction is reference-relative;
- the method claims improved state-origin conditioning.

Measures:

- agreement relative to a chosen reference origin or centroid baseline.

Direction:

- state direction for each metric.

Common misuse:

- describing these as generic endpoint accuracy;
- blurring reference origin with true cell identity.

Required wording:

- "Reference-centered metrics quantify response agreement relative to the
  selected prediction origin, not true cell-wise pairing."

## Pathway Enrichment Diagnostics

Use when:

- interpreting predicted response genes biologically;
- checking consistency with known perturbation mechanisms.

Measures:

- overlap between enriched pathways from predicted response genes and known or
  observed pathways.

Direction:

- depends on enrichment score and comparison design.

Common misuse:

- treating enrichment as proof of mechanism;
- using pathway evidence without quantitative response-gene recovery.

Required wording:

- "Pathway enrichment provides biological diagnostic support and should be
  interpreted together with quantitative response-gene metrics."
