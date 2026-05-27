*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/CircularCurve.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class CircularCurve

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractCurve](AbstractCurve.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.AbstractNetworkCurve](AbstractNetworkCurve.md "class in com.anylogic.engine.markup")<[MarkupSegment](MarkupSegment.md "class in com.anylogic.engine.markup")>

com.anylogic.engine.markup.CircularCurve

All Implemented Interfaces:
:   `IPathData`, `Serializable`, `Iterable<MarkupSegment>`

Direct Known Subclasses:
:   `CircularCurveImpl`

---

```
@AnyLogicInternalAPI
public abstract class CircularCurve
extends AbstractNetworkCurve<MarkupSegment>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.CircularCurve)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CircularCurve()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `arcTo(double x, double y, double z, double startAngle, double endAngle, double ratioStartToEnd)` | Adds arc segment with two circular arcs (available for markup elements created with no-argument constructor) |
| `Rectangle2D` | `getBounds()` | Deprecated. |
| `double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `Path2D` | `getPath2D()` | Returns the [`Path2D`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Path2D.html "class or interface in java.awt.geom") representation of this curve |
| `final Point` | `getPointAtOffset(double offset, Point out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](AbstractCurve.md#getStartPoint(com.anylogic.engine.Point)).  This method may be slightly faster in some cases but returns no orientation information (rotations). |
| `void` | `lineTo(double x, double y, double z)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `void` | `lineTo(Point endPoint)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `void` | `startDrawing(double x, double y, double z)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `void` | `startDrawing(Point startPoint)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `Path3D` | `toPath3D()` | Converts this markup element to [`Path3D`](../Path3D.md "interface in com.anylogic.engine") interface |
