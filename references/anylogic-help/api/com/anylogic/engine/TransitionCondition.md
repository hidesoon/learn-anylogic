*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/TransitionCondition.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class TransitionCondition

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.EventOriginator](EventOriginator.md "class in com.anylogic.engine")

[com.anylogic.engine.Transition](Transition.md "class in com.anylogic.engine")

com.anylogic.engine.TransitionCondition

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Serializable`

---

```
public class TransitionCondition
extends Transition
```

Statechart transition with trigger of type condition. The transition is executed when the
condition becomes `true`. If the agent has continuously changing variables,
the numeric engine constantly monitors the condition. In purely discrete models
the condition is tested when something changes in the active obejct, i.e. when
onChange() is called. If the guard appears to be `false` when the transition is about
to execute, it is not taken and becomes inactive until the next next condition evaluation.
**Memory**: sizeof(Transition) = 22 bytes

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.TransitionCondition)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TransitionCondition(Agent ao)` | Constructs the transition object with Condition trigger. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `cancel()` | Should be called when this transition becomes deactivated e.g. |
| `String` | `getName()` | Returns the name of the condition transition as specified by the user. |
| `void` | `onDestroy()` | Discards the scheduled event, if any (deletes it from the engine). |
| `void` | `start()` | Should be called when the statechart enters to the transition's source state. |
