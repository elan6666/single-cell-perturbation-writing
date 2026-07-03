# Reviewer Fixture: Metric List Without Interpretation

Bad input:

```text
We report Pearson, nMSE, Wasserstein distance, and Overlap@20. TriShift has the
best values on all metrics.
```

Expected flags:

- severity: MAJOR
- issue: Results lists metrics without explaining what capability or advantage
  each metric supports
- required fix: explain metric meaning, strongest baseline, numerical anchor,
  and behavior interpretation; for Overlap@20, state that it evaluates
  response-gene identity recovery and connects prediction to biological
  mechanism interpretation

