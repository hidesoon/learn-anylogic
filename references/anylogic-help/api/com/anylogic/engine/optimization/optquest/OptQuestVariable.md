*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/optquest/OptQuestVariable.html>*

---

Package [com.anylogic.engine.optimization.optquest](package-summary.md)

# Class OptQuestVariable

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.optimization.optquest.OptQuestVariable

All Implemented Interfaces:
:   `IBoundedVariable`, `IVariable`

Direct Known Subclasses:
:   `OptQuestBinaryVariable`, `OptQuestContinuousVariable`, `OptQuestDiscreteVariable`

---

```
public abstract class OptQuestVariable
extends Object
implements IBoundedVariable
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OptQuestVariable()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract double` | `convertToDouble(Object object)` |  |
| `abstract Object` | `convertToObject(double value)` |  |
| `String` | `getName()` |  |
| `com.opttek.optquest.COptQuestVariable` | `getOQVariable()` |  |
| `void` | `setName(String name)` |  |
