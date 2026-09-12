# ⚡ 高效推理与部署(Efficient Inference & Deployment)

在模型与系统层面让 LLM 推理更快、更省、能部署到更小硬件:低精度量化、架构与 KV 压缩、服务系统。每篇均含中文精读页与英文版。

| 论文 | 主题 | 中文精读 | 英文版 |
|------|------|----------|--------|
| FreeToken(2026-09) | MoE · 边缘部署 · 带宽自适应 | [freetoken/](freetoken/) | [en.html(英文速读)](freetoken/en.html) |
| ReSET(2026-08) | 量化 · NVFP4 · 温度缩放 | [reset/](reset/) | [en.html(英文速读)](reset/en.html) |
| DeepSeek-V4.1-Flash(2026-09) | KV Cache 压缩 · MoE · 多模态 · 长上下文 | [deepseek-v41-flash/](deepseek-v41-flash/) | [en.html(完整英译)](deepseek-v41-flash/en.html) |

注意力层面的工作(稀疏注意力、KV Cache 驱逐、稀疏比路由)见 [attention-kv-cache/](../attention-kv-cache/)。

返回[总索引](../README.md)。