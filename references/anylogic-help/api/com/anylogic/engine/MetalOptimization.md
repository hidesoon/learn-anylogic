*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/MetalOptimization.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class MetalOptimization

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.MetalOptimization

All Implemented Interfaces:
:   `IOptimization`

---

```
public class MetalOptimization
extends Object
implements IOptimization
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MetalOptimization()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addObjective(IObjective objective)` |  |
| `void` | `addParameter(IVariable variable)` |  |
| `void` | `addPostConstraint(IPostConstraint requirement)` |  |
| `void` | `addPreConstraint(IPreConstraint constraint)` |  |
| `void` | `addSuggestedSolution()` |  |
| `void` | `continueOptimization()` |  |
| `IBinaryVariable` | `createBooleanVariable()` |  |
| `IContinuousVariable` | `createContinuousVariable()` |  |
| `IDiscreteVariable` | `createDiscreteVariable()` |  |
| `IObjective` | `createObjective()` |  |
| `IPostConstraint` | `createPostConstraint()` |  |
| `IPreConstraint` | `createPreConstraint()` |  |
| `int` | `getBestIteration()` |  |
| `double` | `getBestObjectiveValue()` |  |
| `Object` | `getBestParam(IVariable param)` |  |
| `double` | `getBestParamValue(IVariable param)` |  |
| `int` | `getBestReplicationsNumber()` |  |
| `int` | `getCurrentIteration()` |  |
| `double` | `getCurrentObjectiveValue()` |  |
| `Object` | `getCurrentParam(IVariable parameter)` |  |
| `double` | `getCurrentParamValue(IVariable param)` |  |
| `int` | `getCurrentReplication()` |  |
| `int` | `getMaximumIterations()` |  |
| `int` | `getNumberOfCompletedIterations()` |  |
| `boolean` | `isBestSolutionFeasible()` |  |
| `boolean` | `isCurrentSolutionFeasible()` |  |
| `boolean` | `isLastReplication()` |  |
| `boolean` | `isStarted()` |  |
| `Throwable` | `performParallel(boolean restart)` |  |
| `Throwable` | `performSerial(boolean restart)` |  |
| `void` | `prepareRestart()` |  |
| `void` | `setAutoStop(boolean stop)` |  |
| `void` | `setCurrentObjectiveValue(IObjective objective, double value)` |  |
| `void` | `setCurrentPostConstraintValue(IPostConstraint requirement, double value)` |  |
| `void` | `setCurrentPreConstraintValue(IPreConstraint constraint, double value)` |  |
| `void` | `setExperiment(ExperimentOptimization<?> experimentOptimization)` |  |
| `void` | `setFixedReplicationsNumber(int replicationsNumber)` |  |
| `void` | `setMaximumIterations(int numberOfIterations)` |  |
| `void` | `setParameterSuggestedValue(IVariable variable, Object value)` |  |
| `void` | `setPostConstraint(IPostConstraint postConstraint, double bound, ConstraintTypeEnum type)` |  |
| `void` | `setPreConstraint(IPreConstraint constraint, double bound, ConstraintTypeEnum type, String expression)` |  |
| `void` | `setUserControlledStop(boolean stop)` |  |
| `void` | `stopOptimization()` |  |
| `void` | `validateInput()` |  |
