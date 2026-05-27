*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/optimization/IOptimization.html>*

---

Package [com.anylogic.engine.optimization](package-summary.md)

# Interface IOptimization

All Known Implementing Classes:
:   `MetalOptimization`, `OptQuestOptimization`

---

```
public interface IOptimization
```

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
| `Object` | `getBestParam(IVariable parameter)` |  |
| `double` | `getBestParamValue(IVariable parameter)` |  |
| `int` | `getBestReplicationsNumber()` |  |
| `int` | `getCurrentIteration()` |  |
| `double` | `getCurrentObjectiveValue()` |  |
| `Object` | `getCurrentParam(IVariable parameter)` |  |
| `double` | `getCurrentParamValue(IVariable parameter)` |  |
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
| `void` | `setPostConstraint(IPostConstraint constraint, double bound, ConstraintTypeEnum type)` |  |
| `void` | `setPreConstraint(IPreConstraint constraint, double bound, ConstraintTypeEnum type, String expression)` |  |
| `void` | `setUserControlledStop(boolean stop)` |  |
| `void` | `stopOptimization()` |  |
| `void` | `validateInput()` |  |
