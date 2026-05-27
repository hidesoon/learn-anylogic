*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Shape3D.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Shape3D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.Shape3D

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ElevatorShaft`, `Shape3DObject`, `ShapeEmbeddedObjectPresentation`, `ShapeGISMap`, `ShapeGroup`, `ShapeImage`, `ShapeLine`, `ShapeLineFill`, `ShapeText`

---

```
public abstract class Shape3D
extends Shape
implements Locatable3D
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Shape3D)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `UNKNOWN_NAME` | This string is returned by [`Shape.getName()`](Shape.md#getName()) for shapes with unknown names.  The value of this constant depends on the selected Engine language locale |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Shape3D()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `canHandleClick(boolean publicOnly)` | Checks if the shape can handle mouse clicks in its current condition, namely with current public and visibility settings. |
| `ShapeDrawMode` | `getDrawMode()` | Returns the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  If the shape has been created with no-argument constructor, and has no specific limitations (like 2D-only), and drawing mode hasn't yet been set, then it is initialized to default (2D + 3D). |
| `double` | `getScaleZ()` | Returns the scale of the shape along z axis |
| `double` | `getZ()` | Returns the z coordinate of the shape (relative to the [`Shape.getLevel()`](Shape.md#getLevel()), if any). |
| `double` | `getZOffset()` | Returns the offset from z coordinate of the location base.  This e.g. |
| `void` | `setDrawMode(ShapeDrawMode drawMode)` | Sets the drawing mode of the shape (where to draw this shape: 2D, 3D or 2D+3D).  This method may be called only for shapes created using no-argument constructor (which have no limitations like 2D-only) and only once. |
| `void` | `setPos(double x, double y)` | Sets both coordinates of the shape |
| `void` | `setPos(double x, double y, double z)` | Sets coordinates of the shape |
| `void` | `setPos(Point p)` | Sets all the coordinates of the shape |
| `void` | `setRotation(double r)` | Sets the rotation of the shape. |
| `void` | `setScale(double s)` | Sets the same scale of the shape along all the axes |
| `void` | `setScale(double sx, double sy, double sz)` | Sets the scales of the shape along both axes |
| `void` | `setScaleZ(double sz)` | Sets the scale of the shape along z axis |
| `void` | `setZ(double z)` | Sets the z coordinate of the figure |
