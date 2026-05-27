*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/OptQuestOptimization.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class OptQuestOptimization

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.opttek.optquest.COptQuestOptimization

com.anylogic.engine.OptQuestOptimization

All Implemented Interfaces:
:   `IOptimization`

---

```
public class OptQuestOptimization
extends com.opttek.optquest.COptQuestOptimization
implements IOptimization
```

A wrapper class for COptQuestOptimization. Sets the OptQuest license, and
defines two methods: Evaluate and MonitorStatus so that they call
experiment's evaluate() and monitor() correspondingly. Also takes care of
stopping the optimization if interrupted flag was set.

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OptQuestOptimization()` |  |

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
| `void` | `Evaluate(com.opttek.optquest.COptQuestSolution solution)` |  |
| `int` | `getBestIteration()` |  |
| `double` | `getBestObjectiveValue()` |  |
| `Object` | `getBestParam(IVariable variable)` |  |
| `double` | `getBestParamValue(IVariable variable)` |  |
| `int` | `getBestReplicationsNumber()` |  |
| `int` | `getCurrentIteration()` |  |
| `double` | `getCurrentObjectiveValue()` |  |
| `Object` | `getCurrentParam(IVariable variable)` |  |
| `double` | `getCurrentParamValue(IVariable variable)` |  |
| `int` | `getCurrentReplication()` |  |
| `int` | `getMaximumIterations()` |  |
| `int` | `getNumberOfCompletedIterations()` |  |
| `int` | `getSelectedNthBestIteration()` | Deprecated. |
| `double` | `getSelectedNthBestObjectiveValue()` | Deprecated. |
| `Object` | `getSelectedNthBestParam(IVariable variable)` | Deprecated. |
| `double` | `getSelectedNthBestParamValue(IVariable variable)` | Deprecated. |
| `int` | `getSelectedNthBestReplicationsNumber()` | Deprecated. |
| `boolean` | `isBestSolutionFeasible()` |  |
| `boolean` | `isCurrentSolutionFeasible()` |  |
| `boolean` | `isLastReplication()` |  |
| `boolean` | `isSelectedNthBestSolutionFeasible()` |  |
| `boolean` | `isStarted()` |  |
| `final boolean` | `isUseReplications()` |  |
| `void` | `MonitorStatus(com.opttek.optquest.COptQuestSolution sol)` |  |
| `Throwable` | `performParallel(boolean restart)` |  |
| `Throwable` | `performSerial(boolean restart)` |  |
| `void` | `prepareRestart()` |  |
| `void` | `selectNthBestSolution(int bestSolutionIndex)` | Deprecated. |
| `void` | `setAutoStop(boolean stop)` |  |
| `void` | `setCurrentObjectiveValue(IObjective objective, double value)` |  |
| `void` | `setCurrentPostConstraintValue(IPostConstraint requirement, double value)` |  |
| `void` | `setCurrentPreConstraintValue(IPreConstraint constraint, double value)` |  |
| `void` | `setExperiment(ExperimentOptimization<?> experiment)` |  |
| `void` | `setFixedReplicationsNumber(int replicationsNumber)` |  |
| `void` | `setMaximumIterations(int numberOfIterations)` |  |
| `void` | `setParameterSuggestedValue(IVariable variable, Object value)` |  |
| `void` | `setPostConstraint(IPostConstraint requirement, double bound, ConstraintTypeEnum type)` |  |
| `void` | `setPreConstraint(IPreConstraint constraint, double bound, ConstraintTypeEnum type, String expression)` |  |
| `void` | `setUserControlledStop(boolean stop)` |  |
| `void` | `setUseReplications(boolean useReplications)` |  |
| `void` | `setVariableReplicationsNumber(int minimumReplications, int maximumReplications, ExperimentMultipleRuns.ConfidenceLevel confidenceLevel, double errorPercent)` |  |
| `void` | `stopOptimization()` |  |
| `void` | `validateInput()` |  |
