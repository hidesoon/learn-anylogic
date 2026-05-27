*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Event.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Event

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

com.anylogic.engine.Event

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

Direct Known Subclasses:
:   `EventCondition`, `EventRate`, `EventTimeout`

---

```
public abstract class Event
extends EventOriginator
implements com.anylogic.engine.internal.Child
```

Base class for all kinds of (static) events: EventTimeout, EventRate and
EventCondition.
**Memory**: sizeof(EventOriginator) = 22 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Event)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `reset()` |  |
| `abstract void` | `restart()` |  |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `abstract void` | `start()` | Should be called when the agents starts. |
