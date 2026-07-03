# Claim Ledger Template

Use this ledger to keep Abstract, Results, Discussion, captions, and Supplement
aligned around the same evidence. It is stronger than a language sync checklist:
it controls claim strength across the manuscript.

| Claim ID | Claim | Evidence | Allowed wording | Forbidden wording | Sections affected | Sync status |
|---|---|---|---|---|---|---|
| C1 | `<specific claim>` | `<dataset, split, metric, baseline, number>` | `<scoped verbs and setting>` | `<overbroad wording>` | `<Abstract, Results, Discussion, Caption, Supplement>` | `<open/done>` |

## Required Fields

- Claim ID: stable short identifier such as C1, C2, C3.
- Claim: one sentence, scoped to the tested setting.
- Evidence: dataset, split, held-out object, metric, metric direction, strongest
  baseline, and numerical anchor when available.
- Allowed wording: verbs and phrases that match the evidence strength.
- Forbidden wording: phrases that overgeneralize or imply unsupported
  mechanisms.
- Sections affected: every place the claim appears or is implied.
- Sync status: open, synced, deferred, or removed.

## Example Claims

| Claim ID | Claim | Evidence | Allowed wording | Forbidden wording | Sections affected | Sync status |
|---|---|---|---|---|---|---|
| C1 | A reference-conditioned model improves held-out-control prediction. | `<dataset/split/metric/baseline>` | "supports improved prediction under the held-out-control split" | "solves unseen perturbation prediction" | Abstract, Results, Discussion | open |
| C2 | IFNB1 prior supports PBMC target-domain transfer. | PBMC IFN-beta task only | "in the IFN-beta PBMC task" | "handles cytokines broadly" | Introduction, Results, Caption | open |
| C3 | OT provides state-compatible references. | training-time OT weights or reference retrieval analysis | "soft reference weights" or "state-compatible reference candidates" | "true biological pairs" | Methods, Supplement, Caption | open |

## Anti-Drift Rules

- The Abstract cannot be stronger than Results.
- Discussion can synthesize but cannot introduce new empirical claims.
- Captions cannot imply proof when Results only provides diagnostic support.
- Supplement notation cannot preserve an old version of a Methods claim.
- Translations cannot strengthen scope to save space.
