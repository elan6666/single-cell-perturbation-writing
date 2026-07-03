# Reviewer Fixture: OT True Pairing Error

Bad input:

```text
The optimal transport plan identifies the true biological pair for each
perturbed cell, proving that the model recovers cell-wise perturbation effects.
```

Expected flags:

- severity: CRITICAL
- issue: OT described as true biological pairing
- required fix: describe OT as soft reference weights or state-compatible
  candidates, not true cell pairs
