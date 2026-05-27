*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/MarkupSegmentArc.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class MarkupSegmentArc

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSegment](AbstractMarkupSegment.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupSegment](MarkupSegment.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.MarkupSegmentArc

All Implemented Interfaces:
:   `HasBoundingRectangle`, `IMarkupSegment`, `Serializable`

---

```
public final class MarkupSegmentArc
extends MarkupSegment
implements HasBoundingRectangle
```

Arched markup segment for continuous space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.MarkupSegmentArc)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MarkupSegmentArc()` |  |
| `MarkupSegmentArc(double sx, double sy, double sz, double ex, double ey, double ez, double startAngle, double endAngle, double ratioStartToEnd)` |  |
| `MarkupSegmentArc(double sx, double sy, double sz, double ex, double ey, double ez, double startAngle, double endAngle, double ratioStartToEnd, double sArcCenterX, double sArcCenterY, double sArcRadius, double sArcStartAngle, double sArcAngle, double eArcCenterX, double eArcCenterY, double eArcRadius, double eArcStartAngle, double eArcAngle)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addTo(Path2D path)` | Adds this segment to the given path assuming that path is currently positioned on the start point of this segment |
| `List<Shape>` | `convertToShapes()` | Converts the markup segment into java.awt.geom primitives like [`Arc2D`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Arc2D.html "class or interface in java.awt.geom") or [`Line2D`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Line2D.html "class or interface in java.awt.geom") |
| `static Point` | `getArgNearestPointOnRay2D(double ax, double ay, double bx, double by, double arcCenterX, double arcCenterY, double sx, double sy, double ex, double ey, double arcRadius, double arcAngle, double arcSign, Point out)` | Deprecated. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getDistanceSq(double x, double y)` | For horizontal segments, calculates and returns *the square of distance* to the point (in the XY-projection). |
| `double` | `getDistanceSq(double x, double y, double z)` | Calculates and returns *the square of distance* to the given (x, y, z) point. |
| `Position` | `getEnd(Position out)` | Returns the location of the end position of the segment |
| `double` | `getEndAngle()` | Returns the angle of the tangent to the segment at its end |
| `double` | `getEndArcAngle()` |  |
| `double` | `getEndArcCenterX()` |  |
| `double` | `getEndArcCenterY()` |  |
| `double` | `getEndArcRadius()` |  |
| `double` | `getEndArcSign()` |  |
| `double` | `getEndArcStartAngle()` |  |
| `double` | `getJoinX()` |  |
| `double` | `getJoinY()` |  |
| `double` | `getJoinZ()` |  |
| `double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element pseudo-nearest to the given (x, y, z) point: the chosen point is really nearest in the 2D (XY) plane. |
| `double` | `getNearestPoint(double x, double y, Point out)` | For horizontal segments, calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPointOnRay2D(double x1, double y1, double x2, double y2, Point out)` | Calculates (and sets in the 'out' object) the point where this segment intersects the given ray with the minimum distance from ray beginning (if there are several intersection points like in arc segments). |
| `double` | `getOffsetOfPoint(double x, double y)` | Calculates distance by segment to the given point. |
| `double` | `getRatioStartToEnd()` | Returns the start to end ratio |
| `Position` | `getStart(Position out)` | Returns the location of the start position of the segment |
| `double` | `getStartAngle()` | Returns the angle of the tangent to the segment at its start |
| `double` | `getStartArcAngle()` |  |
| `double` | `getStartArcCenterX()` |  |
| `double` | `getStartArcCenterY()` |  |
| `double` | `getStartArcRadius()` |  |
| `double` | `getStartArcSign()` |  |
| `double` | `getStartArcStartAngle()` |  |
| `void` | `initialize()` |  |
| `void` | `setAngles(double startAngle, double endAngle, double ratioStartToEnd)` | Sets the angles of this arc. |
| `String` | `toString()` |  |
