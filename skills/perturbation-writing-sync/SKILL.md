---
name: perturbation-writing-sync
description: Synchronize Chinese, English, and Supplement text for perturbation-prediction manuscripts. Use when edits affect claims, terminology, notation, figures, metrics, caveats, references, or venue-specific compressed versions.
---

# Perturbation Writing Sync

Use after any manuscript edit that changes scientific content.

## Source-Of-Truth Policy

For TriShift:

1. Chinese manuscript is the content source of truth for claim order,
   terminology, figure references, caveats, and interpretation.
2. English manuscript follows the Chinese scientific content while respecting
   venue style and page budget.
3. Supplement updates only when definitions, provenance, metrics, formulas,
   split policies, or caveats change.

For non-TriShift projects, use the provided canonical manuscript or the user's
named source of truth.

## What Requires Sync

Run synchronization when an edit changes:

- central gap or contribution;
- method description;
- notation or formula;
- figure number or panel interpretation;
- dataset, split, baseline, or metric;
- numerical result;
- caveat or limitation;
- perturbation prior source;
- claim strength;
- Related Work positioning;
- abstract or conclusion implication.

Style-only edits do not require Supplement sync unless meaning changes.

## Sync Checklist

For each changed claim, verify:

- CN and EN state the same scientific claim.
- The English version does not strengthen the Chinese claim.
- The Supplement uses the same symbols and metric names.
- Figure captions match Results text.
- Metric direction and aggregation are consistent.
- Held-out-control and target-domain-control terms are not swapped.
- IFNB1/PBMC limitations remain visible in all relevant versions.
- OT references are not described as true cell pairs in any language.

## Output Format

Report:

```text
Changed claim:
CN location:
EN location:
Supplement/caption location:
Sync status:
Action taken:
Remaining mismatch:
```

## Common Sync Failures

- Chinese says "supports" while English says "demonstrates broad
  generalization".
- English compresses away a limitation due to page budget.
- Supplement keeps old notation after Methods changes.
- Captions refer to an old metric or split.
- PBMC transfer is described as the same as held-out-control genetic transfer.
- Prior examples become broad prior claims.
