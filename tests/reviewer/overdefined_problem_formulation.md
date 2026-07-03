# Reviewer Fixture: Overdefined Problem Formulation

Bad input:

```text
In the problem formulation, let B be batch size, H be hidden size, K be the
top-k reference pool, eta be the learning rate, and s be the random seed. We
also define the internal GEARS message passing variables before introducing the
control and perturbed populations.
```

Expected flags:

- severity: MAJOR
- issue: Problem Formulation mixes implementation details and baseline internals
  before task input/output variables
- required fix: keep task-critical variables in Problem Formulation; move
  hyperparameters to Implementation and baseline details to Experiments

