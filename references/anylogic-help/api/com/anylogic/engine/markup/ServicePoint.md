*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ServicePoint.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ServicePoint<Q extends QueueUnit>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSubunit](AbstractMarkupSubunit.md "class in com.anylogic.engine.markup")<[ServiceBase](ServiceBase.md "class in com.anylogic.engine.markup")<?,Q>>

[com.anylogic.engine.markup.ServiceUnit](ServiceUnit.md "class in com.anylogic.engine.markup")<Q>

com.anylogic.engine.markup.ServicePoint<Q>

All Implemented Interfaces:
:   `HasBoundingRectangle`, `Serializable`

---

```
public class ServicePoint<Q extends QueueUnit>
extends ServiceUnit<Q>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ServicePoint)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ServicePoint(double x, double y, double orientation)` |  |
| `ServicePoint(double x, double y, double orientation, ServiceQueueChoicePolicy queueChoicePolicy)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getOrientation()` | Returns the orientations of the service point |
| `Position` | `getPosition(Position out)` | Returns the [`Position`](../Position.md "class in com.anylogic.engine") object (point and orientation) of this service point |
| `double` | `getX()` | Returns the x coordinate of the service point |
| `double` | `getY()` | Returns the y coordinate of the service point |
| `double` | `getZ()` | Returns the z coordinate of the service point |
