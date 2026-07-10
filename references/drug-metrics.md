# Drug Metrics And Claim Alignment

Choose metrics by endpoint and state direction and aggregation unit.

| Evidence target | Useful measures | Do not infer alone |
|---|---|---|
| Single-cell response | expression error, DE/signature overlap, distributional distance | efficacy, viability, or direct mechanism |
| Dose/time behavior | curve error, rank correlation, trend agreement | untested dynamics from categorical labels |
| Drug ranking | AUROC/AUPRC, enrichment, NDCG, top-k precision | calibrated effect or clinical benefit |
| Viability/toxicity | MAE/RMSE, correlation, calibration | transcriptomic mechanism |
| Combination | endpoint error plus Bliss/Loewe/HSA/ZIP | synergy from raw combination effect |
| Mechanism | target/pathway/signature agreement | direct target engagement or causality |
| Uncertainty | calibration, coverage, error-versus-OOD distance | reliable confidence without validation |

Aggregate and infer uncertainty across the independent exposure, drug, donor, or
plate unit—not only across cells.
