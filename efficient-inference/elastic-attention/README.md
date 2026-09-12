# Elastic Attention — Test-time Adaptive Sparsity Ratios for Efficient Transformers

混合注意力(全注意力 FA + 稀疏注意力 SA)的 FA/SA 比例从静态超参数变为**输入自适应**:每层挂一个 0.27M 参数的轻量 Attention Router,推理时按输入把每个 KV 头分配到 FA 或 SA。

- **中文精读**:[Elastic-Attention论文精读_HTML.html](Elastic-Attention论文精读_HTML.html) · [在线](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/elastic-attention/)
- **English quick-read**:[en.html](en.html) · [online](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/elastic-attention/en.html)
- **图表**:`figs/` 共 32 张(17 Figure + 14 Table + Algorithm 1),300 DPI 从原文提取,中英页共用
- **原文**:<https://openreview.net/forum?id=rLO2NTUHSW>(ICML 2026 投稿) · **代码**:<https://github.com/LCM-Lab/Elastic-Attention>

论文速览:任务天然分成稀疏鲁棒(摘要/代码)与稀疏敏感(QA)两类;8×A800、12 小时、骨干冻结训练,LongBench-E 上 Qwen3-4B/8B 与 Llama-3.1-8B 平均分全部第一;RULER 外推 256K 优势最大,路由器延迟 0.196 ms 且与长度无关。
