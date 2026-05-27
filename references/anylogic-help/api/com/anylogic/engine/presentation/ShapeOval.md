*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeOval.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeOval

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeOval

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ShapeArc`

---

```
public class ShapeOval
extends ShapeLineFill
```

Persistent oval shape.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeOval)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeOval()` | Constructs an oval with default attributes. |
| `ShapeOval(boolean ispublic, double x, double y, double rotation, Paint lineColor, Paint fillColor, double radiusX, double radiusY, double lineWidth, LineStyle lineStyle)` | Constructs a 2D-only oval with specific attributes. |
| `ShapeOval(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, Paint lineColor, Paint fillColor, double radiusX, double radiusY, double zHeight, double lineWidth, LineStyle lineStyle)` | Constructs an oval with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeOval` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getRadiusX()` | Returns the "horizontal" radius of the oval. |
| `double` | `getRadiusY()` | Returns the "vertical" radius of the oval. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `resetSVGComponent()` |  |
| `void` | `setRadius(double radius)` | Sets both radiuses of the oval to the same given value, i.e. |
| `void` | `setRadiusX(double radiusX)` | Sets the "horizontal" radius of the oval. |
| `void` | `setRadiusY(double radiusY)` | Sets the "vertical" radius of the oval. |
