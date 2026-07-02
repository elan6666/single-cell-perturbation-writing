# Single-Cell Perturbation Writing Skills

Modular writing and reviewer skills for single-cell perturbation prediction
manuscripts.

The package was split from a monolithic `perturbation-prediction-writing` skill
into a router-driven system:

- `perturbation-writing-do`: natural-language router, similar to `byte-do`.
- `perturbation-prediction-writing`: legacy-compatible entrypoint.
- `perturbation-writing-core`: shared domain rules and claim boundaries.
- `perturbation-writing-corpus-guide`: distilled corpus writing guide.
- `perturbation-writing-style`: academic style pass.
- `perturbation-writing-sync`: CN/EN/Supplement synchronization.
- Section skills for Abstract, Introduction, Related Work, Methods,
  Experiments, Results, Discussion, and Supplement/Captions.
- `perturbation-reviewer`: one integrated reviewer skill.

## Layout

```text
skills/
  perturbation-writing-do/
  perturbation-prediction-writing/
  perturbation-writing-core/
  perturbation-writing-corpus-guide/
  perturbation-writing-style/
  perturbation-writing-sync/
  perturbation-abstract/
  perturbation-introduction/
  perturbation-related-work/
  perturbation-methods/
  perturbation-experiments/
  perturbation-results/
  perturbation-discussion/
  perturbation-supplement-captions/
  perturbation-reviewer/
references/
  latest-corpus-writing-guide.md
  paper-imitation-guide.md
```

## Usage

Use the automatic router for broad manuscript tasks:

```text
$perturbation-writing-do improve this Results section using the corpus guide
```

Use the stable legacy entrypoint when existing prompts already reference it:

```text
$perturbation-prediction-writing rewrite this Methods section and run reviewer
```

Use specific section skills when the target is already known:

```text
$perturbation-methods check notation and OT reference wording
$perturbation-reviewer review this manuscript like a referee
```

## Scope

These skills are designed for perturbation-response and expression-prediction
papers, including single-cell perturbation prediction, conditional transport,
optimal transport, flow matching, perturbation priors, foundation models, and
TriShift-style reference-conditioned state-transition manuscripts.
