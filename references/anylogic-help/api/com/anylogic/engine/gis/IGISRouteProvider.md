*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/IGISRouteProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Interface IGISRouteProvider

All Superinterfaces:
:   `IRouteProvider<Curve<GISMarkupSegment>>`, `Serializable`

All Known Implementing Classes:
:   `AbstractGISRouteProvider`, `AbstractGISRouteProviderWithCache`, `AnyLogicOnlineRouteProvider`, `BRouterOSMRouteProvider`, `GraphHopperRouteProvider`, `PlainGISRouteProvider`, `YoursOSMRouteProvider`

---

```
public interface IGISRouteProvider
extends IRouteProvider<Curve<GISMarkupSegment>>
```

Basic interface for creation of routes in GIS space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default double` | `getDistance(double... latLonPoints)` | Calculates distance by route with intermediate points. |
| `default double` | `getDistance(double startLat, double startLon, double endLat, double endLon)` | Calculates distance by route between two specified points. |
| `default double` | `getDistance(Point... points)` | Calculates distance by route with intermediate points. |
| `default double` | `getDistance(Point startPoint, Point endPoint)` | Creates a route from one point to another and calculates its length. |
| `default double` | `getLength(Curve<GISMarkupSegment> curve)` | Retrieves length of the specified route. |
| `default Curve<GISMarkupSegment>` | `getPathData(double... latLonPoints)` | Create route with intermediate points specified by pairs of latitude and longitude. |
| `Curve<GISMarkupSegment>` | `getPathData(double startLat, double startLon, double endLat, double endLon)` | Creates route from one point to another. |
| `default Curve<GISMarkupSegment>` | `getPathData(Point... points)` | Create route with intermediate points. |
| `default Curve<GISMarkupSegment>` | `getPathData(Point startPoint, Point endPoint, Curve<GISMarkupSegment> out)` | Retrieves the route data an agent will use to calculate the route length and determine its position on the route by calling [`IRouteProvider.getLength(IPathData)`](../IRouteProvider.md#getLength(T)) and [`IRouteProvider.getPositionAtOffset(IPathData, double, Position)`](../IRouteProvider.md#getPositionAtOffset(T,double,com.anylogic.engine.Position)) respectively. |
| `default Position` | `getPositionAtOffset(Curve<GISMarkupSegment> pathData, double offset, Position out)` | Retrieves agent's position on the route. |
| `default GISRoute` | `getRoute(ShapeGISMap map, double startLat, double startLon, double endLat, double endLon)` | Returns unidirectional GISRoute created according to provider's settings. |
| `default GISRoute` | `getRoute(ShapeGISMap map, double startLat, double startLon, double endLat, double endLon, boolean bidirectional)` | Returns GISRoute created according to provider's settings. |
| `default GISRoute` | `getRoute(ShapeGISMap map, GISPoint start, GISPoint end)` | Returns unidirectional GISRoute created according to provider's settings. |
| `default GISRoute` | `getRoute(ShapeGISMap map, GISPoint start, GISPoint end, boolean bidirectional)` | Returns GISRoute created according to provider's settings. |
