# 会话全程记录(实验经过)

> 本文记录这次实验**从无到有的完整经过**——选题、设计、每一次搭建往返、踩过的坑、以及打分方(Claude)自己的错误与纠正。
> 它与另外两份互补:[transcript.md](transcript.md) 是各阶段**锁定输出 + 官方对照**,[results.md](results.md) 是**逐项打分**,本文是**叙事性的全过程**。
> 环境:Claude Opus 4.7(`claude-opus-4-7`,被测兼记录者)· AnyLogic **8.9.8** PLE · macOS · 日期 2026-05-28。

---

## 0. 起点:从文献综述到"想动手"

- 会话最初任务是**整理 [literature-review.md](../../reports/literature-review.md)(L1–L9)并讨论"LLM 辅助建模:现在哪些方法/工具、能到什么程度"**。产出了综合报告 [llm-assisted-modeling-landscape.md](../../reports/llm-assisted-modeling-landscape.md)(两轴 × 五母题 × 成熟度阶梯)。
- 过程中发现一处与综述不符的事实:本 repo `.venv` 里**实装了 `anylogic-design-time-api` 8.9.7(beta)**,而 L4/L8 当时写它"未发布/仅在路线图"。据此**更正了 L4/L8、刷新了 overview、更新了 README/cspell**。
- 随后用户提出:**"我要实践,实验一下。"**(已装好 AnyLogic Personal + 本 repo 的 Python venv。)

## 1. 设计阶段:两次关键转向

1. **初始提案**:用刚发现的**设计期 Python API** 程序化生成**空间标记**(一个 path-node 矩形环网络)。读了官方 [dt-api.md](../../references/anylogic-help/advanced/code/dt-api.md),确认它是已发 beta、但**只能画空间标记**;并标出可行性闸门——PLE 是否有 "Graphical editor API connector" 未知。
2. **确定被测角色**:用户选择**由 Claude Opus 4.7 现场生成脚本/方案**(我即"被测 LLM"),当场记录、可复现。
3. **场景转向 → Bank Office**:用户指定用[官方 Bank Office 教程](https://anylogic.help/tutorials/bank-office/index.html)当场景。我 fetch 后发现**冲突**:Bank Office 是**纯 Process Modeling Library 流程图**模型(Source/Queue/Delay/Service…),而设计期 API **只能画空间标记、画不了流程块**(那是 Tier D 未发布 R&D)。如实抛出这个矛盾。
4. **方法转向 → Tier A**:用户选择**保留 Bank Office、把方法改成最主流的 Tier A**——LLM 出结构指引 + 嵌入式 Java/表达式,人在 GUI 拖块搭建,用官方 4 阶段教程当 ground truth。
5. **定下防污染协议**(实验有效性的关键):Claude 每阶段**先凭自然语言问题描述生成答案 → 写进 transcript 锁定 → 之后才查官方解法打分**。测"能不能想出来",而非"能不能复述教程"。
6. 阶段计划:**Phase 1 先行**(跑通闭环),再 Phase 3(加柜员)、Phase 4(利用率统计)。

## 2. Phase 1 — 单 ATM

- **锁定方案**:`Source→Queue→Delay→Sink`;Rate 0.6/min;Delay `triangular(0.8,1,2)` min、cap 1;时间单位 minutes;预测"无需 Java"。
- **GUI 小问答**:用户问"**要不要勾 Use multi-part ALP format?alp 是什么?**" → 解释 `.alp` 本质是描述模型的 XML、多部件格式对 git 友好且是 L9/Tier C「IDE 改模型 XML」工作流的前提,**建议勾上**;并建议存进实验文件夹。
- **搭建往返**:第一次"建好了"其实只建了空项目(Main 为空,从 XML 复核得知);提示后用户补齐 4 块并保存。
- **从 ALPX XML 复核**:`source/queue/delay/sink` 全是真实 `com.anylogic.libraries.processmodeling` 类;`rate=0.6 PER_MINUTE`、`queue.capacity=20`、`delay.delayTime=triangular(0.8,1,2)`;**零幻觉**。
- **对照官方**(锁定后查):官方 Rate **0.3**/min、`triangular(0.8,1.5,3.5)`、Queue cap **15**、ATM 用 **Delay**(非 Service)、minutes、无 Java。→ **结构/块选择/时间单位/"无需 Java"全中;参数"形对值偏"**。
- 用户实测 **Run 成功**,队列稳定。✅

## 3. Phase 3 — 加柜员(含一次被实测推翻的误判)

- **锁定方案**:Source 后插 `SelectOutput`(按概率 0.5 分流)→ 上路 ATM(Queue→Delay)、下路 `Service`(`tellerService`)占用 `ResourcePool tellers`(cap 3)、服务 `triangular(2,4,8)`;两路汇入 Sink。事先标注不确定点:用 Service 还是 Seize/Delay/Release、`utilization()` 方法名等。
- **GUI 小问答**:
  - "**`tellerService.out → sink.in` 怎么连?**" → 解释端口拖拽,并强调**一个输入口可接收多条连接**(delay 与 tellerService 可同入一个 sink,无需合并块)。
  - "**teller 是什么意思?**" → 银行柜员(对比 ATM 自助机)。
- 用户搭好、**Run 成功**、给截图。
- **从 XML 复核**:7 块齐全、接线与方案完全一致、Delay 改名 **ATM**、`tellerService` 占用 `{ { tellers } }`、`triangular(2,4,8)`;但 **SelectOutput 的概率/模式未显式设值**。
- **⚠️ Claude 的误判**:据"XML 无显式值"**臆断** SelectOutput 默认 = "If condition is true"→ 全走 ATM、柜员空转,**报了个"能跑但不分流"的静默 bug**。
- **对照官方**:SelectOutput **按概率 0.5**、cap **4**、`triangular(2.5,6,11)`、用 **Service**(非 Seize/Delay/Release)、无 Java → 结构/Service 判断/概率值全中。
- **用户用截图推翻误判**:"我没改任何东西,只是再 run 了一下"——属性面板显示 SelectOutput **默认即"With specified probability 0.5"**(灰色默认值);实测 **69/74 ≈ 50/50** 分流、柜员利用率 ~49%。**模型本就正确,没有 bug。**
- **Claude 当场认错并改正所有记录**。真正的教训(反转到打分方自己):**LLM 当"核查者"时也会从错误假设里凭空造出一个不存在的 bug;实跑观测才是 ground truth。** 读 XML 擅长核对"显式写下的结构/参数",但**推断"没写出来的默认值的行为"不可靠**。

## 4. Phase 4 — 利用率统计(核心 API 赌中,程序细节又栽)

- **锁定方案**:加 Bar Chart;ATM(Delay)利用率 `ATM.statsUtilization.mean()`(**自标"中-低信心",本阶段最不确定项**);柜员 `tellers.utilization()`;并(错误地)让用户"在 Statistics 区勾 Force statistics collection";预测 ATM≈0.38、Tellers≈0.49。
- **GUI 卡点**:用户"**找不到 Statistics 区**"。我先查本地文档镜像——`statsUtilization`、Process 库块类**都不在镜像里**,本地无法证实;遂 **fetch 官方 Phase 4**(方案已锁定,因用户卡住而提前查):
  - 官方逐字:"**Each Delay block has a `statsUtilization` data set**…",用 **`ATM.statsUtilization.mean()`** ——**我赌中了核心 API**;
  - 但统计**默认自动收集**,官方**没开任何开关** → 我"要手动开启"的假设**是错的**。
- 用户随后纠正:那个 **Force statistics collection 勾选框在 Advanced 区**(不是 Statistics 区),且**不必勾**。三方一致:核心 API 对、程序细节(区名 + 是否需开)错。
- 用户实跑截图:Bar Chart **ATM = 0.38、Tellers = 0.47**,无报错。→ **数值预测 ATM 精确命中、Tellers 接近**;ATM(单台)利用率低于 3 柜员,因柜员单次服务长得多。✅

## 5. 总体结论与回填

- **三阶段:模型结构、块选择、API/表达式、"要不要 Java"判断、定量预测——全部命中,零 API 幻觉;模型行为与排队论一致。**
- **错误的"形状"高度一致**:Claude 强在"**是什么**"(块/方法名),弱在"**在哪点 / 默认怎样**"(SelectOutput 默认、统计开关位置与必要性)——两次都靠**实跑/用户观测**纠正。
- **最反直觉的一条**:本场最实质的错误**出自 Claude 当"核查者"时**(臆造不存在的 bug),不在"建模者"时。→ LLM 辅助建模的风险**不只在生成端,也在审查端**。
- **回填 [landscape 报告](../../reports/llm-assisted-modeling-landscape.md)**:为 Tier A「常见模型 LLM 表现好」补一个量化正例;新增边界刻画——**「结构/API 可靠、UI 流程/默认行为不可靠」**,可作为后续跨模型评测的固定维度。压边界的下一步:换**非教科书模型**或测**结构生成**(设计期 API / `.alp`)。

## 6. 同会话续:Tier-C 经 XML 编辑(人搭框架 + LLM 改 XML)

Tier-A 跑通后,用户提议更保守的分工:**人在 client 搭框架,Claude 调 XML 参数**。两步都一次成功:

- **批量加 description(7 块)**:用户先在 GUI 给 1 块(ATM)加描述存盘 → Claude **diff 学到精确格式** → 批量写其余 6 块 → 重载 7/7 显示、模型照常开。
- **给 `sink.onEnter` 加会编译的 Java**:`traceln("Customer left at t=" + time() + " min");` → 重载后**编译通过、控制台逐条输出**;成对时间戳印证 ATM/柜员两路都入 sink。

关键:两次都**仿 AnyLogic 自己写出的格式**(diff 法),不是猜 schema——这是成功护城河,也呼应全场教训"以真样本/实跑为准"。**门槛**:description 只需"能打开",Java 需"能编译"(更高,也过了),但都属"填既有块的既有字段"。**未测的脆弱前沿**:新建 Function 等**新元素类型**、从零生成**拓扑结构**。详见 [results.md](results.md) 的 Tier-C 节。
