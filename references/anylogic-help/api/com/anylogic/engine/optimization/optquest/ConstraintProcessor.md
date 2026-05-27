*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/optquest/ConstraintProcessor.html>*

---

Package [com.anylogic.engine.optimization.optquest](package-summary.md)

# Class ConstraintProcessor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.optimization.optquest.ConstraintProcessor

---

```
public class ConstraintProcessor
extends Object
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConstraintProcessor()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static List<Pair<Pattern,String>>` | `getOptQuestParameterNameTransformers(Map<OptQuestVariable,String> optQuestParameterNames)` | Converts mapping {Parameter -> NewName} to pairs {Pattern\_For\_Parameter\_Name -> NewName} |
| `static LinearConstraint` | `parseLinearConstraint(Collection<OptQuestVariable> optParameters, String expression, ConstraintTypeEnum type, double bound)` | Parses expression and if it is linear, returns a result |
| `static com.opttek.optquest.COptQuestConstraint` | `prepareLinearConstraint(LinearConstraint linearConstraint)` |  |
| `static com.opttek.optquest.COptQuestStringConstraint` | `prepareNonLinearConstraint(Map<OptQuestVariable,String> variables, String expression, ConstraintTypeEnum type, double bound)` |  |
| `static String` | `transformExpression(String expression, List<Pair<Pattern,String>> transformations)` | Applies all patterns to given expression |
