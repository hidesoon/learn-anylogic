*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Wall.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Wall

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractWall](AbstractWall.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Wall

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Wall
extends AbstractWall
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Wall)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Wall()` |  |
| `Wall(Agent owner, ShapeDrawMode drawMode, boolean isPublic, WallFillingType fillingType, Paint color, double lineWidth, double zHeight, boolean isClosed, MarkupSegment... segments)` |  |
| `Wall(Agent owner, ShapeDrawMode drawMode, boolean isPublic, WallFillingType fillingType, Paint color, double lineWidth, double zHeight, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegment segment)` | Adds segment to this markup element |
| `void` | `arcTo(double x, double y, double z, double startAngle, double endAngle, double ratioStartToEnd)` | Adds arc segment with two circular arcs (available for markup elements created with no-argument constructor) |
| `boolean` | `contains(double px, double py)` | Tests if a specified point lies on the wall. |
| `boolean` | `contains(double px, double py, double distance)` | Tests if a specified point lies on the wall with a given distance tolerance. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Tests if a specified point lies on the wall with a given distance tolerance. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `boolean` | `isClosed()` | Returns the wall's `closed` state. |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of the markup element, calculated in 3D space. |
| `void` | `lineTo(double x, double y, double z)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `void` | `setClosed(boolean isClosed)` | Sets the wall's `closed` state. |
| `void` | `startDrawing(double x, double y, double z)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `Path3D` | `toPath3D()` | Converts this markup element to [`Path3D`](../Path3D.md "interface in com.anylogic.engine") interface |
