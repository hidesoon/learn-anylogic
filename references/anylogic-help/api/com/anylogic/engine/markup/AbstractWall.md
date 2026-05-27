*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractWall.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractWall

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.AbstractWall

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `AbstractShapedWall`, `Wall`

---

```
public abstract class AbstractWall
extends AbstractLevelMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractWall)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractWall()` |  |
| `AbstractWall(Agent owner, ShapeDrawMode drawMode, boolean isPublic, WallFillingType fillingType, Paint color, double lineWidth, double zHeight)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Color` | `getColor()` | Returns the color of the shape, or `null` if shape has no color or has textured (in this case `#getFillTexture()` should be used instead) |
| `WallFillingType` | `getFillingType()` | Returns the animation property - filling type of the wall |
| `double` | `getLineWidth()` | Returns the width of the wall. |
| `Texture` | `getTexture()` | Returns the texture of the shape, if the shape has texture |
| `double` | `getZHeight()` | Returns wall height |
| `void` | `setColor(Color color)` | Sets the color of the shape. |
| `void` | `setColor(Paint color)` | Sets the color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setFillingType(WallFillingType fillingType)` | Sets the animation property - filling type of the wall |
| `void` | `setLineWidth(double lineWidth)` | Sets the width of the wall, 0 means 'don't draw' |
| `void` | `setZHeight(double zHeight)` | Set wall height |
