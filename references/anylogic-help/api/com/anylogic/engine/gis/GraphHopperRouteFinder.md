*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GraphHopperRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GraphHopperRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteFinder](AbstractGISRouteFinder.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.GraphHopperRouteFinder

All Implemented Interfaces:
:   `IGISRouteFinder`

---

```
@AnyLogicInternalAPI
public class GraphHopperRouteFinder
extends AbstractGISRouteFinder
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Provider of routes [www.graphhopper.com](https://graphhopper.com/).
It requires file based routing graph and works without internet connection.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static String[]` | `GRAPH_HOPPER_ROUTING_FILES` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GraphHopperRouteFinder(String graphFilesPath, String pathFindingAlgorithm, RoutingMethod routingMethod, int precisionInMeters)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `close()` | Call com.graphhopper.GraphHopper.close() to release files. |
| `static com.graphhopper.GraphHopper` | `createGraphhopperInstance()` |  |
| `static boolean` | `folderContainsGraphHopperRoutingGraph(String folder)` |  |
| `GISResultDouble` | `getDistance(double[] latLonPoints)` | Returns the distance by route with intermediate points. |
| `String` | `getGraphFilesPath()` |  |
| `String` | `getPathFindingAlgorithm()` |  |
| `int` | `getPrecisionInMeters()` |  |
| `GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns curve obtained "as is" from route provider, without generalization |
| `RoutingMethod` | `getRoutingMethod()` |  |
| `void` | `setPathFindingAlgorithm(String pathFindingAlgorithm)` |  |
| `void` | `setPrecisionInMeters(int precisionInMeters)` |  |
| `void` | `setRoutingMethod(RoutingMethod routingMethod)` |  |
