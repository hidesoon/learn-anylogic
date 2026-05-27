*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/IDowntime.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface IDowntime<T>

---

```
public interface IDowntime<T>
```

An interface to play the role of the Downtime block in the engine environment. User interacts with instances of this interface
when querying the list of Downtime blocks connected to the maintenanceable markups.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `customFirstOccurrence(T unit)` | Enables the custom trigger values for the first downtime occurrence. |
| `int` | `cyclesToFirstOccurrence(T unit)` | Defines the number of working cycles from the start of the resource unit's life to the first occurrence of this downtime. |
| `int` | `cyclesToOccurrence(T unit)` | Defines the number of working cycles between subsequent occurrences of this downtime. |
| `String` | `getName()` |  |
| `boolean` | `isActive(IMaintenanceable unit)` |  |
| `boolean` | `mayPreempt(T unit)` | Sets whether the downtime task may preempt the task currently being executed, if any. |
| `double` | `priority(T unit)` | Sets the priority of the downtime task |
| `void` | `restartTriggers(IMaintenanceable unit)` | Resets triggers' countdowns and starts waiting for the next triggering events. |
| `Schedule<Boolean>` | `schedule(T unit)` | Schedule of type "on/off", where each "on" period starts a downtime. |
| `void` | `startTask(IMaintenanceable unit)` | Starts this task logic (maintenance / failure-repair / custom) right now for the given resource unit and resets all the triggers according to their settings. |
| `void` | `stopTask(IMaintenanceable unit)` | [Actual for "Delay until stopTask() is called" downtime task type] Finishes this downtime task logic (maintenance / failure-repair / custom) right now for the given resource unit and restarts all the triggers according to their settings. |
| `double` | `taskDuration(T unit, TimeUnits timeUnits)` | [Actual for "Delay" downtime task type, when downtime uses cyclic occurrence triggers, not schedule] The duration of downtime task (maintenance, failure, etc.). |
| `boolean` | `timeStartsAfterTaskEnd()` | [Actual for "total time" trigger] Depending on this parameter, the total (working+idling) time between subsequent occurrences of the downtime starts countdown either from the beginning or from the end of the corresponding "downtime task". |
| `double` | `totalTimeToFirstOccurrence(T unit, TimeUnits timeUnits)` | Defines the total (working+idling) time from the start of the resource unit's life to the first occurrence of this downtime. |
| `double` | `totalTimeToOccurrence(T unit, TimeUnits timeUnits)` | Defines the total (working+idling) time between subsequent occurrences of this downtime. |
| `double` | `workingTimeToFirstOccurrence(T unit, TimeUnits timeUnits)` | Defines the working time from the start of the resource unit's life to the first occurrence of this downtime. |
| `double` | `workingTimeToOccurrence(T unit, TimeUnits timeUnits)` | Defines the working time between subsequent occurrences of this downtime. |
