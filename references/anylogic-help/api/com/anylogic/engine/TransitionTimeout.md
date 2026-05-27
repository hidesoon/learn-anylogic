*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/TransitionTimeout.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class TransitionTimeout

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

[com.anylogic.engine.Transition](Transition.md "class in com.anylogic.engine")

com.anylogic.engine.TransitionTimeout

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class TransitionTimeout
extends Transition
```

Statechart transition with trigger of type timeout. Is executed with the
timeout specified (counted from the moment the statechart came to the
transition's source state). If the guard appears to be `false` when the
transition is about to execute, it is not taken and becomes inactive.
**Memory**: sizeof(Transition) = 22 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.TransitionTimeout)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TransitionTimeout(Agent ao)` | Constructs the transition object with Timeout trigger. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `cancel()` | Should be called when this transition becomes deactivated e.g. |
| `String` | `getName()` | Returns the name of the timeout transition as specified by the user. |
| `void` | `start()` | Should be called when the statechart enters to the transition's source state. |
