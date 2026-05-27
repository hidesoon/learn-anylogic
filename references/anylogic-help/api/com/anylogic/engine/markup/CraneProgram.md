*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/CraneProgram.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class CraneProgram

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.CraneProgram

All Implemented Interfaces:
:   `Serializable`

---

```
public final class CraneProgram
extends Object
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.CraneProgram)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static interface` | `CraneProgram.Command` |  |
| `static class` | `CraneProgram.CommandMoveAtomic` |  |
| `static class` | `CraneProgram.CommandMoveComposite` |  |
| `static enum` | `CraneProgram.CommandType` |  |
| `static class` | `CraneProgram.CommandWait` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CraneProgram()` | Creates empty program. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final CraneProgram` | `appendProgram(CraneProgram program)` | Appends specified program to end of this program. |
| `CraneProgram` | `clone()` |  |
| `final CraneProgram` | `delay(double delayTime, TimeUnits units)` | Adds command to wait without any movement for specified time. |
| `CraneProgram.Command` | `getCommandInternal(int index)` |  |
| `List<CraneProgram.Command>` | `getCommandsInternal()` |  |
| `final CraneProgram` | `moveBridge(double offset, LengthUnits units)` | Adds command to move bridge to `this` program. |
| `final CraneProgram` | `moveComponentsConcurrently(double bridgeOffset, double trolleyOffset, double hookOffset, LengthUnits units)` | Adds command to move several components simultaneously to `this` program. |
| `final CraneProgram` | `moveHook(double offset, LengthUnits units)` | Adds command to move hook to `this` program. |
| `final CraneProgram` | `moveToPoint(Point destinationPx, double safeHeight, LengthUnits units)` | Adds command to move all components to reach the specified point. |
| `final CraneProgram` | `moveTrolley(double offset, LengthUnits units)` | Adds command to move trolley to `this` program. |
| `String` | `toString()` |  |
