# Declarative Attention · 论文精读

**Language Models Can Control Their Own Attention**(KAIST AI × Google DeepMind,arXiv:2609.02737)

> 让模型在思维链里用 `<global>` / `<focus>` / `<local>` 标签声明"自己要看哪里",推理引擎解析声明并跳过大部分 KV cache 读取——零训练、零样本。15 项长上下文任务上注意力读取降 52.0% / 31.1%,精度仅降 1.27pp / 2.75pp;roofline 解码墙钟 0.71× / 0.77×。

- 精读页:`Declarative-Attention论文精读_HTML.html`(入口 `index.html` 自动跳转)
- 图片:`figs/` — 10 图 + 10 表,300 DPI 高清提取
- 分类:高效推理 · 稀疏注意力 / KV Cache / 长上下文
- [在线阅读](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/declarative-attention/) · [论文原文](https://arxiv.org/abs/2609.02737)

返回[分类目录](../README.md) · [总索引](../../README.md)
