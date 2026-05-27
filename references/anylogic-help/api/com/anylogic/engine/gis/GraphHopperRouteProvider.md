*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GraphHopperRouteProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GraphHopperRouteProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteProvider](AbstractGISRouteProvider.md "class in com.anylogic.engine.gis")

[com.anylogic.engine.gis.AbstractGISRouteProviderWithCache](AbstractGISRouteProviderWithCache.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.GraphHopperRouteProvider

All Implemented Interfaces:
:   `IGISRouteProvider`, `IRouteProvider<Curve<GISMarkupSegment>>`, `Serializable`

---

```
public class GraphHopperRouteProvider
extends AbstractGISRouteProviderWithCache
```

Provider of routes [www.graphhopper.com](https://graphhopper.com/).
It requires file based routing graph and works without internet connection.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.GraphHopperRouteProvider)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GraphHopperRouteProvider(String graphFilesPath, String pathFindingAlgorithm, RoutingMethod routingMethod, int precisionInMeters)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `close()` | Call com.graphhopper.GraphHopper.close() to release files. |
