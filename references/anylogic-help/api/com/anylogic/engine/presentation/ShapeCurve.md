*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCurve.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class ShapeCurve

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeMultiplePoints](ShapeMultiplePoints.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapePolyLine](ShapePolyLine.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.ShapeCurve

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `Path2D`, `Path3D`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
public class ShapeCurve
extends ShapePolyLine
```

Persistent curve shape.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.ShapeCurve)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ShapeCurve()` | Constructs a curve with default attributes. |
| `ShapeCurve(boolean ispublic, double x, double y, Color lineColor, Color fillColor, int npoints, double[] dx, double[] dy, boolean closed, double lineWidth, LineStyle lineStyle)` | Deprecated. use `#ShapeCurve(boolean, double, double, Object, Object, int, boolean, double[], double[], boolean, double, LineStyle)` |
| `ShapeCurve(boolean ispublic, double x, double y, Paint lineColor, Paint fillColor, int npoints, boolean manualControlPoints, double[] dx, double[] dy, boolean closed, double lineWidth, LineStyle lineStyle)` | Constructs a 2D-only curve with specific attributes. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final ShapeCurve` | `clone()` | Creates and returns a copy of this shape (i.e. |
| `boolean` | `contains(double px, double py)` | Tests if the polygon (based on this polyline points) contains the point with coordinates (x,y). |
| `double` | `getPointDx(int i)` | Returns the x coordinate of a particular point of the shape relative to the start point.  In case of manual control points mode ([`isManualControlPoints()`](#isManualControlPoints()) returns `true`) returns x-coordinates of control points too. |
| `double` | `getPointDy(int i)` | Returns the y coordinate of a particular point of the shape relative to the start point.  In case of manual control points mode ([`isManualControlPoints()`](#isManualControlPoints()) returns `true`) returns y-coordinates of control points too. |
| `com.anylogic.engine.internal.presentation.ISVGComponent` | `getSVGComponent()` |  |
| `double` | `getXMax()` | This method isn't currently supported by Curve, it throws `UnsupportedOperationException`.  Please consider using polyline instead of curve. |
| `double` | `getXMin()` | This method isn't currently supported by Curve, it throws `UnsupportedOperationException`.  Please consider using polyline instead of curve. |
| `double` | `getYMax()` | This method isn't currently supported by Curve, it throws `UnsupportedOperationException`.  Please consider using polyline instead of curve. |
| `double` | `getYMin()` | This method isn't currently supported by Curve, it throws `UnsupportedOperationException`.  Please consider using polyline instead of curve. |
| `boolean` | `isManualControlPoints()` | Returns `true` if this curve uses manually specified control points (which are specified in the `dx` and `dy` arrays) |
| `double` | `length()` | This method isn't currently supported by Curve, it throws `UnsupportedOperationException`.  Please consider using polyline instead of curve. |
| `void` | `postSVGShapeSpecificAttributes(List<String> att, List<String> val, boolean publicOnly)` | Posts general properties specific to a particular shape class. |
| `Point` | `randomPointInside(Random rng)` | This method isn't currently supported by Curve, it throws `UnsupportedOperationException`.  Please consider using polyline instead of curve. |
| `void` | `setManualControlPoints(boolean manualControlPoints)` | Sets control points mode: manual or automatic.  In the manual mode curve uses control points specified in the `dx` and `dy` arrays |
| `void` | `setPoint(int i, double ptdx, double ptdy)` | Sets the coordinates of a particular point of the shape relative to the start point.  In case of manual control points mode ([`isManualControlPoints()`](#isManualControlPoints()) returns `true`) sets coordinates of control points too. |
| `void` | `setPointDx(int i, double ptdx)` | Sets the x coordinate of a particular point of the shape relative to the start point.  In case of manual control points mode ([`isManualControlPoints()`](#isManualControlPoints()) returns `true`) sets x-coordinates of control points too. |
| `void` | `setPointDy(int i, double ptdy)` | Sets the y coordinate of a particular point of the shape relative to the start point.  In case of manual control points mode ([`isManualControlPoints()`](#isManualControlPoints()) returns `true`) sets y-coordinates of control points too. |
