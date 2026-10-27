# Revisiting Pipeline Parallelism — 动态 Chunk 与跨 stage 延迟调度

**Revisiting Pipeline Parallelism for LLM Serving**(Soonjae Hwang & Jeongseob Ahn · Korea University · OSDI 2026)

> 重新审视流水线并行:LLM 在线服务的动态分块与跨 stage 延迟调度。在 4×A100(PCIe 4.0)上重审被 TP 挤到角落的流水线并行:把 pipeline bubble 拆成 **P-P / P-D / D-D** 三类,用「动态 chunk 大小」与「跨 stage 延迟调度」两条抓手分别压制。静态调好的 PP 已在 goodput 上反超 TP;DCP_pred 再把 AzureConv 的 TPOT 压 **35%**、E2E 压 **31%**,真实 trace 上 SLO 达成率 **92.5% → 94.6%**。
>
> Revisits pipeline parallelism for online LLM serving on PCIe-class 4×A100: splits pipeline bubbles into **P-P / P-D / D-D** classes and attacks them with dynamic chunk sizing plus cross-stage delay scheduling. Even a tuned static PP already beats TP on goodput; DCP_pred cuts AzureConv TPOT by **35%** and E2E by **31%**, lifting real-trace SLO attainment from **92.5% to 94.6%**.

- **中文精读**:[index.html](index.html) · [在线](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/pp-serving/)
- **English full mirror**:[en.html](en.html) · [online](https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/pp-serving/en.html)
- **分类**:高效推理与部署 · 决策者 = **调度器**(每 $D_p$ 个迭代按 SLO 余量选 chunk 大小;decode-only 迭代里把请求在 microbatch 间迁移)
- **标签**:流水线并行 · 动态 Chunked Prefill · 延迟预测模型 · Delay Scheduling · 在线服务
- **图表**:`figs/` 共 16 张 PNG = 论文 **14 图 + 1 表 + 1 算法** 全部,300 DPI 从原文提取,中英页共用
- **原文**:<https://www.usenix.org/system/files/osdi26-hwang.pdf> · **会议页**:<https://www.usenix.org/conference/osdi26/presentation/hwang>

## 论文速览

实验台是一台 4×A100 40GB(PCIe 4.0、128 核 EPYC 9754、768 GB 内存),在 **SGLang 0.4.1** 上实现(PyTorch 2.5.1 / CUDA 12.4 / FlashInfer);模型为 Qwen2.5-32B 与 14B,负载是 AzureConv、ShareGPT、CNN 三条真实 trace,加上把 CNN 输入输出分布对调得到的 decode-heavy 变体 CNN-Reversed,以及两条合成负载。goodput 按 MLPerf 口径定义为「P90 TTFT 与 P90 TPOT **同时**满足 SLO 的最高请求率」,SLO 取 2000 ms TTFT / 200 ms TPOT。基线是 TP 与默认 chunk=2048 的 PP,三个增量分别是 **DCP_greedy**、**DCP_pred** 与 **DCP_pred+DS**。

## 关键结论与数字

- **bubble 不是一种东西,是三种**。P-P:两条长度 2048 与 128 的 prompt 前后脚进入 prefill,一次气泡约 **627 ms**;P-D:一个 microbatch 全是 decode、另一个全是 prefill,把 TPOT 直接顶高;D-D:decode-only 迭代里 microbatch 之间的请求数失衡——线性层是 step function,batch 从 128 加到 129 可能突然多出约 **31%** 的时延,CNN-Reversed 上由此产生的空转约占 **31%**,而且 batch 只有取 128 的整数倍才划算。
- **静态调好的 PP 已经赢了 TP**:离线搜出的固定 chunk(AzureConv 用 512、CNN-Reversed 用 256)在 goodput、TTFT、TPOT 上同时反超 TP。真正的浪费不是「PP 不行」,而是**这个 chunk 一旦写死就再也跟不上负载**:默认 chunk=2048 时它甚至会输给 TP(32B × AzureConv 是论文点名的例外——算力成本主导,PP 省通信的优势被吃掉),负载一波动就重新长出气泡。
- **DCP_greedy(Algorithm 1)**:每 $D_p$ 个调度迭代读一次 $TTFT_{slack}$、$TPOT_{slack}$、$KV_{free}$,按 α/β/γ 三条边界与 KV 水位 $\theta_{mem}$ 以 ±128 的步长加减 chunk。反馈式、几乎零改动,代价是收敛慢、且反馈被流水深度延迟并被他 stage 的 chunk 扭曲。
- **DCP_pred(ALP 延迟模型)**:把迭代时延拆成离线项 $\alpha_0 N_{tokens}+\alpha_1$(线性层)与在线项 $\beta_0\sum(L_{past}L_{pre})+\beta_1\sum L^2_{pre}+\beta_2\sum L_{dec}+\varepsilon$(注意力),用带遗忘因子的 **RLS** 在线拟合;再用 $TPOT_{SLO}$ 定上界、$TTFT_{SLO}$ 定下界,取**满足两个 SLO 的最小 chunk**以最小化气泡。Table 1:MAPE 从 15.85%(baseline)一路降到 **3.26%**,只比 2 层 DNN(2.56%)差 0.70 pp,却不需要离线训练。
- **delay scheduling** 补上 DCP 管不到的那半边:decode-only 迭代里把请求从最重的 microbatch 迁到最轻的,并把 batch 对齐到硬件友好边界(128/256/384);TPOT 余量紧时优先挂起**老请求**(更耐延迟),KV 吃紧时优先挂起**新请求**(让老请求先跑完、早释放 KV)。
- **收益**:AzureConv 上 DCP_greedy 把 TPOT/E2E 压 19%/18%,DCP_pred 压 **35%/31%**;CNN 上 42%/36%,ShareGPT 上 36%/24%。迭代时延 P90 51.68 → 29.56 → **21.53 ms**,P99 65.34 → **30.94 ms(2.11×)**。decode-heavy 的 CNN-Reversed 只靠 DS 就把 P90 从 28.94 压到 24.53 ms、goodput 最高 **+1.4×**。SLO 收紧(scale 1.0→0.4)时 DCP 相对 PP 的优势从 2.7× 涨到 **5.4×**(32B),14B 从 1.7× 到 2.4×。
- **真实 trace(AzureConv 前 15 分钟,到达率 ×0.9)**:SLO 达成率 TP **1.9%** / PP_2048 **1.6%** / PP_static **92.5%** / DCP_greedy 93.5% / DCP_pred 94.5% / DCP_pred+DS **94.6%**;把 TPOT_SLO 收到 150 ms,DCP_greedy/DCP_pred 的达成率是 PP_static 的 3.06×/4.14×,60 s 内完成的请求数是 1.3×/1.6×。
- **代价同样清楚**:DS 挂起短上下文请求换来 E2E 平均 −4,062 ms、P99 −8,088 ms,但被挂起请求的 P99 TPOT 比 DCP_pred 差 **15%**;SLO scale 压到 0.6 以下,DS 因凑不够激活阈值而失效;CNN-Reversed 这类短输入长输出的负载留给 DCP 的调节空间很小。

## 图表清单

`figs/` 里 16 张 PNG 对应论文全部 **14 Figure + 1 Table + 1 Algorithm**,按讲解顺序内嵌,无单独图库章节。

- **问题与动机**:Figure 1(4×A100 上 PP vs TP 服务 Qwen2.5-32B:TP 被 $TTFT_{SLO}$ 卡住、PP 被 $TPOT_{SLO}$ 卡住)、Figure 2(三类 bubble 的时序示意,下标是迭代号)、Figure 3(prefill 随序列长度线性涨、decode 随 batch 涨、线性层 token 数呈 step function)、Figure 4(不同请求率与 chunk 下的气泡时长与 prefill 吞吐)、Figure 5(chunked-prefill 如何削掉 stall)。
- **方法**:Figure 6(DCP_pred 的五个步骤:读状态 → 更新预测器 → 上界 $TPOT_{SLO}$ → 下界 $TTFT_{SLO}$ → 选最小可行 chunk)、**Algorithm 1**(greedy chunk 调整的伪码)、Figure 7(delay scheduling 前后:挂起 E/F 的 decode 相位,换取跨 stage 平衡)。
- **实验**:Figure 8(trace 的输入/输出长度分布)、Figure 9–10(32B 与 14B 在三条负载上的 goodput + P90 TTFT/TPOT/E2E)、Figure 11(三条 trace 的迭代时延 CDF)、Figure 12(SLO scale 1.0→0.2 下的 goodput)、Figure 13(合成 prefill-heavy / decode-heavy)、Figure 14(真实 trace:SLO 达成率 + TPOT 与 E2E 的条件 CDF)、**Table 1**(预测模型对比:ALP 逐项加 Prefix/Prefill/Dec 注意力与残差项,对照线性回归 / LightGBM / DNN 的 MAPE、预测耗时与模型体积)。

## 分类与相邻工作

它落在**高效推理与部署**里的「系统栈 · 调度 / 部署形态」一档,和同分类的四篇正好互补:DeepSeek-V4.1-Flash 改**模型与缓存**,ReSET 改**精度与内核**,FreeToken 改**部署形态**,KITE/SST 改**扩容的位置**——这四篇都在动模型本身,而本篇**一行权重都不动**,只动「每轮迭代把多少 token 塞进哪个 microbatch」。机制对照表里它的三格是:省的是**跨 stage 空转(pipeline bubble)**;决策者 = **动态 chunk 大小 + 按负载把请求在 microbatch 间迁移**;不需要训练(纯调度,ALP 只做在线 RLS 拟合)。

与它最近的三条线:chunked-prefill(Sarathi-Serve)是把 prefill 切小以救 TPOT,本篇把「切多大」从超参变成被 SLO 约束的在线决策;phase-disaggregated serving(Splitwise / Mooncake 一类)用分离 prefill/decode 来消气泡,但付出权重复制与 KV 传输的代价,本篇坚持统一服务;AlpaServe 用统计多路复用按负载分配 GPU,本篇则在固定的 PP 拓扑内做时间维度的再平衡。评测边界也清楚:只在 PCIe 4.0 的单机 4 卡、Qwen2.5-32B/14B 上做,没有跨机、没有 NVLink、没有 MoE 专家并行的组合,也没有与 DP/EP 的联合调优。

## 在线阅读

- 中文精读:<https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/pp-serving/>
- Read in English:<https://qqtang-code.github.io/Paper-Reading-Collection/efficient-inference/pp-serving/en.html>
- 原文 PDF:<https://www.usenix.org/system/files/osdi26-hwang.pdf> · 会议页:<https://www.usenix.org/conference/osdi26/presentation/hwang>

返回[分类目录](../README.md) · [总索引](../../README.md)
