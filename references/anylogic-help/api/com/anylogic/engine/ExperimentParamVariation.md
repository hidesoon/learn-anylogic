*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentParamVariation.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentParamVariation<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

[com.anylogic.engine.Experiment](Experiment.md "class in com.anylogic.engine")<ROOT>

[com.anylogic.engine.ExperimentRunFast](ExperimentRunFast.md "class in com.anylogic.engine")<ROOT>

[com.anylogic.engine.ExperimentMultipleRuns](ExperimentMultipleRuns.md "class in com.anylogic.engine")<ROOT>

com.anylogic.engine.ExperimentParamVariation<ROOT>

Type Parameters:
:   `ROOT` - class of top-level agent

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

---

```
public abstract class ExperimentParamVariation<ROOT extends Agent>
extends ExperimentMultipleRuns<ROOT>
```

Experiment used to run simulation several times with different parameter
values. To use this experiment you need to subclass from it.
By default, this experiment works in range parameters variation mode
(override [`getRangeParametersNumber()`](#getRangeParametersNumber()),
[`calculateRangeParameterValuesNumbers()`](#calculateRangeParameterValuesNumbers()),
[`setupRangeVariedParameter(Agent, int, int, boolean)`](#setupRangeVariedParameter(ROOT,int,int,boolean)),
[`setupRootParameters(Agent, int, boolean)`](#setupRootParameters(ROOT,int,boolean)) methods),
for freeform parameters override [`getMaximumIterations()`](#getMaximumIterations()) and
[`setupRootParameters(Agent, int, boolean)`](#setupRootParameters(ROOT,int,boolean)) methods
Experiments which use replications should call
[`setUseReplications(boolean)`](#setUseReplications(boolean)) and
[`setFixedReplicationsNumber(int)`](#setFixedReplicationsNumber(int)) or
[`setVariableReplicationsNumber(int, int, com.anylogic.engine.ExperimentMultipleRuns.ConfidenceLevel, double)`](#setVariableReplicationsNumber(int,int,com.anylogic.engine.ExperimentMultipleRuns.ConfidenceLevel,double)) from overridden
`#setup(java.awt.Container)` method,
For varied replications number mode also
[`getValueForConfidenceComputation(Agent)`](#getValueForConfidenceComputation(ROOT)) method should be
overridden define

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentParamVariation)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentParamVariation()` |  |
| `ExperimentParamVariation(boolean allowParallelEvaluations)` | Same as [`ExperimentParamVariation()`](#%3Cinit%3E()) but allows to disable parallel evaluations on multicore/multiprocessor systems (which are enabled by default) |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int[]` | `calculateRangeParameterValuesNumbers()` | This method should be overridden in experiments which work with parameters varied in range  This method will be called only one time |
| `boolean` | `evaluateStopConditions(ROOT root)` | User's extension point for *experiment stop conditions*  By default returns `false` |
| `int` | `getCurrentIteration()` | Returns the current iteration number (1, 2...) |
| `int` | `getCurrentReplication()` | Returns the replication number for the current iteration (1, 2...)  Ensure replications are used ([`ExperimentMultipleRuns.isUseReplications()`](ExperimentMultipleRuns.md#isUseReplications())) before calling this method |
| `int` | `getMaximumIterations()` | Returns total number of iterations being performed in this experiment  Default implementation works with range varied parameters  Override in subclass if experiment uses free-form parameters |
| `int` | `getNumberOfCompletedIterations()` | Returns the number of completed iterations. |
| `final double` | `getProgress()` | Returns the progress of the experiment: a number between 0 and 1 corresponding to the part of the experiment completed so far (based on iteration count or time limit), or `-1` if this cannot be calculated. |
| `int` | `getRangeParametersNumber()` | This method should be overridden to return the number of parameters varied in range in the corresponding experiments |
| `double` | `getValueForConfidenceComputation(ROOT root)` | Returns the value used in confidence computation when experiment uses replications and variable replications number is used  Must be implemented in a subclass in such experiments. |
| `final boolean` | `isLastReplication()` | Return `true` if we have run the last replication for the current iteration |
| `final boolean` | `isUseReplications()` | Returns `true` if experiment uses replications |
| `void` | `setFixedReplicationsNumber(int replicationsNumber)` | Sets experiment to use a fixed number of replications.  No confidence testing is to be used  For confidence testing use [`ExperimentMultipleRuns.setVariableReplicationsNumber(int, int, ConfidenceLevel, double)`](ExperimentMultipleRuns.md#setVariableReplicationsNumber(int,int,com.anylogic.engine.ExperimentMultipleRuns.ConfidenceLevel,double))    *This is setup method, user should not call it* |
| `void` | `setupRangeVariedParameter(ROOT root, int paramIndex, int valueIndex, boolean callOnChangeActions)` | This method should be overridden in experiments which work with parameters varied in range |
| `void` | `setupRootParameters(ROOT root, int index, boolean callOnChangeActions)` | Setups all parameters of top-level agent  Default implementation works only with range varied parameters  Override in subclass if experiment uses freeform parameters or uses range varied parameters and has fixed parameters, in this case overridden method should call `super.setupRootParameters(root, index);` and then setup values for fixed parameters |
| `void` | `setUseReplications(boolean useReplications)` | Sets experiment to use replications    *This is setup method, user should not call it* |
| `void` | `setVariableReplicationsNumber(int minimumReplications, int maximumReplications, ExperimentMultipleRuns.ConfidenceLevel confidenceLevel, double errorPercent)` | Sets experiment to stop replications after the minimum replications when the confidence level is reached (i.e. |
