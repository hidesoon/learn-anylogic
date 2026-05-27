*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/IContinuousVariable.html>*

---

Package [com.anylogic.engine.optimization](package-summary.md)

# Interface IContinuousVariable

All Superinterfaces:
:   `IBoundedVariable`, `IVariable`

All Known Implementing Classes:
:   `MetalContinuousVariable`, `OptQuestContinuousVariable`

---

```
public interface IContinuousVariable
extends IBoundedVariable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default OptimizationParameterType` | `getParameterType()` |  |
| `void` | `set(String name, String min, String max)` |  |
