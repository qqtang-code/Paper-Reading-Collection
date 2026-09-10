# DeepSeek-V4.1-Flash · 论文精读

**Pushing the Limits of KV Cache Compression**(DeepSeek-AI 技术报告,2026-09)

> 552B 骨干参数的多模态 MoE,支持 1M token 上下文:CED(Causal Encoder-Decoder)让 prefill 每 token 只激活 **8B** 参数、解码激活 16B;CSA2 跨层共享主 KV / 索引器 K 并复用 Top-K 索引,配合 FP4(MXFP4)主 KV 缓存,把全局 KV 压到 **890 字节/token**(≈ V4-Flash 的 1/4、V1 的 1/437);SWA Bounded Replay 只回放最近 128 个 token 近似重建 SWA 状态,持久 KV 缓存再降到上代的 **1/8**。45T 多模态 token 预训练 + "零算法创新"的数据管线后训练:DeepSWE v1.1 **74.2**、Terminal-Bench 2.1 **90.6**、Codeforces **3471**,对齐闭源前沿。
>
> A 552B-backbone multimodal MoE with a 1M-token context: CED activates only **8B** params per prefill token (16B at decode); CSA2 cross-layer KV/index sharing plus FP4 (MXFP4) caching squeeze the global KV cache to **890 bytes/token** (≈1/4 of V4-Flash, 1/437 of V1); SWA Bounded Replay approximately rebuilds SWA states by replaying only the last 128 tokens, cutting the persistent cache to **1/8**. After 45T multimodal pre-training tokens and a deliberately algorithm-free, data-pipeline-driven post-training: DeepSWE v1.1 **74.2**, Terminal-Bench 2.1 **90.6**, Codeforces **3471** — matching the closed-source frontier.

- 中文精读页:`DeepSeek-V4.1-Flash论文精读_HTML.html`(入口 `index.html` 按语言偏好自动跳转)
- **英文完整版:[`en.html`](en.html)** — 10 个章节全部翻译,18 张图表(12 图 + 5 表 + 1 算法)全内嵌
- 图片:`figs/` — 12 图 + 5 表 + Algorithm 1,300 DPI 高清提取,中英文页共用
- 分类:高效推理 · KV Cache 压缩 / MoE / 多模态 / 长上下文
- [在线阅读(中文)](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/deepseek-v41-flash/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/deepseek-v41-flash/en.html) · [原文模型页](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

返回[分类目录](../README.md) · [总索引](../../README.md)
