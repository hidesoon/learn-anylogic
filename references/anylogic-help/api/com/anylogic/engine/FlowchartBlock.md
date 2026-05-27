*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/FlowchartBlock.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class FlowchartBlock

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

[com.anylogic.engine.Agent](Agent.md "class in com.anylogic.engine")

com.anylogic.engine.FlowchartBlock

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `IMaintenanceable`, `com.anylogic.engine.internal.Child`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

---

```
public abstract class FlowchartBlock
extends Agent
```

Base class for all process flowchart blocks in new libraries since AnyLogic 7.
Provides standard functions like [`remove(Agent)`](#remove(com.anylogic.engine.Agent)).

Since:
:   7.0

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.FlowchartBlock)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `FlowchartBlock()` |  |
| `FlowchartBlock(Engine engine, Agent owner, AgentList<?> collection)` | Standard Agent constructor |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `FlowchartActivityType` | `defaultAgentActivityType()` | Returns activity type info (used in e.g. |
| `FlowchartBlock` | `getFlowchartBlockRepresentative()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `FlowchartBlock` | `getFlowchartBlockRepresentative(Agent agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isCountersVisible()` | Returns `true` if port / block counters are shown |
| `boolean` | `isInsideFlowchartBlock()` | Returns `true` if this block is a part of some flowchart block |
| `boolean` | `isLoggingToDB(LoggingType loggingType)` | Returns `true` if this agent and its internals may log their data/changes/activity to AnyLogic built-in database (logging options are configurable in the properties of Database / Log in the Projects tree inside AnyLogic) |
| `boolean` | `isPortStateAnimated()` | Returns `true` if states of ports are shown (usually by colored outline). |
| `Agent` | `remove(Agent agent)` | Removes the given agent from the block and returns it. |
| `Agent` | `remove(Agent agent, FlowchartBlock receiver)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Agent` | `resume(Agent agent)` | Tells the block to resume (previously suspended) processing for the given agent. |
| `void` | `setCountersVisible(boolean visible)` | Shows or hides port / block counters |
| `Agent` | `suspend(Agent agent)` | Tells the block to suspend processing the given agent. |
