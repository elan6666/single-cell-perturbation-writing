# Perturbation Manuscript Story Cards

Use these cards to outline or audit a section. They distill reusable structure
from GEARS (Nature Biotechnology, 2023), CPA (Molecular Systems Biology, 2023),
chemCPA (NeurIPS, 2022), scPRAM (Bioinformatics, 2024), and Systema (Nature
Biotechnology, 2025). Copy the reasoning pattern, never paper wording.

## Abstract

For structured journal abstracts: Motivation -> precise gap -> Result/method ->
hard-setting evidence -> restrained implication and availability when required.
For conference abstracts: opportunity -> screen-scale bottleneck -> missing
generalization -> model and unique information source -> hard evaluation ->
measured implication. Avoid module lists and clinical promises.

## Introduction: Four Or Five Paragraphs

1. Why the perturbation response matters at this biological resolution.
2. Why experiments cannot cover the required perturbation/dose/time/context
   space.
3. What method families solve, grouped by modeling assumption.
4. Which exact assumption fails for the target capability.
5. How the proposed formulation answers it and how the evidence ladder will
   test that answer; use compact numbered contributions in conferences.

## Methods: Six Moves

1. Task contract: inputs, output, unpaired/counterfactual status, inference
   information.
2. Data and split contract: independent unit, holdout, controls, leakage
   barriers.
3. Overview: input -> representation -> core operation -> output.
4. Core mechanism: symbols before equations, interpretation after equations.
5. Training versus inference policy.
6. Reproducibility: preprocessing, baseline parity, model selection, seeds,
   availability.

## Results: Six-Block Evidence Ladder

1. Dataset/task reality and response support.
2. Main matched benchmark with simple and strong baselines.
3. Mechanism/ablation for the claimed information source.
4. Hardest declared generalization axis.
5. Biological interpretation as diagnostic support.
6. Failure/boundary analysis by support, distance, effect size, toxicity, or
   systematic variation.

For conference compression, merge 3+4 or 5+6; do not omit the main baseline or
definition of the hard axis. For journals, preview why the blocks are
complementary before the first result.

## Discussion: Five Moves

Contribution/evidence synthesis -> why the design helped -> biological or
practical meaning -> limitations revealed by the hardest test -> concrete next
experiment. Do not upgrade in-silico prediction to causal or clinical evidence.

## Source Patterns

- GEARS: formulation and prior-informed mechanism -> held-out single and
  combinatorial tests -> interaction and phenotype evidence. DOI:
  10.1038/s41587-023-01905-6.
- CPA: compositional formulation -> dose/time/context OOD -> uncertainty and
  known failure conditions. DOI: 10.15252/msb.202211517.
- chemCPA: molecular representation and cross-assay transfer -> unseen-drug
  and drug-covariate generalization. NeurIPS 2022.
- scPRAM: structured abstract -> core OOS fidelity -> DE biology ->
  cross-context transfer -> robustness. DOI: 10.1093/bioinformatics/btae265.
- Systema: simple baselines and systematic variation are first-class Results,
  not a supplementary caveat. DOI: 10.1038/s41587-025-02777-8.
