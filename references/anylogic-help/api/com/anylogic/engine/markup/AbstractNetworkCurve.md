*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractNetworkCurve.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractNetworkCurve<T extends AbstractMarkupSegment>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractCurve](AbstractCurve.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.AbstractNetworkCurve<T>

All Implemented Interfaces:
:   `IPathData`, `Serializable`, `Iterable<T>`

Direct Known Subclasses:
:   `CircularCurve`, `GISCurve`

---

```
@AnyLogicInternalAPI
public abstract class AbstractNetworkCurve<T extends AbstractMarkupSegment>
extends AbstractCurve<T>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractNetworkCurve)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractNetworkCurve()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Returns the point on this curve closest to the specified point |
| `double` | `getNearestPointOnRay(double x1, double y1, double x2, double y2, Point out)` | Calculates the intersection point between this element and the given ray. |
| `boolean` | `isClosed()` | Returns true if the end point of the last segment equals the start point of the first segment, false otherwise |
| `abstract void` | `lineTo(Point endPoint)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `abstract void` | `startDrawing(Point startPoint)` | Starts drawing (available for markup elements created with no-argument constructor) |
