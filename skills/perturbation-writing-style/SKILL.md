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
- confident without being reckless;
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
5. Use confident, evidence-grounded verbs for supported advantages; reserve
   cautious verbs for genuinely indirect or narrow evidence.
6. Preserve notation, split definitions, metric direction, caveats, and figure
   references.
7. Check that the paragraph ends by interpreting evidence or handing off to the
   next question, not by trailing into a list.

## Advantage-Forward Tone

Do not make every result sound defensive. Once the manuscript has stated the
tested setting and metric, write the advantage naturally and directly.

Good:

```text
TriShift achieves the strongest Overlap@20 on Norman, showing that its gains
extend to recovery of response-gene identity.
```

Overly defensive:

```text
TriShift achieves the strongest Overlap@20 on Norman, although this should be
interpreted only as directionally consistent evidence rather than a strong
ranking conclusion.
```

Use boundaries sparingly:

- when the evidence type cannot support the claim;
- when a setting is genuinely narrow, such as IFNB1/PBMC;
- when a visualization is diagnostic rather than quantitative;
- when train/test policy or leakage could be misunderstood.

Do not add a boundary sentence after every advantage. Put routine caveats in a
short final boundary sentence, caption note, or Discussion paragraph.

## Preferred Scientific Verbs

Use:

- improves, recovers, preserves, extends, strengthens, captures, aligns;
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

Overly defensive:

```text
Adamson and Norman show smaller differences and should be viewed as
directionally consistent rather than as strong ranking conclusions.
```

More natural:

```text
Across Adamson and Norman, the same trend supports TriShift's advantage in
recovering perturbation-specific response structure, with the clearest
separation observed in [setting/metric].
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
- Are supported advantages stated directly before limitations are introduced?
- Are routine caveats consolidated instead of repeated after every result?
- Are broad application claims supported by actual experiments?
- Are translation-like and oral phrases removed?
- Are symbols, metrics, and caveats preserved?
