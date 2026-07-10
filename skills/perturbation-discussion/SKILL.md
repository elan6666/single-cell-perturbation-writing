---
name: perturbation-discussion
description: Write, rewrite, or review Discussion, Limitations, Conclusion, and future-work sections for perturbation-prediction manuscripts. Use for contribution synthesis, mechanism interpretation, relation to prior methods, claim boundaries, and cautious implications.
---

# Perturbation Discussion

Use after `perturbation-writing-core` and `perturbation-writing-corpus-guide`.

## Discussion Job

Discussion explains what the evidence means, why the method works, and where
the strongest advantages sit. It should not introduce new results, hide
limitations, or repeat the Results section.

## Required Chain

1. Contribution synthesis:
   - restate the method as a modeling answer to the central constraint;
   - summarize what the combined evidence supports.
2. Mechanism interpretation:
   - explain why the components work together;
   - connect mechanism to observed behavior.
3. Relation to prior methods:
   - endpoint generation;
   - perturbation-prior methods;
   - OT/distributional methods;
   - foundation models or flow/set methods where relevant.
4. Boundary conditions:
   - name where evidence does not yet extend without weakening the main
     contribution paragraph.
5. Future directions:
   - concrete extensions that follow from limitations.

## TriShift Boundaries

State these when relevant:

- OT references are prediction origins or supervision candidates, not true
  one-to-one cell pairs.
- Prediction quality depends on control-pool coverage and OT retrieval fidelity.
- Held-out-control genetic tasks and PBMC target-domain-control transfer are
  related but not identical.
- Protein/cytokine prior claims are limited to IFNB1/PBMC unless additional
  experiments exist.
- Higher-order combinations, dose, time, batch effects, new cell types, new
  platforms, and stronger OOD conditions remain future tests unless evaluated.
- Endpoint errors, response-gene identity, residualized signal, and
  distributional fidelity can favor different behavior and should be interpreted
  together.

Do not scatter all boundaries throughout the Discussion. Lead with the
contribution and advantage, then consolidate limitations into a dedicated
boundary paragraph.

## Drug-Perturbation Boundaries

Separate observed in-vitro response, model-based candidate prioritization,
mechanism hypothesis, and clinical utility. State which level the data support.
Cell-line, organoid, or ex-vivo evidence does not establish patient benefit,
safe dose, PK/PD, selectivity, or clinical efficacy. Name untested doses,
times, donors, drug classes, combinations, and toxicity contexts instead of
treating a narrow transcriptional benchmark as general pharmacology.

## Useful Discussion Moves

- "We introduce [method], a [framework] for [task]."
- "Our results indicate that [principle] is important for [capability]."
- "Together, these findings show that [method] improves [capability] by
  [mechanism]."
- "The gains are most visible in [setting/metric], where [method] recovers
  [advantage]."
- "The effectiveness likely stems from the interplay of [factor A], [factor B],
  and [factor C]."
- "Beyond endpoint accuracy, [method] supports [biological/application
  advantage]."
- "Although promising, several challenges remain."
- "Future work could extend [method] to [larger/more complex/clinically
  realistic setting]."

## Conclusion Mode

If the venue asks for a short Conclusion rather than full Discussion:

1. One sentence for method and task.
2. One sentence for main empirical support.
3. One sentence for ablation/robustness/distributional support.
4. One sentence for limitation or future use.

Do not compress away limitations if the manuscript makes broad claims.

## Avoid

- Introducing new numerical results.
- Claiming clinical, drug-discovery, cytokine, or virtual-cell generality beyond
  evidence.
- Diluting every advantage with a local caveat before the reader understands
  the contribution.
- Saying "future work will solve" without naming a concrete direction.
- Repeating every figure result instead of synthesizing mechanisms.
