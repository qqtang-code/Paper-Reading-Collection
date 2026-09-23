# HySparse2 · 论文精读

**HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing**(arXiv:2609.26368,Xiaomi LLM-Core)

> 长程多轮的 agentic 推理让上下文被"输入"主导:模型自己产出的 action 很短,工具返回的观测却很长。HySparse2 把跨层 KV 共享做成两级——外层 **KV Bridging** 让 cross-decoder 的全注意力层用 self-decoder 全注意力层的**输入隐状态**经各自投影构造 K/V,内层 **KV Reuse** 让同一 block 内的稀疏层复用全注意力层的 KV cache 与选择索引。再配合两处改造(选择粒度从 64-token 块换成单 token;**删掉稀疏层里独立的 SWA 分支**,改为把最近 128 token 强制塞进稀疏选择),cross-decoder 的每一份 KV cache 都能由 self-decoder 隐状态导出,于是 **prefill 建完 cache 就能退出,不必跑 cross-decoder 的 24 层**。80B-A3B 上 1M 上下文的 prefill FLOPs 相对 HySparse/Hybrid SWA 降 2.92×/5.02×,KV cache 2.69 GB(对 6.72/12.09 GB),后训练检索 MRCR-v2 +11.30、RULER-v2 +19.81 个百分点。
>
> Long-horizon multi-turn agentic inference makes the context input-dominated: the model's own actions are short while tool observations are long. HySparse2 turns cross-layer KV sharing into a two-level scheme. At the outer level **KV Bridging** lets each cross-decoder full-attention layer project its own K/V from the **input hidden states** of a self-decoder full-attention layer; at the inner level **KV Reuse** lets a block's sparse layers reuse the full-attention layer's KV cache and selection indices. Two further changes — token-level instead of 64-token-block selection, and **deleting the separate SWA branch** in favour of forcing the most recent 128 tokens into the sparse selection — mean every cross-decoder KV cache can be derived from self-decoder hidden states, so **prefill can exit after the self-decoder** and never runs the cross-decoder's 24 layers. On an 80B-A3B model at 1M context this cuts prefill FLOPs by 2.92×/5.02× against HySparse/Hybrid SWA and the KV cache to 2.69 GB (vs 6.72/12.09 GB), with post-training retrieval gains of +11.30 MRCR-v2 and +19.81 RULER-v2 points.

- 中文精读页:`index.html`
- 英文完整版:[`en.html`](en.html) — 全 9 章 1:1 对应,全部 5 图 5 表原文图注与英文解读
- 图片:`figs/` — 5 图 + 5 表,300 DPI 高清提取,中英文页共用
- 分类:注意力与 KV Cache · 混合稀疏注意力 / 两级 KV 共享 / 长上下文
- [在线阅读(中文)](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/hysparse2/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/hysparse2/en.html) · [论文原文](https://arxiv.org/abs/2609.26368)

## 本页比论文多做的两处推算

1. **配置落到层号**:把 Figure 2 的方框数与正文的 49 层对上 —— self-decoder 25 层(SWA×12 + FA + SWA×12)、cross-decoder 24 层(FA + SA×5 重复 4 组),全模型 5 个 FA 层里只有 1 个在 self-decoder 内,与 Table 1 的「#Full = 5」吻合。
2. **KV cache 账本**:用 Table 1 的 KV head 配置推算每 token 字节数得 2,560 / 6,400 / 11,520 bytes,乘 1M 得 2.56 / 6.40 / 11.52 GB,与论文的 2.69 / 6.72 / 12.09 GB 相差同一个约 1.05 倍(口径差异);而两两比值 2.50 与 4.50 与论文的 2.50 / 4.49 几乎完全吻合,验证了稀疏层确实不带常驻 KV cache。

以上均以「整理 / 推算」显式标注,与论文口径区分。

返回[分类目录](../README.md) · [总索引](../../README.md)