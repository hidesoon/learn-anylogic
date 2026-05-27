*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/optquest/OptQuestDiscreteVariable.html>*

---

Package [com.anylogic.engine.optimization.optquest](package-summary.md)

# Class OptQuestDiscreteVariable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.optimization.optquest.OptQuestVariable](OptQuestVariable.md "class in com.anylogic.engine.optimization.optquest")

com.anylogic.engine.optimization.optquest.OptQuestDiscreteVariable

All Implemented Interfaces:
:   `IBoundedVariable`, `IDiscreteVariable`, `IVariable`

---

```
public class OptQuestDiscreteVariable
extends OptQuestVariable
implements IDiscreteVariable
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OptQuestDiscreteVariable()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `convertToDouble(Object object)` |  |
| `Object` | `convertToObject(double value)` |  |
| `DiscreteParameterDataType` | `getDataType()` |  |
| `void` | `set(String name, DiscreteParameterDataType dataType, String min, String max, String step)` |  |
