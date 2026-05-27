*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Port.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Port<InMessageType,OutMessageType>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Port<InMessageType,OutMessageType>

Type Parameters:
:   `InMessageType` - the type of messages being received by the port
:   `OutMessageType` - the type of messages being sent by the port

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

Direct Known Subclasses:
:   `FlowchartPort`

---

```
public class Port<InMessageType,OutMessageType>
extends Object
implements Serializable, com.anylogic.engine.internal.Child
```

Port is a universal interface of an agent via which it can send and
receive messages - arbitrary objects. Ports are used to graphically connect
objects that do not need to know anything about each other type or structure.
There are two major types of links a port maintains: connections to the
ports of objects on the same hierarchy level (embedded in the same agent)
or "mappings" to the ports of embedded objects or statecharts. In the first
case a message sent at one port is received at the other. In case of mapping
the message sent at the inner port is forwarded out at the outer port, and vice
versa: message received at the outer port is received by the inner port or by
the statechart. The user may define his own actions that are executed upon
reception or sending the message that may prevent the port from continuing
the message processing. The port class is generic with two parameters - the
classes of messages being received and sent. Once instantiated and parameterized,
it will only accept the messages of those classes. Moreover, the port can only
be connected / mapped to a port with the corresponding message types.
**Memory**: sizeof(Object) + 20 bytes = 34 bytes + sizeof up to 4 LinkedList's

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Port)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Port(Agent ao)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `connect(Port<OutMessageType,InMessageType> port)` | Connects the port to another port of an object on the same level. |
| `void` | `disconnect(Port<OutMessageType,InMessageType> port)` | Disconnects the port from another port of an object on the same level. |
| `void` | `disconnectAndUnmapAll()` | Disconnects and unmaps the port from all ports and statechart it is connected and/or mapped to. |
| `Agent` | `getActiveObject()` | Deprecated. Use [`getAgent()`](#getAgent()) instead |
| `Agent` | `getAgent()` | Returns the agent that owns the port. |
| `List<Port<InMessageType,OutMessageType>>` | `getDownLinks()` | Returns an unmodifiable list with mapped ports on agents embedded in the current agent (owner of port) |
| `List<Port<OutMessageType,InMessageType>>` | `getFlatLinks()` | Returns an unmodifiable list with connected ports |
| `String` | `getFullName()` | Returns the name of the port prefixed by the full name of its agent. |
| `String` | `getName()` | Returns the name of the port as specified by the user. |
| `List<Statechart>` | `getStatechartLinks()` | Returns an unmodifiable list with mapped statecharts of the current agent (owner of this port) |
| `List<Port<InMessageType,OutMessageType>>` | `getUpLinks()` | Returns an unmodifiable list with mapped ports on agents which own the current agent (owner of port) |
| `void` | `map(Port<InMessageType,OutMessageType> port)` | Maps (connects) the port to a port of an embedded object. |
| `void` | `map(Statechart statechart)` | Maps (connects) the port to a statechart of the same agent. |
| `void` | `onDestroy()` | Should be called when the port is destroyed, e.g. |
| `void` | `receive(InMessageType msg)` | Receives an incoming message. |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `send(OutMessageType msg)` | Send the message out. |
| `String` | `toString()` |  |
| `void` | `unmap(Port<InMessageType,OutMessageType> port)` | Unmaps (disconnects) the port from a port of an embedded object. |
| `void` | `unmap(Statechart statechart)` | Unmaps (disconnects) the port from the statechart of the same agent. |
