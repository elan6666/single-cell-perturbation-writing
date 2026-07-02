下面把你上传的几篇单细胞扰动/表达预测论文当作一个“小语料库”来蒸馏：不是只总结模型，而是抽出**论文功能模块、每个模块的段落内部结构、语言风格、代表性表达、会议/期刊写法差异**。我把 PPNF 也纳入写作结构分析，但它更偏“single-cell gene expression prediction / imputation”，不是严格的 perturbation-response 论文。

## 1. 这些论文的共同“隐形骨架”

这批论文本质上都在讲同一个故事：

**高通量单细胞扰动实验很有价值 → 真实实验昂贵/不完备/无配对/高维稀疏/异质性强 → 现有方法在 OOD、组合扰动、分布异质性、先验知识、可扩展性上有缺陷 → 提出一个结构化模型或训练框架 → 在多数据集、多拆分、多指标、消融和鲁棒性实验中验证 → 回到生物意义和未来虚拟细胞/药物发现价值。**

CMonge 把问题定位为“非配对分布之间的条件最优传输”，强调已有 OT 方法不能按 drug/dose/cell type 等上下文条件化，因而提出 Conditional Monge Gap；Scouter 把问题定位为“unseen gene perturbation 的类别外推”，核心是用 LLM gene embeddings 替代稀疏 GO 图；scPRAM 把问题定位为“单细胞级异质扰动响应”，用 VAE latent space、Sinkhorn OT 和 attention 计算 cell-specific perturbation vector；scDFM/SCALE 则把问题进一步提升为“population-level / set-level conditional transport”，强调不要只优化平均表达或配对误差，而要恢复分布级扰动效应。

---

## 2. 功能模块：取并集后的完整论文结构

这些论文的模块并不完全相同。期刊文章常把 Related Work 融进 Introduction，会议论文更喜欢显式列出 Related Work 和 Contributions。取并集后，一个完整可复用结构是：

| 模块                                 | 作用                                            | 这些论文中的典型写法                                                                                                                                                         |
| ---------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Title                              | 用“任务 + 核心机制 + 能力”压缩卖点                         | *Conditional Monge Gap enables...*；*Scouter predicts... with LLM embeddings*；*scDFM: Distributional Flow Matching...*                                              |
| Abstract                           | 压缩全篇：价值、瓶颈、gap、方法、结果、意义                       | CMonge、Scouter 是期刊式连续摘要；scPRAM 是 Motivation/Results/Availability 结构；BIBM 论文是会议式单段摘要。                                                                               |
| Introduction                       | 领域价值 → 实验瓶颈 → 现有方法 → 精确 gap → 本文方法/贡献         | CMonge 用“Despite tremendous progress, two key challenges remain”式转折；Enhanced KG 先讲 Perturb-seq 价值，再讲 GO 不足。                                                        |
| Contributions                      | 会议论文常显式列 3 点                                  | SCALE 和 Enhanced KG 都用 threefold/numbered contributions。                                                                                                           |
| Related Work / Background          | 分类现有方法，并为自己的定位铺路                              | scDFM 分 foundation models、perturbation-specific models；SCALE 分 direct mapping、population-level models；scCADE 分 non/self/auxiliary decoupling。                      |
| Problem Formulation                | 用数学符号定义输入、输出、目标分布或条件分布                        | SCALE 明确定义 control set、perturbed set、cell type、perturbation、batch；scDFM 定义 control state、post-perturbation state 和 perturbation condition。                         |
| Method Overview                    | 一段话 + 一张图总览 pipeline                          | CMonge Fig.1、scPRAM Fig.1、scDFM Fig.1、scCADE Fig.1 都先给 workflow 再拆模块。                                                                                              |
| Module Details                     | 每个模块按“输入→操作→输出→为什么有效”展开                       | scPRAM 拆 VAE、OT、attention；scCADE 拆 encoder-decoder、contrastive、attention、loss；PPNF 拆 proximal neural factorization 和 prototype learning。                           |
| Loss / Objective                   | 用公式说明训练信号，并解释每项作用                             | scCADE 明确 reconstruction、counterfactual、contrastive loss；scDFM 用 flow matching + MMD；PPNF 用 prediction/proximal/orthogonalization composite loss。                  |
| Experiments Setup                  | 数据集、split、baseline、metric、实现细节                | CMonge 区分 IS/OOS、dose/drug-dose；SCALE 列 PBMC/Tahoe/Replogle；Scouter 说明 train/val/test splits 和 top DEG metrics。                                                    |
| Results                            | 按研究问题分小节：main、OOD、scaling、biological analysis | CMonge 逐步讲 in-distribution、OOS、scaling；scPRAM 逐步讲 OOS、DEG、cross-species、robustness。                                                                                |
| Ablation / Robustness              | 证明每个模块不是装饰                                    | Enhanced KG 用 disease-gene/drug-gene ablation；scCADE 去掉 attention/contrastive；scPRAM 做 sampling/noise/parameter robustness。                                        |
| Discussion                         | 回答“为什么有效、有什么意义、有什么限制”                         | CMonge 讨论 scaling、RDKit/MoA、condition-agnostic、future work；Scouter 讨论 LLM embedding、compressor-generator、accessibility；scDFM 讨论 representation/path/scalability。   |
| Conclusion / Availability / Ethics | 收束贡献，给代码数据，交代边界                               | scDFM 有 ethics statement；Scouter 和 CMonge 有 data/code availability；Bioinformatics 风格强调 availability。                                                               |

**最推荐的主文结构**：
**Abstract → Introduction → Related Work → Problem Formulation → Method Overview → Module Details → Objective/Training → Experiments → Results → Ablation/Robustness → Biological Interpretation → Discussion/Limitations → Conclusion → Data/Code/Ethics。**

---

## 3. 每个模块的“段落内架构”

### 3.1 Abstract 的段内架构

这些摘要通常不是随便写结果，而是非常固定的 6 步：

**句 1：领域价值。**
说明 perturbation prediction / single-cell modeling 为什么重要。
模板：
“Predicting how cells respond to [perturbations] is central to [functional genomics / drug discovery / precision medicine].”

**句 2：现实瓶颈。**
实验成本、组合空间、无配对、高维稀疏、异质性、OOD。
模板：
“However, [experimental / computational] progress remains limited by [cost, sparsity, unpaired measurements, poor generalization].”

**句 3：现有方法不足。**
用 “Existing methods...” 或 “Although powerful...” 开始。
模板：
“Existing methods typically [assumption], which limits their ability to [desired capability].”

**句 4：提出方法。**
最经典：Here we present / Here we propose。
模板：
“Here we present [METHOD], a [framework/model] that [core mechanism].”

**句 5：机制一句话。**
不是展开公式，而是说核心 design。
模板：
“[METHOD] combines [module A] with [module B] to [effect].”

**句 6：实验结果。**
跨数据集、OOD、SOTA、ablation。
模板：
“Across [datasets/settings], [METHOD] [outperforms/improves/reduces] [baselines/metric], especially in [hard setting].”

**句 7：意义收束。**
虚拟细胞、药物发现、精准医学、可扩展性。
模板：
“These results suggest that [principle] provides a practical route toward [application].”

CMonge 摘要非常完整：先讲 neural OT 适合 unpaired data，再讲现有 OT 不能条件化，再提出 CMonge，再强调 seen/unseen drug、heterogeneity、parameter efficiency 和 drug discovery。Scouter 摘要也很标准：先讲 gene perturbation profiling 价值和 throughput 限制，再讲 GO graph 稀疏和覆盖不全，随后提出 LLM embeddings + compressor-generator，并报告相对 GEARS/biolord 的错误降低。

---

### 3.2 Introduction 的段内架构

推荐 5 段式。

**第 1 段：大背景 + 应用价值。**
结构：
“技术/任务是什么 → 已经带来什么能力 → 对药物发现/个性化治疗/机制研究有什么意义。”
典型句式：
“Single-cell RNA sequencing has enabled…”
“Understanding cellular responses to perturbations is essential for…”

Enhanced KG、scCADE、PPNF 都用这种开头：先讲 single-cell 或 perturb-seq 的价值，再连接到 drug discovery、personalized therapeutics 或 cellular heterogeneity。

**第 2 段：现实不可行性。**
结构：
“实验空间巨大/成本高/数据少 → 需要 in silico prediction。”
典型句式：
“Although powerful, such technology cannot be implemented on a large scale…”
“Therefore, computational methods are needed to overcome these constraints.”

这类句子在 BIBM Enhanced KG 里非常典型，用 cost-intensive、time-consuming、multi-gene combinations 引出计算预测的必要性。

**第 3 段：现有方法谱系。**
结构：
“已有方法 A/B/C → 它们解决了什么 → 仍然有什么问题。”
典型转折词：
“While…”, “However…”, “Nevertheless…”, “Despite…”

CMonge 在引言里把 scGen、generative frameworks、foundation models、OT methods 串起来，然后明确指出两个 key challenges；SCALE 和 scDFM 则把方法分成 direct mapping、population-level、foundation/generative 等路线。

**第 4 段：精确 gap。**
这是最关键的一段。不要泛泛说“existing methods are limited”，要说**某个假设不成立**。
常见 gap 类型：

* **unpaired data gap**：不能观察同一细胞扰动前后。
* **mean-effect gap**：只预测平均表达，忽略 distribution/heterogeneity。
* **conditional generalization gap**：不能对 unseen drug/dose/cell type 条件化。
* **prior knowledge gap**：GO graph 稀疏、覆盖不全、不能表达 disease/drug/gene 关系。
* **scaling gap**：训练/推理 pipeline 不适合 atlas-scale。

CMonge 明确说现有 OT 是 unconditional、local maps，导致新条件不能 inference、训练成本高、不能利用 covariates 和 cross-task benefits；Enhanced KG 明确说 GO annotations 不足以反映 disease-specific gene similarity；scDFM 明确说忽略 population-level distributional fidelity 和 noisy interdependent gene regulation。

**第 5 段：本文方法 + 贡献。**
结构：
“In this work, we propose…” → “The key idea is…” → “We evaluate…” → “Our contributions are…”

SCALE 的引言末尾很强：先说“what is needed instead”，再提出 SCALE，然后接三点贡献，包括 scalable infrastructure、endpoint-aligned conditional transport、biologically grounded metrics。

---

### 3.3 Related Work 的段内架构

Related Work 最好不要写成论文列表，而要写成**分类 + 局限 + 我的位置**。

推荐 4 段式：

**第 1 段：传统/早期路线。**
“Early approaches / direct mapping / GRN-based methods…”
说明它们解决什么，但在哪些设置不够。

**第 2 段：深度学习/autoencoder/foundation model 路线。**
“Recent deep learning methods…”
说明 scGen、CPA、GEARS、scGPT、Geneformer 等。

**第 3 段：与本文最接近的路线。**
例如 transport、flow matching、diffusion、set modeling、prior-knowledge graph。

**第 4 段：Positioning。**
最推荐显式写：
“Compared with X, we…”
“Unlike Y, our method…”
“Our work is most closely related to Z, but differs in…”

SCALE 的 Related Work 非常适合仿写：它先讲 single-cell foundation models，再讲 direct conditional mapping，再讲 population-level perturbation models，最后用“Positioning of SCALE”把自己放到最后一类里。scDFM 也类似，先讲 foundation models，再讲 perturbation-specific models，并说明自己的方法同时连接 attention encoder 和 flow matching。

---

### 3.4 Method / Methods 的段内架构

方法部分的黄金段式是：

**第一句：这个模块解决什么问题。**
“Given [input], our goal is to [output].”

**第二句：为什么普通做法不够。**
“Directly modeling [space/objective] is challenging because…”

**第三句：我们怎么做。**
“We therefore introduce/use/formulate…”

**第四句：数学或操作定义。**
“Formally, let…”
“Specifically, we compute…”

**第五句：输出和优点。**
“This yields…”
“By construction…”
“This allows…”

方法部分的推荐顺序：

1. **Problem setup**：定义数据、符号、任务目标。
   SCALE 定义 control cell set、perturbed cell set、celltype、perturbation、batch，并说明 unordered set 和 conditional law；scDFM 定义 pre-perturbation state、post-perturbation state 和 perturbation condition。

2. **Overview / architecture figure**：总览模型。
   CMonge 的图说明 source distribution + context → learned perturbation；scPRAM 的图说明 VAE encoder → OT matching → attention perturbation vector → decoder；scCADE 的图说明 encoder 将 gene expression/covariates/perturbations 映射到 latent space，再分 actual/counterfactual 两条 decoder 路径。

3. **Representation / encoder**：说明如何表示 cell、gene、perturbation、dose、batch。
   Scouter 用 control expression + LLM-based gene embedding；SCALE 用 set-aware latent population representation；scDFM 用 gene expression encoding + co-expression graph mask。

4. **Core mechanism**：这是论文“方法名”的主体。
   CMonge 是 conditional OT/Monge Gap；scPRAM 是 OT matching + attention vector；scDFM 是 conditional flow matching + MMD + PAD-Transformer；Enhanced KG 是 multi-source KG + Node2Vec + replacing GEARS GO graph；PPNF 是 prototype-based representation + proximal neural factorization。

5. **Loss / objective**：先解释每个 loss 的直觉，再给公式。
   scDFM 的写法很好：先说 flow matching 只保证 local dynamical consistency，不保证 terminal distribution alignment，因此加入 MMD；scCADE 则清晰列出 reconstruction、counterfactual、contrastive；PPNF 列出 prediction、proximal、orthogonalization 三项。

6. **Training / inference**：说明训练拆分、采样、超参、实现。
   Scouter 详细说明每个 epoch 随机选 control cell 和 perturbed cell 构成 triplets，并给出 K random control cells 的 inference 策略；CMonge 说明 IS/OOS setting、leave-one-drug-out、dose/drug-dose conditioning 和 R²/Wasserstein/MMD。

---

### 3.5 Experiments 的段内架构

实验部分推荐固定写法：

**段 1：总实验目标。**
“To comprehensively assess [capability], we evaluate [method] on [datasets/settings].”

**段 2：数据集。**
每个数据集一句：生物场景、规模、任务难点。
SCALE 的数据集段落特别规范：PBMC 对 cytokine signaling，Tahoe-100M 对 chemical perturbation，Replogle-Nadig 对 genetic perturbation，并说明每个 benchmark 的 biological regime。

**段 3：预处理和拆分。**
说明 normalization、HVG selection、train/val/test、OOD/OOS holdout。
Scouter 和 CMonge 都强调 test perturbations 不出现在 training/validation 里，CMonge 还系统区分 IS/OOS、dose OOS、drug OOS。

**段 4：baselines。**
按类别列：identity/mean/linear、domain-specific、SOTA、foundation model。
scDFM 的 appendix 把 scGPT、Geneformer、GEARS、CPA、STATE、CellFlow 分别解释，非常适合 benchmark-heavy 论文。

**段 5：metrics。**
不要只写 MSE。扰动论文更推荐组合指标：
MSE/MAE/R² 看整体拟合；Wasserstein/MMD 看分布；DE-Spearman/DE overlap/DE precision 看生物差异；variance regression 看 heterogeneity。scPRAM 明确用 Wasserstein、mean/variance regression、DEG 和 UMAP；CMonge 用 R²、Wasserstein、MMD；SCALE 强调 biologically meaningful metrics。

---

### 3.6 Results 的段内架构

结果段不要从数字开始，而要从**研究问题**开始：

**句 1：本小节要回答的问题。**
“We first sought to assess whether…”
“We next investigated…”
“To study scalability…”
“To evaluate robustness…”

**句 2：实验设置。**
“We trained/evaluated [models] on [dataset] under [split].”

**句 3：主要定量结果。**
“[Method] outperformed [baseline] on [metric].”

**句 4：细节解释。**
“The improvement was most pronounced in…”
“This suggests that…”

**句 5：图表/可视化支撑。**
“UMAP visualizations show…”
“Pathway enrichment analysis revealed…”

**句 6：承接下一小节。**
“Together, these results establish…”
“We next asked whether…”

CMonge 的 Results 是最标准的“逐级加难度”：先 overview，再 in-distribution，接着 OOS，再 scaling；scPRAM 的 Results 是“能力清单”：OOS prediction、DEG identification、cross-species heterogeneity、cross-individual、robustness；Scouter 的 Results 是“single-gene → two-gene → GO missing → foundation model comparison”。

---

### 3.7 Ablation / Robustness 的段内架构

Ablation 的段落非常固定：

1. **目的**：验证某模块是否必要。
   “We conducted an ablation experiment to further validate…”

2. **去掉什么**：remove A / replace B / use ablated network。

3. **结果**：full model 最好，去掉模块下降。

4. **解释**：模块提供了什么能力，不是单纯堆组件。

Enhanced KG 的 ablation 很清楚：构造 Disease-Gene 和 Drug-Gene 两个 ablated networks，发现单独 disease-gene 或 drug-gene 也有帮助，但三类知识组合最好，说明提升来自知识组合的协同作用。scCADE 的 ablation 去掉 attention 或 contrastive learning 都会降低性能。scPRAM 的 robustness 则测试 sampling rate、noise level 和 attention proportion，并说明模型对样本量、噪声、超参相对稳定。

---

### 3.8 Discussion / Conclusion 的段内架构

Discussion 推荐 5 段：

**第 1 段：一句话重述贡献 + 总结果。**
“We introduce [method], a [framework] for…”
“Our results indicate that…”

**第 2 段：为什么有效。**
Scouter 用 three factors 解释有效性：LLM embeddings、compressor-generator、random control/perturbed pairing；CMonge 解释 RDKit/MoA、scaling、parameter efficiency；scDFM 解释 distribution-level alignment 的必要性。

**第 3 段：生物/应用意义。**
drug discovery、virtual screening、precision medicine、patient-derived organoids、rare cell states。

**第 4 段：限制。**
不要藏缺点。常见写法：
“Although our results demonstrate…, several challenges remain…”
“While [method] has made progress, it currently…”

CMonge 明确提到新 cell type、OOD conditions、noise/batch effects、sparsely sampled drug classes 等挑战；scPRAM 说明主要处理 single perturbations，尚未考虑 dosage/duration 等 perturbation covariates。

**第 5 段：未来工作。**
更强 architecture、更合理 latent space/path、large-scale dataset、more complex perturbations、biologically realistic systems。CMonge 提到更 expressive architectures、优化 OT latent space、patient-derived organoids；scDFM 提到 representation/path design、多 context dataset 和 graph topology。

Conclusion 则短很多，通常 1 段 3–5 句：
“我们提出了什么 → 实验证明什么 → 消融/鲁棒性证明什么 → 未来/意义。”

---

## 4. 语言风格：这些论文共同的“语气”

### 4.1 总体风格

这批论文的语言不是花哨型，而是**问题驱动 + 机制解释 + 证据约束 + 谨慎外推**。

常用动词：
**enable, capture, align, condition, generalize, leverage, incorporate, outperform, demonstrate, suggest, reveal, preserve, improve, address, mitigate, formulate, instantiate, benchmark, validate。**

常用转折：
**However, Nevertheless, Despite, In contrast, Unlike, To address this limitation, Motivated by, Importantly, Notably, Together, These results suggest。**

常用名词短语：
**population-level distributional shift, heterogeneous cellular responses, out-of-distribution generalization, biologically grounded metrics, perturbation-induced transition, conditional transport, prior biological knowledge, gene-gene relationships, differentially expressed genes, robust prediction, scalable inference。**

它们很少直接说“our method is amazing”。更常用：
“results indicate / suggest / demonstrate / establish”。这比 “prove” 更适合期刊和高水平会议。

---

## 5. 期刊 vs 会议：推荐写法差异

| 场景 | 期刊/Nature/Bioinformatics 风格                            | 会议/ICLR/BIBM 风格                                   |
| -- | ------------------------------------------------------ | ------------------------------------------------- |
| 摘要 | 连贯叙事，强调生物意义和 broad implications                        | 更压缩，突出方法、SOTA、metric、贡献                           |
| 引言 | Related work 常融入 introduction                          | Related Work 常独立成节                                |
| 方法 | Results 常在 Methods 前，Methods 更详尽                       | Method 在 Experiments 前，公式和模块更早出现                  |
| 贡献 | 较少显式 bullet，常用 “Here we…”                              | 常用 “Our contributions are threefold”              |
| 结果 | 强调机制解释、可视化、生物发现                                        | 强调 benchmark、table、ablation、efficiency            |
| 讨论 | 一定写 limitations/future，语气谨慎                            | Conclusion 更短，可把 limitations 放 appendix           |
| 语言 | “We found that…”, “Our results indicate…”, “Together…” | “We propose…”, “We benchmark…”, “Ablation shows…” |

**期刊推荐语言：**

* “Here, we present…”
* “We found that…”
* “Our results indicate that…”
* “Notably,…”
* “Together, these results suggest…”
* “Although our results demonstrate…, several challenges remain…”
* “Future work could…”

**会议推荐语言：**

* “Our contributions are threefold.”
* “We formulate [task] as [problem].”
* “We instantiate this formulation with…”
* “We benchmark [method] against [baselines] on [datasets].”
* “Ablation studies demonstrate that…”
* “Compared with [baseline], [method] improves [metric] by…”

SCALE、Enhanced KG 和 PPNF 都有很强的会议式 contribution list；CMonge、Scouter、scPRAM 则更像期刊式“背景—发现—意义”叙事。

---

## 6. 代表性原句片段与可仿写模板

下面每类给一个**短原句片段风格**和一个**可直接改写模板**。

### 6.1 领域价值开场

原句片段：
“Learning the response of single cells…”

仿写模板：
“Predicting how single cells respond to perturbations is central to understanding cellular regulation and designing targeted interventions.”

中文逻辑：
不要一上来讲模型，先讲 biological question。

---

### 6.2 实验瓶颈

原句片段：
“limited by its scalability…”

仿写模板：
“Although perturbation assays provide direct measurements of cellular responses, their cost and combinatorial scale make exhaustive experimental screening impractical.”

---

### 6.3 现有方法不足

原句片段：
“two key challenges remain.”

仿写模板：
“Despite substantial progress, current methods still struggle to capture [heterogeneity/distributional shifts] and to generalize to [unseen perturbations/cell types/contexts].”

---

### 6.4 明确 gap

原句片段：
“GO annotations… cannot sufficiently reflect…”

仿写模板：
“However, [prior/source/objective] is insufficient as the sole signal for [task], because it fails to capture [missing biological relationship].”

---

### 6.5 提出方法

原句片段：
“Here we propose the Conditional Monge Gap…”

仿写模板：
“Here we propose [METHOD], a [framework/model] that [core operation] to [target capability].”

---

### 6.6 方法概览

原句片段：
“consists of a variational autoencoder, optimal transport, and attention mechanism”

仿写模板：
“[METHOD] consists of three components: [encoder/representation], [transport/generation module], and [alignment/loss module].”

---

### 6.7 机制解释

原句片段：
“to address distribution-level fidelity…”

仿写模板：
“To address [limitation], we introduce [module/loss], which directly encourages [desired property] rather than merely optimizing [weaker objective].”

---

### 6.8 Related Work 定位

原句片段：
“our work is most closely related…”

仿写模板：
“Our work is most closely related to [family of methods], but differs in [key modeling assumption/design/evaluation protocol].”

---

### 6.9 实验设置

原句片段：
“We evaluate SCALE on three representative…”

仿写模板：
“We evaluate [METHOD] on [N] representative benchmarks spanning [biological regimes], including [dataset A], [dataset B], and [dataset C].”

---

### 6.10 结果主张

原句片段：
“CMonge consistently outperformed…”

仿写模板：
“Across [settings], [METHOD] consistently outperforms [baselines], with the largest gains observed in [hardest setting].”

---

### 6.11 消融实验

原句片段：
“we conducted an ablation experiment…”

仿写模板：
“To assess the contribution of [component], we conduct ablation experiments by [removing/replacing] it while keeping all other settings unchanged.”

---

### 6.12 鲁棒性分析

原句片段：
“with increasing noise, the performance… declined”

仿写模板：
“To evaluate robustness, we vary [sample size/noise level/hyperparameter] and compare the degradation of [metric] across methods.”

---

### 6.13 可视化解释

原句片段：
“align most closely with the true perturbation responses”

仿写模板：
“UMAP visualizations show that the predicted population overlaps with the ground-truth perturbed distribution, suggesting that [METHOD] preserves both central tendency and heterogeneity.”

---

### 6.14 生物解释

原句片段：
“downstream enrichment analysis”

仿写模板：
“To assess biological relevance, we perform pathway enrichment analysis on the predicted DEGs and compare the enriched pathways with known perturbation mechanisms.”

---

### 6.15 讨论为什么有效

原句片段：
“stems from the interplay…”

仿写模板：
“The effectiveness of [METHOD] likely stems from the interplay of [factor A], [factor B], and [factor C].”

---

### 6.16 限制与未来工作

原句片段：
“several challenges remain”

仿写模板：
“Although our results demonstrate clear potential, several challenges remain, including [generalization/noise/batch effects/scalability].”

---

## 7. 可直接复用的模块句式库

### Abstract 句式

1. “Predicting cellular responses to perturbations is a central task in [field].”
2. “However, exhaustive experimental profiling remains infeasible due to [cost/scale/combinatorial explosion].”
3. “Existing methods often [assumption], limiting their ability to [capability].”
4. “Here, we present [METHOD], a [framework] for [task].”
5. “[METHOD] combines [module A] and [module B] to [mechanism].”
6. “Across [datasets], [METHOD] achieves [improvement] over [baselines].”
7. “These results highlight the importance of [principle] for [application].”

### Introduction 句式

1. “[Technology/task] has become a powerful approach for [biological goal].”
2. “Recent advances in [assay/model] have enabled [new capability].”
3. “Nevertheless, [bottleneck] remains a major obstacle.”
4. “This challenge is exacerbated by [data property].”
5. “Previous work has explored [family A], [family B], and [family C].”
6. “Despite these advances, current methods still struggle with [gap].”
7. “To address this gap, we introduce [METHOD].”
8. “Our key insight is that [modeling principle].”

### Related Work 句式

1. “A first line of work focuses on [category].”
2. “These methods are effective in [setting], but typically assume [assumption].”
3. “A second family of methods models [object] using [technique].”
4. “More recently, [new family] has been proposed to [goal].”
5. “Our method differs from these approaches in two aspects.”
6. “Rather than [old assumption], we formulate [task] as [new problem].”

### Method 句式

1. “Let [X] denote [input] and [Y] denote [target].”
2. “The goal is to learn [conditional mapping/distribution].”
3. “The key difficulty is that [unpaired/noisy/high-dimensional].”
4. “We therefore formulate the problem as [transport/flow/generation].”
5. “The architecture contains [N] components.”
6. “The first component [operation] to obtain [representation].”
7. “The second component [operation] conditioned on [context].”
8. “Finally, [decoder/head] produces [prediction].”
9. “The objective combines [loss A] with [loss B].”
10. “This design encourages [desired property].”

### Experiments 句式

1. “We evaluate [METHOD] on [datasets] covering [settings].”
2. “We compare against [baseline categories].”
3. “We adopt [split] to assess [generalization type].”
4. “All models are evaluated using [metrics].”
5. “For fair comparison, we use [same preprocessing/splits/hyperparameters].”
6. “The best result is highlighted in bold.”

### Results 句式

1. “We first assess whether [component] improves [capability].”
2. “As shown in Table/Fig. [X], [METHOD] achieves [result].”
3. “The improvement is especially pronounced under [hard setting].”
4. “This suggests that [mechanism] is critical for [capability].”
5. “We next investigate whether [METHOD] generalizes to [OOD setting].”
6. “Qualitatively, the predicted distribution [overlaps/preserves/captures] [property].”

### Ablation 句式

1. “To isolate the contribution of [module], we remove/replace [module].”
2. “Removing [module] leads to [performance drop], indicating that [module role].”
3. “The full model consistently performs best, suggesting that [components] are complementary.”
4. “This result confirms that the observed gains are not solely attributable to [single factor].”

### Discussion 句式

1. “We introduce [METHOD], a [framework] for [task].”
2. “Our results indicate that [principle] is important for [capability].”
3. “The effectiveness of [METHOD] stems from [factor A/B/C].”
4. “Beyond accuracy, [METHOD] enables [biological/application advantage].”
5. “Although promising, several challenges remain.”
6. “Future work could extend [METHOD] to [larger/more complex/clinically realistic setting].”

---

## 8. 你写同类论文时最优“段落模板”

### Abstract 模板

> Predicting [cellular response] to [perturbations] is essential for [biological/application goal]. However, [experimental/computational bottleneck] makes exhaustive profiling infeasible. Existing methods often [limitation], which restricts their ability to [OOD/generalization/heterogeneity/distribution]. Here, we present [METHOD], a [framework] that [core idea]. [METHOD] integrates [module A] with [module B] to [mechanism]. Across [datasets/settings], [METHOD] [outperforms/improves] [baselines] on [metrics], with particularly strong gains in [hard setting]. Together, these results suggest that [principle] provides a practical route toward [application].

### Introduction 最后两段模板

> Despite these advances, two challenges remain. First, [challenge 1], because [reason]. Second, [challenge 2], particularly when [OOD/combinatorial/scaling setting]. Addressing these challenges requires [modeling principle].

> In this work, we introduce [METHOD], which [one-sentence method]. The key idea is to [core insight]. We evaluate [METHOD] on [datasets] under [splits/settings], and show that it [main result]. Our contributions are: (1) [methodological contribution]; (2) [empirical contribution]; and (3) [biological/scaling contribution].

### Method overview 模板

> [METHOD] takes as input [control state/source distribution] and [condition/perturbation embedding], and predicts [perturbed state/target distribution]. The model consists of three components. First, [encoder] maps [input] into [latent representation]. Second, [transport/generation module] models [perturbation-induced transition]. Third, [loss/evaluation module] enforces [distributional/biological/semantic alignment]. This design allows [METHOD] to [generalize/capture heterogeneity/scale].

### Results 小节模板

> We first asked whether [method/component] improves [capability]. To this end, we trained [models] on [dataset] under [split] and compared them with [baselines]. [METHOD] achieved [metric result], outperforming [baseline]. The gain was most pronounced in [hard setting], suggesting that [mechanistic explanation]. Qualitative analysis using [UMAP/pathway/DEG] further confirmed that [METHOD] captures [biological property].

### Discussion 模板

> We have presented [METHOD], a [framework] for [task]. Across [settings], [METHOD] improves [accuracy/distributional fidelity/generalization] while preserving [biological property]. These gains likely arise from [factor A], [factor B], and [factor C]. Importantly, [METHOD] is [scalable/flexible/lightweight/interpretable], making it suitable for [application]. However, several challenges remain, including [limitations]. Future work should explore [extensions], which may further improve [goal].

---

## 9. 最实用的写作策略

第一，**先确定你的 central gap**。这些论文之所以好写，是因为 gap 很锋利：CMonge 是“unconditional OT 不能 generalize to new contexts”；Scouter 是“GO graph 稀疏且覆盖不全”；scPRAM 是“平均响应不够，cell-level heterogeneity 被忽略”；scDFM/SCALE 是“cell-wise/mean-effect objective 不适合 population-level perturbation”。你的论文也要先确定一个这样的 gap。

第二，**方法命名要绑定能力，而不是只绑定模块**。例如 Conditional Monge Gap 绑定“conditional + OT generalization”，Scouter 绑定“unseen perturbation + LLM embeddings”，scDFM 绑定“distributional + flow matching”，SCALE 绑定“scalable + conditional atlas-level endpoint transport”。名字最好让审稿人一眼看到“你解决了什么 gap”。

第三，**实验不要只有主表**。这批论文的共同强项是：主结果 + OOD/OOS + ablation + robustness/scaling + biological interpretation。对单细胞扰动预测，最好至少有：DEG 指标、distributional metric、OOD split、消融、UMAP 或 pathway analysis。

第四，**语言要克制但有力**。少用 “perfect / revolutionary / unprecedented”，多用 “suggests / demonstrates / indicates / enables / provides a practical route”。期刊更喜欢“结果说明了什么”，会议更喜欢“贡献是什么、提升多少、为什么 fair”。

第五，**每段只承担一个功能**。背景段只讲价值；gap 段只讲缺陷；method 段只讲机制；result 段只回答一个实验问题；discussion 段只做解释和边界。这样读者不会迷失。
