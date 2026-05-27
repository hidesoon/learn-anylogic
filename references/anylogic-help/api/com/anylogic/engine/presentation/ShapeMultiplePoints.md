*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeMultiplePoints.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeMultiplePoints

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeMultiplePoints

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `Path2D`, `Path3D`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ShapePolyLine`

---

```
public abstract class ShapeMultiplePoints
extends ShapeLineFill
implements Path3D
```

A base class for shapes having multiple points, such as polyline
or curve.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeMultiplePoints)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeMultiplePoints()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `getNPoints()` | Returns the number of points in the shape. |
| `double` | `getPointDx(int i)` | Returns the x coordinate of a particular point of the shape relative to the start point. |
| `double` | `getPointDy(int i)` | Returns the y coordinate of a particular point of the shape relative to the start point. |
| `double` | `getPointDz(int i)` | Returns the z coordinate of a particular point of the shape relative to the start point. |
| `boolean` | `isClosed()` | Returns the closed/open status of the shape. |
| `void` | `setClosed(boolean closed)` | Sets the shape closed or open. |
| `void` | `setNPoints(int n)` | Sets the number of points in the shape. |
| `void` | `setPoint(int i, double ptdx, double ptdy)` | Sets the coordinates of a particular point of the shape relative to the start point. |
| `void` | `setPoint(int i, double ptdx, double ptdy, double ptdz)` | Sets the coordinates of a particular point of the shape relative to the start point. |
| `void` | `setPointDx(int i, double ptdx)` | Sets the x coordinate of a particular point of the shape relative to the start point. |
| `void` | `setPointDy(int i, double ptdy)` | Sets the y coordinate of a particular point of the shape relative to the start point. |
| `void` | `setPointDz(int i, double ptdz)` | Sets the z coordinate of a particular point of the shape relative to the start point. |
