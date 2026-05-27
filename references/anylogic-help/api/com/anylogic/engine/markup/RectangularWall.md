*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RectangularWall.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RectangularWall

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractWall](AbstractWall.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractShapedWall](AbstractShapedWall.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.RectangularWall

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class RectangularWall
extends AbstractShapedWall
implements HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RectangularWall)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RectangularWall()` |  |
| `RectangularWall(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double width, double height, double rotation, double lineWidth, double zHeight, WallFillingType fillingType, Paint color)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getHeight()` | Returns the height of the rectangular wall. |
| `double` | `getWidth()` | Returns the width of the rectangular wall. |
| `void` | `setSize(double width, double height)` | Sets the width and height of the rectangular wall. |
