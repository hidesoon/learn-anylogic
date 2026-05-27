*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/EventOriginator.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class EventOriginator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.EventOriginator

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `DynamicEvent`, `Event`, `Transition`

---

```
public abstract class EventOriginator
extends Object
implements Serializable
```

Base class for all constructs in AnyLogic modeling language that are able
to schedule discrete events, like Event, DynamicEvent and Transition.
**Memory**: sizeof(Object) + 8 bytes = 22 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.EventOriginator)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `cancel()` | Deprecated. User should not call this method for events, call `reset()` instead |
| `Agent` | `getActiveObject()` | Deprecated. Use [`getAgent()`](#getAgent()) instead |
| `Agent` | `getAgent()` | Returns the agent that owns the event originator. |
| `String` | `getFullName()` | Returns the name of the event originator prefixed by the full name of its agent. |
| `abstract String` | `getName()` | Returns the name of the event originator, i.e. |
| `double` | `getRest()` | Returns the time remaining before the scheduled occurrence of the event, or `+infinity` if the event is not scheduled. |
| `double` | `getRest(TimeUnits units)` | Returns the time remaining before the scheduled occurrence of the event, or `+infinity` if the event is not scheduled. |
| `boolean` | `isActive()` | Returns `true` if the event is currently scheduled by this event originator, `false` otherwise. |
| `boolean` | `isCurrent()` | Tests if the event is being currently executed, or just has been executed. |
| `boolean` | `isLoggingToDB()` | Return `true` if the given event (or dynamic event) is logged to database (note that this may be overridden by logging settings of Agent). |
| `void` | `onDestroy()` | Discards the scheduled event, if any (deletes it from the engine). |
| `String` | `toString()` |  |
