---
name: perturbation-writing-do
description: Natural-language router for perturbation-prediction manuscript work. Use when the user asks broadly to write, revise, polish, review, synchronize, adapt, shorten, expand, imitate papers, improve academic style, or continue work on a single-cell perturbation-response manuscript without naming a specific section skill.
---

# Perturbation Writing Do

This is the front door for perturbation-prediction manuscript work, analogous to
`byte-do` for Byte OS. It reads the user's natural-language request, identifies
the manuscript section and operation, loads the required modular skills, and
executes the matching workflow instead of only naming the skill.

Use this skill when the request is broad, mixed, or ambiguous:

- "optimize this paper";
- "make this more academic";
- "continue the manuscript";
- "check whether it reads like a strong paper";
- "turn this into a BIBM version";
- "sync Chinese and English";
- "review this like a referee";
- "rewrite based on the local perturbation papers";
- "improve methods/results/discussion";
- "fix reviewer risks";
- "make the story more natural".

## Operating Model

Run the manuscript work like a focused editorial system:

- Domain first: fix perturbation-prediction logic before general polish.
- Section roles visible: every paragraph must have a section-appropriate job.
- Evidence bounded: claims must cite setting, metric, split, baseline, and
  boundary when needed.
- Venue aware: journal and conference papers compress and order evidence
  differently.
- Reviewer driven: after edits, run one integrated reviewer gate.
- Overlay disciplined: load project-specific overlays such as
  `trishift-writing-core` only when the text or request requires them.
- Drug disciplined: load `perturbation-drug-writing-core` whenever an exposure
  involves a compound, biologic, dose/time program, or drug combination.

## Required Preflight

1. Identify explicit skill mentions. If the user names a specific
   perturbation-writing skill, use that skill.
2. Identify perturbation modality: genetic, drug, multimodal, cytokine/protein,
   or unknown. For drug work, load `perturbation-drug-writing-core` after the
   shared core and complete its Drug Study Card before scientific drafting.
3. Identify target venue if present: Bioinformatics, Nature-style journal,
   BIBM, IEEE, ICLR/ML conference, supplement, response letter, or unknown.
4. Identify manuscript section:
   - abstract;
   - introduction;
   - related work or background;
   - methods, problem formulation, notation, objective, training;
   - experiments, datasets, splits, baselines, metrics;
   - results, ablation, robustness, biological interpretation;
   - discussion, limitations, conclusion;
   - supplement, caption, provenance;
   - whole manuscript.
5. Identify operation:
   - draft from notes;
   - rewrite;
   - compress for venue;
   - expand with more story;
   - polish academic style;
   - imitate local exemplar papers;
   - review only;
   - synchronize CN/EN/Supp;
   - adapt venue;
   - fix reviewer findings.
6. Load `perturbation-writing-core` and
   `perturbation-writing-corpus-guide` for all non-trivial tasks.
7. Load `trishift-writing-core` only if the request or text contains TriShift
   markers such as TriShift, reference-conditioned, held-out-control, PBMC,
   IFNB1, Systema, reference-centered, centroid-centered, or `Overlap@20`.
8. When drafting or restructuring a whole section, load
   `references/section-story-cards.md` and state the intended evidence ladder
   before prose editing.
9. Route to the smallest set of section skills that covers the request.

## Routing Table

Apply the first strong match:

| User intent | Route |
|---|---|
| "do", "continue", "help with the paper", "optimize manuscript" | this skill, then infer section |
| abstract, summary, motivation/results abstract | `perturbation-abstract` |
| introduction, intro, motivation, gap, contribution | `perturbation-introduction` |
| related work, background, prior work, references positioning | `perturbation-related-work` |
| methods, method, formulation, notation, objective, loss, training | `perturbation-methods` |
| experiments, setup, dataset, split, baseline, metric | `perturbation-experiments` |
| results, result, ablation, robustness, case study, UMAP, DEG | `perturbation-results` |
| discussion, limitation, conclusion, future work | `perturbation-discussion` |
| supplement, caption, figure legend, provenance | `perturbation-supplement-captions` |
| sync, synchronize, Chinese-English, CN/EN, supplement consistency | `perturbation-writing-sync` |
| style, academic, natural, translation-like, oral, journal tone | section skill + `perturbation-writing-style` |
| review, referee, pre-submission, risk check | `perturbation-reviewer` |
| drug, compound, small molecule, biologic, dose, time course, combination, synergy, MoA, toxicity, viability | `perturbation-drug-writing-core` + relevant section skill + `perturbation-reviewer` |
| local papers, imitate, corpus, CMonge, Scouter, scPRAM, SCALE, scDFM | section skill + `perturbation-writing-corpus-guide` + `references/paper-imitation-guide.md` |

If the section is unknown, inspect the provided text headings or ask one
concise question only if the wrong choice would materially change the result.

## Routing Examples

Example 1:

```text
User: Make this paragraph less oral and more academic.
Route: infer section from text -> relevant section skill -> perturbation-writing-style
Reason: style work is safe only after section role and claim boundaries are checked.
```

Example 2:

```text
User: Rewrite Methods and check formula rigor.
Route: perturbation-methods -> perturbation-reviewer
Reason: notation, dimensions, train/eval policy, and OT interpretation are high-risk.
```

Example 3:

```text
User: Convert this into a BIBM version.
Route: perturbation-writing-core -> perturbation-writing-corpus-guide ->
perturbation-introduction/related-work/methods/experiments/results/discussion ->
perturbation-abstract -> perturbation-writing-sync -> perturbation-reviewer
Reason: venue conversion changes section order, compression, contribution style,
and claim visibility.
```

Example 4:

```text
User: Review this like a referee, do not edit yet.
Route: perturbation-reviewer
Reason: review-only requests should lead with severity-ranked findings.
```

Example 5:

```text
User: Learn from CMonge and Scouter, then improve Results.
Route: perturbation-results -> perturbation-writing-corpus-guide ->
references/paper-imitation-guide.md -> selected local PDFs -> perturbation-reviewer
Reason: Results imitation requires paragraph moves, metric setup, strongest
comparison, behavior interpretation, and boundary transfer.
```

## Whole-Manuscript Routing

For whole-manuscript work, use this order:

1. `perturbation-writing-core`
2. `perturbation-drug-writing-core` when the manuscript contains a drug exposure
3. `perturbation-writing-corpus-guide`
4. `perturbation-introduction`
5. `perturbation-related-work` when the venue has a separate Related Work
6. `perturbation-methods`
7. `perturbation-experiments`
8. `perturbation-results`
9. `perturbation-discussion`
10. `perturbation-abstract`
11. `perturbation-supplement-captions`
12. `perturbation-writing-style`
13. `perturbation-writing-sync`
14. `perturbation-reviewer`

Abstract is late in whole-paper workflows because it should reflect the final
evidence chain.

## Goal Mode Decision

Use a durable goal when the request asks for a multi-step deliverable such as:

- rewriting several sections;
- venue conversion;
- CN/EN/Supp synchronization plus review;
- "finish all skills" or "do everything";
- complete manuscript package.

Do not require goal mode for a single paragraph, single section, or review-only
answer.

## Subagent Decision

Use subagents only when actual independent scopes exist and the platform allows
it:

- one agent for Methods/notation;
- one for Results/evidence chain;
- one for language/style;
- one for reviewer gate.

Do not split a single paragraph across agents. The main agent owns final merge,
consistency, and reviewer resolution.

## Execution Contract

Default to quiet routing. In normal writing or review tasks, use one concise
sentence such as:

```text
I will handle this as Methods + reviewer gate, focusing on notation,
train/eval policy, and OT claim boundaries.
```

Only print the full routing block when the user asks for routing details,
debugging, a plan, or a handoff:

```text
Routing:
Reason:
Venue:
Section:
Operation:
Skills loaded:
Source of truth:
Will edit files: yes/no
Reviewer gate:
```

Then execute the workflow. Do not stop at a routing recommendation unless the
user explicitly asks for discussion only.

## State-Aware Defaults

If the user says "continue" or "next" and no section is named:

1. Check whether a manuscript file, selected text, previous review, or active
   Byte OS note identifies the current section.
2. If the previous step was review with CRITICAL or MAJOR findings, route to
   the section skill needed to fix those findings.
3. If the previous step was section rewrite, route to `perturbation-reviewer`.
4. If the previous step was accepted review, route to
   `perturbation-writing-sync` when multiple language versions exist, otherwise
   report completion.
5. Ask one concise question only when there is no reliable section or source of
   truth.

## Default Source-Of-Truth Policy

For TriShift manuscript work, after loading `trishift-writing-core`:

1. Chinese manuscript controls claim order, terminology, caveats, figure
   interpretation, and teacher-preferred story.
2. English manuscript follows the Chinese scientific content while respecting
   venue language and page budget.
3. Supplement follows only when definitions, provenance, metrics, or caveats
   change.

For non-TriShift papers, use the provided manuscript text and target venue as
source of truth.

## Completion Criteria

The route is complete when:

- the correct section skill was applied;
- domain story logic is fixed before style;
- required synchronization is done or explicitly unnecessary;
- `perturbation-reviewer` has run after manuscript edits;
- CRITICAL and MAJOR reviewer issues are fixed or explicitly deferred;
- the response reports remaining risks and verification.
