# DoSA — Dots Sparse Attention

**DoSA: Dots Sparse Attention**(arXiv:2610.13990 · Dots Studio, Xiaohongshu Inc. 小红书)

> 稀疏注意力只访问少数 key,但「找出这些 key」这一步,在 DSA 里仍要对每个可见 key 打一遍**全部 indexer 头的分**。DoSA 的核心观察是:**Top-K 选择只需要「能否排除某个候选」的充分证据,而不需要它的完整分数**——选一个至少有 K 个 key 的种子集合给出阈值**下界** $\tau$,再为每个候选构造一个严格不低于其真实分数的**上界** $U_i$,两者一旦分离($U_i < \tau$)就完成一次**认证式拒绝**。难点在于打分函数是「ReLU 在内 + 头权重有正有负」:丢掉正头会低估分数,丢掉负头会让上界变松。DoSA 的做法是正头**投影到已算过的头上**、负头**按激活多数聚合成一行**,最终选出的 token 与全量打分完全一致(**无损 / lossless**)。
>
> Sparse attention visits few keys, yet *finding* them still scores every visible key with every indexer head. DoSA's observation: **Top-K selection needs sufficient evidence to reject a candidate, not that candidate's full score.** A seed set of at least K keys supplies a lower bound $\tau$ on the true threshold; a per-key upper bound $U_i$ is then built for every candidate, and once they separate ($U_i < \tau$) the key is **certifiably rejected**. The hard part is the signed ReLU scorer — dropping positive heads underestimates, dropping negative heads loosens the bound — so positive heads are **projected onto already-computed heads** and negative heads **aggregated into a single row by activation majority**. The selected token set is identical to full scoring, hence **lossless**.

- **中文精读**:[DoSA论文精读_HTML.html](DoSA论文精读_HTML.html) · [在线](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/dosa/)
- **English full mirror**:[en.html](en.html) · [online](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/dosa/en.html)
- **独立项目页**:<https://qqtang-code.github.io/DoSA-Project-Page/>
- **分类**:注意力与 KV Cache · 决策者 = **分数的上界证书**(不改变谁被看到,只让「筛选」本身变成条件计算)
- **图表**:`figs/` 共 12 张(论文共 12 个 Figure,正文与附录**无编号 Table**),300 DPI 从原文提取,中英页共用
- **原文**:<https://arxiv.org/abs/2610.13990> · **代码**:<https://github.com/llm-sys/flash-indexer>

论文速览:在 GLM-5.2(32 头)与 DeepSeek-V3.2(64 头)上,Top-K = 2048,21 个产生 indexer 的层。Indexer 占 prefill GPU 时间在约 1M token 时达 **73.0% / 90.8%**,而 FLOPs 占比只有 47.4% / 83.2%——时间比算术更贵,这是全文的设计前提。完整 Indexer 加速在 **60/60** 个微基准配置中最快:相对 SGLang **1.12×–2.74×**、相对 LiteTopK **1.17×–1.69×**,512K 以上每个配置都超过 2×;1M 上下文 TTFT 加速 **1.86× / 1.94×**;剪枝率 **97.2%–97.5%**,且三个语言域曲线几乎重合(第 1 层最低,89%–93%)——说明这是**分数几何**的性质而非数据性质。消融显示 screening 与 sparse writeback 单独省 37.4% / 23.4%、合起来省 47.3%;证书组件里**负头聚合是命门**:去掉它候选存活率从 2.65% 飙到 **95.06%**、延迟变为 **9.507×**。

本页另含四处编者整理与追问:**配置走查**(把 $r=14,16,20$ 三条路径、两个 FP8 辅助行、$m < 1-(r+d_a)/H$ 的省算门槛落到具体数字)、**技术来源一览**(检索侧的 MaxScore / WAND / Block-Max WAND 与 DSA 的接合点)、**6 条「未披露、值得补测」清单**(候选缓冲的显存账本与恢复触发率、p99 尾延迟、激活统计的采集成本与漂移、$r$ 与 $d_a$ 的联合调优表、独立复现、与近似方法的正面对比),以及对附录 D.4「候选存储容量修复 +9.94 GiB、且未重跑全矩阵」这一披露的解读——它与附录 C.3 的理论警告是同一个正确性问题在实测中的现身。

返回[分类目录](../README.md) · [总索引](../../README.md)