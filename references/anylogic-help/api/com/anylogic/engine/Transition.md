*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Transition.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Transition

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

com.anylogic.engine.Transition

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

Direct Known Subclasses:
:   `TransitionCondition`, `TransitionMessage`, `TransitionRate`, `TransitionTimeout`

---

```
public abstract class Transition
extends EventOriginator
implements com.anylogic.engine.internal.Child
```

Base class for all kinds of statechart transitions: TransitionTimeout, TransitionRate,
TransitionCondition and TransitionMessage
**Memory**: sizeof(EventOriginator) = 22 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Transition)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `cancel()` | Should be called when this transition becomes deactivated e.g. |
| `boolean` | `isLoggingToDB()` | Return `true` if the given event (or dynamic event) is logged to database (note that this may be overridden by logging settings of Agent). |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
