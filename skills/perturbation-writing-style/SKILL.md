---
name: perturbation-writing-style
description: Academic style pass for perturbation-prediction manuscripts after section logic is correct. Use to remove translation-like prose, oral phrasing, panel-list narration, overclaiming, vague praise, and reviewer-unfriendly wording while preserving technical rigor.
---

# Perturbation Writing Style

Use this only after the relevant section skill has fixed the scientific story.
Do not use generic polish to hide weak logic, missing definitions, unsupported
claims, or metric ambiguity.

## Style Goal

The prose should read as a progressive scientific argument:

- problem-driven;
- mechanism-aware;
- evidence-bound;
- cautious in extrapolation;
- natural in English or Chinese;
- free of oral explanation and translation artifacts.

## Required Pass

For each paragraph:

1. Name the paragraph role: value, gap, setup, method rationale, formula
   interpretation, experiment setup, main comparison, mechanism interpretation,
   boundary, or handoff.
2. Replace mechanical openings with causal openings.
3. Remove panel-list narration unless the sentence's job is explicitly to guide
   a figure.
4. Replace vague strength words with metric- or behavior-specific claims.
5. Use cautious verbs when evidence is indirect.
6. Preserve notation, split definitions, metric direction, caveats, and figure
   references.
7. Check that the paragraph ends by interpreting evidence or handing off to the
   next question, not by trailing into a list.

## Preferred Scientific Verbs

Use:

- evaluates, quantifies, supports, indicates, suggests, is consistent with;
- constructs, estimates, conditions on, aligns, preserves, captures, mitigates;
- benchmarks, validates, instantiates, formulates, generalizes, integrates.

Avoid:

- proves, guarantees, perfectly matches, completely solves, revolutionary;
- is good/bad, works well, obvious, simply, we just, as can be seen;
- "this is used to" when the object and purpose can be named directly.

## Weak-To-Strong Rewrites

Weak:

```text
Figure 2 shows that TriShift performs better than other methods.
```

Stronger:

```text
To test whether reference-conditioned prediction transfers to unseen control
origins, we compared TriShift with the strongest baseline under the held-out
control split. The gain in [metric] suggests that conditioning on state-matched
references reduces collapse toward a shared endpoint.
```

Weak:

```text
The UMAP proves that the model recovers the true response.
```

Stronger:

```text
The UMAP provides diagnostic support for the quantitative trend: predicted
cells occupy a region closer to the observed perturbed distribution, consistent
with improved preservation of population structure.
```

Weak:

```text
Our method handles cytokines.
```

Stronger:

```text
In the IFN-beta PBMC task, the IFNB1 prior supports target-domain stimulated
response prediction; broader cytokine or protein-prior generalization remains
outside the current evidence.
```

## Chinese Style Rules

- Avoid literal English-to-Chinese ordering that delays the subject or predicate.
- Avoid long semicolon chains that mix premise, method, evidence, and caveat.
- Prefer clear causal connectors: "therefore", "this setting", "this
  difference", and "this indicates" in the target language.
- Do not overuse generic additive connectors when the relation is actually
  contrast, cause, or boundary.
- Keep technical nouns stable across CN/EN/Supplement.

## English Style Rules

- Put the main subject and verb early.
- Do not stack too many prepositional phrases before the action.
- Avoid repeated openings across adjacent paragraphs.
- Use "although" for real concessions and "whereas" for contrasts.
- Use "may", "suggests", and "is consistent with" for indirect evidence.

## Final Style Checklist

- Does each paragraph have exactly one main job?
- Does the first sentence explain why the paragraph exists?
- Are results interpreted as model behavior rather than generic superiority?
- Are visual claims bounded as diagnostic?
- Are broad application claims supported by actual experiments?
- Are translation-like and oral phrases removed?
- Are symbols, metrics, and caveats preserved?
