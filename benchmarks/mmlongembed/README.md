# MMLongEmbed · 论文精读

**MMLongEmbed: 长上下文场景下的多模态嵌入模型基准**([原文仓库](https://github.com/AmamiSora1228/MMLongEmbed))

> 首个专门评测多模态嵌入模型(MEM)长上下文能力的基准:4 个检索任务、8 个数据集、8,460 个查询、11 个模型。核心发现:现役模型依赖表面特征匹配"作弊",细粒度信息保持随长度显著衰退——"窗口大"不等于"读得懂"。
>
> The first benchmark dedicated to long-context multimodal embedding: 4 retrieval tasks, 8 datasets, 8,460 queries, 11 models. Key findings: current MEMs "cheat" via surface-feature matching; fine-grained retention decays after ~2K tokens; targets in mid-sequence are systematically lost (positional bias); and scaling parameters buys almost nothing (Qwen3 8B vs 2B: p=0.5375).

- 中文精读页:`index.html`
- 英文速读版:[`en.html`](en.html) — 完整论证摘要 + 全部 22 张图表原文图注
- 图片:`figs/` — 6 图 + 16 表,300 DPI 高清提取,中英文页共用
- 分类:评测基准 · 多模态 / 嵌入模型 / 长上下文
- [在线阅读(中文)](https://qqtang-code.github.io/Paper-Reading-Collection/benchmarks/mmlongembed/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/benchmarks/mmlongembed/en.html) · [论文原文](https://github.com/AmamiSora1228/MMLongEmbed)

返回[分类目录](../README.md) · [总索引](../../README.md)
