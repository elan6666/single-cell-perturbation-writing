---
name: perturbation-methods
description: Write, rewrite, or review Methods for perturbation-prediction manuscripts. Use for problem formulation, notation, model overview, module rationale, OT/reference construction, perturbation priors, objectives, training, inference, and evaluation reference policy.
---

# Perturbation Methods

Use after `perturbation-writing-core` and `perturbation-writing-corpus-guide`.

## Methods Job

Methods converts the scientific gap into a precise modeling formulation. It
must make the reader understand:

- what objects are observed;
- what is unpaired or missing;
- what the model predicts;
- what each symbol means;
- why each module exists;
- how training differs from evaluation;
- what the method does not imply.

## Required Story Chain

1. Start from destructive, unpaired single-cell observations.
2. Define prediction objects: control cells, perturbed cells, labels,
   perturbation priors, reference origins, target distributions, and splits.
3. State the modeling form: reference-conditioned transition, conditional
   transport, distributional flow, endpoint generation, or another precise
   formulation.
4. Explain workflow as consequence of the modeling form:
   - representation creates comparable state space;
   - reference or transport module identifies state-compatible origins;
   - perturbation prior or condition embedding captures unseen perturbation
     information;
   - generator, decoder, flow, or shift head produces the prediction.
5. Present formulas only after symbols are defined.
6. Separate training-time construction from evaluation-time reference policy.
7. Put long hyperparameters, metric derivations, and implementation details in
   Supplement unless needed in main text.

## Paragraph Types

- Problem framing, 80-150 words.
- Notation setup, 120-250 words.
- Overview, 180-350 words.
- Module rationale, 70-140 words.
- Formula block, 1-3 equations plus 80-180 words.
- Formula interpretation, 50-120 words.
- Training/inference protocol, 120-250 words.
- Boundary note, 60-120 words.

## Golden Methods Paragraph

```text
Given [input], our goal is to [output]. Directly modeling [space/objective] is
challenging because [unpaired/noisy/high-dimensional/missing reference issue].
We therefore formulate [task] as [modeling form]. Formally, let [symbols] denote
[objects]. This construction yields [output] and allows [capability].
```

## Notation Rules

- Define full vectors before scalar components.
- Define sample sets before distributions over them.
- Define indices and dimensions before matrix entries.
- Define measures, marginals, cost matrix, coupling set, entropy, and
  regularization before OT objectives.
- Do not use a symbol in an equation before it has a prose role.
- Avoid "where ..." clauses that introduce every symbol after a dense formula;
  move definitions before the formula.
- Use neutral training-expression notation for arbitrary VAE inputs; reserve
  control and perturbed symbols for actual control/perturbed cells.

## TriShift-Specific Methods Rules

- Start from destructive, unpaired control and perturbed observations.
- State that TriShift predicts a reference-relative expression shift.
- Explain that OT constructs state-compatible reference supervision or
  candidates, not biological one-to-one matches.
- Distinguish training-time OT pools from evaluation-time held-out references.
- Define external perturbation priors and their dimensionality/source.
- Explain how reference state and perturbation prior combine.
- State the evaluation-time rule: held-out control references can be used as
  prediction origins but target perturbed cells cannot leak into training or
  model selection.

## Loss And Objective Guidance

For each objective term:

1. State the failure mode it addresses.
2. Define inputs and outputs.
3. Present the formula.
4. Interpret the term's behavioral effect.
5. State whether it is main-text essential or Supplement-level detail.

Do not write "we add loss X" without explaining why a weaker objective is
insufficient.

## Avoid

- Beginning Methods with "Module 1".
- Describing formulas before defining symbols.
- Saying OT matches true cells.
- Mixing implementation details with conceptual rationale in one long sentence.
- Hiding train/eval reference differences.
- Naming architecture components without their modeling role.
