# 实验:LLM 辅助搭建 Bank Office 模型(Tier A)

> 本文件 = 设计 + 结论摘要。配套:[session-log.md](session-log.md) 完整经过(叙事)· [transcript.md](transcript.md) 各阶段锁定输出 + 官方对照 · [results.md](results.md) 逐项打分 · [capability-assessment.md](capability-assessment.md) 能力评估(已验证 / 待验证)· [test-bank/](test-bank/) 多部件 ALPX 模型 · [raw-session.jsonl](raw-session.jsonl) 原始对话日志(Claude Code session `1ef6b6c6-70e8-4b91-a720-af7b6b362364` 快照)。

## 元信息

- **日期**:2026-05-28
- **被测 LLM + 版本**:Claude Opus 4.7(`claude-opus-4-7`,1M context)—— 在「带 AnyLogic 官方文档上下文」条件下(见局限)
- **工具档位**:AnyLogic Personal Learning Edition(PLE)
- **场景**:Bank Office —— 官方 Process Modeling 教程 <https://anylogic.help/tutorials/bank-office/index.html>(4 阶段:①简单 ATM 模型 ②动画 ③加柜员 ④利用率统计)
- **方法档位**:Tier A(LLM 出结构指引 + 嵌入式 Java/表达式;人在 GUI 拖块搭建)——见 [现状全景 Tier A](../../reports/llm-assisted-modeling-landscape.md)

## 研究问题

给一段**自然语言问题描述**(非官方解法),Claude Opus 4.7 能否产出正确的 Bank Office 模型结构(该用哪些 Process 块、怎么连、参数/分布)+ 可用的嵌入式 Java/表达式?需要多少人工修正?会不会幻觉 AnyLogic API?

## 方法

L1 webinar 式工作流,分工:

| 谁 | 做什么 |
|---|---|
| Claude(被测) | ①结构指引(块 + 拓扑 + 每个属性填什么);②需要代码处的 Java 片段/分布表达式/统计函数;③逐步 GUI 操作说明 |
| 用户 | 在 PLE 里照着拖块搭建、运行,把「跑通/报错/看起来不对」回喂 |
| 一起 | Claude 锁定答案后,对照官方教程打分,记入 `results.md` |

### 🔑 防污染协议(实验有效性的关键)

Claude **每阶段先凭问题描述生成答案 → 写进 `transcript.md` 锁定 → 之后才查官方解法细节来打分**。测的是「LLM 能不能想出来」,而非「能不能复述教程」。

- 已知的高层结构(银行排队 ≈ Source→Queue→Delay→Sink;加柜员 ≈ Service+ResourcePool)属通用建模常识,是被测的**及格线**,允许已知。
- **未预读**官方的具体参数值、分布、统计函数写法。

## 阶段计划

- **Phase 1 —— 单 ATM**(本次先行):Source → Queue → Delay → Sink。先把「LLM 出方案 → GUI 搭 → 跑通 → 回喂」闭环跑通。
- Phase 3 —— 加柜员(跑通后再做):Service + ResourcePool + SelectOutput 分流 + 利用率统计。
- Phase 2 动画 / Phase 4 统计:按需并入。

## 成功标准(Phase 1)

1. 按 Claude 的方案,模型在 PLE 里**能编译、能运行、无报错**。
2. 顾客流经 Source→Queue→Delay→Sink;ATM 一次服务一人,等待时队列可见。
3. 「能编译 ≠ 逻辑对」:行为合理(队列不无限爆、不瞬间清空)。

## 评测指标(记入 `results.md`)

- 结构正确性(块 + 拓扑 vs 官方)
- 参数/分布合理性
- **API 幻觉**(是否编造不存在的块/方法,呼应 L1 的「Decision」block)
- Java 片段/表达式正确性
- 人工修正次数 · 调试迭代轮数

## 用到的 prompt

见 [transcript.md](transcript.md)。若提炼出可复用的好 prompt,反哺 [prompts/](../../prompts/)。

## 结论

**Phase 1 — 成功(结构/方法满分,参数"形对值偏")**。详见 [results.md](results.md)。

- Claude Opus 4.7(带文档)从纯自然语言描述出发,**一次**给出与官方完全一致的结构:Source→Queue→Delay→Sink、ATM 用 **Delay** 非 Service(自标的不确定点赌对了)、时间单位 minutes、并正确预测「Phase 1 无需自定义 Java」。
- **零幻觉 API、零迭代、零实质人工修正**(用户搭出的 ALPX XML 逐块核对全部对得上)。
- 唯一偏差是**具体数值**(到达率 0.6 vs 官方 0.3 /min;服务 triangular(0.8,1,2) vs (0.8,1.5,3.5);队列容量 20 vs 15)——均在合理域、模型稳定;数值本就该由建模者按真实数据定,不是结构能力考点。
- **启示**:教科书型模型(银行排队 ≈ M/G/1)上,Tier A「LLM 出结构+嵌入式表达式、人在 GUI 搭」几乎零摩擦,印证 L1/landscape「常见模型 LLM 表现好」。能力边界要靠 **Phase 3(加柜员分流/资源/统计)** 与**非教科书模型**去压。
- **副产物**:多部件 ALPX = 可读 XML,使「从模型文件复核 LLM 产出」成为可能(本次打分即据此),呼应 L4/L9 的 XML 路径。

**Phase 3 — 加柜员(结构/方法满分,模型实测正确)**。SelectOutput + Service + ResourcePool、用 Service 而非 Seize/Delay/Release、概率 0.5、`utilization()`——全中、零幻觉;实测 ~50/50 分流、柜员利用率 ~49%。**本阶段最大的错来自打分方 Claude**:据 XML 臆断 SelectOutput 默认行为、误报一个不存在的"静默 bug",被用户实跑推翻(默认即概率 0.5)。

**Phase 4 — 利用率统计(核心 API + 数值预测全中)**。`ATM.statsUtilization.mean()`(事先标注最不确定项)赌中、Bar Chart 对、无 Java 对;实测 **ATM 0.38(预测 0.38)、Tellers 0.47(预测 0.49)**。唯一错的又是**程序性细节**:把统计开关说成 "Statistics 区"(实为 Advanced)、误判"需手动开启"(实为默认自动)。

## 总体结论(Phase 1+3+4)

**一句话**:对 Bank Office 这种**教科书型 DES**,Claude Opus 4.7(带文档)在 Tier A 用法上几乎零摩擦——**三阶段的模型结构、块选择、API/表达式、"是否需要 Java" 判断,以及定量预测,全部命中,零 API 幻觉**;模型最终行为也与排队论一致(ATM 0.38 < 3 柜员 0.47)。

**最有价值、也最反复出现的发现 —— 错误的"形状"很一致**:

- ✅ **Claude 强在"是什么"**:用哪些块、怎么连、调哪个方法(`triangular`/`utilization`/`statsUtilization.mean`)、要不要写 Java —— 稳。
- ❌ **Claude 弱在"在哪/默认怎样"**:SelectOutput 的默认行为、统计开关在哪个属性区/要不要开 —— **两次都栽在这类程序性/默认值臆断上**,且都是**实跑/用户观测**才纠正的。
- 🔁 一个意外但重要的转折:本实验**最实质的一次错误出自 Claude 当"核查者"时**(凭 XML 臆造了一个不存在的 bug),而非当"建模者"时。说明 LLM 辅助建模的风险**不只在生成端,也在审查端**;**实跑观测是最终裁决**。

**对 landscape 报告的回填**:这为 Tier A「常见模型 LLM 表现好」补了一个量化正例;同时新增一条边界刻画——**「结构/API 可靠、UI 流程/默认行为不可靠」**,值得作为后续跨模型评测的一个固定维度。下一步若要压边界,应换**非教科书模型**或测**结构生成**(设计期 API / `.alp`)。

## 局限

1. 单次、n=1;非统计性评测。
2. 被测模型处于**「带文档」条件**(官方 dt-api/Java 文档与 PML 知识在 Claude 上下文/训练内),非「裸模型」——结论是「LLM+文档」的上限,不代表零上下文表现。
3. 仅 Process Modeling Library 的 DES 流程;未测空间标记/设计期 API/RL。
4. 「被测」与「打分」均由 Claude 参与,存在自评偏倚;防污染协议(先锁后查)部分缓解,但用户的独立核对是更强的把关。
