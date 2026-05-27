*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AbstractShapeGISMap.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface AbstractShapeGISMap

All Known Implementing Classes:
:   `ShapeGISMap`

---

```
@Deprecated
@AnyLogicInternalAPI
public interface AbstractShapeGISMap
```

Deprecated.

Will be removed in future releases, use [`ShapeGISMap`](presentation/ShapeGISMap.md "class in com.anylogic.engine.presentation") class instead

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getDistance(double latFrom, double lonFrom, double latTo, double lonTo)` | Deprecated. |
| `double` | `getDistance(GISPoint fromPoint, GISPoint toPoint)` | Deprecated. |
| `double` | `getDistanceByRoute(double latFrom, double lonFrom, double latTo, double lonTo)` | Deprecated. |
| `double` | `getDistanceByRoute(GISPoint fromPoint, GISPoint toPoint)` | Deprecated. |
| `GISRoute` | `getRoute(double startLatitude, double startLongitude, double endLatitude, double endLongitude)` | Deprecated. |
| `GISRoute` | `getRoute(GISPoint start, GISPoint end)` | Deprecated. |
| `IGISRouteProvider` | `getRouteProvider()` | Deprecated. |
| `void` | `pan(double toEast, double toNorth)` | Deprecated. |
| `GISPoint` | `searchFirst(String query)` | Deprecated. |
| `void` | `setCenterLatitude(double centerLatitude)` | Deprecated. |
| `void` | `setCenterLongitude(double centerLongitude)` | Deprecated. |
| `void` | `setMapScale(double mapScale)` | Deprecated. |
| `void` | `setProjectionCenter(double centerLatitude, double centerLongitude)` | Deprecated. |
| `void` | `zoomIn()` | Deprecated. |
| `void` | `zoomOut()` | Deprecated. |
