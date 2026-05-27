*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeRectangle.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeRectangle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeRectangle

All Implemented Interfaces:
:   `Area2D`, `Area3D`, `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ShapeRoundedRectangle`

---

```
public class ShapeRectangle
extends ShapeLineFill
implements Area3D
```

Persistent rectangle shape.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeRectangle)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeRectangle()` | Constructs a rectangle with default attributes. |
| `ShapeRectangle(boolean ispublic, double x, double y, double rotation, Paint lineColor, Paint fillColor, double width, double height, double lineWidth, LineStyle lineStyle)` | Constructs a 2D-only rectangle with specific attributes. |
| `ShapeRectangle(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, Paint lineColor, Paint fillColor, double width, double height, double zHeight, double lineWidth, LineStyle lineStyle)` | Constructs a rectangle with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeRectangle` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Point` | `getCenter()` | Returns (x, y) coordinates of the rectangle center in 2D (returned z is the base-level of rectangle). |
| `Point` | `getCenter3D()` | Returns (x, y, z) coordinates of the rectangle center. |
| `double` | `getHeight()` | Returns the height of the rectangle. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `double` | `getWidth()` | Returns the width of the rectangle. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `resetSVGComponent()` |  |
| `void` | `setHeight(double height)` | Sets the height of the rectangle. |
| `void` | `setSize(double width, double height)` | Sets the width and height of the rectangle. |
| `void` | `setSize(double width, double height, double zHeight)` | Sets the width, height and height along z axis (z-height) of the rectangle. |
| `void` | `setWidth(double width)` | Sets the width of the rectangle. |
