*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/IVariable.html>*

---

Package [com.anylogic.engine.optimization](package-summary.md)

# Interface IVariable

All Known Subinterfaces:
:   `IBinaryVariable`, `IBoundedVariable`, `IContinuousVariable`, `IDiscreteVariable`

All Known Implementing Classes:
:   `MetalBinaryVariable`, `MetalContinuousVariable`, `MetalDiscreteVariable`, `MetalVariable`, `OptQuestBinaryVariable`, `OptQuestContinuousVariable`, `OptQuestDiscreteVariable`, `OptQuestVariable`

---

```
public interface IVariable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getName()` |  |
| `OptimizationParameterType` | `getParameterType()` |  |
| `void` | `setName(String name)` |  |
