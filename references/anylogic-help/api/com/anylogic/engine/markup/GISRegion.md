*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISRegion.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISRegion

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.GISMarkupElement](GISMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.GISNode](GISNode.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.GISRegion

All Implemented Interfaces:
:   `IGeographicSearchEntry`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `INetworkMarkupElement`, `INode<GISNode,GISRoute>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class GISRegion
extends GISNode
```

Geographic region in GIS space. Could be a part of a network.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISRegion)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISRegion(ShapeGISMap map, boolean isPermanent, double[] latitudes, double[] longitudes, Paint fillColor, Paint lineColor, double lineWidth, LineStyle linestyle, String title, double realArea)` |  |
| `GISRegion(ShapeGISMap map, boolean isPermanent, double[] latLonPairs, Paint fillColor, Paint lineColor, double lineWidth, LineStyle linestyle, String title, double realArea)` |  |
| `GISRegion(ShapeGISMap map, double[] latLonPairs)` | Geographical region defined by a list of latitude-longitude coordinate pairs. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `area()` | Returns the area of this region (measured in m2) |
| `double` | `area(AreaUnits units)` | Returns the area of this region (measured in @units) |
| `boolean` | `contains(double lat, double lon)` | Check this element contains a point with given coordinates. |
| `void` | `doInitialize()` |  |
| `double` | `getNearestPoint(double lat, double lon, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `double[]` | `getPoints()` | Returns an array of decimal degree values in format [lat1, lon1, lat2, lon2, ... |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `Presentable` | `getPresentable()` |  |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
