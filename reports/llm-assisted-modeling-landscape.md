# LLM 辅助仿真建模:现状全景(方法 / 工具 / 成熟度)

> 本文是对 [literature-review.md](literature-review.md)(L1–L9)的**综合**:不复述单条来源,而是把它们整理成一张「现在能用什么、能到什么程度」的全景图。
> 整理日期:**2026-05-28**。因 LLM 能力随版本演化,本文的成熟度判断带时效,需定期复核。
> 视角以 **AnyLogic** 为主,旁及 FlexSim(L2)、NetLogo(L6)做跨工具对照。

## 一、先看证据等级(读全景前的免责声明)

9 条来源里,**只有 L6(Chen 等,CHI '24)是同行评审实证**,且是 **GPT-3.5 上的质性研究**(无成功率/对照);其余 8 条是厂商官方材料(L1/L5/L8)、实践者博客(L9)、单案例论文(L2)或奠基性教材/文档(L3/L4/L7),普遍是**轶事式单例演示,带推广倾向,无量化指标**。

> **结论先行**:目前关于「LLM 能把仿真建到什么程度」的认知,**大多是 demo,而非测量**。下面的成熟度判断据此打折,而「补上量化测量」正是本 repo 的研究缝隙。

## 二、两根轴:把 9 条材料钉在一张表上

材料其实在讲三件不同的事,可用「**LLM 触碰模型的哪一层**」×「**建模生命周期的哪一端**」定位:

| | 学习端 | 搭建端(authoring) | 运行/分析端 |
|---|---|---|---|
| **嵌入式 Java 片段层** | L1 学 Java、L6 知识鸿沟 | **L1 写片段 / L9 聊天机器人出片段**(主战场) | — |
| **模型结构层**(flowchart / statechart / 空间标记) | — | **L2 FlexScript 建模** / **L4 设计期 Python API** / **L9 改 ALPX XML** / `.alp` 旁路 | — |
| **数据 / 结果层** | — | — | **L5 Noorjax 让模型"说话"**(靠 L8 Pypeline 当桥) |
| **背景标尺(本身不谈 LLM)** | L3 建模是"艺术" | L4 Java 只是嵌入层 / L7 许可证闸门 | L8 Pypeline 基础设施 |

两点立刻可见:(1) 绝大多数成功案例落在**嵌入式片段层**;(2) **模型结构层**是公认最难、也最有研究价值的部分,目前有四条互不等价的路径(见 §四 Tier C/D)。

## 三、贯穿全综述的 5 个母题(比单条来源更可复用)

1. **「喂结构化上下文 > 喂原始输入」** —— 反复出现的同一规律:L1 的 priming 提示词、L2「喂坐标表胜过让模型看图」、L5 的 `NameOfStat:{{Time:Value}}` 约定、L6 对官方文档做 RAG、L8 用 JSON 往返。**给 LLM 可信、结构化的上下文,是几乎所有正面案例的共同前提。**
2. **「能编译 ≠ 逻辑对」,必须验证行为** —— L1 厂商逐字自标对错、L2 看图读尺寸不可靠、L5 连"变化何时发生"都答错。验证的是**行为**,不是能否编译。
3. **专家比新手获益更多(L6 的"知识鸿沟")** —— 最反直觉、也是唯一同行评审实证给出的结论:要先懂建模,才能用好 LLM。直接呼应 L3「选抽象层次是艺术」——「专家获益更多」是「先懂建模才会用 LLM」的实证版。
4. **AnyLogic 的 Java 只是嵌入层(L4)** —— 硬架构事实,决定"LLM 该输出什么":写**片段**容易,生成**结构**难。
5. **低资源语言(LRPL)→ 高幻觉(L6)** —— AnyLogic 的 Java API 在线语料稀少,预期幻觉率高于通用 Java(L1 杜撰过不存在的 "Decision" block);priming / 文档 RAG 是已知缓解。

## 四、成熟度阶梯:现在能用什么、到什么程度

从"现在可靠"到"还在 R&D":

### 🟢 Tier A —— 现在就能用、有 ROI(嵌入式片段层)
- **能做**:写 / 改 / 解释 Java 片段、加注释、调试报错、HyperSQL 查询、当 Java/AnyLogic 概念家教。
- **工具**:任意现代聊天 LLM(ChatGPT / Claude / Grok / Perplexity)+ **priming 提示词**([../prompts/anylogic-priming-template.md](../prompts/anylogic-priming-template.md))。
- **程度**:L1/L9 的主战场,**PLE 免费档可用**。产出是标准 Java,**不能直接拖进 GUI**,要人工译写进属性框 / Function 对象(L9 的"译写鸿沟")。
- **风险**:幻觉 AnyLogic API(报错 `the method is undefined` / `cannot be resolved`);priming/RAG 缓解。

### 🟡 Tier B —— 能用,但需重度人工验证
- **概念结构建议**:让 LLM 给 agent 划分、变量建议作为**起点**(L1/L9)。但"选抽象层次/方法(SD vs DE vs AB)"这步(L3 的"艺术")仍须人把关。
- **读运行结果**:把仿真输出喂给 LLM 做自然语言分析(L5 Noorjax,靠 **L8 Pypeline** 当 Java↔Python 桥,**PLE 可用**)。程度:能识别因果方向,时序事实会答错;只能当辅助决策。
- **运行期 Python 集成**:Pypeline 把 matplotlib / TensorFlow / LLM API 接进**运行中的**模型(L8,PLE 可用),但**不生成模型结构**。

### 🟠 Tier C —— 刚冒头 / 官方但 beta / 无官方支持(模型结构层,部分可达)
- **设计期 Python API(空间标记)**:官方 `anylogic-design-time-api` **已作为 beta 发布(8.9.7+,需 Graphical Editor API Connector)**,能程序化生成**空间标记**(Path / Node / Conveyor / Robot / Crane / RackStorage / Rail / Road / Pipe… 共 42 个 wrapper 类)。这是 LLM 生成"模型结构"的**官方落点**,但**目前只覆盖空间布局,不含 flowchart / statechart 逻辑**。详见 §五更正。
- **IDE + Copilot 改 ALPX XML(L9)**:把模型存成 multi-part ALPX,让 Copilot agent 在 VS Code/GitHub 上改 —— 但 L9 只演示**改 `Description>` 元数据**(最安全一类),**未生成拓扑**;无官方 schema,脆弱,可复现性弱。

### 🔴 Tier D —— R&D,未发布(模型逻辑生成)
- **LLM 生成完整 flowchart / statechart 逻辑**:co-design 演讲里 GPT-5 + Cursor 经 Python API 一键生成完整流程图/状态图/参数([字幕](../references/transcripts/ai-model-and-modeler-co-design.txt))。**这是"端到端 AI 建模"的方向,但逻辑生成部分仍未发布。**

### ⛔ 跨层都做不到的
替你**拖拽 GUI**;替你做**抽象层次 / 方法的架构决策**(L3 的"艺术");**保证 100% 正确**;**理解你这个具体模型**的上下文。

## 五、需要更正的一处事实(设计期 Python API 已发 beta)

[literature-review.md](literature-review.md) 的 L4/L8 写"空间标记的 Python API 已在**公开路线图**,完整模型逻辑生成仍属**未发布 R&D**"。实际已往前一步:

> **设计期 Python API 已发布为 beta**(`anylogic-design-time-api` **8.9.7**,`Development Status :: 4 - Beta`,依赖 `py4j`,需 AnyLogic 8.9.7+ 配 Graphical Editor API Connector,用一次性 token 连到**正打开的编辑器**)——而且**已安装在本 repo 的 `.venv` 里**。它能程序化创建 **42 类空间标记**对象。

更准确的表述:**空间标记的代码化建模 = 已发布 beta(不再只是路线图);flowchart / statechart 逻辑生成 = 仍是 R&D**。这把 L4/L8 笼统的"设计期 API"拆成 **Tier C(空间标记,已 beta)+ Tier D(逻辑,未发布)**。

**仍未解的可及性问题**:该 beta 需要 8.9.7+ 与编辑器内的 Connector —— 这条通路在 **PLE / University / Professional** 各档是否都可用,尚需实测(承 L4/L7 的"许可证闸门"追踪项)。

## 六、一句话现状

> 嵌入式代码助手已经实用(Tier A);模型结构生成正从"无官方支持的旁路 / R&D"过渡到"**官方 beta,但仅限空间标记**"(Tier C);而真正难的部分 —— **动态逻辑生成**(Tier D)与**选对抽象层次**(人的活)—— 仍未被攻克。整个领域**缺乏严谨测量**,这正是本 repo 要补的空白。

## 七、对本 repo 的启示(下一步实验候选)

1. **设计期 API 首跑**:既然 `anylogic-design-time-api` 已在手,让 LLM 生成调用该 API 的 Python 脚本,程序化搭一个空间布局(如传送带网络),量化一次成功率与人工修正量——这是把 Tier C 操作化的天然首个实验。
2. **复现已知基线**:Bass 扩散(L1,参数已知)、单银行排队(L3,Fig 1.7)用当前模型重跑,量化"一次成功率"。
3. **LRPL 假设检验**:对照"裸 LLM" vs "AnyLogic 文档 RAG"的 API 幻觉率(L6 方法移植)。
4. **片段 vs 结构两类任务分别评测**(承 L4):验证二者难度差。

## 来源

全部源自本 repo 的 [literature-review.md](literature-review.md)(L1–L9)与其引用的一手材料;设计期 API 现状据本 repo `.venv` 内 `anylogic-design-time-api` 8.9.7 包元数据(2026-05-28 复核)。
