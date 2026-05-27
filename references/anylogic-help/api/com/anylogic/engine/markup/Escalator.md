*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Escalator.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Escalator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSubunit](AbstractMarkupSubunit.md "class in com.anylogic.engine.markup")<[EscalatorGroup](EscalatorGroup.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.Escalator

All Implemented Interfaces:
:   `Serializable`

---

```
public class Escalator
extends AbstractMarkupSubunit<EscalatorGroup>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Escalator)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Escalator()` |  |
| `Escalator(EscalatorMovementDirection movementDirection)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `block()` | Blocks the escalator. |
| `EscalatorDataSource` | `getDataSource()` |  |
| `EscalatorMovementDirection` | `getMovementDirection()` | Returns the current movement direction for the escalator. |
| `List<? extends Agent>` | `getPeds()` | Returns the collection of pedestrians currently present on the escalator |
| `double` | `getSpeed()` | Returns the speed of the escalator (in meters per second) |
| `double` | `getSpeed(SpeedUnits units)` | Returns the speed of the escalator (in the units passed via the units argument). |
| `boolean` | `isBlocked()` | Checks whether the escalator is blocked, or not. |
| `boolean` | `isRunning()` | Checks whether the escalator is running, or not. |
| `void` | `setBlocked(boolean isBlocked)` | Blocks or unblocks the escalator depending on the isBlocked value |
| `void` | `setDataSource(EscalatorDataSource dataSource)` |  |
| `void` | `setMovementDirection(EscalatorMovementDirection movementDirection)` | Sets new movement direction for the escalators. |
| `void` | `setRunning(boolean isRunning)` | Turns the escalator on if the `isRunning` value is true; turns the escalator off otherwise. |
| `void` | `setSpeed(double speedInMPS)` | Sets the speed of the escalator (in meters per second). |
| `void` | `setSpeed(double speed, SpeedUnits units)` | Sets the speed of the escalator (in the units passed via the `units` argument). |
| `void` | `turnOff()` | Turns off the esaclator. |
| `void` | `turnOn()` | Turns the escalator on setting the steps into motion |
| `void` | `unblock()` | Unblocks the escalator allowing pedestrians to enter this escalator |
