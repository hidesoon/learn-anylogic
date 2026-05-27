*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentMultipleRuns.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentMultipleRuns<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

[com.anylogic.engine.Experiment](Experiment.md "class in com.anylogic.engine")<ROOT>

[com.anylogic.engine.ExperimentRunFast](ExperimentRunFast.md "class in com.anylogic.engine")<ROOT>

com.anylogic.engine.ExperimentMultipleRuns<ROOT>

Type Parameters:
:   `ROOT` - class of top-level agent

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

Direct Known Subclasses:
:   `ExperimentOptimization`, `ExperimentParamVariation`

---

```
public abstract class ExperimentMultipleRuns<ROOT extends Agent>
extends ExperimentRunFast<ROOT>
```

Base class for all experiments that support multiple simulation runs (e.g.
optimization, parameter variation)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentMultipleRuns)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `ExperimentMultipleRuns.ConfidenceLevel` | Confidence level constants |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final ExperimentMultipleRuns.ConfidenceLevel` | `CONFIDENCE_LEVEL_80` | Confidence level constant `80%` |
| `static final ExperimentMultipleRuns.ConfidenceLevel` | `CONFIDENCE_LEVEL_90` | Confidence level constant `90%` |
| `static final ExperimentMultipleRuns.ConfidenceLevel` | `CONFIDENCE_LEVEL_95` | Confidence level constant `95%` |
| `static final ExperimentMultipleRuns.ConfidenceLevel` | `CONFIDENCE_LEVEL_98` | Confidence level constant `98%` |
| `static final ExperimentMultipleRuns.ConfidenceLevel` | `CONFIDENCE_LEVEL_99` | Confidence level constant `99%` |
| `static final ExperimentMultipleRuns.ConfidenceLevel` | `CONFIDENCE_LEVEL_99_9` | Confidence level constant `99.9%` |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentMultipleRuns(boolean singleEngine)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract int` | `getCurrentIteration()` | Returns the current iteration number (1, 2...) |
| `abstract int` | `getCurrentReplication()` | Returns the replication number for the current iteration (1, 2...)  Ensure replications are used ([`isUseReplications()`](#isUseReplications())) before calling this method |
| `final Engine` | `getEngine()` | **It is strongly recommended not to call this method because of possible parallel execution environment.** |
| `abstract int` | `getMaximumIterations()` | Returns the total number of iterations being performed in this experiment |
| `Object` | `getMutexRead_xjal()` | *This field shouldn't be called by user*  is public due to technical reasons |
| `Object` | `getMutexWrite_xjal()` | *This field shouldn't be called by user*  is public due to technical reasons |
| `int` | `getNumberOfCompletedIterations()` | Returns the number of completed iterations. |
| `int` | `getParallelEvaluatorsCount()` | Returns the number of parallel evaluators used in this experiment. |
| `double` | `getProgress()` | Returns the progress of the experiment: a number between 0 and 1 corresponding to the part of the experiment completed so far (based on iteration count), or `-1` if this cannot be calculated. |
| `final int` | `getRunCount()` | Returns the number of the current simulation run, more precisely the number of times the model was destroyed. |
| `double[]` | `getSimulationProgress_xjal(double[] output)` | *This method is not designed to be called by user and may be changed/removed in the future releases.*  Returns the progress of the parallel simulation runs: an array of numbers between 0 and 1. |
| `long` | `getStep()` | Returns the number of events executed by the engine. |
| `abstract boolean` | `isLastReplication()` | Return `true` if we have run the last replication for the current iteration |
| `abstract boolean` | `isUseReplications()` | Returns `true` if experiment uses replications |
| `void` | `onAfterExperiment()` | User's extension point for *after experiment code*.  Executed when all planned iterations are completed. |
| `void` | `onAfterIteration()` | User's extension point for *after iteration code*  By default does nothing |
| `void` | `onDestroy_xjal()` | *This method normally shouldn't be called by user.*  Is called when the experiment object is dynamically disposed - before closing the model window.  This method should be overridden to release resources (e.g. |
| `void` | `registerExperimentHost_xjal(IExperimentHost experimentHost)` | **This method isn't designed to be called by user.**  *Public due to technical reasons*  May be removed in future releases |
| `abstract void` | `setFixedReplicationsNumber(int replicationsNumber)` | Sets experiment to use a fixed number of replications.  No confidence testing is to be used  For confidence testing use [`setVariableReplicationsNumber(int, int, ConfidenceLevel, double)`](#setVariableReplicationsNumber(int,int,com.anylogic.engine.ExperimentMultipleRuns.ConfidenceLevel,double))    *This is setup method, user should not call it* |
| `abstract void` | `setUseReplications(boolean useReplications)` | Sets experiment to use replications    *This is setup method, user should not call it* |
| `abstract void` | `setVariableReplicationsNumber(int minimumReplications, int maximumReplications, ExperimentMultipleRuns.ConfidenceLevel confidenceLevel, double errorPercent)` | Sets experiment to stop replications after the minimum replications when the confidence level is reached (i.e. |
