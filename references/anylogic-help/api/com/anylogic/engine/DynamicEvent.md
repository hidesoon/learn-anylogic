*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/DynamicEvent.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class DynamicEvent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

com.anylogic.engine.DynamicEvent

All Implemented Interfaces:
:   `AgentDestroyListener`, `Serializable`

---

```
public class DynamicEvent
extends EventOriginator
implements AgentDestroyListener
```

This class is a base class for dynamic events created by the user. Dynamic events
are used to schedule any number of concurrent and independent events; a typical
object that uses dynamic event would be a Delay object that can delay arbitrary
number of entities concurrently. The event gets scheduled when a DynamicEvent is
instantiated. Upon execution of the dynamic event the instance is deleted.
When the [`Agent`](Agent.md "class in com.anylogic.engine") is destroyed, all dynamic events belonging to it are discarded.
**Memory**: sizeof(EventOriginator) = 22 bytes + sizeof(HashSet entry - in AO) + user data

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.DynamicEvent)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DynamicEvent(Agent ao, double dt)` | A base class constructor for dynamic events. |
| `DynamicEvent(Agent ao, double t, boolean absoluteTime)` | A base class constructor for dynamic events. |
| `DynamicEvent(Agent ao, double dt, TimeUnits units)` | A base class constructor for dynamic events. |
| `DynamicEvent(Agent ao, double t, TimeUnits units, boolean absoluteTime)` | A base class constructor for dynamic events. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `execute()` | This method should be implemented at the subclass with a necessary call to super.execute() at the beginning. |
| `String` | `getName()` | Returns the name of the dynamic event - actually, the simple name of the dynamic event class. |
| `void` | `onDestroy(Agent agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `reset()` | Discards the scheduled occurrence of the event unregisters this dynamic event at the agent |
