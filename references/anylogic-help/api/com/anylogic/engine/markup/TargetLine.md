*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/TargetLine.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class TargetLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.TargetLine

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class TargetLine
extends AbstractLevelMarkup
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.TargetLine)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TargetLine()` |  |
| `TargetLine(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double[] dx, double[] dy, Color color)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addPoint(double x, double y)` | Adds a point to the collection that will be used to build a polyline of this target line. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(double px, double py, double distance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Color` | `getColor()` | Returns the color of the shape, or `null` if shape has no color |
| `double` | `getNearestPoint(double x, double y, Point out)` | Returns a point on the target line that is closest to the specified point |
| `int` | `getNPoints()` | Returns the number of points in the shape. |
| `final Point` | `getPointAtOffset(double offset, Point out)` | Returns the point located on the path with the given `offset` distance calculated from start point. |
| `double` | `getPointDx(int i)` | Returns the x coordinate of a particular point of the shape relative to the start point. |
| `double` | `getPointDy(int i)` | Returns the y coordinate of a particular point of the shape relative to the start point. |
| `double` | `getX()` | Returns the x coordinate of the shape. |
| `double` | `getY()` | Returns the y coordinate of the shape. |
| `final double` | `length()` | Returns the length of the path, calculated in 3D space. |
| `Point` | `randomPointInside()` | Returns a random point on this target line |
| `final Point` | `randomPointInside(Random rng, Point out)` | Returns a random point on this target line |
| `void` | `setColor(Color color)` | Sets the color of the shape. |
| `void` | `setPos(double x, double y)` | Sets coordinates of the shape |
| `Path2D` | `toPath2D()` | Returns the [`Path2D`](../Path2D.md "interface in com.anylogic.engine") representation of this target line |
