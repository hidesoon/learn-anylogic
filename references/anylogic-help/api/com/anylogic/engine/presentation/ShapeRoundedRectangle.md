*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeRoundedRectangle.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeRoundedRectangle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeRectangle](ShapeRectangle.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeRoundedRectangle

All Implemented Interfaces:
:   `Area2D`, `Area3D`, `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeRoundedRectangle
extends ShapeRectangle
```

Persistent rounded rectangle shape.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeRoundedRectangle)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeRoundedRectangle()` | Constructs a rounded rectangle with default attributes. |
| `ShapeRoundedRectangle(boolean ispublic, double x, double y, double rotation, Paint lineColor, Paint fillColor, double width, double height, double radius, double lineWidth, LineStyle lineStyle)` | Constructs a rounded rectangle with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final ShapeRoundedRectangle` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getRadius()` | Returns the corner radius of the rounded rectangle. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `setRadius(double radius)` | Sets the corner radius of the rounded rectangle. |
