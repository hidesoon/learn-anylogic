*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISPoint.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISPoint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.GISMarkupElement](GISMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.GISNode](GISNode.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.GISPoint

All Implemented Interfaces:
:   `IGeographicSearchEntry`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `INetworkMarkupElement`, `INode<GISNode,GISRoute>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class GISPoint
extends GISNode
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISPoint)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISPoint(ShapeGISMap map, boolean isPermanent, double latitude, double longitude)` |  |
| `GISPoint(ShapeGISMap map, boolean isPermanent, double latitude, double longitude, double radius, Paint fillColor, Paint lineColor, double linewidth, LineStyle lineStyle, String title)` |  |
| `GISPoint(ShapeGISMap map, double latitude, double longitude)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double lat, double lon)` | Check this element contains a point with given coordinates. |
| `double` | `distance(double latitude, double longitude)` | Calculates distance from this point to another. |
| `double` | `distance(double latitude, double longitude, LengthUnits units)` | Calculates distance from this point to another. |
| `double` | `distance(GISPoint givenPoint)` | Calculates distance from this point to another. |
| `double` | `distance(GISPoint givenPoint, LengthUnits units)` | Calculates distance from this point to another. |
| `double` | `getLatitude()` | Returns the latitude of this gis point |
| `Point` | `getLocation()` | Returns the (latitude, longidute) of this GIS point |
| `Point` | `getLocation(Point out)` | Returns the (latitude, longidute) of this GIS point, uses the given `out` instance, if not `null` |
| `double` | `getLongitude()` | Returns the longitude of this gis point |
| `double` | `getNearestPoint(double lat, double lon, Point out)` |  |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `Presentable` | `getPresentable()` |  |
| `double` | `getRadius()` | Returns radius of the circle of this GIS point |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setRadius(double radius)` | Dynamically changes radius of GISPoint |
| `String` | `toString()` |  |
