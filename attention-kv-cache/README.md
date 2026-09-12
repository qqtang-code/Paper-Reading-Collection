# 🎯 注意力与 KV Cache(Attention & KV Cache)

从注意力本身省算力:让注意力看得更少(声明式稀疏、混合稀疏)→ 让 KV Cache 留得更少(驱逐)→ 让稀疏比按输入自适应。每篇均含中文精读页与英文版。

| 论文 | 主题 | 中文精读 | 英文版 |
|------|------|----------|--------|
| Declarative Attention(2026-09) | 声明式稀疏注意力 · KV Cache · 长上下文 · CoT | [declarative-attention/](declarative-attention/) | [en.html(完整英译)](declarative-attention/en.html) |
| Random Attention(2026-09) | KV Cache 驱逐 · 推理模型 · 长思维链 · vLLM | [random-attention/](random-attention/) | [en.html(英文速读)](random-attention/en.html) |
| Elastic Attention(2026-09) | 混合注意力 · 测试时自适应 · Attention Router · 长上下文 | [elastic-attention/](elastic-attention/) | [en.html(英文速读)](elastic-attention/en.html) |

模型层的效率工作(量化、架构压缩、服务系统)见 [efficient-inference/](../efficient-inference/)。

返回[总索引](../README.md)。