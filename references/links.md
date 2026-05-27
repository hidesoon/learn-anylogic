# 链接收藏

外部资料链接 + 一句话摘要。按主题分组。

## AnyLogic 官方:LLM / ChatGPT

- [Webinar: Exploring the Utility of ChatGPT for AnyLogic Modeling](https://www.anylogic.com/resources/educational-videos/webinar-exploring-the-utility-of-chatgpt-for-anylogic-modeling/) — 官方 webinar,把 ChatGPT 当 Java 脚本助手。字幕已存 `transcripts/`;官方 supplemental 材料拆为两处:40 页对话日志 PDF + 厂商说明存 [`chatgpt-anylogic-webinar-docs/`](chatgpt-anylogic-webinar-docs/),4 个 `.alp` 演示模型存 [`models/chatgpt-anylogic-webinar/`](models/chatgpt-anylogic-webinar/)。
- [AI with the Model and Modeler: Exploring Integration for Simulation Co-Design](https://www.youtube.com/watch?v=PBm3uIuFLTk) — AnyLogic 官方会议演讲(2025-12-12),首次公开其 AI R&D:用 GPT-5 + Cursor AI,经一个暴露**设计期 Python API**(镜像 AnyLogic 元素)的特殊 build,从模型文字描述自动生成完整模型(流程图、状态图);还演示了内置 LLM 聊天窗口原型。字幕已存 `transcripts/`。
- [Unlocking the power of simulation modeling in ChatGPT](https://www.anylogic.com/blog/unlocking-the-power-of-simulation-modeling-in-chatgpt/) — 官方博客,工作流与提示技巧。
- [How to use ChatGPT in the field of simulation modeling (Medium)](https://medium.com/@anylogic/how-to-use-chatgpt-in-the-field-of-simulation-modeling-e33238c24149) — 上文的 Medium 版。
- [Use ChatGPT for data analysis: make your AnyLogic model talk](https://www.anylogic.com/blog/use-chatgpt-for-data-analysis-make-your-anylogic-model-talk/) — 在模型里嵌入 ChatGPT 聊输出数据(第三方 Noorjax 库)。

## 实践者经验

- [Using AI to help build AnyLogic Simulation Models (The AnyLogic Modeler)](https://www.theanylogicmodeler.com/post/using-ai-to-help-build-anylogic-simulation-models) — 一位资深 modeler 的实战:VS Code + Copilot + ALPX 玩法。

## AnyLogic 文档(API / 排错)

- **[anylogic-help/](anylogic-help/) — 官方文档本地 Markdown 镜像**:已抓取 `/advanced/`(207 页散文教程)+ `/api/`(826 页引擎 Javadoc 类参考,精简为方法 summary),离线可读、可检索。下面这几个常用页都在镜像里。
- [Java in AnyLogic](https://anylogic.help/advanced/code/general.html) — 本地:[anylogic-help/advanced/code/general.md](anylogic-help/advanced/code/general.md)
- [Functions (methods)](https://anylogic.help/advanced/code/functions.html) — 本地:[anylogic-help/advanced/code/functions.md](anylogic-help/advanced/code/functions.md)
- [API Reference(引擎类参考)](https://anylogic.help/api/index.html) — 本地索引:[anylogic-help/api/com/anylogic/engine/package-summary.md](anylogic-help/api/com/anylogic/engine/package-summary.md)(核心包)
- [Troubleshooting](https://anylogic.help/anylogic/troubleshooting/troubleshooting.html) —(`/anylogic/` 章节,暂未镜像)
- [Pypeline(Java↔Python 桥)](https://github.com/the-anylogic-company/AnyLogic-Pypeline)

## 研究文献

- Chen, J., Lu, X., Rejtig, M., Du, D., Bagley, R., Horn, M. S., & Wilensky, U. J. (2024). **Learning Programming of Agent-based Modeling with LLM Companions: Experiences of Novices and Experts Using ChatGPT & NetLogo Chat.** *CHI '24.* arXiv [2401.17163](https://arxiv.org/abs/2401.17163);DOI [10.1145/3613904.3642377](https://doi.org/10.1145/3613904.3642377) — 同行评审(CHI 顶会),首篇 LLM 辅助 ABM 实证;设计了 NetLogo Chat、访谈 30 人,揭示**专家比新手更获益**、「知识鸿沟」、低资源语言(LRPL)高幻觉、文档 RAG 压制幻觉。PDF 存于 [papers/learning-abm-with-llm-companions-netlogo-chat.pdf](papers/learning-abm-with-llm-companions-netlogo-chat.pdf)。
- Romero-Guerrero, J. A., Suarez-Luna, J. M., Bautista-Orduna, G. E., & Arenas-Islas, D. (2026). **Creation of discrete event simulation models using artificial intelligence and FlexSim.** *Ingeniería Investigación y Tecnología, XXVII*(1), 1–12. DOI [10.22201/fi.25940732e.2026.27.1.004](https://doi.org/10.22201/fi.25940732e.2026.27.1.004) — 同行评审。用 ChatGPT 从**工业布局图**生成 FlexSim 代码、自动摆放机器。PDF 存于 [papers/creation-of-des-models-using-ai-and-flexsim.pdf](papers/creation-of-des-models-using-ai-and-flexsim.pdf)。
- [Can large language models assist choice modelling? (arXiv 2507.21790)](https://arxiv.org/pdf/2507.21790) — 文档 in-context 的提示效果最好。
- LLM-driven discrete-event simulation for manufacturing (ScienceDirect) — LLM 生成仿真"能跑但逻辑常错"。
