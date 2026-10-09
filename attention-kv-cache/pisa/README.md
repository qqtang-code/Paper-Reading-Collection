# PISA · 论文精读

**Block Sparse Attention with Log-Linear Complexity**(arXiv:2609.31093,Bohao Tang, Zhen Qin, Yuqi Pan, Zheng Li, Pengfei Liu · 上海交通大学 / 上海创智学院 / ByteDance Seed)

> 块稀疏注意力省下了注意力计算,却没省下"挑哪些块"的开销:传统做法要为每个 query 对全部 $N/C$ 个键块打分,选择阶段仍是 $O(N^2/C)$。PISA 把键按 $C\to2\to2\to\cdots$ 均值池化成 $O(\log N)$ 层的金字塔,选择时从最粗层往下逐层 Top-K——每层只给上一层幸存块的孩子打分,保留 Top-$K$ 再展开;块分数用子块摘要上的 LogSumExp,而非均值平均。每个 query 的选路开销因此降到 $O(\log N)$,整段序列 $O(N\log N)$,解码 $O(\log N)$。
>
> Block-sparse attention saves the attention computation but not the cost of choosing the blocks: the conventional recipe scores every query against all $N/C$ key blocks, leaving selection at $O(N^2/C)$. PISA mean-pools keys into an $O(\log N)$-level pyramid and selects coarse-to-fine, scoring only the children of the previous level's survivors and ranking them by a LogSumExp over child summaries rather than an average of means. Routing drops to $O(\log N)$ per query, $O(N\log N)$ over the sequence, and $O(\log N)$ per decode step.

- 中文精读页:`index.html`
- 英文速读版:[`en.html`](en.html) — 完整速览 + 全部 3 图 7 表 1 算法框图的原文图注与英文解读 + 点评
- 图片:`figs/` — 3 图 + 7 表 + 1 算法框图,300 DPI 高清提取,中英文页共用
- 分类:注意力与 KV Cache · 决策者 = 层内内容打分(键金字塔 Top-K)/ LogSumExp / O(N log N)
- [在线阅读(中文)](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/pisa/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/pisa/en.html) · [论文原文](https://arxiv.org/abs/2609.31093)

## 本页比论文多做的三处推算

1. **配置落到层号**:把 $C=64$、$g=2$ 与论文的两套训练配置代入,4K 预训练($K=8$)时塔高 $L=7$,最上面 4 层因候选数不超过 $K$ 而完全免费,真正打分的只有 2 个中间层(各 16 个候选)加叶层 1024 个原始键,最终 512 个键参与注意力;16K 继续预训练($K=32$)时塔高 $L=9$,最上面 6 层免费,叶层对 4096 个原始键打分、保留 2048 个键。
2. **交换点的量级估算**:令 BSA 每 query 扫描的块摘要数 $N/C$ 等于 PISA 叶层打分的原始键数 $gKC$,得 $N=gKC^2\approx 65\text{K}$;论文实测交叉点落在 16K 与 32K 之间,同量级但不等——该式只比较点积次数,未计入 BSA 内核常数因子更低与 PISA 中间层/融合内核的额外开销。
3. **16K 列的四家族平均**:对 Table 3 的 16K 一列取四家族算术平均得 PISA 30.86、PISA-2 32.56、PISA-1 28.09、BSA 25.90、NSA 39.99、Full Attention 53.50——PISA 家族高于 BSA 但不是该列最强者。

以上均以「整理 / 推算」显式标注,与论文口径区分。

## 读这张表时容易踩的两个坑

- **论文的加粗位置与直觉不符**:Table 2 的"最佳稀疏 loss"加粗在 **HiLS** 行(2.5596 / 2.3084 / 2.2047),不是 PISA;Table 3 的 RULER 最佳稀疏总平均是 **PISA-2 的 62.92**,略高于完整版 PISA 的 62.80。论文正文的措辞与加粗口径一致,没有越界。
- **两处 containment 均值不可直接比较**:Table 2 覆盖 6 个任务(52.14),Table 6 只覆盖 3 个(SWDE / SQuAD / FDA,66.40)。

另外,Figure 3 与 Table 4 的"9.95×"是**选块阶段**的加速,明确排除被选中块上的稀疏注意力计算;端到端倍数论文未测量。

返回[分类目录](../README.md) · [总索引](../../README.md)