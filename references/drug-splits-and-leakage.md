# Drug Splits And Leakage

Name the held-out object and split key. A random cell-level split cannot support
an unseen-drug claim when cells from the same exposure appear in training.

| Claimed capability | Minimum split key | Frequent leakage |
|---|---|---|
| Unseen drug | canonical compound | replicate wells or cells of the same compound cross splits |
| New chemistry | scaffold | close analogues cross splits |
| New target/MoA | target family or MoA | target labels/embeddings expose test identity |
| New dose/time | dose or time | interpolation is described as extrapolation |
| New combination | component pair/set | single-agent or reversed-pair duplicates cross splits |
| New patient/context | donor, model, or dataset | cells from the same donor/plate cross splits |

Always report canonicalization, dose/time transformation, vehicle controls,
plate/batch and donor allocation, pretraining isolation, information available
to each model, and the number of unique drugs/contexts rather than only cells.
