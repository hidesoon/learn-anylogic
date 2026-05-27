*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/MarkupSegment.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class MarkupSegment

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSegment](AbstractMarkupSegment.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.MarkupSegment

All Implemented Interfaces:
:   `HasBoundingRectangle`, `IMarkupSegment`, `Serializable`

Direct Known Subclasses:
:   `MarkupSegmentArc`, `MarkupSegmentLine`

---

```
public abstract class MarkupSegment
extends AbstractMarkupSegment
implements HasBoundingRectangle
```

Basic implementation of `IMarkupSegment` for continuous space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.MarkupSegment)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract List<Shape>` | `convertToShapes()` | Converts the markup segment into java.awt.geom primitives like [`Arc2D`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Arc2D.html "class or interface in java.awt.geom") or [`Line2D`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Line2D.html "class or interface in java.awt.geom") |
| `abstract double` | `getDistanceSq(double x, double y)` | For horizontal segments, calculates and returns *the square of distance* to the point (in the XY-projection). |
| `abstract double` | `getDistanceSq(double x, double y, double z)` | Calculates and returns *the square of distance* to the given (x, y, z) point. |
| `double` | `getDistanceSq(Point givenPoint)` | Calculates and returns *the square of distance* to the given point. |
| `final Point` | `getEnd(Point out)` | Returns the location of the end point of the segment |
| `final double` | `getEndX()` | Returns the x coordinate of the end point of the segment |
| `final double` | `getEndY()` | Returns the y coordinate of the start point of the segment |
| `final double` | `getEndZ()` | Returns the z coordinate of the start point of the segment |
| `abstract double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `abstract double` | `getNearestPoint(double x, double y, Point out)` | For horizontal segments, calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | For horizontal segments, calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getOffsetFrom2D(double offset2D)` | Converts offset from the beginning of this segment given in XY-projection, to true offset, which may be used in various methods which require offset |
| `final Position` | `getPositionAtOffset(double offset, Position out)` | Returns the point located on the segment with the given `offset` distance calculated from start point. |
| `final Point` | `getStart(Point out)` | Returns the location of the start point of the segment |
| `final double` | `getStartX()` | Returns the x coordinate of the start point of the segment |
| `final double` | `getStartY()` | Returns the y coordinate of the start point of the segment |
| `final double` | `getStartZ()` | Returns the z coordinate of the start point of the segment |
| `final double` | `length()` | Returns the length of the path segment |
| `final double` | `length2D()` | Returns the length of the path segment in XY-projection |
| `final void` | `setEnd(double x, double y, double z)` | Sets the end point of the path segment.  This function may be called only for segments created using constructor without arguments.  *Please call `AbstractMarkupSegment.initialize()` after segment setup is finished.* |
| `final void` | `setEnd(Point p)` | Sets the end point of the path segment.  This function may be called only for segments created using constructor without arguments.  *Please call `AbstractMarkupSegment.initialize()` after segment setup is finished.* |
| `final void` | `setStart(double x, double y, double z)` | Sets the start point of the path segment.  This function may be called only for segments created using constructor without arguments.  *Please call `AbstractMarkupSegment.initialize()` after segment setup is finished.* |
| `final void` | `setStart(Point p)` | Sets the start point of the path segment.  This function may be called only for segments created using constructor without arguments.  *Please call `AbstractMarkupSegment.initialize()` after segment setup is finished.* |
| `final void` | `setStartNextTo(IMarkupSegment previousSegment)` | Sets the start point of the path segment to the coordinates of the end point of the given `previousSegment`.  This function may be called only for segments created using constructor without arguments.  *Please call `AbstractMarkupSegment.initialize()` after segment setup is finished.* |
