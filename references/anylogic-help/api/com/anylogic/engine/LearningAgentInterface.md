*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LearningAgentInterface.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface LearningAgentInterface<O,A,C>

Type Parameters:
:   `O` - Observation data structure type, see `ExperimentReinforcementLearning#getObservation(Agent, Object)`
:   `A` - Action data structure type, see `ExperimentReinforcementLearning#applyAction(Agent, Object)`
:   `C` - Configuration data structure type, see `ExperimentReinforcementLearning#applyConfiguration(Agent, Object)`

All Superinterfaces:
:   `Serializable`

---

```
public interface LearningAgentInterface<O,A,C>
extends Serializable
```

Data communication interface designed for use with [`ExperimentReinforcementLearning`](ExperimentReinforcementLearning.md "class in com.anylogic.engine"): describes
the interaction between the model and Learning Platform / pre-trained Learning Agent

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `A` | `takeAction(O observation, A emptyAction)` |  |
