*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/EventRate.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class EventRate

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

[com.anylogic.engine.Event](Event.md "class in com.anylogic.engine")

com.anylogic.engine.EventRate

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class EventRate
extends Event
```

Event with trigger of type rate. Such event is executed periodically
with time intervals distributed exponentially with the parameter rate, i.e. if
the rate is 5, the event will occur on average 5 times per time unit. If the rate
changes dynamically, the event occurrence gets re-scheduled; such changes may
only be noticed by EventRate if onChange() is called for the agent.
**Memory**: sizeof(Event) + 8 = 30 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.EventRate)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `EventRate(Agent ao)` | Constructs the event object with Rate trigger. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getName()` | Returns the name of the rate event as specified by the user. |
| `void` | `onChange()` | Should be called when something changes in the object (and probably the rate changes). |
| `void` | `reset()` | Cancels the currently scheduled event, if any. |
| `void` | `restart()` | Cancels the currently scheduled event, if any, and schedules the next occurrence according to the Rate. |
| `void` | `start()` | Should be called when the agents starts. |
