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
  metric-cards.md
  claim-ledger-template.md
  method-variable-scope.md
manifest.yml
tests/
```

## Installation

Copy the skill directories into your local skill directory:

```bash
cp -R skills/* ~/.agents/skills/
```

If your runtime uses a different skill root, copy `skills/*` into that root
instead. Keep `references/` available next to this repository or copy the
reference files into the installed `perturbation-prediction-writing/references/`
folder.

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

## Quickstart

Broad rewrite:

```text
$perturbation-writing-do improve this Results section using the corpus guide
```

Review only:

```text
$perturbation-reviewer review this manuscript like a referee
```

Venue conversion:

```text
$perturbation-writing-do convert this manuscript to BIBM style
```

TriShift-specific work:

```text
$perturbation-writing-do revise the TriShift PBMC IFNB1 Results paragraph
```

## Scope

These skills are designed for perturbation-response and expression-prediction
papers, including single-cell perturbation prediction, conditional transport,
optimal transport, flow matching, perturbation priors, foundation models, and
TriShift-style reference-conditioned state-transition manuscripts.

TriShift-specific claims live in `trishift-writing-core` and should only be
loaded when the manuscript or user request is actually about TriShift or a
TriShift-style reference-conditioned model.

## Smoke Tests

Run:

```bash
python tests/run_skill_tests.py
git diff --check
```

Expected:

- skill front matter is valid;
- `manifest.yml` names the router, legacy alias, TriShift overlay, reviewer, and
  output modes;
- `perturbation-prediction-writing` remains a legacy alias;
- metric cards and claim ledger templates exist.

## Quality Principles

- No broad claim without dataset, split, held-out object, metric, metric
  direction, strongest baseline, and boundary.
- No OT true-cell-pair wording.
- No visual proof without quantitative support.
- No TriShift-specific boundary unless `trishift-writing-core` is loaded.
- No template placeholders such as `[METHOD]`, `[dataset]`, or `[metric]` in
  final prose.
- No "substantially outperforms" without a numerical or clearly described
  evidence anchor.
- No overdefined Problem Formulation: define task-critical variables first, and
  move module-local variables, hyperparameters, split details, and baseline
  internals to the right subsection.
