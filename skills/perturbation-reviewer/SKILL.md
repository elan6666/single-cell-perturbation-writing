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
- dimensions and indices before matrix entries;
- distributions and coupling sets before OT objectives;
- no ambiguous symbols such as `z_mu`;
- main text and Supplement symbols match;
- equations numbered only when referenced.

Results evidence:

- metric direction is defined;
- strongest relevant baseline is used;
- numerical anchors are sparse but specific;
- visualizations are diagnostic, not proof;
- mixed metric behavior is explained rather than hidden.

TriShift boundaries:

- OT references are not true cell pairs;
- held-out-control genetic tasks differ from PBMC target-domain-control
  transfer;
- IFNB1/PBMC protein/cytokine claims are not broadened;
- Systema, reference-centered, centroid-centered, response-gene, and
  distributional metrics are named consistently.

Language maturity:

- no oral phrasing;
- no translation-like sentence order;
- no panel-list narration unless a caption requires it;
- no vague "better/good/perfect" claims;
- cautious verbs used for indirect evidence.

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
Verification needed:
```

If no blocking issues are found, say so clearly and list remaining residual
risks or test gaps.
