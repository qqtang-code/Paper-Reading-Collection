# Declarative Attention · 论文精读

**Language Models Can Control Their Own Attention**(KAIST AI × Google DeepMind,arXiv:2609.02737)

> 让模型在思维链里用 `<global>` / `<focus>` / `<local>` 标签声明"自己要看哪里",推理引擎解析声明并跳过大部分 KV cache 读取——零训练、零样本。15 项长上下文任务上注意力读取降 52.0% / 31.1%,精度仅降 1.27pp / 2.75pp;roofline 解码墙钟 0.71× / 0.77×。
>
> The model declares where to look with `<global>` / `<focus>` / `<local>` tags in its own chain-of-thought; the engine parses the declarations and skips most KV-cache reads — zero training, zero auxiliary scorers. Across 15 long-context tasks: attention reads down 52.0% / 31.1% (Gemma-4-31B / Qwen-3.6-27B) for a 1.27pp / 2.75pp accuracy drop; roofline decode wall-time 0.71× / 0.77×.

- 中文精读页:`Declarative-Attention论文精读_HTML.html`(入口 `index.html` 按语言偏好自动跳转)
- **英文完整版:[`en.html`](en.html)** — 9 个章节全部翻译,20 张图表全内嵌
- 图片:`figs/` — 10 图 + 10 表,300 DPI 高清提取,中英文页共用
- 分类:高效推理 · 稀疏注意力 / KV Cache / 长上下文
- [在线阅读(中文)](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/declarative-attention/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/declarative-attention/en.html) · [论文原文](https://arxiv.org/abs/2609.02737)

返回[分类目录](../README.md) · [总索引](../../README.md)
