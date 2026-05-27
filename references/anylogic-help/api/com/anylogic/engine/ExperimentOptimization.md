*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentOptimization.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentOptimization<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

[com.anylogic.engine.Experiment](Experiment.md "class in com.anylogic.engine")<ROOT>

[com.anylogic.engine.ExperimentRunFast](ExperimentRunFast.md "class in com.anylogic.engine")<ROOT>

[com.anylogic.engine.ExperimentMultipleRuns](ExperimentMultipleRuns.md "class in com.anylogic.engine")<ROOT>

com.anylogic.engine.ExperimentOptimization<ROOT>

Type Parameters:
:   `ROOT` - class of top-level agent

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

---

```
public abstract class ExperimentOptimization<ROOT extends Agent>
extends ExperimentMultipleRuns<ROOT>
```

Experiment used to search for optimal solutions. Uses OptQuest optimizer. To
use this experiment you need to subclass from it and define the methods
[`setupRootParameters(Agent, boolean)`](#setupRootParameters(ROOT,boolean)) which needs to retrieve the
parameter values suggested by OptQuest and [`Experiment.onEngineFinished()`](Experiment.md#onEngineFinished()) to set
the objective according to simulation output.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentOptimization)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentOptimization()` | Creates the experiment, a new simulation engine, and a new optimizer that will be used throughout the whole experiment execution. |
| `ExperimentOptimization(boolean allowParallelEvaluations)` | Same as [`ExperimentOptimization()`](#%3Cinit%3E()) but allows to disable parallel evaluations on multicore/multiprocessor systems (which are enabled by default) |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConstraint(IPreConstraint constraint)` |  |
| `void` | `addParameterVariable(IVariable parameter)` | Adds the variable defined by the input parameter to the optimization    *This is optimization setup method, user should not call it* |
| `void` | `addRequirement(IPostConstraint requirement)` | Adds the requirement defined by the input parameter to the optimization    *This is optimization setup method, user should not call it* |
| `void` | `addSuggestedSolution()` | This method signals the completion of a suggested solution definition.  `#setParameterVariableSuggestedValue(COptQuestVariable, double)` is used to set a value for each variable.  This method signals a value has been set for each variable.  The solution is added to the set of suggested solution and will be one of the first solutions evaluated if the optimization has not started.  If the optimization is running, the suggested solution will be one of the next solutions to be evaluated    *This is optimization setup method, user should not call it* |
| `IBinaryVariable` | `createBinaryVariable_xjal()` |  |
| `IContinuousVariable` | `createContinuousVariable_xjal()` |  |
| `IDiscreteVariable` | `createDicsreteVariable_xjal()` |  |
| `IObjective` | `createObjective_xjal()` |  |
| `static com.opttek.optquest.COptQuestOptimization` | `createOptimization(Engine engine)` | Creates and returns new OptQuest optimization instance for Custom Experiment  This method should only be used in custom experiment code  *This method is designed for use in the AnyLogic Professional only* |
| `static com.opttek.optquest.COptQuestOptimization` | `createOptimization(Engine engine, OptimizationCallback callback)` | Creates and returns new OptQuest optimization instance for Custom Experiment with objective function defined in a free form using [evaluate](OptimizationCallback.md#evaluate(com.opttek.optquest.COptQuestOptimization,com.opttek.optquest.COptQuestSolution,com.anylogic.engine.Engine)) method of a special callback. |
| `IPostConstraint` | `createPostConstraint_xjal()` |  |
| `IPreConstraint` | `createPreConstraint_xjal()` |  |
| `void` | `evaluateConstraints(List<? extends IPreConstraint> constraints, List<? extends IVariable> variables)` |  |
| `void` | `evaluateSerial(int iteration)` | Is called to obtain and set a value of the objective function corresponding to the currently suggested set of parameters (decision variables). |
| `int` | `getBestIteration()` | Returns the iteration that resulted in the best solution thus far  (solution may be infeasible) |
| `double` | `getBestObjectiveValue()` | Returns the value of the objective function for the best solution found thus far  Returned value may be infeasible |
| `double` | `getBestParamValue(IVariable parameter)` | Returns the value of the given optimization parameter variable for the best solution found thus far  (solution may be infeasible) |
| `int` | `getBestReplicationsNumber()` | Returns the number of replications that were run for the best solution  (solution may be infeasible)  Ensure replications are used ([`isUseReplications()`](#isUseReplications())) before calling this method |
| `int` | `getCurrentIteration()` | Returns the current value of iteration counter |
| `double` | `getCurrentObjectiveValue()` | Returns the value of the objective function for the current solution |
| `Object` | `getCurrentParam(IVariable optimizationParameterVariable)` |  |
| `double` | `getCurrentParamValue(IVariable parameter)` | Returns the value of the given optimization parameter variable for the current solution |
| `int` | `getCurrentReplication()` | Returns the replication number for the current solution being evaluated  Ensure replications are used ([`isUseReplications()`](#isUseReplications())) before calling this method |
| `int` | `getMaximumIterations()` | Returns the number of iterations set by [`setMaximumIterations(int)`](#setMaximumIterations(int)) |
| `int` | `getNumberOfCompletedIterations()` | Returns the current value of iteration counter |
| `com.opttek.optquest.COptQuestOptimization` | `getOptimization()` | Deprecated. the method is deprecated and available only with OptQuest optimization engine. |
| `abstract OptimizationEngine` | `getOptimizationEngineType()` |  |
| `final double` | `getProgress()` | Returns the progress of the experiment: a number between 0 and 1 corresponding to the part of the experiment completed so far (based on iteration count or time limit), or `-1` if this cannot be calculated. |
| `int` | `getSelectedNthBestIteration()` | Returns the iteration number for the Nth best solution, where the Nth best solution is identified by the method [`selectNthBestSolution(int)`](#selectNthBestSolution(int)) |
| `double` | `getSelectedNthBestObjectiveValue()` | Returns the objective value for the Nth best solution, identified by the method [`selectNthBestSolution(int)`](#selectNthBestSolution(int)) |
| `double` | `getSelectedNthBestParamValue(IVariable parameter)` | Used to retrieve the value of the variable for the solution that produced the Nth best objective value  The Nth best solution is identified by calling [`selectNthBestSolution(int)`](#selectNthBestSolution(int)) |
| `int` | `getSelectedNthBestReplicationsNumber()` | Returns the number of replications for the Nth best solution, where the Nth best solution is identified by the method [`selectNthBestSolution(int)`](#selectNthBestSolution(int))  Ensure replications are used ([`isUseReplications()`](#isUseReplications())) before calling this method |
| `boolean` | `isBestSolutionFeasible()` | Returns `true` if the best solution satisfies all constraints and requirements |
| `boolean` | `isCommandEnabled(Experiment.Command cmd)` | Checks if a command can be executed. |
| `boolean` | `isCurrentSolutionBest()` | Returns `true` if current solution is the best one at this moment |
| `boolean` | `isCurrentSolutionFeasible()` | Returns `true` if current solution satisfies all constraints and requirements |
| `boolean` | `isLastReplication()` | Deprecated. |
| `boolean` | `isParallel()` |  |
| `boolean` | `isSelectedNthBestSolutionFeasible()` | Returns `true` if nth best solution satisfies all constraints and requirements |
| `final boolean` | `isUseReplications()` | Returns `true` if optimization uses replications |
| `ROOT` | `prepareRoot(Engine engine)` |  |
| `void` | `selectNthBestSolution(int bestSolutionIndex)` | Called by the user to identify the Nth best soluiton.  Subsequent calles to [`getSelectedNthBestObjectiveValue()`](#getSelectedNthBestObjectiveValue()) and [`getSelectedNthBestParamValue(IVariable)`](#getSelectedNthBestParamValue(com.anylogic.engine.optimization.IVariable)) methods use this setting to identify the solution. |
| `void` | `setAutoStop(boolean stop)` | Sets the auto stop option.  If the input parameter is `true`, auto stop is turned on. |
| `void` | `setConstraint(IPreConstraint constraint, double bound, ConstraintTypeEnum type, String expression)` |  |
| `void` | `setCurrentObjectiveValue(double value)` | Used to set the value of the objective for the current solution. |
| `void` | `setCurrentPreConstraintValue_xjal(IPreConstraint constraint, double value)` |  |
| `void` | `setCurrentRequirementValue_xjal(IPostConstraint requirement, double value)` | Used to set the value of the requirement for the current solution. |
| `void` | `setFixedReplicationsNumber(int replicationsNumber)` | Sets experiment to use a fixed number of replications.  No confidence testing is to be used  For confidence testing use [`ExperimentMultipleRuns.setVariableReplicationsNumber(int, int, ConfidenceLevel, double)`](ExperimentMultipleRuns.md#setVariableReplicationsNumber(int,int,com.anylogic.engine.ExperimentMultipleRuns.ConfidenceLevel,double))    *This is setup method, user should not call it* |
| `void` | `setLogBufferLength(int length)` |  |
| `void` | `setMaximumIterations(int numberOfIterations)` | Sets the number of iterations the optimization should perform before stopping. |
| `void` | `setObjectiveMaximize()` | Sets the goal of the optimization to maximize the objective value    *This is optimization setup method, user should not call it* |
| `void` | `setObjectiveMinimize()` | Sets the goal of the optimization to minimize the objective value    *This is optimization setup method, user should not call it* |
| `void` | `setParameterSuggestedValue(IVariable parameter, Object value)` | Allows the user to suggest a solution by setting a suggested value for each variable  [`addSuggestedSolution()`](#addSuggestedSolution()) indicates the suggested solution is complete and should be added to the set of solutions to be evaluated.    *This is optimization setup method, user should not call it* |
| `void` | `setParameterVariable(IBinaryVariable parameter, String name)` |  |
| `void` | `setParameterVariable(IContinuousVariable parameter, String name, String min, String max)` |  |
| `void` | `setParameterVariable(IDiscreteVariable parameter, String name, DiscreteParameterDataType dataType, String min, String max, String step)` |  |
| `void` | `setRequirement(IPostConstraint requirement, double bound, ConstraintTypeEnum type)` |  |
| `abstract void` | `setupRootParameters(ROOT root, boolean callOnChangeActions)` | Is called to setup parameters of top-level agent. |
| `void` | `setUserControlledStop(boolean stop)` | Indicates the user will stop the optimization by calling the [`stopOptimization()`](#stopOptimization()) method    *This is optimization setup method, user should not call it* |
| `void` | `setUseReplications(boolean useReplications)` | Sets optimization to use replications    *This is optimization setup method, user should not call it* |
| `void` | `setVariableReplicationsNumber(int minimumReplications, int maximumReplications, ExperimentMultipleRuns.ConfidenceLevel confidenceLevel, double errorPercent)` | Sets experiment to stop replications after the minimum replications when the confidence level is reached (i.e. |
| `void` | `stopOptimization()` | Stops the currently running optimization    *This is optimization setup method, user should not call it* |
