---
name: perturbation-drug-writing-core
description: Domain overlay for writing or reviewing drug-perturbation manuscripts, especially single-cell drug-response, dose-time, combination, mechanism-of-action, and translational studies. Use with perturbation-writing-do and the relevant section skill whenever a manuscript models, benchmarks, or interprets small-molecule, biologic, or drug-combination perturbations.
---

# Drug Perturbation Writing Core

Load this overlay after `perturbation-writing-core`. It supplies drug-specific
scientific constraints; it does not replace section skills or the single
integrated `perturbation-reviewer`.

## Required Preflight

Classify the manuscript before substantive drafting:

1. **Task:** transcriptional response, viability/toxicity, phenotype,
   dose-response, time course, combination/synergy, mechanism inference, or
   prioritization.
2. **Exposure:** canonical compound/biologic identity, salt or formulation,
   vehicle, dose and unit, exposure duration, dosing schedule, and whether the
   condition is single agent or combination.
3. **Biological system:** assay, readout, cell line/organoid/primary sample,
   donor, disease context, cell state, and replicate/batch/plate structure.
4. **Generalization claim:** unseen drug, chemical scaffold, target/MoA, dose,
   time, cell type, donor, disease context, combination, or dataset.
5. **Translation level:** in-vitro response, screening prioritization,
   mechanism hypothesis, preclinical efficacy, or clinical claim.

Complete `references/drug-study-card.md`. Preserve missing facts as
limitations; never infer them.

## Drug Scientific Contract

- Treat a drug as an exposure with identity **and** context, not a name token.
- State which representation reaches each model: structure, fingerprint,
  target/MoA, text, gene signature, or multimodal combination. Disclose unequal
  input information across baselines.
- Separate pharmacologic response from generic stress, cell-cycle arrest,
  apoptosis, low viability, or cell-composition changes.
- Separate interpolation across tested doses/times from extrapolation to an
  unseen value. Report units and range.
- For combinations, name the response endpoint and additivity null (for example
  Bliss, Loewe, HSA, or ZIP). Do not call a raw combination response synergy.
- Treat target/pathway agreement as mechanism-supporting rather than evidence
  of direct binding or causality.
- Bound in-vitro prediction to hypothesis generation or assay prioritization;
  it does not establish patient benefit, dose, safety, PK/PD, or clinical
  efficacy.

## Evidence And Section Contract

Before Experiments, read `references/drug-splits-and-leakage.md` and
`references/drug-metrics.md`. Before Results or Discussion, read
`references/drug-evidence-ladder.md`; it orders the main benchmark, strict
generalization, biological consistency, and failure boundary.

- **Introduction/Related Work:** distinguish chemical representation, context,
  dose/time, and translational gaps from genetic perturbation gaps.
- **Methods:** define the exposure tuple, representation, combination
  composition, dose/time encoding, and inference regime.
- **Experiments:** disclose split keys, vehicle, replicates, viability handling,
  and baseline-input parity.
- **Results:** report the matched baseline before hard OOD; then provide
  biological interpretation and a failure map.
- **Discussion:** keep response prediction, mechanism hypothesis, screening
  value, and clinical translation on separate evidence levels.

## Completion Gate

Run `perturbation-reviewer` with its Drug-Perturbation Gate. The manuscript is
not ready when exposure, split, confound, null model, or translation boundary is
ambiguous.
