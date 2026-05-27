*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/EventCondition.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class EventCondition

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

[com.anylogic.engine.Event](Event.md "class in com.anylogic.engine")

com.anylogic.engine.EventCondition

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class EventCondition
extends Event
```

Event with trigger of type condition. The event is executed when the
condition becomes true. If the agent has continuously changing variables,
the numeric engine constantly monitors the condition. In purely discrete models
the condition is tested when something changes in the active obejct, i.e. when
onChange() is called.
**Memory**: sizeof(Event) + 1 byte = 23 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.EventCondition)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `EventCondition(Agent ao)` | Constructs the event object with Condition trigger. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getName()` | Returns the name of the condition event as specified by the user. |
| `boolean` | `isMonitoring()` | Returns `true` if this event is currently monitoring (waiting on) its condition. |
| `void` | `onChange()` | Should be called when something changes in the object and probably condition changes. |
| `void` | `onDestroy()` | Discards the scheduled event, if any (deletes it from the engine). |
| `void` | `reset()` | Cancels the currently scheduled event, if any. |
| `void` | `restart()` | Resumes waiting on the condition. |
| `void` | `start()` | Should be called when the agents starts. |
