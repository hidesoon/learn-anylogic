*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractShapedWall.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractShapedWall

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractWall](AbstractWall.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractShapedWall

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `CircularWall`, `RectangularWall`

---

```
public abstract class AbstractShapedWall
extends AbstractWall
implements AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractShapedWall)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractShapedWall()` |  |
| `AbstractShapedWall(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double rotation, double lineWidth, double zHeight, WallFillingType fillingType, Paint color)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getRotation()` | Returns the rotation of the shape. |
| `double` | `getX()` | Returns the x coordinate of the shape. |
| `double` | `getY()` | Returns the y coordinate of the shape. |
| `double` | `getZ()` | Returns the z coordinate of the shape. |
| `void` | `setPos(double x, double y, double z)` | Sets coordinates of the shape |
| `void` | `setRotation(double rotation)` | Sets the rotation of the shape. |
