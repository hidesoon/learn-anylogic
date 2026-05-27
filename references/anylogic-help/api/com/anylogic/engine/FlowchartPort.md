*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/FlowchartPort.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class FlowchartPort<InMessageType,OutMessageType>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Port](Port.md "class in com.anylogic.engine")<InMessageType,OutMessageType>

com.anylogic.engine.FlowchartPort<InMessageType,OutMessageType>

Type Parameters:
:   `InMessageType` - the type of messages being received by the port
:   `OutMessageType` - the type of messages being sent by the port

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

Direct Known Subclasses:
:   `FlowchartMappedPort`

---

```
public abstract class FlowchartPort<InMessageType,OutMessageType>
extends Port<InMessageType,OutMessageType>
```

Special Port class for flowchart blocks.
See also [`Port`](Port.md "class in com.anylogic.engine")

Since:
:   7.0

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`Port`](Port.md "class in com.anylogic.engine")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.FlowchartPort)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `FlowchartPort(FlowchartBlock ao)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract long` | `count()` | Returns the number of agents passed through this port so far |
| `FlowchartBlock` | `getAgent()` | Returns the agent that owns the port. |
| `FlowchartBlock` | `getFlowchartBlockRepresentative()` | Returns the flowchart block which is the representative block for this port.  The returned value differs from [`getAgent()`](#getAgent()) in case when this is the port of the block from internal flowchart of some other flowchart-block. |
| `FlowchartBlock` | `getFlowchartBlockRepresentative(Agent agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isCannotAccept()` | Returns `true` if this (input) port can't accept agents at the current time. |
| `abstract boolean` | `isError()` | Returns `true` if there is an error with this port, e.g. |
| `boolean` | `isPortStateAnimated()` | Returns `true` if states of port are shown (usually by colored outline). |
| `boolean` | `isReadyToExit()` | Returns `true` if there is some agent ready to exit this (output) port. |
| `abstract void` | `markError()` | Marks this port as having error |
| `String` | `toString()` | Returns formatted number of agents passed through this port so far |
