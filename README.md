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
- [reports/llm-anylogic-overview.md](reports/llm-anylogic-overview.md) — 用 LLM 搭建 AnyLogic 模型的完整实操指南

### Prompt
- [prompts/anylogic-priming-template.md](prompts/anylogic-priming-template.md) — AnyLogic priming(预热)提示词模板

### 参考资料
- [references/transcripts/chatgpt-anylogic-webinar.txt](references/transcripts/chatgpt-anylogic-webinar.txt) — AnyLogic 官方 webinar 字幕
- [references/links.md](references/links.md) — 链接收藏

## 进展

- [x] 建立 repo 结构
- [x] 收集 AnyLogic 官方 ChatGPT webinar transcript
- [x] 整理首份方法论指南
- [ ] 第一个动手实验
