*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/EventTimeout.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class EventTimeout

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

[com.anylogic.engine.Event](Event.md "class in com.anylogic.engine")

com.anylogic.engine.EventTimeout

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class EventTimeout
extends Event
```

Event with trigger of type timeout. The event occurs exactly in
timeout time after it is started. Optionally, the event may be made cyclic
and set to occur at startup.
**Memory**: sizeof(Event) + 8 bytes = 30 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.EventTimeout)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `EventTimeout.Mode` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `EventTimeout(Agent ao)` | Constructs the event object with Timeout trigger. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getName()` | Returns the name of the timeout event as specified by the user. |
| `void` | `reset()` | Cancels the currently scheduled event, if any. |
| `void` | `restart()` | Cancels the currently scheduled event, if any, and schedules the next occurrence according to the Timeout specified |
| `void` | `restart(double timeout)` | Cancels the currently scheduled event, if any, and schedules the next occurrence in time `t`. |
| `void` | `restart(double timeout, TimeUnits units)` | Cancels the currently scheduled event, if any, and schedules the next occurrence in time `t`. |
| `void` | `restartTo(double time)` | Cancels the currently scheduled event, if any, and schedules the next occurrence at the (absolute) model time `time`. |
| `void` | `restartTo(double time, TimeUnits units)` | Cancels the currently scheduled event, if any, and schedules the next occurrence at the (absolute) model time `time` expressed in the given `units`. |
| `void` | `restartTo(Date date)` | Cancels the currently scheduled event, if any, and schedules the next occurrence at the (absolute) model date `date`. |
| `void` | `resume()` | Re-schedules the previously suspended event in the remaining time. |
| `void` | `start()` | Should be called when the agents starts. |
| `void` | `suspend()` | Cancels the currently scheduled event, if any, and remembers the remaining time so that it can be resumed by calling [`resume()`](#resume()). |
