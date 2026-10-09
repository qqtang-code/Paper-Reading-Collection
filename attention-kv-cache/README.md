# 🎯 注意力与 KV Cache(Attention & KV Cache)

**这一层解决「一层里哪些 key 被看到」。** 六篇论文按同一条谱系排列——**可见键集合由谁决定**,决定权从外在结构逐步移向模型自身,直到被刻意放弃:

| 决策者 | 论文 | 机制 | 精读 | 英文版 |
|--------|------|------|------|--------|
| **位置 / 结构**(零学习、零选择开销) | CoWindow Attention(2026-10) | 共享近邻窗 + 前缀 sink 窗,长程距离按全局 KV-head 索引均分成互补区间;训练与推理同一规则 | [cowindow-attention/](cowindow-attention/) | [en.html(完整英译)](cowindow-attention/en.html) |
| **复用同模型已有的选择** | HySparse2(2026-09) | 两级 KV 共享:cross-decoder 全注意力层用 self-decoder 隐状态构造 K/V;稀疏层复用全注意力层的 KV cache 与选择索引,并把最近 128 token 强制入选 | [hysparse2/](hysparse2/) | [en.html(完整英译)](hysparse2/en.html) |
| **层内内容打分** | PISA(2026-09) | 键做 $O(\log N)$ 层金字塔,从最粗层逐层 Top-K 展开,块分数用子块摘要上的 LogSumExp | [pisa/](pisa/) | [en.html(英文速读)](pisa/en.html) |
| **层内学习的轻量路由** | Elastic Attention(2026-09) | 每层 0.27M 参数 Attention Router 按输入决定每个 KV 头走全注意力还是稀疏注意力 | [elastic-attention/](elastic-attention/) | [en.html(英文速读)](elastic-attention/en.html) |
| **模型自己声明** | Declarative Attention(2026-09) | 模型在思维链里用 `<global>` / `<focus>` / `<local>` 标签声明看哪里,引擎解析后跳过大部分 KV 读取 | [declarative-attention/](declarative-attention/) | [en.html(完整英译)](declarative-attention/en.html) |
| **不需要信号** | Random Attention(2026-09) | 保住 prompt + 每个 KV 头内均匀随机驱逐;证明选择信号几乎不贡献精度 | [random-attention/](random-attention/) | [en.html(英文速读)](random-attention/en.html) |

几个互补的读法:

- **CoWindow Attention 与 HySparse2 都在"不动选择质量"的前提下省钱**,但省钱的位置不同:前者消掉跨 head 重复的长程连接(位置定义、零开销),后者消掉跨层重复的 KV 构建与存储(复用全注意力层的既有选择)。两者都要求架构里保留足够多的注意力头 / 全注意力层作为"锚"。
- **PISA 与 Elastic Attention 都承认"选择"本身要花钱**,于是一个把选择复杂度压到 $O(\log N)$(金字塔),一个把选择器压到 0.27M 参数并只训它。
- **Declarative Attention 把决定权完全交给模型自述**(零训练零样本,代价是多花解码步);**Random Attention 是这条谱系的边界反例**——既然不选也行,前几种方法省下的到底是哪部分钱就需要重新算账。

模型层与系统层的效率工作(架构与缓存压缩、量化与内核、服务系统)见 [efficient-inference/](../efficient-inference/);度量能力边界的工作见 [benchmarks/](../benchmarks/)。

返回[总索引](../README.md)。
