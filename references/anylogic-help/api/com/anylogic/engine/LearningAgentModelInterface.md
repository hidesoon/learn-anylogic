*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LearningAgentModelInterface.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface LearningAgentModelInterface<ROOT extends Agent>

Type Parameters:
:   `ROOT` - root model agent type

All Superinterfaces:
:   `Serializable`

All Known Implementing Classes:
:   `ExperimentReinforcementLearning`

---

```
@AnyLogicInternalAPI
public interface LearningAgentModelInterface<ROOT extends Agent>
extends Serializable
```

Internal interface designed for different usage patterns with Reinforcement Learning

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `takeActionForModel(ROOT root)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
