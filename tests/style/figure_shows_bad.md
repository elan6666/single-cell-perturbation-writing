# Style Fixture: Figure-List Result

Bad input:

```text
Figure 2 shows the main results. Figure 3 shows ablations. Figure 4 shows
generalization. Figure 5 shows distribution recovery.
```

Expected fix:

- rewrite around evaluated questions;
- state setting, metric direction, strongest comparison, interpretation, and
  boundary;
- avoid panel-by-panel narration.
