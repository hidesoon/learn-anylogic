*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/IGISRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Interface IGISRouteFinder

All Known Implementing Classes:
:   `AbstractGISRouteFinder`, `AnyLogicOnlineRouteFinder`, `BRouterOSMRouteFinder`, `CachedGISRouteFinder`, `ChainedGISRouteFinder`, `GeneralizingGISRouteFinder`, `GISStraightRouteFinder`, `GraphHopperRouteFinder`, `ServerCaringGISRouteFinder`, `StrangeRouteGuard`, `YoursOSMRouteFinder`

---

```
@AnyLogicInternalAPI
public interface IGISRouteFinder
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResultDouble` | `getDistance(double[] latLonPoints)` | Returns the distance by route with intermediate points. |
| `GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns the route build with the given input coordinates.  The result may depend on internal state of this route finder (e.g. |
| `void` | `registerDistanceCache(BiConsumer<double[],GISResultDouble> distanceCachePut)` |  |
