---
name: perturbation-reviewer
description: Single integrated reviewer for perturbation-prediction manuscripts. Use after manuscript edits or for review-only tasks to assess story chain, notation, evidence, claims, venue fit, CN/EN/Supp sync, and academic language without splitting into multiple reviewer skills.
---

# Perturbation Reviewer

This is the only reviewer skill for the modular perturbation-writing system.
Do not split reviewer work into many separate reviewer skills unless the user
explicitly asks. Keep the output integrated and severity-ranked.

## Review Stance

Prioritize:

1. Scientific correctness and claim boundaries.
2. Section story-chain compliance.
3. Notation and formula rigor.
4. Results evidence quality.
5. CN/EN/Supplement synchronization.
6. Venue fit.
7. Academic language maturity.

Findings should be ordered by severity and grounded in concrete text, section,
paragraph, figure, metric, symbol, or line references where available.

## Reviewer Modes

Use `diagnose-only` when the user asks for review without edits.

Use `diagnose-and-patch` when the user asks to fix issues after review. In this
mode, produce a required patch plan before editing.

Use `final-pre-submission` when the manuscript is close to delivery. In this
mode, be stricter about claim scope, synchronization, venue constraints,
captions, references, and formatting-adjacent risks.

## Severity Levels

CRITICAL:

- false or unsupported core claim;
- train/test leakage or split confusion;
- OT described as true biological pairing;
- major CN/EN scientific mismatch;
- missing central gap in a section that depends on it;
- formula or notation error that changes meaning.

MAJOR:

- section story chain is incomplete;
- Results lacks metric direction, strongest baseline, or numerical anchor;
- broad claim exceeds evidence;
- method family is misrepresented;
- held-out-control and target-domain-control are blurred;
- Supplement/caption contradicts main text;
- reviewer would not understand why a module exists.

MINOR:

- local awkwardness, repeated transitions, stiff phrasing;
- weak paragraph handoff;
- citation placement issue;
- caption wording can be clearer;
- style issue that does not change scientific meaning.

## Required Checks

Story-chain compliance:

- Abstract: value, bottleneck, gap, method, mechanism, evidence, implication.
- Introduction: value, bottleneck, prior families, precise gap, method.
- Related Work: category, solved problem, remaining assumption, positioning.
- Methods: unpaired data, notation, modeling form, components, objective,
  training/evaluation policy.
- Experiments: goal, datasets, splits, baselines, metrics, fairness.
- Results: question, setup, metric direction, strongest comparison, sparse
  numbers, behavior, boundary.
- Discussion: synthesis, mechanism, prior relation, boundaries, future work.
- Supplement/Captions: definitions, provenance, metric contract, claim boundary.

Notation rigor:

- vectors before scalar components;
- Problem Formulation defines task-critical variables only;
- module-local variables are defined inside their module sections;
- hyperparameters, splits, preprocessing, and baseline internals are not mixed
  into task notation;
- dimensions and indices before matrix entries;
- distributions and coupling sets before OT objectives;
- no ambiguous symbols such as `z_mu`;
- main text and Supplement symbols match;
- equations numbered only when referenced.

Results evidence:

- metric direction is defined;
- strongest relevant baseline is used;
- numerical anchors are sparse but specific;
- important metrics are interpreted as model advantages, not merely listed;
- response-gene recovery metrics explain why gene-identity recovery matters for
  mechanism interpretation;
- visualizations are diagnostic, not proof;
- mixed metric behavior is explained rather than hidden.
- a simple matched baseline is included or its omission is justified;
- shared stress, cell-cycle, selection, batch, or average-effect variation is
  tested or bounded before interpreting performance as perturbation-specific.

TriShift boundaries:

- OT references are not true cell pairs;
- held-out-control genetic tasks differ from PBMC target-domain-control
  transfer;
- IFNB1/PBMC protein/cytokine claims are not broadened;
- Systema, reference-centered, centroid-centered, response-gene, and
  distributional metrics are named consistently.

Drug-Perturbation Gate, when applicable:

- drug identity, salt/formulation, vehicle, dose unit, and exposure time are
  sufficient to reproduce the stated condition;
- unseen-drug claims use an exposure-level split and disclose scaffold, MoA,
  dose/time, donor, and batch leakage risks;
- models receive comparable drug information and representation pretraining
  does not silently expose test identities;
- viability, stress, cell-cycle, apoptosis, and composition confounds are
  assessed or bounded when relevant;
- combination claims name the endpoint and additivity null; raw effects are not
  mislabeled as synergy;
- target/pathway agreement is not presented as direct target engagement or
  causality without evidence;
- in-vitro response, prioritization, mechanism hypothesis, and clinical claims
  remain on distinct evidence levels;
- the Results section follows the Drug-Perturbation Evidence Ladder or gives a
  reasoned venue-specific compression of it.

Language maturity:

- no oral phrasing;
- no translation-like sentence order;
- no panel-list narration unless a caption requires it;
- no vague "better/good/perfect" claims;
- supported advantages are stated directly rather than overqualified;
- cautious verbs used for genuinely indirect evidence.

## Output Format

Use this format:

```text
Verdict: ship | iterate | block

Findings:
- [Severity] Section/location: issue -> required fix.

Story-chain assessment:
Notation assessment:
Results/evidence assessment:
Claims/boundaries assessment:
CN/EN/Supp sync:
Venue fit:
Language maturity:

Required fixes:
Suggested fixes:
Patch plan:
Verification needed:
```

If no blocking issues are found, say so clearly and list remaining residual
risks or test gaps.

## Patch Plan Requirements

For every CRITICAL or MAJOR issue, the patch plan should name:

1. the section or paragraph to change;
2. the exact scientific function to restore;
3. the evidence object that must be inserted or scoped;
4. synchronization targets such as Abstract, Results, Discussion, caption, or
   Supplement;
5. verification needed after patching.

Example:

```text
Patch plan:
1. Rewrite Methods paragraph 2 to define the OT coupling as soft reference
   weights, not biological pairs.
2. Move Wasserstein direction before the main Results comparison.
3. Replace broad IFNB1 cytokine wording in Discussion with PBMC-specific scope.
4. Update the matching caption and claim ledger entry.
```
