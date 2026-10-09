# CoWindow Attention — Full Causal Coverage Is a Collective Property

**CoWindow Attention(CoWA)**(arXiv:2609.32704 · HKUST(GZ) × BAAI × Université Paris Cité)

> 把「每个 head 都要重复看到完整因果历史」换成「一组 KV head 合起来看到完整因果历史」:所有 KV head 共享近邻窗与前缀 sink 窗,剩余长程距离被均分成互补区间、每个 KV head 认领一段。不引入路由器或索引器,训练前向/反向、prefill 与自回归解码共用同一条位置定义的窗口规则,并按<b>全局 KV-head 编号</b>分配窗口以对齐张量并行的 KV-head 切分。
>
> CoWA replaces "every head must repeat the full causal history" with "a group of KV heads collectively sees the full causal history": all KV heads share a near window and a prefix-sink window, while the remaining long-range distances are cut into complementary intervals, one per KV head. No router, no indexer; one position-defined window rule covers the training forward/backward passes, prefill and autoregressive decoding, with windows assigned by **global** KV-head index so they align with tensor-parallel KV-head sharding.

- **中文精读**:[CoWindow-Attention论文精读_HTML.html](CoWindow-Attention论文精读_HTML.html) · [在线](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/cowindow-attention/)
- **English full mirror**:[en.html](en.html) · [online](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/cowindow-attention/en.html)
- **分类**:注意力与 KV Cache · 决策者 = 位置与全局 KV-head 索引(零学习)/ 结构化稀疏 / 张量并行
- **图表**:`figs/` 共 16 张(4 Figure + 10 Table + 2 Algorithm),300 DPI 从原文提取,中英页共用
- **原文**:<https://arxiv.org/abs/2609.32704> · **代码**:开源名 `flash-sparse-attention`(论文标注,未给 URL)

论文速览:8K 关联召回上 100% 集体覆盖拿到 **89.73%**(满注意力 89.97%,同窗宽下只覆盖 12.5% 的重复窗版本仅 21.32%);128K、8×H100、TP=8 的算子级基准里相对满注意力前向快 **7.4×**、反向 **8.6×**、解码 **3.0×**,解码算子峰值显存低 **7.6×**;0.6B→14B 的 scaling law 上困惑度持平,14B 训 32K 时总训练 FLOPs 降 **28.5%**(4K 预训练阶段降 3.1%)。收益来自「互补分配」而非「窗口更大」,且选择开销为 $O(1)$ per QO block、辅助状态 $O(H_k)$ 与序列长度无关。

本页另含三处编者整理:**配置走查**(论文披露的全部 per-QO-head 预算都恰好等于 $1024+(N_k-1024)/8$,即「共享窗 1024 + 8 段等宽 + 满覆盖」)、**张量并行分工推算**($H_k=TP=8$ 时 8 段长程窗恰好一 rank 一段),以及 **6 条「未披露、值得补测」清单**。

返回[分类目录](../README.md) · [总索引](../../README.md)