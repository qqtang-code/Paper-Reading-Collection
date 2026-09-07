# 📚 Paper Reading Collection · 论文精读合集

我的论文中文精读页合集。每篇论文一个**图文配合**的单文件 HTML 精读页:全部 Figure / Table 以 **300 DPI 高清 PNG** 内嵌在对应讲解段落中(等比缩放、不裁剪),配中文逐点解读,支持深色模式、点击看原图、KaTeX 公式渲染、打印友好。

> 🌐 **Bilingual · 中英双语**:每篇论文均提供**中文精读版 + 英文版**——旗舰论文 Declarative Attention 为**完整英译**(`en.html`),其余四篇为**英文速读版**(完整论证摘要 + 全部图表原文图注 + 英文导读)。门户页右上角一键切换 中/EN,首次访问跟随浏览器语言,切换后偏好会被记住。
>
> This collection ships a **full Chinese deep-read plus an English edition for every paper** — a complete English translation for the flagship paper (Declarative Attention), and English quick-read editions (full digest of the argument + every figure with its original caption) for the rest. Toggle 中/EN from the portal topbar; the site follows your browser language on first visit and remembers your choice.

> 由 [paper-reading-html](https://github.com/qqtang-code/paper-reading-html) skill 制作 · 在线门户:[**qqtang-code.github.io/Paper-Reading-Collection**](https://qqtang-code.github.io/Paper-Reading-Collection/)

## 论文总览

| # | 论文 | 分类 | 主题标签 | 语言 | 精读时间 | 图表 | 原文 |
|---|------|------|----------|------|----------|------|------|
| 1 | **Declarative Attention** — Language Models Can Control Their Own Attention | [高效推理](efficient-inference/) | 稀疏注意力 · KV Cache · 长上下文 · CoT · vLLM | [中](efficient-inference/declarative-attention/) · [EN 完整版](efficient-inference/declarative-attention/en.html) | 2026-09 | 10 图 10 表 | [arXiv:2609.02737](https://arxiv.org/abs/2609.02737) |
| 2 | **FreeToken** — 边缘原生的 MoE 服务系统(Bandwidth-Adaptive Execution) | [高效推理](efficient-inference/) | MoE · 边缘部署 · 服务系统 · 带宽自适应 | [中](efficient-inference/freetoken/) · [EN 速读](efficient-inference/freetoken/en.html) | 2026-09 | 5 图 1 表 | [arXiv:2608.16157](https://arxiv.org/abs/2608.16157) |
| 3 | **ReSET** — Accurate Latency-Critical NVFP4 Reasoning via Step-Aware Temperature Scaling | [高效推理](efficient-inference/) | 量化 · NVFP4 · 低精度推理 · 温度缩放 | [中](efficient-inference/reset/) · [EN 速读](efficient-inference/reset/en.html) | 2026-08 | 8 图 16 表 | [arXiv:2606.13233](https://arxiv.org/abs/2606.13233) |
| 4 | **Random Attention** — Rethinking KV Cache Eviction for Efficient Reasoning | [高效推理](efficient-inference/) | KV Cache 驱逐 · 推理模型 · 长思维链 · vLLM | [中](efficient-inference/random-attention/) · [EN 速读](efficient-inference/random-attention/en.html) | 2026-09 | 5 图 11 表 | [arXiv:2609.03430](https://arxiv.org/abs/2609.03430) |
| 5 | **MMLongEmbed** — 长上下文场景下的多模态嵌入模型基准 | [评测基准](benchmarks/) | 多模态 · 嵌入模型 · 长上下文 · Benchmark | [中](benchmarks/mmlongembed/) · [EN 速读](benchmarks/mmlongembed/en.html) | 2026-08 | 6 图 16 表 | [GitHub](https://github.com/AmamiSora1228/MMLongEmbed) |

点击论文名直达精读页:**[① Declarative Attention](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/declarative-attention/)** · **[② FreeToken](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/freetoken/)** · **[③ ReSET](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/reset/)** · **[④ Random Attention](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/random-attention/)** · **[⑤ MMLongEmbed](https://qqtang-code.github.io/Paper-Reading-Collection/benchmarks/mmlongembed/)**

## 目录结构

```
Paper-Reading-Collection/
├── README.md                    ← 本文件(总索引)
├── index.html                   ← 在线门户页(GitHub Pages 首页,中英双语切换)
├── efficient-inference/         ← 分类一:高效推理与部署
│   ├── declarative-attention/   ← arXiv:2609.02737(10 图 10 表)
│   ├── freetoken/               ← arXiv:2608.16157(5 图 1 表)
│   ├── reset/                   ← arXiv:2606.13233(8 图 16 表)
│   └── random-attention/        ← arXiv:2609.03430(5 图 11 表)
└── benchmarks/                  ← 分类二:评测基准
    └── mmlongembed/             ← 多模态长上下文嵌入基准(6 图 16 表)

每个论文目录:中文精读页(index.html 或 <论文名>精读_HTML.html)
            + en.html(英文版:DA 为完整英译,其余为英文速读)
            + figs/(300 DPI 图表原图,中英文页共用)
```

## 分类与各篇速览

### ⚡ efficient-inference/ · 高效推理与部署

让 LLM 推理更快、更省、能部署到更小硬件的研究。

**① Declarative Attention(2026-09 · KAIST AI × Google DeepMind)**
让模型在思维链里用 `<global>` / `<focus>` / `<local>` 标签**声明自己要看哪里**,推理引擎像解析工具调用一样解析声明并跳过大部分 KV cache 读取——零训练、零样本。15 项长上下文任务上注意力读取降 **52.0% / 31.1%**(Gemma-4-31B / Qwen-3.6-27B),精度仅降 1.27pp / 2.75pp;roofline 估算解码墙钟降至 **0.71× / 0.77×**。→ [精读页](efficient-inference/declarative-attention/) · [原文](https://arxiv.org/abs/2609.02737)

**② FreeToken(2026-09)**
把个人电脑变成统一的弹性推理平台:带宽自适应执行(Bandwidth-Adaptive Execution)让 **8GB 显存笔记本跑 35B 模型**、游戏台式机跑 284B、单张工作站 GPU 跑 **753B GLM-5.2**,且快到能支撑真实 agent 负载。→ [精读页](efficient-inference/freetoken/) · [原文](https://arxiv.org/abs/2608.16157)

**③ ReSET(2026-08)**
NVFP4 低精度推理在延迟敏感(交互式)场景下的精度救星:**步骤感知温度缩放**(Step-Aware Temperature Scaling)按解码步骤动态调整 softmax 温度,在不牺牲延迟的前提下恢复量化精度。→ [精读页](efficient-inference/reset/) · [原文](https://arxiv.org/abs/2606.13233)

**④ Random Attention(2026-09 · Salesforce AI Research + UIUC)**
KV cache 驱逐不需要打分:保住 prompt + 每个 KV 头内均匀随机驱逐、不打任何分,4 模型 × 6 推理任务追平最强基线(**60 格中 31 格显著领先**、仅 1 格落后),vLLM 部署吞吐再快 **32–43%**。机制账:prompt 是 cache 的脆弱部分;推理轨迹靠"文本复述 + 跨头复制"两层冗余自我保护——选择信号真正剩下的用武之地,是"只说一次、从不复述"的稀有事实。→ [精读页](efficient-inference/random-attention/) · [原文](https://arxiv.org/abs/2609.03430)

### 📏 benchmarks/ · 评测基准

度量模型真实能力的研究。

**⑤ MMLongEmbed(2026-08)**
首个专门评测**多模态嵌入模型(MEM)长上下文能力**的基准:4 个检索任务、8 个数据集、8,460 个查询、11 个模型。核心发现:现役模型依赖表面特征匹配"作弊",细粒度信息保持随上下文长度显著衰退——"窗口大"不等于"读得懂"。→ [精读页](benchmarks/mmlongembed/) · [原文](https://github.com/AmamiSora1228/MMLongEmbed)

## 如何阅读

- **在线**:打开 [GitHub Pages 门户](https://qqtang-code.github.io/Paper-Reading-Collection/),或直接访问上表任一精读页链接;
- **本地**:`git clone` 后用浏览器打开任意论文目录下的 `index.html`(图片为相对路径 `figs/`,无需联网;公式渲染需联网加载 KaTeX CDN);
- **语言切换**:门户页与每个精读页顶栏都有 **中/EN** 按钮——中文页点击 `EN` 跳转同目录 `en.html`,英文页点击 `中文` 跳回中文精读页;首次访问跟随浏览器语言,偏好保存在浏览器本地(localStorage `pr-lang`)。

每个精读页的章节结构大致为:**速览 → 背景 → 方法 → 系统实现 → 实验 → 规模化 → 讨论/点评 → 术语速查**,图表内嵌在对应讲解段落里,而非单独的图库。英文速读版结构对应:**Overview → Background → Observations/Challenges → Method → Kernel/System → Results → Commentary → Glossary**,包含全部图表与原文图注。

## 如何新增一篇精读

1. 用 [paper-reading-html](https://github.com/qqtang-code/paper-reading-html) skill 生成精读页(`index.html` + `figs/`);
2. 放入对应分类目录(没有合适的分类就新建一个);
3. 在本 README 的总览表格与分类速览里登记一行;
4. push 到 `main`,GitHub Pages 自动更新。

## 说明

- 各精读页此前以独立仓库发布(`ReSET-Project-Page`、`MMLongEmbed-PaperReading-Page`、`FreeToken-Project-Page`、`Declarative-Attention-Project-Page`),现已整合至本仓库;旧仓库与其 Pages 链接暂时保留,后续可归档。
- 精读页中的解读文字为编者观点,关键数字均与论文原文核对;图片以 300 DPI 摘自原文,版权归原作者所有,仅供学习研究。
