---
name: perturbation-prediction-writing
description: Legacy-compatible alias for perturbation-writing-do. Use when existing prompts mention perturbation-prediction-writing; delegate broad manuscript writing, review, polishing, synchronization, and venue adaptation tasks to perturbation-writing-do.
---

# Perturbation Prediction Writing

This is the stable legacy entrypoint. It exists so older prompts that invoke
`perturbation-prediction-writing` continue to work.

For all non-trivial manuscript work, immediately load and follow
`perturbation-writing-do`. Do not maintain a separate routing table here.
`perturbation-writing-do` is the single source of truth for:

- natural-language task detection;
- section routing;
- venue handling;
- TriShift overlay detection;
- synchronization decisions;
- reviewer gate selection;
- quiet versus debug routing output.

## Delegation Rule

Use this mapping:

```text
perturbation-prediction-writing request
-> perturbation-writing-do
-> required core/corpus/section/style/sync/reviewer skills
```

Only answer directly from this file when the user explicitly asks what the
legacy entrypoint does.
