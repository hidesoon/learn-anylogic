*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseLogState.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseLogState

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseLogState

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public class DatabaseLogState
extends Object
implements Serializable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

This class is responsible for storing some intermediate state required by the model logging.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.database.DatabaseLogState)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DatabaseLogState()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `generateAgentElementId()` | This method generates new id for dynamically created agent elements |
| `int` | `generateAgentId()` | Internal method, used to initialize [`Agent.getId()`](../Agent.md#getId()) property |
| `int` | `getAgentTypeElementId(LoggingType loggingType, Agent agent, String elementName)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getAgentTypeId(Agent agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `<T extends Enum<T> & IStatechartState<?, T>> int` | `getAgentTypeStateId(Agent agent, Statechart<T> statechart, T state)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getEventId(EventOriginator event)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `getStatechartId(Statechart<?> statechart)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetBeforeStart()` |  |
