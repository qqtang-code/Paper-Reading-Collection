# figs_audit.md — 图表提取三重校验审计

论文: `KSA V2 Technical Report` (arXiv:2610.18654v1, 32 页)  
输入: `/tmp/paper_2610.18654.pdf` + `/tmp/crops.json`  
输出: `/tmp/figs/*.png`（300 DPI，`page.get_pixmap(dpi=300, clip=rect)`，无缩放）  
坐标系: `crops.json` 的 `page` 为 **0 基索引**；`rect` 为 PDF 点坐标 `[x0,y0,x1,y1]`。下表 `page` 列给出 0 基 →（1 基显示）。

定位方法: 先用 `page.get_drawings()` 取图/表外框与 `get_text("blocks")` 取图注/正文 span 边界围出安全窗口，
再在窗口内渲染扫描灰度 <248 的像素求**墨迹包围盒**，四边加约 2–5pt 留白（受相邻元素距离限制时取空隙中点）。

校验口径（SKILL.md 第 3 步）：
- **(a) 防错页**：用 fitz 直渲染 `doc[page]` 同一 rect，与输出 PNG 逐像素比对（要求 maxdiff=0、MD5 一致）；再渲染 `doc[page+1]` 同一 rect，要求与前者**不同**。
- **(b) 文本块核对**：列出框内全部文本块，确认含完整图注、且无正文段落混入（表内长数据行按数字占比区分，非正文）。
- **(c) 边框全白**：PNG 四边 1px 内无灰度 <248 像素。

| key | page (0基→1基) | 最终 rect [x0,y0,x1,y1] | PNG 尺寸 | (a) 防错页 | (b) 框内文本块 | (c) 四边无墨迹 |
|---|---|---|---|---|---|---|
| `fig1` | 0 → p.1 | [60.0, 458.0, 535.3, 767.2] | 1981×1289 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 115 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig2` | 2 → p.3 | [60.0, 83.0, 535.3, 246.1] | 1981×681 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 32 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig3` | 3 → p.4 | [60.0, 83.0, 535.3, 273.1] | 1981×793 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 29 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig4` | 4 → p.5 | [60.0, 83.0, 535.3, 292.6] | 1981×875 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 37 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig5` | 6 → p.7 | [60.0, 84.0, 535.3, 502.0] | 1981×1742 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 33 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig6` | 8 → p.9 | [62.0, 86.0, 535.3, 394.0] | 1973×1284 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 19 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig7` | 9 → p.10 | [59.5, 201.0, 535.3, 351.2] | 1984×627 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 27 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig8` | 12 → p.13 | [59.5, 659.0, 534.5, 757.8] | 1981×413 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 6 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig9` | 15 → p.16 | [60.0, 83.0, 535.3, 311.8] | 1981×955 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 21 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig10` | 17 → p.18 | [262.7, 83.9, 536.0, 230.2] | 1140×611 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 18 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig11` | 17 → p.18 | [60.0, 539.0, 536.0, 760.8] | 1984×925 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 65 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig12` | 20 → p.21 | [60.4, 83.0, 534.9, 298.8] | 1978×900 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 23 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `fig13` | 21 → p.22 | [60.4, 158.8, 534.9, 728.8] | 1978×2376 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 58 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table1` | 7 → p.8 | [59.7, 78.5, 535.3, 350.0] | 1983×1132 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 23 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table2` | 12 → p.13 | [59.7, 78.5, 535.0, 552.0] | 1982×1973 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 5 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table3` | 13 → p.14 | [59.7, 78.5, 536.0, 345.0] | 1986×1111 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 7 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table4` | 14 → p.15 | [59.7, 78.5, 535.5, 455.0] | 1984×1569 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 8 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table5` | 16 → p.17 | [59.7, 78.5, 535.3, 524.5] | 1983×1859 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 10 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table6` | 16 → p.17 | [59.7, 402.0, 535.3, 524.5] | 1983×511 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 3 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table7` | 17 → p.18 | [60.2, 83.9, 254.0, 230.0] | 809×610 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 3 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table8` | 18 → p.19 | [60.2, 186.2, 535.0, 272.5] | 1980×361 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 3 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table9` | 19 → p.20 | [59.7, 78.5, 536.3, 325.5] | 1987×1030 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 6 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table10` | 20 → p.21 | [59.7, 299.5, 535.0, 449.0] | 1982×624 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 4 块，含完整图注，无正文混入 | PASS 最暗=255 |
| `table11` | 22 → p.23 | [304.0, 251.5, 536.3, 414.0] | 969×678 | PASS maxdiff=0；page+1 差异 maxdiff=255 | PASS 4 块，含完整图注，无正文混入 | PASS 最暗=255 |

## 结论

- 数量：**13 图 + 11 表 = 24 张，不重不漏**，与论文正文/附录一致。
- 全部 24 张 (a)(b)(c) 三项校验 **PASS**。
- 肉眼复核（read_image）：fig2 / fig3 / fig4 / fig5 已确认内容正确、面板标签齐全、图注完整；另加验 fig7、fig8、table9。

## 定位过程中修正的边界问题

| key | 问题 | 处置 |
|---|---|---|
| fig7 | 原 rect 顶端混入 2.4 节正文段落与标题 | 顶端收到 y=201（正文止于 195，图内容起于 207.7） |
| fig8 | 原 rect 顶端混入公式行 (15) | 顶端收到 y=659（公式止于 655，图起于 662.6） |
| fig10 | 原 rect 下边缘切断 x 轴标签、且漏掉图注 | 采用复核后 rect，底边收到 y=230.2（图注止于 228.4） |
| fig11 | 原 rect 左右过窄，削掉图本体（墨迹 x 至 62.5/533.5） | 左右放宽到 60.0/536.0 |
| table3 | 原 rect 底边混入 “S-KSA adaptation.” 正文段 | 底边收到 y=345（末行止于 335，正文起于 355.3） |
| table4 | 原 rect 底边混入 “Compression and sparsity compose.” 正文段 | 底边收到 y=455（末行止于 444，正文起于 463.8） |
| table7 | 原 rect 底边截断表格最后一行，且漏表题 | 采用复核后 rect（左栏 x60.2–254） |
| table8 | 原 rect 高 444pt，把表格下方三段正文全框进来 | 采用复核后 rect，高降到 86.3pt |
| table9 | 原 rect 底边混入 “Max versus sum teacher pooling.” 等三段正文 | 底边收到 y=325.5（末行止于 315.9，正文起于 335.4） |
| fig1–fig13 | 除 fig10 外，全部图原 rect 均**未包含图注**（系统性疏漏） | 统一把底边下延到图注结束与下文起始的空隙中点 |
