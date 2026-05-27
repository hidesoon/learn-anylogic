*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentRunFast.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentRunFast<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

[com.anylogic.engine.Experiment](Experiment.md "class in com.anylogic.engine")<ROOT>

com.anylogic.engine.ExperimentRunFast<ROOT>

Type Parameters:
:   `ROOT` - class of top-level agent

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

Direct Known Subclasses:
:   `ExperimentCompareRuns`, `ExperimentMultipleRuns`

---

```
public abstract class ExperimentRunFast<ROOT extends Agent>
extends Experiment<ROOT>
```

Base class for all experiments that support fast simulation run (e.g.
optimization, parameter variation, compare runs)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentRunFast)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentRunFast(boolean singleEngine)` | Creates the experiment, a new simulation engine is created. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Engine` | `getEngine()` | Returns the engine executing the model. |
| `double` | `getProgress()` | Returns the progress of the experiment: a number between 0 and 1 corresponding to the part of the experiment completed so far (based on iteration count or time limit), or `-1` if this cannot be calculated. |
| `final double` | `getRunTimeSeconds()` | Returns the real duration of the experiment in seconds.  This includes simulation run time and excludes pause times. |
| `final Experiment.State` | `getState()` | Returns the current state of the experiment. |
| `final void` | `pause()` | Pauses the model execution.  This method has different behavior depending on context where it is called: When this method is called from *the model execution thread, from control action code, or from on-click code of a shape*, it returns immediately. |
| `void` | `registerExperimentHost_xjal(IExperimentHost experimentHost)` | **This method isn't designed to be called by user.**  *Public due to technical reasons*  May be removed in future releases |
| `final void` | `run()` | Runs the model from the current state. |
| `final void` | `step()` | Performs one step of the model execution. |
| `final void` | `stop()` | Terminates the model execution, destroys and forgets the model and calls garbage collector, but keeps all experiment data.  This method has different behavior depending on context where it is called: When this method is called from *the model execution thread, from control action code, or from on-click code of a shape*, it returns immediately. |
