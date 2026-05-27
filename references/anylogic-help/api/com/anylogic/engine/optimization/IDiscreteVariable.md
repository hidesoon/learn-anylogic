*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/IDiscreteVariable.html>*

---

Package [com.anylogic.engine.optimization](package-summary.md)

# Interface IDiscreteVariable

All Superinterfaces:
:   `IBoundedVariable`, `IVariable`

All Known Implementing Classes:
:   `MetalDiscreteVariable`, `OptQuestDiscreteVariable`

---

```
public interface IDiscreteVariable
extends IBoundedVariable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `DiscreteParameterDataType` | `getDataType()` |  |
| `default OptimizationParameterType` | `getParameterType()` |  |
| `void` | `set(String name, DiscreteParameterDataType parameterType, String min, String max, String step)` |  |
