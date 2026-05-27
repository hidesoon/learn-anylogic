*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/optquest/OptQuestContinuousVariable.html>*

---

Package [com.anylogic.engine.optimization.optquest](package-summary.md)

# Class OptQuestContinuousVariable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.optimization.optquest.OptQuestVariable](OptQuestVariable.md "class in com.anylogic.engine.optimization.optquest")

com.anylogic.engine.optimization.optquest.OptQuestContinuousVariable

All Implemented Interfaces:
:   `IBoundedVariable`, `IContinuousVariable`, `IVariable`

---

```
public class OptQuestContinuousVariable
extends OptQuestVariable
implements IContinuousVariable
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OptQuestContinuousVariable()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertToDouble(Object object)` |  |
| `Object` | `convertToObject(double value)` |  |
| `void` | `set(String name, String min, String max)` |  |
| `void` | `setMax(String value)` |  |
| `void` | `setMin(String value)` |  |
