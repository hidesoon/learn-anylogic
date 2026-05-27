*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentCompareRuns.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentCompareRuns<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

[com.anylogic.engine.Experiment](Experiment.md "class in com.anylogic.engine")<ROOT>

[com.anylogic.engine.ExperimentRunFast](ExperimentRunFast.md "class in com.anylogic.engine")<ROOT>

com.anylogic.engine.ExperimentCompareRuns<ROOT>

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

---

```
public abstract class ExperimentCompareRuns<ROOT extends Agent>
extends ExperimentRunFast<ROOT>
```

Experiment used to run simulation several times with different parameter
values set by user before each run.
To use this experiment you need to subclass from it and override method
[`Experiment.onEngineFinished()`](Experiment.md#onEngineFinished()).

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentCompareRuns)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentCompareRuns()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final double` | `getProgress()` | Returns the progress of the experiment: in this case it is the same as the progress of the current simulation run. |
| `boolean` | `isCommandEnabled(Experiment.Command cmd)` | Checks if a command can be executed. |
| `void` | `onDestroy_xjal()` | *This method normally shouldn't be called by user.*  Is called when the experiment object is dynamically disposed - before closing the model window.  This method should be overridden to release resources (e.g. |
| `abstract void` | `setupRootParameters(ROOT root, boolean callOnChangeActions)` | Is called to setup parameters of top-level agent. |
