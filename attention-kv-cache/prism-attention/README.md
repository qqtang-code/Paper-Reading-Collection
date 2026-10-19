# Prism Attention — Proposal-Refined Index Sharing

**Prism Attention:Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference**(arXiv:2610.22985 · 苏州大学 × 百度 · NeurIPS 2026)

> 长上下文解码时,每一层每步都要回答「该看历史上哪 κ 个 token」,而选出这 κ 个要先给全部 $L_t$ 个 token 打分——稀疏注意力自己先付了一笔 $O(L_t)$ 的**索引税**。跨层共享索引是公认的省税办法,但它共享的是一个**已完成的判决**:锚层算出的 top-κ 被后续层照抄,抄得越远越不准。Prism 只改一件事——锚层(Proposal Layer)不再只交 top-κ,而交一个放大 $\rho$ 倍的候选池($n=\rho\kappa$);下游精修层(Refined Layer)拿这个池子,只用**自己这一层的** query 与 INT2 键在池内重新打分、自选 top-κ。于是「谁被看到」的决定权回到每层手里,而精修成本正比于 $\rho\kappa$ 而非上下文长度:每层约 **0.011 ms**,8K→128K 几乎不变。提案层只占 1/4(Proposal:Refined = 1:3,Qwen3-4B 的 36 层里 9 层),其全上下文打分改用 INT2 分组非对称量化的键缓存、并在 GQA 组内做 max 归约,每 KV head 每步只读一次。1:3 的分区沿用 IndexCache 的离线贪心校准,不训练权重。
>
> At every decoding step each layer must decide which κ tokens of the $L_t$-token history to read — and picking them means scoring all of them, an $O(L_t)$ **index tax** paid before any sparse saving. Sharing an index across layers is the standard way to avoid it, but what gets shared is a **finished verdict**: the anchor layer's top-κ, copied by every downstream layer and increasingly wrong with distance. Prism changes one thing — the anchor (Proposal) layer hands down not top-κ but a candidate pool expanded by $\rho$ ($n=\rho\kappa$); each Refined layer re-scores inside that pool with **its own** query and INT2 keys and picks its own top-κ. The decision returns to every layer, while refinement costs $\rho\kappa$ rather than $L_t$: about **0.011 ms** per layer, flat from 8K to 128K. Only 1/4 of the layers are proposals (Proposal:Refined = 1:3; 9 of Qwen3-4B's 36 layers); their full-context scoring uses an INT2 group-wise asymmetric key cache with a within-GQA-group max reduction, so each KV head is read once per step. The 1:3 partition comes from IndexCache's offline greedy calibration; no weights are trained.

- **中文精读**:[index.html](index.html) · [在线](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/prism-attention/)
- **English full mirror**:[en.html](en.html) · [online](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/prism-attention/en.html)
- **分类**:注意力与 KV Cache · 决策者 = **复用同模型已有的选择(修正版:共享候选池而非判决,每层保留一次池内复议)**
- **标签**:Token 级稀疏注意力 · 跨层索引复用 · 候选池 + 池内精修 · INT2 打分 · 长上下文解码
- **图表**:`figs/` 共 26 张 PNG(论文 **14 图 + 11 表 + 1 算法** 全部)+ **1 张本页自绘**(`chart-layer-ledger.svg`,英文页为 `chart-layer-ledger-en.svg`),300 DPI 从原文提取,中英页共用
- **原文**:<https://arxiv.org/abs/2610.22985>

论文速览:主实验用 Qwen3-4B / Qwen3-8B,稠密注意力为基线,对照 Quest、SeerAttention-R、LessIsMore、IndexCache 四条稀疏路线,全部按 training-free 方式适配,因此 Prism 与 IndexCache 之间只差「传递的东西不同」(传判决 vs 传候选)。配置 $\kappa=2048$,$\rho=4$(长上下文,候选池 8192)/ $2$(推理,候选池 4096),Proposal:Refined = 1:3。端到端每步解码在 **128K / BSZ=16** 下 **3.36×**(15.03 ms → 4.47 ms,vs FlashAttention);推理均分 **71.43 / 73.83**(全注意力 71.95 / 74.33),LongBench 均分 **54.98 / 54.97**(全注意力 55.07 / 54.58)。精度不是白拿的:增益集中在 AIME24(AIME25 落后 2.1–2.3 分、GPQA 最多落后 1.4 分),Qasper / SQuAD 这类单段落抽取式 QA 系统性偏弱。补充实验把结论推广到 MLA 架构(GLM-4.7-Flash)、4K/8K/16K 长度与四类任务——索引重合度从 24% 变到 35%,但这些索引承载的**注意力质量占比稳定在 76%–81%**,这是「稳的核心大、漂的尾巴碎」最有力的证据。

本页另含五处编者整理与追问:**把配置落到层号上**(Qwen3-4B group-4 的校准字符串是 `FSSSSSSFFSSSSFSFSFFSSSSSSSFSSSSSSSSF`,9 个提案层落在第 0、7、8、13、15、17、18、26、35 层)、**一张本页自绘图**(层身份 × 每层索引成本地图,论文只给了公式与按长度排列的分解图,没把这两件事画在一起)、**成本解耦的推算**(用 Table 6 实测值算得提案层 0.338 ms、精修层 0.056 ms,摊薄后每层 0.126 ms ≈ FlashAttention 的 5.54×)、**一条论文没画出来的交叉点曲线**(候选池 8192 意味着 $L_t \approx 8192$ 时机制红利归零,Table 7 的 8K/BSZ=1 处 0.61×、16K 0.67×、64K 0.89×、128K 1.50× 正好印证,交叉点在 32K–64K),以及 **7 条「未披露、值得补测」清单**(INT2 的位宽与分组大小 $g$、校准预算 512 与推理预算 2048 不一致、prefill 侧完全未测、$\rho \times \kappa$ 缺二维网格、未与 MoBA/NSA 等端到端稀疏训练方法对比、2-bit 缓存的额外显存账、单段落抽取式 QA 的系统性退化)。

> **工程约定**:本页 KaTeX 走**本地 `assets/katex/`**,`file://` 直接打开即可离线渲染公式——与合集内其他页使用 CDN 的写法不同,这是刻意的:本页承诺「重排数字可离线复核」。
>
> **Note on KaTeX**: this page ships KaTeX under `assets/katex/` so formulas render from `file://` with no network. Other pages in this collection use a CDN; here it is deliberate.

## 这篇在谱系里的位置

它落在「**复用同模型已有的选择**」这一档,但把这一档的问法改了。这一档此前的成员共享的都是一个**现成的、被信任的决定**:HySparse2 复用全注意力层的 KV 与选择索引(共享即采信),KSA V2 复用模型自己逐层算出来的 Summary,Declarative Attention 让模型自己声明看哪里。Prism 的立场是:**决定可以被共享,但不能被信任**——共享的应该是一个更宽的候选集,而不是一个已经做完的判决。因此它补上的是此前空着的一个位置:**共享的结构 + 每层的复议权**。

读之前值得记住一句:Prism 的加速来自「把 $O(L_t)$ 的全上下文打分限制在 1/4 的层里」,而不是来自「候选池很小」——候选池其实是放大的(4 倍),省下来的是扫描范围。这条区别决定了它的成立条件:加速比随上下文长度与 batch 单调上升(128K/BSZ=16 为 3.36×,而 16K/BSZ=1 只有 0.86×,比稠密注意力还慢);相对 IndexCache,它的时延反而慢约 0.7%,真正的收益是精度(推理侧 AIME24+25 合并平均 +1.46、LongBench 4B +1.71,均为相对 IndexCache 的口径)。把它和 Random Attention(证明选择信号几乎不贡献精度)放在一起读,会得到一个很尖锐的问题:精修出来的这部分精度,能不能用更便宜的方式买到。这是这一档接下来最值得做的一次对撞实验。

返回[分类目录](../README.md) · [总索引](../../README.md)
