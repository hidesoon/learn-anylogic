*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/MarkupSegmentLine.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class MarkupSegmentLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSegment](AbstractMarkupSegment.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupSegment](MarkupSegment.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.MarkupSegmentLine

All Implemented Interfaces:
:   `HasBoundingRectangle`, `IMarkupSegment`, `Serializable`

---

```
public final class MarkupSegmentLine
extends MarkupSegment
```

Straight markup segment for continuous space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.MarkupSegmentLine)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MarkupSegmentLine()` |  |
| `MarkupSegmentLine(double sx, double sy, double sz, double ex, double ey, double ez)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addTo(Path2D path)` | Adds this segment to the given path assuming that path is currently positioned on the start point of this segment |
| `List<Shape>` | `convertToShapes()` | Converts the markup segment into java.awt.geom primitives like [`Arc2D`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Arc2D.html "class or interface in java.awt.geom") or [`Line2D`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Line2D.html "class or interface in java.awt.geom") |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getDistanceSq(double x, double y)` | For horizontal segments, calculates and returns *the square of distance* to the point (in the XY-projection). |
| `double` | `getDistanceSq(double x, double y, double z)` | Calculates and returns *the square of distance* to the point. |
| `Position` | `getEnd(Position out)` | Returns the location of the end position of the segment |
| `double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, Point out)` | For horizontal segments, calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPointOnRay2D(double x1, double y1, double x2, double y2, Point out)` | Calculates (and sets in the 'out' object) the point where this segment intersects the given ray with the minimum distance from ray beginning (if there are several intersection points like in arc segments). |
| `double` | `getOffsetOfPoint(double x, double y)` | Calculates distance by segment to the given point. |
| `Position` | `getStart(Position out)` | Returns the location of the start position of the segment |
| `final void` | `initialize()` |  |
| `String` | `toString()` |  |
