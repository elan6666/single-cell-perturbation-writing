# Reviewer Fixture: Unsupported Cytokine Claim

Bad input:

```text
The IFNB1 experiment demonstrates that the model handles cytokine perturbations
broadly across immune contexts.
```

Expected flags:

- severity: CRITICAL
- issue: broad cytokine/protein-prior claim exceeds IFNB1/PBMC evidence
- required fix: scope the claim to the IFN-beta PBMC task unless additional
  cytokine experiments exist
