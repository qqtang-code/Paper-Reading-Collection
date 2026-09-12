# Random Attention · 论文精读

**Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning**(arXiv:2609.03430,Salesforce AI Research + UIUC)

> KV cache 驱逐一直被当作"打分排序"问题——给每个缓存 token 估计未来重要性,保住分最高的。本文直接检验并否定这个前提:保住 prompt + 每个 KV 头内均匀随机驱逐、不打任何分,就能在 4 模型 × 6 推理任务上追平最强基线(60 格中 31 格显著领先、仅 1 格落后),并在 vLLM 部署中以 32–43% 的吞吐优势胜出。两个控制实验给出机制账:prompt 是 cache 的脆弱部分;推理轨迹靠"文本复述 + 跨头复制"两层冗余自我保护,随机抽取天然契合逐头独立决策。
>
> Every KV cache evictor scores tokens by estimated future importance and keeps the top-scoring ones. This paper rejects that premise: pin the prompt, evict uniformly at random within each KV head, compute no score at all — and you match the strongest prior evictor across four models and six reasoning tasks (significantly ahead in 31 of 60 cells) while serving 32–43% higher throughput in vLLM. The prompt is the fragile part of the cache; the reasoning trace protects itself through redundancy in the text and across attention heads, which is exactly what independent per-head draws preserve.

- 中文精读页:`index.html`
- 英文速读版:[`en.html`](en.html) — 完整论证摘要 + 全部 5 图 11 表原文图注与解读
- 图片:`figs/` — 5 图 + 11 表,300 DPI 高清提取,中英文页共用
- 分类:高效推理 · KV Cache 驱逐 / 推理模型 / 服务系统
- [在线阅读(中文)](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/random-attention/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/random-attention/en.html) · [论文原文](https://arxiv.org/abs/2609.03430) · [代码](https://github.com/SalesforceAIResearch/Random-Attention)

返回[分类目录](../README.md) · [总索引](../../README.md)
