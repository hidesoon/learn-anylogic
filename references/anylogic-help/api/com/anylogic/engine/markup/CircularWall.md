*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/CircularWall.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class CircularWall

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractWall](AbstractWall.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractShapedWall](AbstractShapedWall.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.CircularWall

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class CircularWall
extends AbstractShapedWall
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.CircularWall)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CircularWall()` |  |
| `CircularWall(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double radiusX, double radiusY, double rotation, double lineWidth, double zHeight, WallFillingType fillingType, Paint color)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getRadiusX()` | Returns the "horizontal" radius of the oval wall. |
| `double` | `getRadiusY()` | Returns the "vertical" radius of the oval wall. |
| `void` | `setRadius(double radius)` | Sets both radiuses of the oval wall to the same given value, i.e. |
| `void` | `setRadius(double radiusX, double radiusY)` | Sets radiuses of the oval wall to the given values |
| `void` | `setRadiusX(double radiusX)` | Sets the "horizontal" radius of the oval wall. |
| `void` | `setRadiusY(double radiusY)` | Sets the "vertical" radius of the oval wall. |
