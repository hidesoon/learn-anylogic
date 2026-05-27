*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ServiceLine.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ServiceLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSubunit](AbstractMarkupSubunit.md "class in com.anylogic.engine.markup")<[ServiceBase](ServiceBase.md "class in com.anylogic.engine.markup")<?,Q>>

[com.anylogic.engine.markup.ServiceUnit](ServiceUnit.md "class in com.anylogic.engine.markup")<[QueuePath](QueuePath.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.ServiceLine

All Implemented Interfaces:
:   `HasBoundingRectangle`, `Serializable`

---

```
public class ServiceLine
extends ServiceUnit<QueuePath>
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ServiceLine)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ServiceLine(double x, double y, double dx, double dy)` |  |
| `ServiceLine(double x, double y, double dx, double dy, ServiceQueueChoicePolicy queueChoicePolicy)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getEndX()` | Returns the x coordinate of the end of the queue line |
| `double` | `getEndY()` | Returns the y coordinate of the end of the queue line |
| `double` | `getEndZ()` | Returns the y coordinate of the end of the queue line |
| `double` | `getForwardOrientation()` | Returns the orientation (in angle radians) of this queue line |
| `Position` | `getForwardPositionByOffset(double offset, Position out)` | Returns [`Position`](../Position.md "class in com.anylogic.engine") object with forward orientation (see [`getForwardOrientation()`](#getForwardOrientation())) and coordinates of the point that is located at the given offset distance from the queue line starting point. |
| `Position` | `getForwardStartPosition(Position out)` | Returns [`Position`](../Position.md "class in com.anylogic.engine") object with start point and forward orientation |
| `double` | `getReverseOrientation()` | Returns the orientation (in angle radians) opposite to this queue line orientation |
| `Position` | `getReversePositionByOffset(double offset, Position out)` | Returns [`Position`](../Position.md "class in com.anylogic.engine") object with reverse orientation (see [`getReverseOrientation()`](#getReverseOrientation())) and coordinates of the point that is located at the given offset distance from the queue line starting point. |
| `Position` | `getReverseStartPosition(Position out)` | Returns [`Position`](../Position.md "class in com.anylogic.engine") object with start point and reverse orientation |
| `double` | `getStartX()` | Returns the x coordinate of the start of the queue line |
| `double` | `getStartY()` | Returns the y coordinate of the start of the queue line |
| `double` | `getStartZ()` | Returns the y coordinate of the start of the queue line |
| `double` | `length()` | Returns length in 2D space |
