# Paper Imitation Guide for Perturbation-Prediction Writing

Use this guide when high-level story chains are not enough. Its job is to force
the writer to look at real perturbation-prediction papers and extract concrete
paragraph moves, sentence functions and transition patterns before revising
TriShift.

Do not copy text from these papers. Copy the structure of reasoning: how a
paragraph earns its claim, how a metric is made meaningful, how the evidence
sequence becomes a story, and how caveats are bounded.

## Local Reference Papers

The default local paper folder should be configured by the user. In the original
local setup this was a folder containing the papers below.

| Paper | Local path | Best use |
|---|---|---|
| scPRAM | `<local-paper-folder>/scpram.pdf` | Bioinformatics article scale, structured abstract, Results rhythm, figure-linked paragraphs |
| SCALE | `<local-paper-folder>/SCALE.pdf` | problem-driven Methods, population/transport framing, metric-conflict explanation, benchmark roadmap |
| scDFM | `<local-paper-folder>/scdfm.pdf` | formula-after-definition discipline, setup before result claims, distribution-level modeling prose |
| Scouter | `<local-paper-folder>/scouter.pdf` | concise Nature-style benchmark results, prior provenance, metric orientation, case-study linkage |
| Conditional Monge Gap | `<local-paper-folder>/Conditional Monge Gap enables generalizable single-cell perturbation modelling.pdf` | OT notation, conditional generalization story, explaining weak/strong regimes, limitations |

If a file is missing, inspect the available papers and say which exemplar was
unavailable. If `pdftotext` is unavailable, use Python PDF extraction with
`pypdf` and search for the relevant section heading.

## Extraction Workflow

Before rewriting a section, extract a small pattern table from 2-3 relevant
papers. Keep it short, but make it concrete.

For each exemplar paragraph, record:

1. Section and paragraph role, for example "Results overview", "metric setup",
   "main comparison", "case visualization", "Methods task setup".
2. Opening move: what question, constraint or benchmark is introduced.
3. Evidence move: what metric, split, baseline, figure or example appears.
4. Interpretation move: what the result says about model behavior.
5. Boundary move: what is deferred, caveated or limited.
6. Useful sentence pattern, rewritten in abstract form rather than copied.
7. What not to transfer because it conflicts with TriShift evidence or teacher
   requirements.

Example extraction format:

```text
Paper: scPRAM
Paragraph role: Results metric setup
Opening move: To demonstrate out-of-sample accuracy, state the held-out cell-type setting.
Evidence move: Define Wasserstein distance first, then mean/variance regression.
Interpretation move: Link mean to population response and variance to heterogeneity.
Transfer to TriShift: introduce metrics by what behavior they test, then report sparse anchors.
Avoid: claims like "perfectly aligns" unless backed by exact evidence.
```

## Results Overview Patterns

The Results overview should make the evidence feel necessary. It should not be a
list of figures or a proof checklist.

### scPRAM pattern

Typical chain:

1. State the first evaluation purpose, often out-of-sample prediction.
2. Name the dataset or split logic.
3. Explain why the metric is appropriate for unpaired cells.
4. Move from aggregate metrics to a visualization or gene-level view.
5. Use later subsections to broaden the setting, such as cross-species,
   cross-individual or robustness.

What to transfer:

- Start a Results subsection with the question being tested.
- Introduce metric meaning before reporting numbers.
- Use visual panels as intuition after quantitative metrics, not as proof.

TriShift adaptation:

- Replace scPRAM's "unseen cell type response" framing with "held-out reference
  origin / target-domain control transfer".
- Preserve the distinction between unpaired distribution comparison and
  non-existent true cell-wise errors.

### SCALE pattern

Typical chain:

1. Define benchmark scope and why existing metrics can be incomplete.
2. Separate reconstruction accuracy from biological fidelity.
3. Explain apparent metric conflicts rather than hiding them.
4. Use scaling or atlas-level experiments only after the core model behavior is
   established.

What to transfer:

- A Results overview can say which biological question each evidence block
  addresses.
- When one metric is imperfect, explain what it measures and why another metric
  is needed.

TriShift adaptation:

- Use this for Systema-style and distribution-level paragraphs: endpoint
  metrics, perturbation-specific residual metrics and distribution recovery
  test different failure modes.

### scDFM pattern

Typical chain:

1. Establish benchmark, data, baselines and split before making claims.
2. Move from additive or holdout generalization to harder drug or combination
   settings.
3. Use ablations to show which objective or architecture supports the result.

What to transfer:

- Setup paragraphs are not administrative. They are part of the evidence.
- Use "we evaluated..." only after the split and comparison are clear.

TriShift adaptation:

- In each Results subsection, state whether the task is held-out-control genetic
  prediction, PBMC target-domain-control transfer or Norman combination
  generalization before reporting metrics.

### Scouter pattern

Typical chain:

1. Present the method gap in one compact sentence.
2. Compare against state-of-the-art baselines with a small number of metrics.
3. Use fixed cases to show response-gene behavior.
4. Discuss coverage or prior-knowledge limitations where relevant.

What to transfer:

- Do not report every panel. Choose the strongest anchor and explain its
  implication.
- Keep prior-source claims concrete and reproducible.

TriShift adaptation:

- Use for GenePert/GEARS/BioLORD/scGPT comparisons and for PBMC IFNB1 prior
  provenance.

### CMonge pattern

Typical chain:

1. Start with conditional generalization or treatment-context generalization.
2. Define in-sample and out-of-sample regimes.
3. Pair quantitative metrics with distribution-shape or UMAP evidence.
4. Explain regimes where performance changes, such as dose, embedding distance,
   small effect size or support shift.

What to transfer:

- Results should explain why a hard condition is hard.
- Weak or mixed cases should be bounded, not ignored.

TriShift adaptation:

- Use this for Dixit distance-stratified robustness and PBMC cross-cell-type
  transfer wording.

## Results Paragraph Recipes

### Evidence roadmap

Use when writing the opening of Results.

Natural chain:

1. The central empirical question.
2. Why one metric or one dataset is insufficient.
3. The sequence of evidence blocks.
4. What main figures versus supplement figures do.

Template:

```text
We evaluated [method] through [number] complementary analyses that test whether
[central modeling requirement] improves [target behavior]. First, [setting]
tests [question]. We next use [ablation/diagnostic] to isolate [mechanism].
We then examine [harder generalization setting]. Finally, [distribution/case
analysis] assesses whether [cell-level/biological behavior] is preserved.
Supplementary analyses provide [condition-level distributions, robustness,
additional cases] rather than replacing the main evidence.
```

Avoid:

- "If the method works, then..." proof checklists.
- "Fig. 2 shows..., Fig. 3 shows..." with no scientific question.
- Starting with "In this section..." unless the paragraph has no better
  conceptual opening.

### Metric setup paragraph

Natural chain:

1. Why this metric is needed.
2. What it measures.
3. Which direction is better.
4. What failure mode it catches.

Template:

```text
Because the observed and predicted cells are not paired, we evaluated
distributional agreement rather than cell-wise error. [Metric] measures
[behavior]; lower/higher values indicate [direction]. We use it together with
[second metric] because [first metric] captures [aspect] but not [other aspect].
```

### Main comparison paragraph

Natural chain:

1. State the strongest relevant comparison.
2. Give one or two numerical anchors.
3. Explain the model behavior suggested by the result.
4. Bound the claim to the evaluated setting.

Template:

```text
In [dataset/split], TriShift achieved [metric] of [value], compared with [best
baseline] at [value]. The improvement was most apparent in [metric/failure
mode], suggesting that [mechanistic interpretation]. This conclusion is limited
to [setting], where [held-out object and evaluation protocol].
```

### Case or visualization paragraph

Natural chain:

1. State why the case was selected.
2. Describe the observed pattern using specific axes or distributions.
3. Link the visualization to aggregate metrics.
4. Avoid treating UMAP/violin as proof.

Template:

```text
To provide a gene- or cell-level view of this trend, we examined [case]. The
observed perturbed cells [distribution/position behavior], whereas [baseline]
[failure mode]. TriShift [behavior]. This visualization is consistent with
[metric trend], but is used as diagnostic support rather than as a standalone
test.
```

## Methods Imitation Patterns

### SCALE-style task setup

Use for Methods overview and problem formulation.

Natural chain:

1. Define the data objects and biological context.
2. State that observations are unpaired.
3. Formulate the task as population or reference-conditioned transition.
4. Only then introduce model components.

TriShift transfer:

- Start with destructive unpaired observations.
- Define \(\bm{x}_i^0\), \(\bm{y}_j\), \(p_j\), \(\bm{e}_j\), reference origins and
  prediction targets before equations that use them.
- Explain that OT is training-time reference supervision, not a true cell match.

### CMonge-style OT notation

Use when editing OT or distributional methods.

Natural chain:

1. Define source/target samples or measures.
2. Define marginals.
3. Define cost matrix and index meaning.
4. Define coupling set.
5. Define entropy and regularization coefficient.
6. Define objective.
7. Interpret the coupling and state what it does not imply.

TriShift transfer:

- Define \(N_0^{\mathrm{train}}\), \(\mathcal{J}_{\mathrm{train}}\), \(\mathbf{C}\),
  \(\Pi(\bm{a},\bm{b})\), \(\tau\), \(H(\mathbf{P})\), and \(\mathbf{P}^\star\)
  before using them.
- State that \(P_{ij}^\star\) is a soft reference weight, not a biological
  pairing probability.

### scDFM-style formula discipline

Use when formulas feel decorative or symbols appear too early.

Natural chain:

1. Define variables and dimensions in prose.
2. Present the formula.
3. Interpret the formula's role.
4. Defer implementation details to supplement if not essential.

TriShift transfer:

- In VAE and generation losses, define full vectors before scalar components.
- Define weights before objectives that use them.
- If a formula needs "where ..." for every symbol, check whether some definitions
  should move before the formula.

## Discussion Imitation Patterns

### CMonge/SCALE-style discussion

Natural chain:

1. Restate the contribution as a modeling answer to the core constraint.
2. Explain why the mechanism works.
3. Relate to prior method families fairly.
4. State concrete evidence boundaries.
5. Give future directions that follow from those boundaries.

TriShift transfer:

- Contribution: reference-conditioned state transition for unpaired
  perturbation prediction.
- Mechanism: state-compatible references plus external perturbation priors.
- Prior methods: endpoint generation, prior-based perturbation models, OT or
  distributional mapping, foundation models.
- Boundaries: IFNB1/PBMC only for cytokine prior evidence, OT reference quality,
  higher-order combinations, dose/time/batch/platform shifts.

## Sentence-Level Transfer Rules

Use these rules after the section chain is correct.

- Prefer causal openings over mechanical openings:
  - Weak: "Figure 2 shows..."
  - Stronger: "To test whether the model transfers to unseen reference origins,
    we evaluated..."
- Prefer behavior interpretation over generic superiority:
  - Weak: "TriShift performs better."
  - Stronger: "This improvement suggests that conditioning on held-out control
    origins reduces collapse toward a shared endpoint."
- Prefer scoped claims over broad claims:
  - Weak: "The method handles cytokines."
  - Stronger: "In the IFN-beta PBMC task, the IFNB1 ProtT5 prior supports
    target-domain stimulated-response prediction."
- Prefer "supports", "is consistent with", "suggests", "indicates" when the
  evidence is indirect.
- Avoid repeated paragraph openings such as "First", "Next", "Finally" in
  every subsection. Use them when sequencing matters, otherwise open with the
  evaluated question.

## Pre-Submission Reviewer Prompt Add-On

When asking a reviewer to check a section revised with this guide, include:

```text
Please check whether the edited section only follows a high-level architecture,
or whether it actually imitates the paragraph moves of the relevant local
reference papers. In particular, check whether Results paragraphs state the
evaluated question, setup, metric meaning, strongest comparison, sparse
quantitative anchor, behavior interpretation and boundary. Flag figure lists,
metric piles, oral phrasing, or unsupported broad claims.
```
