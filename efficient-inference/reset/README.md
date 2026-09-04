# ReSET · 论文精读

**ReSET: Accurate Latency-Critical NVFP4 Reasoning via Step-Aware Temperature Scaling**(arXiv:2606.13233)

> NVFP4 低精度推理在延迟敏感(交互式)场景下的精度救星:步骤感知温度缩放按解码步骤动态调整 softmax 温度,在不牺牲延迟的前提下恢复量化精度。
>
> ReSET rescues the accuracy of latency-critical NVFP4 reasoning with zero weight changes: a step-aware temperature policy plus a CUDA-core small-M decode kernel. AIME-120 +2.6 avg over the NVFP4 baseline (Qwen3-32B 77.5, beating BF16's 75.8); 1.57–2.49× kernel speedups at M=1; 1.97× end-to-end over BF16 with the ~1.5% sampler overhead included.

- 中文精读页:`index.html`(8 图 + 16 张数据表)
- 英文速读版:[`en.html`](en.html) — 完整论证摘要 + 全部 8 图原文图注 + 关键数据表
- 图片:`figs/` — 300 DPI 高清提取,中英文页共用;16 张表格按原文数据重建(中文页)
- 分类:高效推理 · 量化 / NVFP4 / 低精度推理 / 温度缩放
- [在线阅读(中文)](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/reset/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/reset/en.html) · [论文原文](https://arxiv.org/abs/2606.13233)

返回[分类目录](../README.md) · [总索引](../../README.md)
