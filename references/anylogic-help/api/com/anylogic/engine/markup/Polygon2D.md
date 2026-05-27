*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Polygon2D.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Polygon2D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.Polygon2D

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public class Polygon2D
extends Object
implements Serializable
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Polygon2D)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Polygon2D(MarkupShape owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addVertex(double x, double y)` |  |
| `boolean` | `contains(double px, double py)` |  |
| `double` | `getArea()` |  |
| `Point` | `getCenter(Point out)` |  |
| `double` | `getNearestPoint(Point output, double rx, double ry)` |  |
| `int` | `getNPoints()` | Returns the number of points in the markup element. |
| `Path2D.Double` | `getPath()` |  |
| `double` | `getPointDx(int i)` | Returns the x coordinate of a particular point of the markup element relative to the start point. |
| `double` | `getPointDy(int i)` | Returns the y coordinate of a particular point of the markup element relative to the start point. |
| `double` | `getXMax()` | Returns the x coordinate of the bottom-right corner of bounding rectangle for this markup element. |
| `double` | `getXMin()` | Returns the x coordinate of the top-left corner of bounding rectangle for this markup element. |
| `double` | `getYMax()` | Returns the y coordinate of the bottom-right corner of bounding rectangle for this markup element. |
| `double` | `getYMin()` | Returns the y coordinate of the top-left corner of bounding rectangle for this markup element. |
| `void` | `initialize()` |  |
| `Point` | `randomPointInside(Random rng, Point out)` |  |
| `void` | `setPoints(double[] dx, double[] dy)` |  |
