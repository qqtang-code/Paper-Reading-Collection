# KITE / SST — KV-Invariant Transformer Expansion

**KITE / SST**(arXiv:2609.27294 · StepFun)

> 扩容时把新容量只加在"不产生 KV"的一侧:先训 33.8B 小模型,再用中间 checkpoint 把容量扩成一座**只读 KV 的 Decoder 塔**继续联合训练。推理时 bulk prefill 只跑原来的 Prefiller 塔,新增容量只在 decode 与 prompt 末位预测上场。SST 在累计理论训练算力 ≈1.000 $B_{\text{ref}}$ 下训练 EMA-200 损失 **1.5900**,低于 47B classic(1.6006)与 63B classic(1.5921);prefill 活跃体参数只有 **1.120B**(比 47B 基线的 1.477B 还少),decode 2.155B;75:25 的 P/D 成本代理比 47B 低 **6.7%**、比 63B 低 **31.6%**。七项下游任务全部第一,核心约束只有一条:**未来 KV 的产生不得依赖 Decoder 的历史状态**。
>
> Grow only the side that produces no KV. KITE first trains a 33.8B source; expansion then adds a **KV-reading Decoder tower** initialized from the source weights, and both towers continue training jointly. At inference, bulk prefill still runs only the Prefiller tower, while the added capacity appears only in decode and the prompt-boundary prediction. SST reaches a training EMA-200 loss of **1.5900** at ≈1.000 $B_{\text{ref}}$ cumulative training compute — below 47B classic (1.6006) and 63B classic (1.5921) — running prefill with just **1.120B** active body parameters (below the 47B baseline's 1.477B) and 2.155B at decode; the 75:25 prefill:decode cost proxy is **6.7%** under 47B and **31.6%** under 63B. Best on all seven downstream tasks. The central constraint is one line: **future KV production must not depend on historical Decoder states**.

- **中文精读**:[index.html](index.html) · [在线](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/kite/)
- **English full mirror**:[en.html](en.html) · [online](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/kite/en.html)
- **分类**:高效推理与部署 · 决策者 = **扩容的位置**(只加在不产生 KV 的一侧)/ 架构扩展 / Prefill-Decode 成本分离
- **图表**:`figs/` 共 13 张(6 Figure + 7 Table),300 DPI 从原文提取,中英页共用
- **原文**:<https://arxiv.org/abs/2609.27294>

论文速览:SST 把 33.819B 源模型扩成 **66.959B MoE**(源塔与 Decoder 塔各 18 层、hidden 2304、512 选 8 专家、SSSF 注意力),源阶段 167.98B token + 续训 222.55B token = **390.54B token / 31,037 步**;训练损失在转换点先抬升(约 +0.14)再反超两条从零训练的基线;推理成本随 prefill 占比升高而占优,与 63B 在 13.4:86.6、与 47B 在 **65.5:34.5** 打平,正好覆盖 OpenRouter 实测的 67.4–76.7% 未缓存输入账单区间。

本页另含两处编者推算:**参数账差额拆解**($2\times33.819-0.594-0.085=66.959$;Decoder 缺的 18 层 K/V 投影与 K 归一化 ≈85M,同一笔数解释 decode 活跃参数 $2.155=1.120+1.035$)与 **训练算力复算**(按式(5)与四个 forward 系数复算,三个模型都落在 $5.168\times10^{21}\approx B_{\text{ref}}$ 的千分之一内),以及 **5 条「未披露、值得补测」清单**(实测服务加速缺位、扩展时点未扫描、容量分配未探、单次运行无方差、两塔 KV/显存账未展开)。

返回[分类目录](../README.md) · [总索引](../../README.md)