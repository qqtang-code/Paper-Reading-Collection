# 📚 Paper Reading Collection · 论文精读合集

我的论文中文精读页合集。每篇论文一个**图文配合**的单文件 HTML 精读页:全部 Figure / Table 以 **300 DPI 高清 PNG** 内嵌在对应讲解段落中(等比缩放、不裁剪),配中文逐点解读,支持深色模式、点击看原图、KaTeX 公式渲染、打印友好。

> 🌐 **Bilingual · 中英双语**:每篇论文均提供**中文精读版 + 英文版**——四篇旗舰论文(Declarative Attention、DeepSeek-V4.1-Flash、CoWindow Attention、HySparse2)为**完整英译**(`en.html`),其余六篇为**英文速读版**(完整论证摘要 + 全部图表原文图注 + 英文导读)。门户页右上角一键切换 中/EN,首次访问跟随浏览器语言,切换后偏好会被记住。
>
> This collection ships a **full Chinese deep-read plus an English edition for every paper** — complete English editions for the four flagship papers (Declarative Attention, DeepSeek-V4.1-Flash, CoWindow Attention, HySparse2), and English quick-read editions (full digest of the argument + every figure with its original caption) for the rest. Toggle 中/EN from the portal topbar; the site follows your browser language on first visit and remembers your choice.

> 由 [paper-reading-html](https://github.com/qqtang-code/paper-reading-html) skill 制作 · 在线门户:[**qqtang-code.github.io/Paper-Reading-Collection**](https://qqtang-code.github.io/Paper-Reading-Collection/)

## 分类原则

分类只用一个轴:**这项工作在「哪一层」把钱省下来**,三层不重叠。

| 分类 | 一句话定义 | 判定问题 |
|------|-----------|---------|
| [🎯 attention-kv-cache](attention-kv-cache/) | **注意力层内部的可见键集合**——一层里哪些 key 被看到、以什么方式被决定 | 「谁来决定每个 head/层看到哪些 key?」 |
| [⚡ efficient-inference](efficient-inference/) | **模型权重与系统栈**——精度、内核、调度、部署形态 | 「同样的模型,怎么在更小的机器上更快跑起来?」 |
| [📏 benchmarks](benchmarks/) | **度量而非优化**——怎么测出模型真实的能力边界 | 「我们怎么知道它真的读懂了长上下文?」 |

第一类是这个合集里最厚的一叠(6 篇),它们按同一条谱系排列:**可见集合由谁决定**——从零学习的结构,一路走到「不需要信号」。

**结构/位置(①)** → **复用同模型已有的选择(②)** → **层内内容打分(③)** → **层内学习的轻量路由(④)** → **模型自己在思维链里声明(⑤)** → **不由信号决定(⑥)**

这条谱系越往后,决定权越靠近模型自身或越被刻意放弃:① 完全不需要选择,②③④ 用越来越贵的方式做选择(跨层复用 → 金字塔 Top-K → 层内路由器),⑤ 把选择权交给模型的自然语言输出,⑥ 则是把「选择信号到底值多少」当作被检验的对象。

## 论文总览

| # | 论文 | 分类 | 主题标签 | 语言 | 精读时间 | 图表 | 原文 |
|---|------|------|----------|------|----------|------|------|
| 1 | **CoWindow Attention** — Full Causal Coverage Is a Collective Property | [注意力与 KV Cache](attention-kv-cache/) | 稀疏注意力 · 结构化窗口 · GQA · 张量并行 | [中](attention-kv-cache/cowindow-attention/) · [EN 完整版](attention-kv-cache/cowindow-attention/en.html) | 2026-10 | 4 图 10 表 + 2 算法 | [arXiv:2609.32704](https://arxiv.org/abs/2609.32704) |
| 2 | **HySparse2** — Hybrid Sparse Attention with Two-Level KV Sharing | [注意力与 KV Cache](attention-kv-cache/) | 混合稀疏注意力 · 两级 KV 共享 · Agentic · MoE · 长上下文 | [中](attention-kv-cache/hysparse2/) · [EN 完整版](attention-kv-cache/hysparse2/en.html) | 2026-09 | 5 图 5 表 | [arXiv:2609.26368](https://arxiv.org/abs/2609.26368) |
| 3 | **PISA** — Block Sparse Attention with Log-Linear Complexity | [注意力与 KV Cache](attention-kv-cache/) | 块稀疏注意力 · 金字塔 Top-K · LogSumExp · O(N log N) | [中](attention-kv-cache/pisa/) · [EN 速读](attention-kv-cache/pisa/en.html) | 2026-09 | 3 图 7 表 | [arXiv:2609.31093](https://arxiv.org/abs/2609.31093) |
| 4 | **Elastic Attention** — Test-time Adaptive Sparsity Ratios for Efficient Transformers | [注意力与 KV Cache](attention-kv-cache/) | 混合注意力 · 测试时自适应 · Attention Router · 长上下文 | [中](attention-kv-cache/elastic-attention/) · [EN 速读](attention-kv-cache/elastic-attention/en.html) | 2026-09 | 17 图 14 表 | [OpenReview](https://openreview.net/forum?id=rLO2NTUHSW) · [代码](https://github.com/LCM-Lab/Elastic-Attention) |
| 5 | **Declarative Attention** — Language Models Can Control Their Own Attention | [注意力与 KV Cache](attention-kv-cache/) | 声明式稀疏注意力 · KV Cache · 长上下文 · CoT · vLLM | [中](attention-kv-cache/declarative-attention/) · [EN 完整版](attention-kv-cache/declarative-attention/en.html) | 2026-09 | 10 图 10 表 | [arXiv:2609.02737](https://arxiv.org/abs/2609.02737) |
| 6 | **Random Attention** — Rethinking KV Cache Eviction for Efficient Reasoning | [注意力与 KV Cache](attention-kv-cache/) | KV Cache 驱逐 · 推理模型 · 长思维链 · vLLM | [中](attention-kv-cache/random-attention/) · [EN 速读](attention-kv-cache/random-attention/en.html) | 2026-09 | 5 图 11 表 | [arXiv:2609.03430](https://arxiv.org/abs/2609.03430) |
| 7 | **DeepSeek-V4.1-Flash** — 552B 多模态 MoE 高效推理技术报告 | [高效推理](efficient-inference/) | KV Cache 压缩 · MoE · 多模态 · 长上下文 · FP4 | [中](efficient-inference/deepseek-v41-flash/) · [EN 完整版](efficient-inference/deepseek-v41-flash/en.html) | 2026-09 | 12 图 5 表 | [项目页](https://github.com/qqtang-code/DeepSeek-V4.1-Flash-Project-Page) |
| 8 | **ReSET** — Accurate Latency-Critical NVFP4 Reasoning via Step-Aware Temperature Scaling | [高效推理](efficient-inference/) | 量化 · NVFP4 · 低精度推理 · 温度缩放 | [中](efficient-inference/reset/) · [EN 速读](efficient-inference/reset/en.html) | 2026-08 | 8 图 16 表 | [arXiv:2606.13233](https://arxiv.org/abs/2606.13233) |
| 9 | **FreeToken** — 边缘原生的 MoE 服务系统(Bandwidth-Adaptive Execution) | [高效推理](efficient-inference/) | MoE · 边缘部署 · 服务系统 · 带宽自适应 | [中](efficient-inference/freetoken/) · [EN 速读](efficient-inference/freetoken/en.html) | 2026-09 | 5 图 1 表 | [arXiv:2608.16157](https://arxiv.org/abs/2608.16157) |
| 10 | **MMLongEmbed** — 长上下文场景下的多模态嵌入模型基准 | [评测基准](benchmarks/) | 多模态 · 嵌入模型 · 长上下文 · Benchmark | [中](benchmarks/mmlongembed/) · [EN 速读](benchmarks/mmlongembed/en.html) | 2026-08 | 6 图 16 表 | [GitHub](https://github.com/AmamiSora1228/MMLongEmbed) |

点击论文名直达精读页:**[① CoWindow Attention](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/cowindow-attention/)** · **[② HySparse2](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/hysparse2/)** · **[③ PISA](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/pisa/)** · **[④ Elastic Attention](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/elastic-attention/)** · **[⑤ Declarative Attention](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/declarative-attention/)** · **[⑥ Random Attention](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/random-attention/)** · **[⑦ DeepSeek-V4.1-Flash](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/deepseek-v41-flash/)** · **[⑧ ReSET](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/reset/)** · **[⑨ FreeToken](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/freetoken/)** · **[⑩ MMLongEmbed](https://qqtang-code.github.io/Paper-Reading-Collection/benchmarks/mmlongembed/)**

## 机制对照表

把「省什么、谁来决定、要不要训练」三件事横向排开,是这个合集里 10 篇论文最直接的分工图:

| # | 论文 | 省的是什么 | 机制 / 决策者 | 需要训练吗 | 代表数字 |
|---|------|-----------|--------------|-----------|---------|
| 1 | **CoWindow Attention** | 跨 head 重复的长程 query-key 连接 | **位置与全局 KV-head 索引**(零学习、零额外开销) | 从头训练(0.6B→14B scaling law) | 8K 覆盖消融 21.32 → 89.73;128K 前向 7.4× / 反向 8.6×;14B 训 32K 时 FLOPs −28.5% |
| 2 | **HySparse2** | 长上下文 prefill 里重复的 KV 构建与跨层重复存储 | **复用同模型全注意力层已有的选择与隐状态**(两级 KV 共享:KV Bridging + KV Reuse) | 从头预训练 + 后训练(80B-A3B,1M 上下文) | 1M 上下文 prefill FLOPs 降 2.92× / 5.02×;KV cache 2.69 GB;MRCR-v2 +11.30、RULER-v2 +19.81 |
| 3 | **PISA** | 「挑哪些块」本身的开销(块稀疏的选择仍是 O(N²/C)) | **键金字塔上的 LogSumExp 打分 + 逐层 Top-K**(每 query O(log N)) | 从头训练(4K 预训练 + 16K 继续预训练) | 256K 选块延迟比 BSA 快 9.95×;Recall@8 90.95% 对 85.91%;RULER 平均 62.80 对 54.99 |
| 4 | **Elastic Attention** | 混合注意力里被写死的 FA/SA 稀疏比 | **学习到的轻量路由器**(0.27M 参数,Gumbel-Softmax + STE) | 只训路由器,骨干完全冻结(8×A800,12 小时) | LongBench-E 平均分全部第一;加速 1.51×–3.28×;路由器延迟 0.196 ms |
| 5 | **Declarative Attention** | 解码时实际读取的 KV cache 量 | **模型自己**在思维链里声明(`<global>`/`<focus>`/`<local>`) | 零训练、零样本 | 注意力读取 −52.0% / −31.1%;精度 −1.27pp / −2.75pp;解码墙钟 0.71× / 0.77× |
| 6 | **Random Attention** | 被驱逐的那部分 KV 条目本身 | **不由任何信号决定**:保住 prompt + 每个 KV 头内均匀随机 | 零训练(免调参) | 4 模型 × 6 任务共 60 格中 31 格显著领先;vLLM 吞吐 +32–43% |
| 7 | **DeepSeek-V4.1-Flash** | 全栈:激活参数、KV cache 体积、量化位宽 | **架构 + 缓存 + 精度协同**:Causal Encoder-Decoder + CSA2 跨层 KV 复用 + FP4 + SWA Bounded Replay | 预训练技术报告(45T 多模态 token) | 全局 KV cache 每 token 890 字节;DeepSWE v1.1 74.2;Codeforces 3471 |
| 8 | **ReSET** | NVFP4 量化带来的精度损失 | **按解码步骤调整 softmax 温度** + CUDA-core 小 M 解码内核 | 零权重改动(免训练) | AIME-120 +2.6(Qwen3-32B 77.5,超 BF16 的 75.8);内核 1.57–2.49×;端到端 1.97× |
| 9 | **FreeToken** | 单机显存与内存带宽瓶颈 | **带宽自适应执行**(Bandwidth-Adaptive Execution) | 系统实现,非训练方法 | 8GB 笔记本跑 35B;游戏台式机跑 284B;单张工作站 GPU 跑 753B GLM-5.2 |
| 10 | **MMLongEmbed** | —(度量,不优化) | **基准构建**:4 个检索任务 / 8 个数据集 / 8,460 个查询 / 11 个模型 | 需要(训练与评测协议) | 现役模型依赖表面特征匹配"作弊";细粒度信息保持随上下文长度显著衰退 |

## 目录结构

```
Paper-Reading-Collection/
├── README.md                    ← 本文件(总索引)
├── index.html                   ← 在线门户页(GitHub Pages 首页,中英双语切换)
├── attention-kv-cache/          ← 分类一:注意力与 KV Cache(6 篇)
│   ├── cowindow-attention/      ← arXiv:2609.32704(4 图 10 表 + 2 算法)★ 最新
│   ├── hysparse2/               ← arXiv:2609.26368(5 图 5 表)
│   ├── pisa/                    ← arXiv:2609.31093(3 图 7 表 + 1 算法)
│   ├── elastic-attention/       ← OpenReview rLO2NTUHSW(17 图 14 表)
│   ├── declarative-attention/   ← arXiv:2609.02737(10 图 10 表)
│   └── random-attention/        ← arXiv:2609.03430(5 图 11 表)
├── efficient-inference/         ← 分类二:高效推理与部署(3 篇)
│   ├── deepseek-v41-flash/      ← DeepSeek-V4.1-Flash 技术报告(12 图 5 表)
│   ├── reset/                   ← arXiv:2606.13233(8 图 16 表)
│   └── freetoken/               ← arXiv:2608.16157(5 图 1 表)
└── benchmarks/                  ← 分类三:评测基准(1 篇)
    └── mmlongembed/             ← 多模态长上下文嵌入基准(6 图 16 表)

每个论文目录:中文精读页(index.html 或 <论文名>精读_HTML.html)
            + en.html(英文版:CoWA / HySparse2 / DA / DeepSeek-V4.1-Flash 为完整英译,其余为英文速读)
            + figs/(300 DPI 图表原图,中英文页共用)
```

> 说明:`efficient-inference/` 下仍留有 `declarative-attention/`、`random-attention/`、`elastic-attention/` 三个**旧链接重定向存根**(不是精读页),用于保住分类调整前的旧 URL,请勿当作重复内容。

## 分类与各篇速览

### 🎯 attention-kv-cache/ · 注意力与 KV Cache

一层里「哪些 key 被看到」由谁决定。六篇按决策权排列:结构 → 复用已有选择 → 层内内容打分 → 层内学习路由 → 模型自述 → 不需要信号。

**① CoWindow Attention(2026-10 · HKUST(GZ) × BAAI · arXiv:2609.32704)**
把「每个 head 都要重复看到完整因果历史」换成「**一组 KV head 合起来看到完整因果历史**」:所有 KV head 共享近邻窗与前缀 sink 窗,剩余长程距离均分成互补区间、每个 head 认领一段。不带路由器也不带索引器,训练前向/反向、prefill 与自回归解码共用一条位置定义的规则,并按全局 KV-head 编号分配以对齐张量并行。8K 关联召回上 100% 覆盖拿到 **89.73%**(满注意力 89.97%;同窗宽、只覆盖 12.5% 的重复窗版本仅 21.32%),说明收益来自「互补」而非「窗口更大」;128K、8×H100、TP=8 的算子级基准里前向快 **7.4×**、反向 **8.6×**、解码 **3.0×**,解码算子峰值显存低 **7.6×**;0.6B→14B 上困惑度与满注意力持平,14B 训 32K 时总训练 FLOPs 降 **28.5%**。→ [精读页](attention-kv-cache/cowindow-attention/) · [原文](https://arxiv.org/abs/2609.32704)

**② HySparse2(2026-09 · 小米 LLM-Core · arXiv:2609.26368)**
长程多轮的 agentic 推理让上下文被"输入"主导:模型自己产出的 action 很短,工具返回的观测却很长。HySparse2 把跨层 KV 共享做成两级——外层 **KV Bridging** 让 cross-decoder 的全注意力层用 self-decoder 全注意力层的**输入隐状态**经各自投影构造 K/V,内层 **KV Reuse** 让同一 block 内的稀疏层复用全注意力层的 KV cache 与选择索引;再把选择粒度从 64-token 块换成单 token,并**删掉稀疏层里独立的 SWA 分支**(改为把最近 128 token 强制塞进稀疏选择)。于是 cross-decoder 的每一份 KV cache 都能由 self-decoder 隐状态导出,**prefill 建完 cache 就能退出,不必跑 cross-decoder 的 24 层**。80B-A3B 上 1M 上下文的 prefill FLOPs 相对 HySparse/Hybrid SWA 降 **2.92× / 5.02×**,KV cache **2.69 GB**(对 6.72 / 12.09 GB),后训练检索 MRCR-v2 **+11.30**、RULER-v2 **+19.81** 个百分点。→ [精读页](attention-kv-cache/hysparse2/) · [原文](https://arxiv.org/abs/2609.26368)

**③ PISA(2026-09 · 上海交通大学 / 上海创智学院 / ByteDance Seed · arXiv:2609.31093)**
块稀疏注意力省下了注意力计算,却没省下"挑哪些块"的开销:传统做法要为每个 query 对全部 $N/C$ 个键块打分,选择阶段仍是 $O(N^2/C)$。PISA 把键按 $C\to2\to2\to\cdots$ 均值池化成 $O(\log N)$ 层的金字塔,选择时从最粗层往下逐层 Top-K——每层只给上一层幸存块的孩子打分,保留 Top-$K$ 再展开;块分数用子块摘要上的 LogSumExp(并给出 Jensen 不等式夹逼论证),而非均值平均。每个 query 的选路开销因此降到 $O(\log N)$,整段序列 $O(N\log N)$,解码 $O(\log N)$。256K 选块延迟比 BSA 快 **9.95×**,Recall@8 **90.95%** 对 BSA 的 85.91%,RULER 平均 **62.80** 对 54.99;16K 以内 BSA 更快,交叉点在 16K–32K 之间。→ [精读页](attention-kv-cache/pisa/) · [原文](https://arxiv.org/abs/2609.31093)

**④ Elastic Attention(2026-09 · 苏州大学 LCM Lab × 百度,ICML 2026 投稿)**
混合注意力(FA + SA)的 FA/SA 比例从静态超参数变成**输入自适应**:每层挂一个 **0.27M 参数**的轻量 Attention Router(Gumbel-Softmax + STE 训练),推理时按输入把每个 KV 头分配到 FA 或 SA——摘要/代码任务稀疏到 ~0.82、问答任务守住 0.63–0.68。**8×A800 训练 12 小时、骨干完全冻结**,Qwen3-4B/8B 与 Llama-3.1-8B 在 LongBench-E 平均分全部第一,RULER 外推 256K 优势最大;融合 kernel 让同层不同模式的头一次前向算完,加速 **1.51×–3.28×**,路由器延迟仅 **0.196 ms** 且与序列长度无关。→ [精读页](attention-kv-cache/elastic-attention/) · [原文](https://openreview.net/forum?id=rLO2NTUHSW) · [代码](https://github.com/LCM-Lab/Elastic-Attention)

**⑤ Declarative Attention(2026-09 · KAIST AI × Google DeepMind)**
让模型在思维链里用 `<global>` / `<focus>` / `<local>` 标签**声明自己要看哪里**,推理引擎像解析工具调用一样解析声明并跳过大部分 KV cache 读取——零训练、零样本。15 项长上下文任务上注意力读取降 **52.0% / 31.1%**(Gemma-4-31B / Qwen-3.6-27B),精度仅降 1.27pp / 2.75pp;roofline 估算解码墙钟降至 **0.71× / 0.77×**。→ [精读页](attention-kv-cache/declarative-attention/) · [原文](https://arxiv.org/abs/2609.02737)

**⑥ Random Attention(2026-09 · Salesforce AI Research + UIUC)**
KV cache 驱逐不需要打分:保住 prompt + 每个 KV 头内均匀随机驱逐、不打任何分,4 模型 × 6 推理任务追平最强基线(**60 格中 31 格显著领先**、仅 1 格落后),vLLM 部署吞吐再快 **32–43%**。机制账:prompt 是 cache 的脆弱部分;推理轨迹靠"文本复述 + 跨头复制"两层冗余自我保护——选择信号真正剩下的用武之地,是"只说一次、从不复述"的稀有事实。→ [精读页](attention-kv-cache/random-attention/) · [原文](https://arxiv.org/abs/2609.03430)

### ⚡ efficient-inference/ · 高效推理与部署

在模型权重与系统栈上省算力与显存:架构与缓存压缩、低精度量化与内核、服务系统。三篇按「模型 → 权重 → 系统」排列:

**⑦ DeepSeek-V4.1-Flash(2026-09 · DeepSeek 技术报告)**
552B 多模态 MoE:Causal Encoder-Decoder 让 prefill 只激活 8B(decode 16B);CSA2 跨层 KV 复用 + FP4(MXFP4)量化把全局 KV Cache 压到**每 token 890 字节**(V4-Flash 的 1/4、V1 的 1/437),SWA Bounded Replay 再把持久缓存压到上代的 1/8;配 196B 条件记忆 Engram 与 45T 多模态 token 预训练,性能反超更大的 V4-Flash——DeepSWE v1.1 **74.2**、Terminal-Bench 2.1 **90.6**、Codeforces **3471**。→ [精读页](efficient-inference/deepseek-v41-flash/) · [项目页](https://github.com/qqtang-code/DeepSeek-V4.1-Flash-Project-Page)

**⑧ ReSET(2026-08)**
NVFP4 低精度推理在延迟敏感(交互式)场景下的精度救星:**步骤感知温度缩放**(Step-Aware Temperature Scaling)按解码步骤动态调整 softmax 温度,配合 CUDA-core 小 M 解码内核,在不牺牲延迟的前提下恢复量化精度。→ [精读页](efficient-inference/reset/) · [原文](https://arxiv.org/abs/2606.13233)

**⑨ FreeToken(2026-09)**
把个人电脑变成统一的弹性推理平台:带宽自适应执行(Bandwidth-Adaptive Execution)让 **8GB 显存笔记本跑 35B 模型**、游戏台式机跑 284B、单张工作站 GPU 跑 **753B GLM-5.2**,且快到能支撑真实 agent 负载。→ [精读页](efficient-inference/freetoken/) · [原文](https://arxiv.org/abs/2608.16157)

### 📏 benchmarks/ · 评测基准

度量模型真实能力的研究。

**⑩ MMLongEmbed(2026-08)**
首个专门评测**多模态嵌入模型(MEM)长上下文能力**的基准:4 个检索任务、8 个数据集、8,460 个查询、11 个模型。核心发现:现役模型依赖表面特征匹配"作弊",细粒度信息保持随上下文长度显著衰退——"窗口大"不等于"读得懂"。→ [精读页](benchmarks/mmlongembed/) · [原文](https://github.com/AmamiSora1228/MMLongEmbed)

## 如何阅读

- **在线**:打开 [GitHub Pages 门户](https://qqtang-code.github.io/Paper-Reading-Collection/),或直接访问上表任一精读页链接;
- **本地**:`git clone` 后用浏览器打开任意论文目录下的 `index.html`(图片为相对路径 `figs/`,无需联网;公式渲染需联网加载 KaTeX CDN);
- **语言切换**:门户页与每个精读页顶栏都有 **中/EN** 按钮——中文页点击 `EN` 跳转同目录 `en.html`,英文页点击 `中文` 跳回中文精读页;首次访问跟随浏览器语言,偏好保存在浏览器本地(localStorage `pr-lang`)。

每个精读页的章节结构大致为:**速览 → 背景 → 方法 → 系统实现 → 实验 → 规模化 → 讨论/点评 → 术语速查**,图表内嵌在对应讲解段落里,而非单独的图库。英文速读版结构对应:**Overview → Background → Observations/Challenges → Method → Kernel/System → Results → Commentary → Glossary**,包含全部图表与原文图注。

## 如何新增一篇精读

1. 用 [paper-reading-html](https://github.com/qqtang-code/paper-reading-html) skill 生成精读页(`index.html` + `figs/`),并按 skill 的溯源规范补齐:速览章「读数约定」、上游方法的行内引用、点评章「技术来源一览」与「未披露、值得补测」清单、图注原文页码(`scripts/add_pagerefs.py` 从 `crops.json` 批量注入);
2. 按上面的分类原则放入对应分类目录(没有合适的分类就新建一个),并在该目录 `README.md` 里登记,同时写明它在「决策者」谱系上的位置;
3. 在本 README 的**总览表**、**机制对照表**、**目录结构树**与**分类速览**四处登记,并同步门户页 `index.html`;编号 = 分类顺序,新论文插入所属分类的正确位置并顺延后续编号;
4. push 到 `main`,GitHub Pages 自动更新。

## 说明

- 各精读页此前以独立仓库发布(`ReSET-Project-Page`、`MMLongEmbed-PaperReading-Page`、`FreeToken-Project-Page`、`Declarative-Attention-Project-Page`、`DeepSeek-V4.1-Flash-Project-Page`、`Elastic-Attention-Project-Page`、`CoWindow-Attention-Project-Page`),现已整合至本仓库;旧仓库与其 Pages 链接暂时保留,后续可归档。
- 分类调整历史:注意力层的工作(Declarative / Random / Elastic Attention)已从 `efficient-inference/` 移至 `attention-kv-cache/`,旧链接留有自动重定向页面。最新一次规整把分类依据统一为「**省在哪一层**」,注意力类内部改用「**可见键集合由谁决定**」这条谱系排序,**编号改为按分类顺序**(注意力与 KV Cache ①–⑥、高效推理与部署 ⑦–⑨、评测基准 ⑩),并新增「机制对照表」;目录名与 URL 均未改动,旧链接照常可访问。
- 精读页中的解读文字为编者观点,关键数字均与论文原文核对;图片以 300 DPI 摘自原文,版权归原作者所有,仅供学习研究。