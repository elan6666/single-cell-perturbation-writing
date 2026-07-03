# Method Variable Scope Rules

Good Methods sections do not define every variable. They define the variables
that affect task understanding, model inputs and outputs, training objectives,
core modules, or reviewer-risk boundaries. Standard neural-network layers,
one-off local variables, and common mathematical notation can be introduced
lightly or left implicit.

## Core Rule

Problem Formulation defines only the variables needed to understand the task.
Module subsections define variables needed to understand that module.
Experiments and Appendix carry split variables, hyperparameters, preprocessing,
and implementation details.

Do not mix:

- task variables;
- module-internal variables;
- experiment split variables;
- implementation-detail variables.

## Must Define

Define a variable when at least one condition holds:

1. It is a task input or output.
   - Examples: control population, perturbed population, perturbation label,
     perturbation prior, predicted perturbed response.
2. It expresses the core innovation.
   - Examples: reference state, OT reference pool, shift vector, residual
     generator, conditional distribution.
3. It appears across multiple subsections.
   - Examples: latent control state, latent perturbed state, reference
     representation, perturbation shift.
4. It could be misread as factual pairing, leakage, or biological trajectory.
   - Examples: selected reference control, measured perturbed cell, target
     perturbed centroid, reference selection, test perturbation cell.
5. It enters a loss, metric, or objective.
   - Examples: loss weights, direction-aware loss, MMD kernel, top-k DEG set,
     Pearson-delta score.

## Can Usually Leave Implicit

These can usually be left implicit or explained inline:

- ordinary indices such as `i`, `j`, `k`;
- common notation such as real vector spaces, norms, expectations, sums,
  transpose, `argmax`, and `softmax`;
- standard layers or optimizers such as MLP, encoder, decoder, LayerNorm,
  attention, Adam, or AdamW;
- baseline internals unless the method modifies the baseline;
- standard preprocessing and implementation settings;
- temporary variables that appear only once in one formula.

Explain common notation only when it has a paper-specific meaning. For example,
define a permutation matrix if permutation equivariance is a design point, or
define concatenation if the symbol is nonstandard.

## Where Variables Belong

Problem Formulation:

- observed control and perturbed populations;
- perturbation identity or condition;
- fixed condition/prior embedding when it is an input;
- prediction target;
- conditional distribution or mapping;
- unpaired-observation statement.

Module subsections:

- latent representations;
- coupling matrices or soft reference weights;
- perturbation shifts;
- reference-state representations;
- generator or decoder outputs;
- module-specific objectives.

Experiments or Appendix:

- batch size;
- learning rate;
- hidden dimensions;
- top-k value;
- number of epochs;
- random seed;
- exact split ratio;
- embedding dimensionality when not central to the mechanism;
- normalization and HVG details;
- baseline implementation details.

## Baseline Rule

If a baseline is reused, do not redefine all of its internal variables. Define
only:

- what information it receives;
- whether the split and preprocessing match the proposed method;
- what was changed, if anything;
- what comparison is fair or limited.

## TriShift Method A Minimal Scope

For TriShift-like manuscripts, the Problem Formulation should define only:

```text
X^0 = {x_i^0}_{i=1}^{n_0}, x_i^0 in R^G
Y = {y_j}_{j=1}^{n_1}, y_j in R^G
p, e(p)
\hat y_{m,p} = F_theta(x_m^0, e(p))
```

And it must state:

```text
x_m^0 denotes a selected reference control state rather than a factual
pre-perturbation counterpart of any measured perturbed cell.
```

Do not put these in Method A unless the paragraph specifically needs them:

| Variable or content | Better location |
|---|---|
| latent control and perturbed states | encoder and latent-space subsection |
| OT coupling or Sinkhorn objective | OT reference-pool subsection or Appendix |
| perturbation shift vector | perturbation-shift subsection |
| residual generator formula | generator subsection |
| GenePT or ProtT5 details | perturbation-prior subsection |
| PBMC or Norman split | Experiments |
| Systema metric formula | Experiments or evaluation metrics |
| hyperparameters | Implementation details or Appendix |
| baseline details | Experiments or Baselines |

## Reviewer Check

A Methods section is too notation-heavy when:

- Problem Formulation contains hyperparameters or split ratios;
- baseline internals are fully formalized without modification;
- standard layers are explained like contributions;
- one-off formula variables interrupt the main task definition;
- the reader sees module variables before understanding inputs, outputs, and
  unpaired-observation assumptions.

A Methods section is under-defined when:

- task input and output variables are unclear;
- the prediction target is ambiguous;
- factual pairing or trajectory assumptions could be inferred;
- loss variables are not defined;
- repeated module variables appear without a stable meaning.

