# LongHarness Bench · 论文精读

**LongHarness Bench: 压力测试长上下文推理的语言模型 harness**（[arXiv:2609.38137](https://arxiv.org/abs/2609.38137) · [论文项目页](https://stringnlplab.github.io/longharness/)）

> 第一个把 **LM harness 本身**当作被评测对象的基准：四个信息密集、检索随推理步骤变化的任务，同时测准确率**与**成本。结论很硬：五个模型 × 五种配置里最好的只到 **68%** 宏平均；同样的准确率成本可以差 **12.4 倍**；而「多推理」既不必要也不充分——RLM 在 Outlier Memo Detection 上花 $7.23 拿到 92%，mini-swe-agent 只花 $0.583 就拿到 100%。
>
> The first benchmark that evaluates **LM harnesses themselves** rather than only the underlying model: four information-dense tasks whose retrieval demands shift as reasoning unfolds, measuring accuracy **and** cost together. The headline results are blunt: the best of 25 model–harness configurations reaches only **68%** macro accuracy; equally accurate systems can differ **12.4×** in cost; and more inference is neither necessary nor sufficient.

- 中文精读页：[`index.html`](index.html)
- 英文完整版：[`en.html`](en.html) — 10 节 1:1 完整英译 + 全部图表
- 图片：`figs/` — 4 图 + 6 表，300 DPI 高清提取，中英文页共用
- 分类：评测基准 · 长上下文 / Agent Harness / 准确率–成本权衡
- [在线阅读（中文）](https://qqtang-code.github.io/Paper-Reading-Collection/benchmarks/longharness/) · [Read in English](https://qqtang-code.github.io/Paper-Reading-Collection/benchmarks/longharness/en.html) · [论文原文](https://arxiv.org/abs/2609.38137)

## 它要解决的问题

长上下文系统越来越不是「一个模型」，而是「模型 + harness」——harness 负责管理上下文、工具与交互序列。但现有长上下文评测有两个缺口：

1. **准确率已饱和**：强模型 × 强 harness 在 LongBench-v2、OOLONG-Synth 上挤成一团（本页 Table 3：LongBench-v2 全部落在 60–68%），分不出 harness 的差异；
2. **只看准确率看不见成本**：同样准确率的两套系统，算力消耗可以差一个数量级。

论文用四个任务把这两个缺口同时打开：既要求**自适应检索**（lexical search / 语义匹配 / 直接阅读随信息需求切换），又显式允许**成本不同的多种解法**（选择性搜索 vs 穷举）。

## 四个任务

| 任务 | 规模 | 答案形式 | 省算力的走法 |
|------|------|---------|-------------|
| **Constraint Solving Search** | 约 120K tokens、160 人、3–5 个条件 | 恰好 5 个人 ID | 先查满足人数最少（≤10%）的那个条件，再只对候选验证其余条件 |
| **Equivalent Program Pair Search** | 约 100K tokens、200 个 Python 程序 | 5 个无序程序对 | 先按用途分组，再用区分性输入剔除行为不同的 mutant |
| **Program Execution Tracing** | 320 个打乱的计算记录（8 步 × 40 cell 池） | 8 个 cell ID + 最终结果 | 把上一步输出当作下一步搜索键，复用已记录的结果而非重算 |
| **Outlier Memo Detection** | 700 条 memo、2,500 条陈述 | 恰好 15 个矛盾 memo ID | 读一遍就建成关系表/图，之后所有校验复用同一份证据 |

四个任务都要求**验证检索到的证据**，而不只是「找到」——这是它们区别于传统 needle-in-a-haystack 的地方。矛盾/等价性往往只有把多条证据组合起来才可见。

## 评测配置与核心数字

5 个模型（GPT-5.6-sol、Gemini 3.8 Flash、GLM-5.3、Qwen3.8-27B、Kimi-K2.6）× 5 种配置（Direct 直推 + RLM / OpenCode / mini-swe-agent / ReAct），每实例 3M token 预算。

- **天花板低**：最佳 68%（GPT-5.6-sol + mini-swe-agent）；最强非 GPT 42.5%（GLM-5.3 + mini-swe-agent）；Kimi-K2.6 从未超过 1.5%；
- **无全能选手**：没有任何配置在四个任务上全胜。OpenCode 把 Outlier Memo Detection 从 44% 拉到 **10%**、Pairs 从 44% 拉到 **0%**，却把 Tracing 从 94% 提到 96%；
- **同等准确率 ≠ 同等成本**：Outlier Memo Detection 上 RLM 92% @ $7.23，mini-swe-agent 100% @ $0.583（12.4× 成本差）；
- **多推理不保证成功**：Pairs 上 RLM 2% @ $7.86，反而低于直推的 44% @ $0.780；
- **弱模型获益更多**：Qwen3.8-27B 0% → 38.5%，GLM-5.3 9.5% → 42.5%，Gemini 10% → 25%，GPT-5.6-sol 60% → 68%（论文的规律；Kimi-K2.6 是这条规律的反例，本页已标注）。

## 本页图表

Figure 1–4 与 Table 1–6 全部 300 DPI 内嵌于对应讲解段落，无单独图库章节。附录 A（详细 token/成本账本）、附录 B（四个任务的构造流程）、附录 C（API 费率）一并覆盖。

返回[分类目录](../README.md) · [总索引](../../README.md)