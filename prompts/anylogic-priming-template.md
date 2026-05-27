# AnyLogic Priming(预热)提示词模板

把下面这段贴在对话开头,一次性教会 LLM 把"通用 Java 环境"映射到 AnyLogic,之后就不用每次重复解释。出自 AnyLogic 官方 webinar 推荐的 "seeding" 技巧。

## 模板

```
我在用 AnyLogic(基于 Java 的仿真软件)写代码,请遵守以下映射规则:
- Agent 类型 ≈ Java 的 class
- 对象从 palette 拖出、在 properties 面板配置;构造参数 ≈ 模型里的 parameter
- population(智能体群) ≈ 一个 ArrayList,并带自动生成的函数如 add_<populationName>()
- AnyLogic 内置函数可直接调用(无前缀):time()、traceln()、uniform()、
  exponential()、getIndex()、getOwner() 等
- 模型元素的方法用点号:event.restart()、statechart.receiveMessage() 等
- import 语句放在专门的 import 区
我需要的是能粘进 AnyLogic 字段的代码片段,不是独立的完整 Java 程序。
除非我要求,否则只给单行/最小片段。请给我标准 Java 之外的 AnyLogic 专用写法。
```

## 使用提示

- 贴完模板后,再描述你的具体需求(目标、涉及的 collection 名/agent 类型/返回值)。
- 它跑偏(比如写了一整个 class)时直接打断:"我只要一行版本"。
- 想重置上下文就开新对话。

## 迭代记录

> 在这里记录你对模板的改进:哪条规则有用、补充了什么、什么场景下需要额外上下文。

- 2026-05-27:初版,基于官方 webinar 的 seeding 思路。
