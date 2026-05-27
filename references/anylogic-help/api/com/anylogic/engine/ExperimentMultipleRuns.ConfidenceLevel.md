*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentMultipleRuns.ConfidenceLevel.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Enum Class ExperimentMultipleRuns.ConfidenceLevel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[ExperimentMultipleRuns.ConfidenceLevel](ExperimentMultipleRuns.ConfidenceLevel.md "enum class in com.anylogic.engine")>

com.anylogic.engine.ExperimentMultipleRuns.ConfidenceLevel

All Implemented Interfaces:
:   `Serializable`, `Comparable<ExperimentMultipleRuns.ConfidenceLevel>`, `Constable`

Enclosing class:
:   [ExperimentMultipleRuns](ExperimentMultipleRuns.md "class in com.anylogic.engine")<[ROOT](ExperimentMultipleRuns.md "type parameter in ExperimentMultipleRuns") extends [Agent](Agent.md "class in com.anylogic.engine")>

---

```
public static enum ExperimentMultipleRuns.ConfidenceLevel
extends Enum<ExperimentMultipleRuns.ConfidenceLevel>
```

Confidence level constants

See Also:
:   * [`ExperimentMultipleRuns.setVariableReplicationsNumber(int, int, ConfidenceLevel, double)`](ExperimentMultipleRuns.md#setVariableReplicationsNumber(int,int,com.anylogic.engine.ExperimentMultipleRuns.ConfidenceLevel,double))

## Nested Class Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `getOptQuestConstant()` | Returns corresponding `int` constant for use with OptQuest API |
| `int` | `getStudentTableIndex()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static ExperimentMultipleRuns.ConfidenceLevel` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static ExperimentMultipleRuns.ConfidenceLevel[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
