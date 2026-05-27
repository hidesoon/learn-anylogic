# ChatGPT × AnyLogic Webinar — 演示模型

AnyLogic 官方 webinar **《Exploring the Utility of ChatGPT as a Java Scripting Aid for AnyLogic Modeling》** 演示用的 4 个 `.alp` 模型(原始 supplemental ZIP 解压而来)。

配套的对话日志 PDF 与厂商原始说明在 [../../chatgpt-anylogic-webinar-docs/](../../chatgpt-anylogic-webinar-docs/)。

- 对应字幕:[../../transcripts/chatgpt-anylogic-webinar.txt](../../transcripts/chatgpt-anylogic-webinar.txt)
- 对应综述条目:[reports/literature-review.md › L1](../../../reports/literature-review.md)
- 文件日期:2023-04-19(对应 GPT-3.5 / GPT-4 时代)。

## 为什么在 `references/models/` 而非顶层 `models/`

顶层 [models/](../../../models/) 留给**本 repo 自己用 LLM 构建 / 研究**的模型(自带实验 provenance)。这里是**厂商发布的演示模型**(外部、被引用),故归到 `references/`(引用区)下的 `models/`。

> 厂商说明强调:**这些都不是「能跑」的完整仿真**,只是把 ChatGPT 给的代码落地后的结果模型。

## 模型清单

| 模型 | 说明 |
|---|---|
| `USA States/` | 调用公开 API(datausa.io)按年份动态生成 agent,每个代表一个美国州 + 人口。API 查询代码(含 import)全由 ChatGPT 写。 |
| `DB View Test/` | 供应链模型起点,演示用**数据库视图(HyperSQL)**把多表整形成可喂给 population 的格式。含 ChatGPT 写的**初版(错误)查询与修正后查询**(多重 LEFT JOIN 计数翻倍 → 子查询修复)。 |
| `Dynamic Agent Placement/… - 1.alp` | 1 个 `Location` population,按 `tier`(1–3 合法、4 非法)切换动画图标;图标可见性条件由 ChatGPT 写。 |
| `Dynamic Agent Placement/… - 2.alp` | 3 个 population(每个合法 tier 一个),按规模动态计算 X 位置;X 位置公式由 ChatGPT 写(含其自己发现并修复的「单元素除零 → NaN」边界)。 |

## 未纳入

原 ZIP 中 `DB View Test/cache/`(约 5.7 MB 的 GIS 瓦片缓存,`giscache*`)是**可再生**派生文件,未提交;AnyLogic 打开模型时会按需重新下载(已在 [.gitignore](../../../.gitignore) 中忽略)。
