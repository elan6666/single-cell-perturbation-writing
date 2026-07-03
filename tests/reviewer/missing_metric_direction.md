# Reviewer Fixture: Missing Metric Direction

Bad input:

```text
TriShift achieved a Wasserstein distance of 0.42 and Pearson of 0.81, showing
better performance than all baselines.
```

Expected flags:

- severity: MAJOR
- issue: metric direction and aggregation are missing
- required fix: define what each metric measures, which direction is better,
  and which baseline is strongest
