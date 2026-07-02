---
name: perturbation-abstract
description: Write, rewrite, compress, expand, or review abstracts for perturbation-prediction manuscripts. Use for journal structured abstracts, conference single-paragraph abstracts, TriShift summaries, and venue-adapted abstract revisions.
---

# Perturbation Abstract

Use this skill after loading `perturbation-writing-core` and
`perturbation-writing-corpus-guide`.

## Abstract Job

An abstract compresses the whole paper into one causal chain. It should not be a
module list or a results dump. It should let a reviewer answer:

- What biological or modeling problem matters?
- Why can experiments or existing methods not solve it?
- What precise gap does the method address?
- What is the core mechanism?
- What evidence supports the claim?
- What implication is justified by the evidence?

## Required Story Chain

Use this chain for most perturbation-prediction abstracts:

1. Value: perturbation response prediction matters for functional genomics,
   drug discovery, cellular regulation, therapeutic design, or precision
   medicine.
2. Opportunity: single-cell perturbation assays reveal cell-state-specific
   responses.
3. Constraint: exhaustive profiling is costly, incomplete, destructive,
   unpaired, sparse, high-dimensional, or heterogeneous.
4. Gap: existing methods assume an endpoint, mean effect, observed perturbation
   background, dense prior graph, or missing state-matched reference origin.
5. Method: present the method as a framework, model, formulation, or training
   system.
6. Mechanism: state the core design in one sentence.
7. Evidence: name benchmark scope, hard settings, metrics or baselines, and
   deeper evidence such as ablation, robustness, distribution recovery, or
   response-gene identity.
8. Implication: close with what principle the evidence supports.

For TriShift, the default chain is:

```text
value -> single-cell opportunity -> destructive/incomplete perturbation coverage
-> endpoint or perturbation-only gap without state-matched reference origins
-> reference-conditioned state-transition framework
-> denoising VAE latent space, OT state-compatible references, reference-relative
shift prediction, and perturbation priors
-> unseen genetic perturbations, held-out controls, Norman combinations, PBMC
IFN-beta transfer, Systema-style diagnostics, Overlap@20, and distribution
recovery where available
-> preservation of perturbation-specific signals and cellular heterogeneity
```

## Venue Modes

Journal or Bioinformatics:

- May use structured labels if the venue requires them.
- Emphasize biological value, findings, and restrained implications.
- Results can be described as "we found" or "our results indicate".
- Availability belongs only if the venue style requires it.

Conference or BIBM:

- Usually one compact paragraph.
- Make the method, contribution, benchmark, and metric evidence more explicit.
- If space permits, include a three-part contribution only in Introduction, not
  necessarily in the abstract.
- Avoid long biological future-work claims.

## Sentence Functions

Use one sentence per function where possible:

1. Field value.
2. Experimental or modeling bottleneck.
3. Existing-method limitation.
4. Method introduction.
5. Core mechanism.
6. Empirical support.
7. Implication.

If the venue imposes a strict word limit, combine value+constraint and
method+mechanism, but do not remove the precise gap.

## Required Checks

- Is the central gap sharper than "existing methods are limited"?
- Does the method name bind to a capability, not only modules?
- Are claims limited to tested perturbation types and datasets?
- Are metrics or settings specific enough to be credible?
- Does the close avoid overclaiming drug discovery, cytokines, proteins,
  virtual cells, or clinical utility?

## Preferred Wording

Use:

- "Predicting cellular responses to perturbations is..."
- "However, exhaustive experimental profiling remains infeasible..."
- "Existing methods often..."
- "Here, we present/propose..."
- "The framework combines..."
- "Across [datasets/settings]..."
- "These results suggest..."

Avoid:

- "Our method perfectly predicts..."
- "This proves..."
- "The model solves perturbation prediction..."
- listing modules before stating the constraint.
