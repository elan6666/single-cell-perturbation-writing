---
name: perturbation-related-work
description: Write or review Related Work and Background sections for perturbation-prediction manuscripts. Use for method-family organization, citation positioning, prior-work comparison, venue-specific Related Work, and reference coverage checks.
---

# Perturbation Related Work

Use after `perturbation-writing-core` and `perturbation-writing-corpus-guide`.

## Related Work Job

Related Work should classify prior methods by modeling assumption and explain
where the current work sits. It should not be a citation list.

Each paragraph should answer:

1. What family of methods is this?
2. What problem does it solve?
3. What assumption or limitation remains?
4. How does the present work differ?

## Recommended Structure

1. Early or direct methods:
   - linear models, GRN methods, mean-response predictors, identity baselines,
     direct mapping approaches;
   - useful for simple settings but limited under OOD, unpaired observations, or
     heterogeneous population shifts.
2. Deep generative and representation methods:
   - scGen, CPA, BioLORD, autoencoder or conditional generation methods;
   - improve latent representation and counterfactual generation but can rely
     on endpoint assumptions or insufficient reference-origin modeling.
3. Prior-based and foundation-model methods:
   - GEARS, GenePert, Scouter, scGPT, Geneformer, GO/KG/LLM/protein embeddings;
   - improve unseen perturbation representation but priors alone do not define
     cell-state starting points.
4. Distributional, OT, flow, and set-level methods:
   - CellOT, CMonge, scPRAM, SCALE, scDFM, flow matching, set modeling;
   - address unpaired distributional structure but may not cover the target
     reference-conditioned or held-out-reference setting.
5. Positioning paragraph:
   - name the closest family;
   - state the exact difference in formulation, mechanism, or evaluation.

## TriShift Positioning

TriShift should be positioned as:

- close to unpaired OT and distributional perturbation modeling because it uses
  state-compatible references under destructive observation;
- close to perturbation-prior methods because it uses external perturbation
  information for unseen perturbations;
- distinct because it predicts reference-relative shifts from held-out or
  state-matched control origins rather than direct endpoints or
  perturbation-only effects.

## Venue Rules

Journal:

- Related Work can be folded into Introduction.
- Avoid a long standalone method taxonomy unless the journal style supports it.

Conference:

- A separate Related Work section is common.
- Use compact paragraphs and explicit comparison sentences.
- Make the closest related family clear before Method.

## Useful Sentence Patterns

- "A first line of work focuses on..."
- "These methods are effective when..., but typically assume..."
- "A second family of methods models..."
- "More recently, ... has been proposed to..."
- "Our work is most closely related to..., but differs in..."
- "Rather than [old assumption], we formulate [task] as [new problem]."

## Reviewer Checks

- Are essential baselines and closest methods represented?
- Are citations grouped by modeling role rather than chronology alone?
- Does every limitation apply to the cited family and not misrepresent it?
- Does the positioning avoid strawman comparisons?
- Is the contribution differentiated by assumption, mechanism, or evaluation?
