# Results

> 逐项打分与官方对照。Claude 的方案先锁在 [transcript.md](transcript.md),此处在「搭建 + 查官方解法」后填写。
> 官方 Phase 1 解法来源:<https://anylogic.help/tutorials/bank-office/1-creating-simple-model.html>(2026-05-28 抓取)。

## Phase 1 — 单 ATM

### 一次成功(用户在 PLE 实测)

- 结构是否按方案搭出(从 ALPX XML 复核):**是** —— 4 块 + 3 连接器,`source→queue→delay→sink`,全部为真实 `com.anylogic.libraries.processmodeling` 类。
- 是否首跑无报错:**是**(用户实测 Run 成功)。行为符合预期:顾客流经 Source→Queue→Delay→Sink,ATM 一次一人,队列稳定不发散。
- 调试迭代轮数:**0**(首版即可搭,无报错回喂)。
- 人工修正:**0 处实质修正**(唯一差异:用户把 Delay 的 `capacity` 留默认,而默认即 1,与方案等价)。

### 对照官方教程

| 维度 | Claude 方案(锁定) | 官方 Phase 1 | 评判 |
|---|---|---|---|
| 块与拓扑 | Source→Queue→Delay→Sink | Source→Queue→Delay→Sink | ✅ **完全一致** |
| ATM 用 Delay 还是 Service | **Delay**(cap 1) | **Delay**(renamed "ATM") | ✅ **判断正确**(我曾自标此为不确定点,赌对了) |
| 到达定义 | Rate,**0.6 /min** | Rate,**0.3 /min** | ◐ 模式/单位对,值偏高 2× |
| 服务时间分布 | **triangular(0.8, 1.0, 2.0)** min | **triangular(0.8, 1.5, 3.5)** min | ◐ 分布族/形对、min 同(0.8),mode/max 偏小(我低估了服务时长) |
| 队列容量 | 20 | 15 | ◐ 同量级,均为"给足"的任意值 |
| 模型时间单位 | minutes | minutes | ✅ 一致 |
| 自定义 Java | 预测"**无需**,仅内置 `triangular()` 表达式" | 无自定义代码 | ✅ **预测正确** |

### API 幻觉检查

- **0 处幻觉**。方案给的块名(Source/Queue/Delay/Sink)、字段名(`rate`/`capacity`/`delayTime`/Specified time)在 ALPX XML 与官方教程里全部真实存在。对比 L1 里 ChatGPT 杜撰「Decision」block,本次未出现。

### 稳定性核对(两套参数都合理)

- Claude:λ=0.6/min,服务均值 1.27 min → 服务率 0.79/min,**ρ≈0.76**(偏忙但稳定)。
- 官方:λ=0.3/min,服务均值 1.93 min → 服务率 0.52/min,**ρ≈0.58**(更闲)。
- 两者均为稳定的 M/G/1 型队列,队列有限可见、不发散——Claude 的"稳定性自检"成立,只是把系统调得更忙。

### Phase 1 结论

**成功(结构与方法层面满分,参数层面"形对值偏")**。

- 结构、块类型选择(Delay 非 Service)、时间单位、"无需 Java"判断——**全部命中官方**;一次成功、零迭代、零幻觉、零实质人工修正。
- 唯一偏差在**具体数值**(到达率、服务分布的 mode/max、队列容量),但都落在合理域、模型仍稳定。这正符合预期:问题描述里没给数值,LLM 只能"合理假设";数值本应由建模者按真实数据定,不是结构能力的考点。
- **最值得记住的一条**:对**教科书型模型**(银行排队 ≈ M/G/1),带文档的 Claude Opus 4.7 在"结构 + 块选择 + 嵌入式表达式"上几乎零摩擦——印证 L1/landscape「常见模型 LLM 表现好」。真正的能力边界要靠**新颖/非教科书模型**与**动态逻辑**(Phase 3 加柜员分流、统计)去压。

## Phase 3 — 加柜员

> 官方 Phase 3 解法来源:<https://anylogic.help/tutorials/bank-office/3-adding-tellers.html>(2026-05-28 抓取)。

### 结构/方法(从 ALPX XML 复核)

- 7 块齐全:Source / Queue / Delay(改名 **ATM**)/ Sink / **SelectOutput** / **ResourcePool(`tellers`)** / **Service(`tellerService`)**,全部真实 `processmodeling` 类。
- 连线**与方案完全一致**:`source→selectOutput`;`outT→queue→ATM→sink`;`outF→tellerService→sink`。
- Service 正确占用资源池:`resourceSets = { { tellers } }`,seize 数量默认 1。
- 用户还按可选项加了 **TimePlot**,`Expression2 = tellers.utilization()` —— **证明 `utilization()` 是真方法(编译运行通过),非幻觉**。

### 对照官方

| 维度 | Claude 方案(锁定) | 官方 Phase 3 | 评判 |
|---|---|---|---|
| 新增块 | SelectOutput + Service + ResourcePool | 同 | ✅ 完全一致 |
| 柜员用 Service 还是 Seize+Delay+Release | **Service** | **Service** | ✅ **赌对(不确定点 #1)** |
| 分流机制 | SelectOutput **按概率 0.5** | SelectOutput **按概率 0.5** | ✅ 机制 + 数值都中 |
| 柜员数(ResourcePool capacity) | 3 | **4** | ◐ 形对,值差 1 |
| 柜员服务时间 | triangular(2, 4, 8) min | **triangular(2.5, 6, 11)** min | ◐ 分布族对、min 近;我又低估了时长(同 Phase 1 模式) |
| 利用率方法 | `tellers.utilization()` | (Phase 4 才正式画;方法名一致) | ✅ 方法真实 |
| 自定义 Java | 预测"无需" | 无 | ✅ 预测正确 |

### API 幻觉检查

- **0 处幻觉**。SelectOutput / Service / ResourcePool 的类名、`resourceSets` 配置、`tellers.utilization()` 在 XML 中全部真实、且编译运行通过。

### 关键发现(含一处被实测推翻的误判)

- **实测结论:模型正确,分流正常。** 用户实跑截图:`selectOutput` 143 进 → **69 走 ATM(true)/ 74 走柜员(false)**,约 50/50;`tellers` **2/3 忙、利用率 ~49%**;sink 收 142。行为完全符合意图。
- **被实测推翻的误判(诚实记录)**:Claude(打分方)曾据 XML「`probability`/`conditionIsProbabilistic` 无显式值」**臆断** SelectOutput 默认 =「If condition is true」(condition=`true`)→ 全走 ATM、柜员空转,并据此报了个「静默 bug」。**这是错的。** 用户**未改任何设置**的属性面板显示:`Select True output` 默认即 **「With specified probability」、Probability 默认 0.5**(灰色=未编辑的默认值)。即**默认本身就做 50/50 概率分流**,留默认照样正确。
- **真正的教训(反转到打分方自己)**:这恰好再次印证「**别靠假设、要验证行为**」——只不过这次犯错的是 **Claude 对一个默认值的臆断**,而**用户的实跑观测**才是 ground truth,把它纠正了过来。比「LLM 帮人建模会出错」更微妙的一条:**LLM 当『评审/核查者』时,也会从错误假设里凭空造出一个并不存在的 bug;人去实跑、看行为,才是最终裁决。**
- **方法论小结**:读 XML 能高效核对**结构与显式参数**(这部分本次全对、零幻觉);但**推断「未显式设置项的默认行为」不可靠**——默认值要么查官方文档、要么以实跑为准,不能从「XML 里没写」反推。

### Phase 3 结论

**结构/方法再次满分、且模型实测正确。** SelectOutput-vs-Service 判断、分流机制(按概率)、概率值 0.5、`utilization()` 方法、无 Java——全中、零幻觉;用户实跑确认 ~50/50 分流(69/74)、柜员利用率 ~49%,行为正确。参数延续"形对值偏"(柜员 3 vs 官方 4、服务时间 triangular(2,4,8) vs (2.5,6,11) 偏短),不影响正确性。

**本阶段最大教训出在打分方(Claude),不在被测建模能力**:Claude 据"XML 无显式值"臆断 SelectOutput 默认行为、误报了一个**并不存在的"静默 bug"**,被用户实跑(截图)推翻。记一笔——核查者(LLM)对**默认值**的假设同样需要验证;**实跑观测 > 纸面推断**。讽刺地反向印证了 landscape 母题 #2(verify behavior),只是这次该被 verify 的是 Claude 自己的断言。

## Phase 4 — 收集利用率统计

> 官方 Phase 4 解法来源:<https://anylogic.help/tutorials/bank-office/4-collecting-utilization-statistics.html>(2026-05-28 抓取,因用户卡在 statsUtilization 步骤而提前查阅;Claude 的方案已先锁定于 transcript)。

### 实测(用户运行截图)

- Bar Chart 两根柱:**ATM = 0.38、Tellers = 0.47**;分流 ~50/50(203/202);`tellers` 2/3 忙(46%)。
- `ATM.statsUtilization.mean()` **无报错、正常出值**。

### 对照官方 + Claude 预测

| 维度 | Claude 方案(锁定) | 官方 Phase 4 / 实测 | 评判 |
|---|---|---|---|
| ATM(Delay)利用率表达式 | **`ATM.statsUtilization.mean()`**(自标"中-低信心") | 官方逐字相同:"Each Delay block has a `statsUtilization` data set…",用 `ATM.statsUtilization.mean()` | ✅ **赌中(且是事先标注最不确定的一项)** |
| 图表 | Bar Chart(Analysis 调色板) | Bar Chart(Analysis) | ✅ |
| 柜员利用率 | `tellers.utilization()` | 官方本阶段只画 ATM;`utilization()` 已于 Phase 3 验证 | ✅(在官方基础上的合理扩展) |
| 自定义 Java | 预测"无需" | 无 | ✅ |
| 数值预测 | ATM≈0.38、Tellers≈0.49 | 实测 ATM **0.38**、Tellers **0.47** | ✅ ATM 精确命中、Tellers 接近 |
| **要不要 / 在哪开统计** | 让用户"在 Statistics 区勾 Force statistics collection" | 实际:统计**默认自动收集**(官方没开);那个勾选框**在 Advanced 区、且不必勾** | ❌ **程序性细节错**(区名错 + 误判"需手动开") |

### API 幻觉检查

- 核心 API **0 幻觉**:`statsUtilization.mean()` / `utilization()` 均真实可用、运行通过。
- 唯一不准的是 **UI 流程**(把 "Force statistics collection" 误放进 "Statistics 区",又一度过度修正为"压根没有该勾选框")——非幻觉 API,而是对 GUI 位置/默认行为的臆断。

### Phase 4 结论

**结构/核心 API/数值预测全部命中(含事先标注最不确定的 `statsUtilization.mean()`),零 Java、零 API 幻觉。** 唯一栽的还是**程序性细节**:统计开关的所在区(Advanced 非 Statistics)与"是否需要手动开启"(默认自动收集,不必开)。与 Phase 3 的 SelectOutput 误判同一模式——**Claude 对"块/方法名"记得准,对"UI 在哪点 / 默认行为如何"靠不住,只有实跑/查文档能定。**

## Tier-C 延伸:人搭框架 + LLM 经 XML 编辑(同一 test-bank · 同会话续)

> Tier-A 跑通后,继续测 L4/L9 那条"LLM 直接改模型 XML"的难度梯度(landscape Tier C)。分工:人在 GUI 搭好框架,Claude 直接编辑多部件 ALPX 文件;每步以 AnyLogic 重新加载/编译/运行为验收。

**两步,均一次成功:**

1. **加元数据(description)到全部 7 个块** —— 先让用户在 GUI 给 1 个块(ATM)加描述并保存,Claude **diff 学到精确格式**(`<Description><![CDATA[…]]>` 紧跟 `<Name>`),再批量写入其余 6 块。重载后 7/7 显示、模型照常打开,**零返工**、XML well-formed。
2. **给 `sink.onEnter` 注入会编译的 Java 行为** —— 写入 `traceln("Customer left at t=" + time() + " min");`(`<Value Class="CodeValue"><Code>` 包法,仿 AnyLogic 自身序列化)。重载后**编译通过、运行时控制台逐条输出**;近乎同时的成对时间戳印证 ATM 与柜员两路都汇入 sink。

**发现:**

- **"改既有 XML 且仿 AnyLogic 自己的序列化"是可靠的** —— 元数据 ✅、**会编译会跑的 Java 行为** ✅,均一次成。
- **护城河 = 先拿一个真样本再仿(diff 法)**:description 与 code-value 的格式都不是猜的,是从 AnyLogic 自己写出的 XML 学的——与全场教训一致:**别臆断序列化/默认,以真样本/实跑为准**。
- **门槛对比**:description 只需"能打开";Java 行为需"能编译"——后者更高却也过了。但二者仍属"**填既有块的既有字段**",不是"生成新结构"。
- **尚未测、也是真正脆弱的前沿**:① 新建**全新元素类型**(如 Function 元件)——无样本即从零生成;② 从零生成**流程图拓扑**(块 + 连接 + 一致的 ID 交叉引用)。这两者才是 L4/L9 的核心开放问题。

**Tier-C 小结**:在"人搭框架 + LLM 改 XML"分工下,**LLM 可靠胜任 (a) 元数据编辑、(b) 给既有块填会编译的 Java 动作**;真正难的"生成新元素/新拓扑"尚待专门实验(建议续作,沿用 diff 法逐步逼近)。

