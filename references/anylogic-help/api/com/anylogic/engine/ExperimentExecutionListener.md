*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentExecutionListener.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExperimentExecutionListener

All Superinterfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public interface ExperimentExecutionListener
extends Serializable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   * [`Experiment.addExecutionListener(ExperimentExecutionListener)`](Experiment.md#addExecutionListener(com.anylogic.engine.ExperimentExecutionListener))
    * [`Experiment.removeExecutionListener(ExperimentExecutionListener)`](Experiment.md#removeExecutionListener(com.anylogic.engine.ExperimentExecutionListener))

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default void` | `onAfterSimulationRun(Agent root)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `default void` | `onBeforeSimulationRun(Agent root)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
