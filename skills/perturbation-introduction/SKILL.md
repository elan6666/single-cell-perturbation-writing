---
name: perturbation-introduction
description: Write, rewrite, review, or venue-adapt introductions for perturbation-prediction papers. Use for motivation, central gap, contribution framing, prior-method progression, teacher-style causal funnel, and conference contribution lists.
---

# Perturbation Introduction

Use after `perturbation-writing-core` and `perturbation-writing-corpus-guide`.

## Introduction Job

The Introduction should build a causal funnel:

```text
biological value -> experimental bottleneck -> existing method families -> exact
remaining gap -> method insight -> evidence preview or contributions
```

It is not a literature inventory. Each prior-work family should solve one
problem and leave one precise remaining problem.

## Default Five-Part Chain

1. Background and value:
   - cellular response prediction supports functional genomics, drug discovery,
     therapeutic design, gene-function analysis, and personalized intervention;
   - single-cell assays expose heterogeneous responses.
2. Experimental bottleneck:
   - candidate perturbations expand across genes, combinations, drugs,
     cytokines, doses, cell types, states, patients, and batches;
   - single-cell perturbation assays are destructive and unpaired;
   - exhaustive profiling is infeasible.
3. Existing method families:
   - endpoint, conditional generation, and disentangled representation methods;
   - perturbation-prior methods such as gene embeddings, GO/KG methods, LLM
     embeddings, or foundation models;
   - OT, flow-matching, distributional, or set-level methods.
4. Precise gap:
   - name the assumption that fails in the target task;
   - for TriShift, emphasize state-matched reference origin plus
     perturbation-specific shift.
5. Method and contribution:
   - "In this work..." with one-sentence mechanism;
   - evidence preview;
   - explicit contribution list for conference venues if appropriate.

## TriShift Introduction Chain

Use this when TriShift is the target:

1. Cellular response prediction supports drug discovery, therapeutic design,
   gene-function analysis, and personalized intervention.
2. Perturbation spaces expand across genes, combinations, drugs/cytokines, cell
   types, and states; single-cell assays are destructive and unpaired.
3. Endpoint, conditional generation, or disentangled methods such as scGen and
   BioLORD enable post-perturbation generation but can extrapolate poorly when
   observed states or perturbation backgrounds are missing.
4. External-prior methods such as GEARS, GenePert, Scouter, scGPT-like models,
   or protein/gene embeddings improve unseen-perturbation representation, but
   perturbation identity alone does not determine the control state.
5. OT and distributional methods such as CellOT, CMonge, SCALE, scDFM, and
   scPRAM motivate unpaired distributional alignment, but observed transitions
   or unconditional maps do not solve unseen perturbation plus held-out
   reference-origin prediction.
6. TriShift is introduced as a reference-conditioned state-transition model
   using OT reference supervision, external perturbation priors, held-out
   references, and evidence across reference transfer, ablation, combination
   generalization, and distribution recovery.

## Contribution Framing

For conference papers, explicit contributions are acceptable:

```text
Our contributions are threefold. First, we formulate [task] as [problem],
which addresses [gap]. Second, we instantiate this formulation with [mechanism].
Third, we benchmark [method] under [settings], showing [evidence].
```

For journal papers, integrate contributions into prose unless the venue
encourages bullets.

## Paragraph Quality Checks

- Does paragraph 1 start with the biological task, not the model?
- Does the bottleneck paragraph make in silico prediction necessary?
- Does each prior family have one solved problem and one remaining assumption?
- Is the central gap explicit and narrow?
- Does the method paragraph state the key insight before listing modules?
- Does the evidence preview match actual figures and metrics?

## Avoid

- "Many methods exist" without categorization.
- A paragraph that lists citations without explaining the unresolved assumption.
- Broad claims about drug/cytokine/protein generalization without evidence.
- Ending the Introduction with modules instead of contributions or evidence.
