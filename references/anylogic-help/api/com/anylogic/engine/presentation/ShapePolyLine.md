*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapePolyLine.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapePolyLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeMultiplePoints](ShapeMultiplePoints.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapePolyLine

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `Path2D`, `Path3D`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

Direct Known Subclasses:
:   `ShapeCurve`

---

```
public class ShapePolyLine
extends ShapeMultiplePoints
```

Persistent polyline shape.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapePolyLine)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapePolyLine()` | Constructs a polyline with default attributes. |
| `ShapePolyLine(boolean ispublic, double x, double y, Paint lineColor, Paint fillColor, int npoints, double[] dx, double[] dy, boolean closed, double lineWidth, LineStyle lineStyle)` | Constructs a 2D-only polyline with specific attributes. |
| `ShapePolyLine(ShapeDrawMode drawMode, boolean ispublic, double x, double y, double z, Paint lineColor, Paint fillColor, int npoints, double[] dx, double[] dy, double[] dz, boolean closed, double zHeight, double lineWidth, LineStyle lineStyle)` | Constructs a polyline with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ShapePolyLine` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Tests if the polygon (based on this polyline points) contains the point with coordinates (x,y). |
| `Position` | `getPosition(double value, double maxValue, boolean reverseOffset, Position out)` |  |
| `Position` | `getPosition(int index, int totalNumber, Position out)` |  |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `double` | `getXMax()` | Returns the x coordinate of the bottom-right corner of bounding rectangle for this polyline. |
| `double` | `getXMin()` | Returns the x coordinate of the top-left corner of bounding rectangle for this polyline. |
| `double` | `getYMax()` | Returns the y coordinate of the bottom-right corner of bounding rectangle for this polyline. |
| `double` | `getYMin()` | Returns the y coordinate of the top-left corner of bounding rectangle for this polyline. |
| `double` | `length()` | Calculates and returns the length of the polyline (not [scaled](Shape.md#getScaleX())), respecting its closeness.  For 3D polylines this method also respects z coordinates of points.  This method doesn't work for Curve. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside()` | Returns the randomly chosen point inside the fill-area of the polyline (like if it was closed). |
| `Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the fill-area of the polyline (like if it was closed). |
| `void` | `resetSVGComponent()` |  |
| `void` | `setRotation(double r)` | Sets the rotation of the shape. |
| `void` | `setScale(double s)` | Sets the same scale of the shape along all the axes |
| `void` | `setScale(double sx, double sy)` | Sets the scales of the shape along both axes |
| `void` | `setScaleX(double sx)` | Sets the scale of the shape along x axis |
| `void` | `setScaleY(double sy)` | Sets the scale of the shape along y axis |
