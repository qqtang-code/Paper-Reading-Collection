# KSA V2 — Kwai Summary Attention V2

**Kwai Summary Attention V2 Technical Report**(arXiv:2610.18654 · OneRec Team, 快手)

> KSA 这类 Summary token 混合架构里,每个 chunk 后面的 Summary 每层都被算出来、又被逐层精修,却只被当作"低分辨率记忆"给 KSA 层读。KSA V2 的核心观察是:**同一套 Summary 可以同时演两个角色**。作为**记忆**,它可以在**存储时**被再压一次——把每 $k_m$ 个连续 Summary KV 池化成一个层私有的 Meta 条目,远端历史压缩率从 $k_s=8$ 变成 $k_s k_m = 1024$,而**层间流动的 Summary 表示完全不动**,于是"压多狠"与"传多粗"这两个原本焊死在同一个参数上的旋钮被拆开(C-KSA)。作为**索引**,它可以当路由查询去给每个 $b$-token 文本块打分,让原来读全部因果 KV 的 Full 层只读 sink + 选中的块 + 局部窗口(S-KSA)。两者都不新增 token、不改变布局,因此可直接 retrofit 进已训好的模型。1.9B / 128K 下常驻缓存降 **40.4%**、prefill **1.51×**、decode **1.27×**,RULER 均值仅从 72.61 掉到 72.39。
>
> In summary-token hybrids, each chunk's Summary is computed and refined at every layer yet used only as low-resolution memory. KSA V2's observation: **one Summary hierarchy can play two roles.** As **memory**, it can be compressed a second time *at storage time* — pooling every $k_m$ consecutive Summary KV entries into a layer-local Meta entry, raising the distant-history compression factor from $k_s=8$ to $k_s k_m = 1024$ — while **the Summary representation passed between layers is untouched**, which decouples "how hard to store-compress" from "how coarse the inter-layer representation is" (C-KSA). As an **index**, it doubles as a routing query that scores each $b$-token text block, so the Full layers that previously read all causal KV read only sinks + selected blocks + a local window (S-KSA). Neither adds tokens nor changes the layout, so both retrofit into a pretrained model. At 1.9B / 128K: resident cache **−40.4%**, prefill **1.51×**, decode **1.27×**, with the RULER mean moving only 72.61 → 72.39.

- **中文精读**:[KSA-V2论文精读_HTML.html](KSA-V2论文精读_HTML.html) · [在线](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/ksa-v2/)
- **English full mirror**:[en.html](en.html) · [online](https://qqtang-code.github.io/Paper-Reading-Collection/attention-kv-cache/ksa-v2/en.html)
- **分类**:注意力与 KV Cache · 决策者 = **复用同模型已有的 Summary**(既是可压缩的记忆,又是稀疏路由的索引)
- **图表**:`figs/` 共 25 张 = 论文 **13 图 + 11 表** 全部 + **1 张本页自绘**(`chart-cache-ledger.svg`),300 DPI 从原文提取,中英页共用
- **原文**:<https://arxiv.org/abs/2610.18654> · **代码**:论文未给出仓库地址
- **提取审计**:[figs_audit.md](figs_audit.md)(24 张逐张记录 rect / 尺寸 / 三重复核结论)

论文速览:两个模块各自负责一侧的成本。C-KSA 把远端历史压缩率提到 $1/(k_s k_m)$,同时保持 GQA / MLA 的正交性(压缩率相乘,不改变 KV head 数与表示宽度);S-KSA 把 Full 层换成块稀疏,路由候选数比 token 级索引少 $b$ 倍。1.9B(MHA, 24 层)与 4B(GQA, 36 层)两档均按 3:1 布局 retrofit:$k_m = 128$ / $32$,$b = 4$,$K = 4096$ token 远端预算(含 8 个 sink),1024 token 局部窗口。6 长度 RULER 均值 1.9B 为 **72.39%**(父模型 72.61、Full 67.55),4B 为 **84.15%**(父模型 84.45);4B 的 128K 单点 **74.41%** 反而高于父模型的 71.67%。效率侧 128K 常驻缓存 **6.31 GiB**(Hybrid KSA 10.59、Full 24.00),prefill **44,971 tok/s**(29,837 / 20,830),decode **198.85 tok/s**(157.02)。消融给出两个关键结论:**层级压缩优于直接加大 chunk**(72.68 vs 70.63),以及 **max-pooled teacher 优于 sum**(72.39 vs 71.49);oracle 实验进一步显示,冻结 backbone、只读约 3.9% 的位置就能保留 **82.83%** 的 decode 注意力质量,RULER 66.24 对 dense 的 66.31——**选得准,骨架甚至不需要更新**。

本页另含五处编者整理与追问:**"把配置落到具体数字"走查**(24 层里 18 层 C-KSA + 6 层 S-KSA、128K 时每层约 128 个 Meta 条目、远端压缩 1024×、$K/b = 1024$ 个候选块、实际读取占比 $5120/131072 \approx 3.91\%$)、**一张本页自绘图**(论文的 1024× 是"远端历史"名义口径,而对外宣传的"降 40.4%"是"128K 常驻缓存"实测口径,两者相差两个数量级——论文没有任何一张图做过这个对照)、**技术来源一览**(Summary token ← KSA、逐维度聚合 ← DeepSeek-V4 的 CSA/HCA、Lightning Indexer ← DSA、块级 max-pool teacher ← QSA、meta-gist 层级压缩 ← H-SSA、landmark 检索 ← Landmark Attention)、**一处论文自身口径不一致的核对**(正文 §3.6 称缓存相对 Hybrid KSA 小 1.35×,Figure 1 图内标注写 2.9×,而用论文自己的实测值验算 $10.59/6.31 = 1.68$ —— 对两个来源都不吻合;相对 Full 的 $24.00/6.31 = 3.80$ 则与正文 3.86、图内 3.9 自洽),以及 **6 条"未披露、值得补测"清单**(4B 未验通用能力与效率、Meta 的逐层信息量分布、论文自述支持但未做实验的逐层异构 $k_m$、解码稀疏 kernel 在大 batch / 连续批处理下的表现、Indexer Q/K RMSNorm 未在 1.9B 复现、**FWE 类聚合任务明确退化 45.00 → 26.67**)。

> **工程约定**:本页 KaTeX 走**本地 `assets/katex/`**(含 20 个 woff2 字体),`file://` 直接打开即可离线渲染公式——与合集内其他页使用 CDN 的写法不同,这是刻意的:本页承诺"重排数字可离线复核"。实测在 `offline=True` 下 0 网络请求、0 控制台错误、522 个行内 + 17 个块级公式正常渲染。
>
> **Note on KaTeX**: this page ships KaTeX under `assets/katex/` (20 woff2 fonts) so formulas render from `file://` with no network. Other pages in this collection use a CDN; here it is deliberate. Verified offline: 0 network requests, 0 console errors, 522 inline + 17 display formulas rendered.

返回[分类目录](../README.md) · [总索引](../../README.md)