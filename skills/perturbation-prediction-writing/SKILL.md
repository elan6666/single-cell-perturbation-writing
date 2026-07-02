---
name: perturbation-prediction-writing
description: Router skill for writing, reviewing, polishing, synchronizing, and venue-adapting perturbation-prediction manuscripts. Use for single-cell perturbation response prediction papers, especially TriShift, when the task mentions Abstract, Introduction, Related Work, Methods, Experiments, Results, Discussion, Supplement, captions, reviewer risks, CN/EN synchronization, local exemplar papers, or teacher-style manuscript revision.
---

# Perturbation Prediction Writing

This is the legacy-compatible entrypoint skill. For broad natural-language
requests, first load `perturbation-writing-do`; it acts like `byte-do` and
decides the section, operation, venue, synchronization needs, and reviewer gate.
This file remains the stable public router name for existing prompts.

TriShift is the default local example, but the routing applies to other
single-cell perturbation-response, expression-prediction, conditional transport,
flow-matching, optimal-transport, perturbation-prior, and foundation-model
papers.

## Mandatory Priority

1. Follow the teacher's requested story style first.
2. Follow target venue constraints: page budget, anonymity, template, section
   order, abstract format, contribution style, and reference limits.
3. Load `perturbation-writing-core` for domain invariants and TriShift-specific
   claim boundaries.
4. Load `perturbation-writing-corpus-guide` for the distilled paper-corpus
   guidance: module structure, paragraph architecture, language style,
   conference-vs-journal differences, and reusable sentence patterns.
5. Load the section skill that matches the task.
6. Load `perturbation-writing-style` for late prose naturalness after section
   logic is correct.
7. Load `perturbation-writing-sync` whenever claims, metrics, definitions,
   figures, symbols, caveats, or interpretation might affect Chinese, English,
   or Supplement consistency.
8. Run `perturbation-reviewer` after manuscript or supplement edits.
9. Use `nature-polishing` only after the domain story, section role, notation,
   evidence chain, and reviewer gate are already satisfied.

For broad requests such as "optimize the paper", "continue", "adapt this for a
venue", "review and fix", or "make this more academic", delegate routing to
`perturbation-writing-do` before selecting section skills.

## Routing Table

| User task or section | Required skill |
|---|---|
| Abstract, summary, structured abstract, conference abstract | `perturbation-abstract` |
| Introduction, motivation, gap, contributions in intro | `perturbation-introduction` |
| Related Work, Background, citation positioning, method families | `perturbation-related-work` |
| Methods, model overview, problem formulation, notation, objective, training policy | `perturbation-methods` |
| Experiment setup, datasets, splits, baselines, metrics, fairness | `perturbation-experiments` |
| Results, ablations, robustness, biological interpretation, figure-linked evidence | `perturbation-results` |
| Discussion, limitations, future work, conclusion | `perturbation-discussion` |
| Supplement, captions, figure notes, provenance, metric formulas | `perturbation-supplement-captions` |
| Natural academic style, stiff prose, translation-like wording | `perturbation-writing-style` plus section skill |
| CN/EN/Supplement synchronization | `perturbation-writing-sync` plus section skill |
| Final check, referee simulation, risk audit | `perturbation-reviewer` |

When a task spans multiple sections, use the section skills in manuscript order:
Abstract, Introduction, Related Work, Methods, Experiments, Results,
Discussion, Supplement/Captions. For TriShift manuscript edits, preserve the
project order: Chinese manuscript first, then English manuscript, then
Supplement only when definitions, provenance, metrics, or caveats change.

## Required Workflow

1. Identify the target venue and section. If a venue-specific skill exists, use
   it together with this router. The venue skill controls format and page
   budget; the perturbation skill controls scientific story logic.
2. Identify the operation: draft, rewrite, compress, expand, polish, translate,
   synchronize, review, or adapt.
3. Load `perturbation-writing-core` and `perturbation-writing-corpus-guide`.
4. Load the relevant section skill and apply its story chain before sentence
   polishing.
5. If the user asks for naturalness, formal style, reviewer-friendly wording,
   or imitation of strong papers, also load:
   - `perturbation-writing-style`
   - `references/paper-imitation-guide.md`
   - the relevant local exemplar PDFs under the user's configured local paper
     folder, only for the sections needed.
6. If the edit changes scientific content, claims, figures, metrics, notation,
   or caveats, load `perturbation-writing-sync` and synchronize CN/EN/Supp.
7. After edits, run `perturbation-reviewer`. Fix all CRITICAL and MAJOR
   findings, or explicitly record why a finding is deferred.
8. When working inside TriShift project repos, record review and verification in
   the active Byte OS status or review/iteration note.

## Section Story Chains

| Section | Required chain |
|---|---|
| Abstract | value -> bottleneck -> gap -> method -> mechanism -> evidence -> implication |
| Introduction | value -> experimental bottleneck -> method families and limits -> precise gap -> method/contributions |
| Related Work | category -> what it solves -> remaining assumption -> positioning |
| Methods | destructive unpaired data -> task/notation -> reference-conditioned transition -> components/objective -> training vs evaluation policy |
| Experiments | goal -> datasets -> splits -> baselines -> metrics -> fairness/provenance |
| Results | evaluated question -> setup -> metric direction -> strongest comparison -> sparse numbers -> behavior interpretation -> boundary |
| Discussion | contribution synthesis -> why it works -> relation to prior methods -> boundaries -> future work |
| Supplement/Captions | definition/provenance -> figure or metric contract -> interpretation boundary -> main-text alignment |

## Non-Negotiable Domain Rules

- Do not describe OT references as true cell-wise biological pairs.
- Define vectors before scalar components.
- Define dimensions, indices, distributions, matrices, losses, and metrics
  before use.
- Keep generic training-expression vectors distinct from control and perturbed
  cells.
- Separate training-time OT reference construction from evaluation-time
  held-out reference use.
- Keep held-out-control genetic tasks distinct from PBMC target-domain-control
  transfer.
- Limit protein/cytokine prior claims to IFNB1/PBMC unless additional
  experiments exist.
- Treat UMAP, violin plots, and case visualizations as diagnostics, not proof.
- Compare against the strongest relevant baseline, not a weak strawman.
- Use cautious verbs when evidence is indirect: supports, suggests, indicates,
  is consistent with, may be limited by.

## Output Contract

For any manuscript-editing response, report:

```text
Section:
Venue:
Skills used:
Source of truth:
Edits made:
Synchronization:
Reviewer gate:
Verification:
Remaining risks:
```

For review-only requests, lead with findings ordered by severity and cite
specific section, paragraph, line, figure, metric, or symbol when available.
