*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/TransitionRate.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class TransitionRate

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

[com.anylogic.engine.Transition](Transition.md "class in com.anylogic.engine")

com.anylogic.engine.TransitionRate

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class TransitionRate
extends Transition
```

Statechart transition with trigger of type rate. Such transition is executed with
the timeout distributed exponentially with the parameter rate (counted from the
moment the statechart came to the transition's source state), i.e. if
the rate is 5, the timeout will on average be 1/5 of the time unit. If the rate
changes dynamically, the timeout gets re-evaluated; such changes may
only be noticed by TransitionRate if onChange() is called for the agent.
If the guard appears to be `false` when the transition is about to execute,
it is not taken and becomes inactive until the rate changes.
**Memory**: sizeof(Transition) + 8 = 30 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.TransitionRate)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TransitionRate(Agent ao)` | Constructs the transition object with Rate trigger. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `cancel()` | Should be called when this transition becomes deactivated e.g. |
| `String` | `getName()` | Returns the name of the rate transition as specified by the user. |
| `void` | `start()` | Should be called when the statechart enters to the transition's source state. |
