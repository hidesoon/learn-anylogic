*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeArc.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeArc

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeOval](ShapeOval.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeArc

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeArc
extends ShapeOval
```

Arc shape. The shape has a start angle and a angular extent, or simply angle. For angles equal to 2\*PI (with
a certain tolerance), a full circle is drawn. For angles greater than 2\*PI, the remainder
of the angle divided by 2\*PI is drawn.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeArc)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeArc()` | Constructs an arc with default attributes. |
| `ShapeArc(boolean ispublic, double x, double y, double rotation, Paint lineColor, Paint fillColor, double radiusX, double radiusY, double angleStart, double angle, double lineWidth, LineStyle lineStyle)` | Constructs a 2D-only arc with specific attributes. |
| `ShapeArc(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, double rotation, Paint lineColor, Paint fillColor, double radiusX, double radiusY, double zHeight, double dz, double angleStart, double angle, double lineWidth, LineStyle lineStyle)` | Constructs an arc with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapeArc` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `getAngle()` | Returns the angular extent of the arc in radians, clockwise. |
| `double` | `getAngleStart()` | Returns the starting angle of the arc (0 means 3 o'clock) in radians, clockwise. |
| `double` | `getDz()` | Returns the difference of z coordinates of the arc end and start points. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the shape area.  This method utilises the given Random Number Generator.  Throws error if this shape type doesn't support returning random point inside. |
| `void` | `setAngle(double angle)` | Sets the angular extent of the arc in radians, clockwise. |
| `void` | `setAngleStart(double angleStart)` | Sets the starting angle of the arc (0 means 3 o'clock) in radians, clockwise. |
| `void` | `setDz(double dz)` | Sets the difference of z coordinates of the arc end and start points. |
