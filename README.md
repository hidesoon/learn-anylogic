# learn-anylogic

研究 repo:**LLM 辅助仿真建模(LLM-assisted simulation modeling)**,以 AnyLogic 为主要载体。

收集研究报告、外部文献、被研究的 AnyLogic 模型、可复用的 prompt,以及 LLM 实验记录。

## 研究目标

- 探索 LLM(ChatGPT / Claude 等)在 AnyLogic 建模各环节(学习、设计、写 Java、调试、维护、加功能)中的实际能力与边界。
- 沉淀可复用的方法论:有效的 prompt、工作流、规避坑的最佳实践。
- 用可复现的实验记录,追踪 LLM 能力随时间/版本的变化。

## 目录结构

| 目录 | 内容 | 区分原则 |
|---|---|---|
| [reports/](reports/) | **我自己写的**研究报告、综述、阶段性发现 | 原创 |
| [references/](references/) | **外部资料**:论文、视频字幕、链接收藏 | 引用 |
| [models/](models/) | 被研究的 AnyLogic 模型(`.alp`/`.alpx`)+ 导出的 Java | 每个模型一个文件夹 |
| [prompts/](prompts/) | 可复用的 prompt 库 | 跨实验复用 |
| [experiments/](experiments/) | 单次 LLM 实验记录 / 对比 / 评测 | 时间+主题命名的快照 |

## 约定

- 文件夹用 `kebab-case`。
- 实验、带时间属性的报告加 `YYYY-MM-DD-` 前缀(便于排序、体现 LLM 能力随时间演化)。
- 每个 `models/<name>/` 和 `experiments/<name>/` 自带 `README.md` 记录出处与方法,保证可复现。

## 索引

### 报告
- [reports/llm-assisted-modeling-landscape.md](reports/llm-assisted-modeling-landscape.md) — 现状全景:方法 / 工具 / 成熟度阶梯(对文献综述 L1–L9 的综合,含设计期 Python API 已发 beta 的更正)
- [reports/llm-anylogic-overview.md](reports/llm-anylogic-overview.md) — 用 LLM 搭建 AnyLogic 模型的完整实操指南
- [reports/literature-review.md](reports/literature-review.md) — 文献综述(带批注的文献条目)

### Prompt
- [prompts/anylogic-priming-template.md](prompts/anylogic-priming-template.md) — AnyLogic priming(预热)提示词模板

### 实验
- [experiments/2026-05-28-bank-office-llm-assist/](experiments/2026-05-28-bank-office-llm-assist/) — 首个动手实验:Claude Opus 4.7 辅助搭建官方 Bank Office 模型(Process 库,Phase 1/3/4)。结构/API/定量预测全中、零幻觉;最大教训是"LLM 当核查者也会臆造 bug"。含 [完整经过 session-log](experiments/2026-05-28-bank-office-llm-assist/session-log.md) + transcript + results

### 参考资料
- [references/papers/learning-abm-with-llm-companions-netlogo-chat.pdf](references/papers/learning-abm-with-llm-companions-netlogo-chat.pdf) — Chen 等(CHI '24):首篇 LLM 辅助 ABM 的**同行评审**实证(NetLogo Chat + 新手/专家差异、「知识鸿沟」、LRPL 幻觉、文档 RAG)。详评见 [文献综述 L6](reports/literature-review.md)
- [references/papers/big-book-of-simulation-modeling-ch1.md](references/papers/big-book-of-simulation-modeling-ch1.md) — Borshchev《The Big Book of Simulation Modeling》第 1 章:建模与仿真建模基础(解析 vs. 仿真、排队论的局限、抽象层次与三种方法)。[原始 PDF](references/papers/big-book-of-simulation-modeling-ch1.pdf)
- [references/papers/generative-digital-twins-vlsm-flexscript.pdf](references/papers/generative-digital-twins-vlsm-flexscript.pdf) — Hsu 等(NYCU,arXiv 2025-12,**预印本**):训练视觉-语言模型(VLSM)从布局草图+提示生成可执行 FlexScript;GDT-120K 数据集 + SVR/PMR/ESR 三指标;实证「小专用/代码模型 > 大通用模型」。[L2] 的跨工具后继。详评见 [文献综述 L10](reports/literature-review.md)
- [references/transcripts/chatgpt-anylogic-webinar.txt](references/transcripts/chatgpt-anylogic-webinar.txt) — AnyLogic 官方 webinar 字幕
- [references/models/chatgpt-anylogic-webinar/](references/models/chatgpt-anylogic-webinar/) — 该 webinar 的 4 个演示 `.alp` 模型(厂商发布,被引用)
- [references/chatgpt-anylogic-webinar-docs/](references/chatgpt-anylogic-webinar-docs/) — 该 webinar 的 40 页 ChatGPT 对话日志 PDF + 厂商说明(priming 提示词出处)
- [references/transcripts/ai-model-and-modeler-co-design.txt](references/transcripts/ai-model-and-modeler-co-design.txt) — AnyLogic R&D 演讲字幕:GPT-5 + Cursor 经 Python API 自动生成模型
- [references/transcripts/pypeline-python-anylogic.txt](references/transcripts/pypeline-python-anylogic.txt) — AnyLogic 官方 webinar 字幕(2020-10):Tyler Wolf-Adam 介绍 Pypeline——连接 AnyLogic 与 Python 的开源库(运行期 Python 桥,PLE 可用)。详评见 [文献综述 L8](reports/literature-review.md)
- [references/anylogic-help/](references/anylogic-help/) — AnyLogic 官方文档本地 Markdown 镜像,含可复现抓取脚本:**Advanced Modeling with Java**(`/advanced/`,207 页:Java 基础、内置函数、调试、自定义库、团队协作、Action chart、集成)+ **API Reference**(`/api/`,826 页引擎 Javadoc 类参考,精简为类说明 + 方法 summary 表)
- [各版本对比 editions.html](https://anylogic.help/anylogic/ui/editions.html) — AnyLogic 官方版本功能/许可对比(PLE / University / Professional):导出、库、版本控制、调试差异 + PLE 容量上限。详评见 [文献综述 L7](reports/literature-review.md)
- [Using AI to help build AnyLogic models（The AnyLogic Modeler 博客,2025-10）](https://www.theanylogicmodeler.com/post/using-ai-to-help-build-anylogic-simulation-models) — 实践者署名 how-to:ChatGPT/Grok/Perplexity 概念+片段、VS Code/Copilot/ALPX 直接编辑模型文件、GitHub Copilot agent 跑分支/PR/checklist。详评见 [文献综述 L9](reports/literature-review.md)
- [references/links.md](references/links.md) — 链接收藏

## 进展

- [x] 建立 repo 结构
- [x] 收集 AnyLogic 官方 ChatGPT webinar transcript
- [x] 收集 AnyLogic R&D 演讲 transcript(AI 经 Python API 自动建模)
- [x] 收集 Pypeline webinar transcript(Python ↔ AnyLogic 连接库)
- [x] 整理首份方法论指南
- [x] 收集仿真建模基础理论文献(Borshchev《The Big Book》第 1 章)
- [x] 收集首篇同行评审的 LLM 辅助 ABM 实证研究(Chen 等,CHI '24)
- [x] 镜像 AnyLogic 官方文档「Advanced Modeling with Java」到本地(207 页 Markdown)
- [x] 镜像 AnyLogic 引擎 API Reference(`/api/`,826 页 Javadoc 精简为方法 summary)
- [x] 收集首篇覆盖现代多工具 + IDE/Copilot agent 工作流的实践者文章(The AnyLogic Modeler,2025-10)
- [x] 收集首篇「训练专用多模态模型生成可执行仿真代码」的定量论文(Hsu 等,arXiv 2025-12,FlexSim/VLSM + GDT-120K + SVR/PMR/ESR)
- [x] 综合文献综述,产出「方法 / 工具 / 成熟度」现状全景报告(并据 `.venv` 实证更正设计期 Python API 为已发 beta)
- [x] 第一个动手实验:Bank Office(Process 库)用 LLM(Claude Opus 4.7)辅助搭建 Phase 1/3/4([experiments/2026-05-28-bank-office-llm-assist/](experiments/2026-05-28-bank-office-llm-assist/))
- [ ] 下一个实验:压能力边界(换非教科书模型,或测结构生成——设计期 Python API / `.alp`)
