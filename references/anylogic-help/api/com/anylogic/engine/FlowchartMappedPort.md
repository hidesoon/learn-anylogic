*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/FlowchartMappedPort.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class FlowchartMappedPort<InMessageType,OutMessageType>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Port](Port.md "class in com.anylogic.engine")<InMessageType,OutMessageType>

[com.anylogic.engine.FlowchartPort](FlowchartPort.md "class in com.anylogic.engine")<InMessageType,OutMessageType>

com.anylogic.engine.FlowchartMappedPort<InMessageType,OutMessageType>

Type Parameters:
:   `InMessageType` - the type of messages being received by the port
:   `OutMessageType` - the type of messages being sent by the port

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class FlowchartMappedPort<InMessageType,OutMessageType>
extends FlowchartPort<InMessageType,OutMessageType>
```

An implementation of [`FlowchartPort`](FlowchartPort.md "class in com.anylogic.engine") which delegates its [`count()`](#count()) and [`isError()`](#isError())
methods to another port, this one is mapped with.
Usage: create a custom port of this type and add connector from this port
to the port of embedded object (or call [`map(Port)`](#map(com.anylogic.engine.Port)) on this port).
There should be one and only one mapped port, otherwise an error will be thrown.

Since:
:   7.0

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`FlowchartPort`](FlowchartPort.md "class in com.anylogic.engine")[`Port`](Port.md "class in com.anylogic.engine")[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.FlowchartMappedPort)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `FlowchartMappedPort(FlowchartBlock ao)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `long` | `count()` | Returns the number of agents passed through this port so far |
| `void` | `disconnectAndUnmapAll()` | Disconnects and unmaps the port from all ports and statechart it is connected and/or mapped to. |
| `boolean` | `isCannotAccept()` | Returns `true` if this (input) port can't accept agents at the current time. |
| `boolean` | `isError()` | Returns `true` if there is an error with this port, e.g. |
| `boolean` | `isReadyToExit()` | Returns `true` if there is some agent ready to exit this (output) port. |
| `void` | `map(Port<InMessageType,OutMessageType> port)` | Maps (connects) the port to a port of an embedded object. |
| `void` | `markError()` | Marks this port as having error |
| `void` | `unmap(Port<InMessageType,OutMessageType> port)` | Unmaps (disconnects) the port from a port of an embedded object. |
