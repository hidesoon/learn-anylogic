*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/TransitionMessage.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class TransitionMessage

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

[com.anylogic.engine.Transition](Transition.md "class in com.anylogic.engine")

com.anylogic.engine.TransitionMessage

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class TransitionMessage
extends Transition
```

Statechart transition with trigger of type message. Such transition is executed
when the statechart receives a message (integer or Object) that conforms with the
transition trigger.
If the guard appears to be `false` when the transition is about to execute,
it is not taken and becomes inactive until the next message arrival.
**Memory**: sizeof(Transition) + 8 bytes = 30 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.TransitionMessage)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TransitionMessage(Agent ao)` | Constructs the transition object with Message trigger. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `cancel()` | Should be called when this transition becomes deactivated e.g. |
| `String` | `getName()` | Returns the name of the message transition as specified by the user. |
| `void` | `start()` | Should be called when the statechart enters to the transition's source state. |
