*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/CachedGISRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class CachedGISRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.ChainedGISRouteFinder](ChainedGISRouteFinder.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.CachedGISRouteFinder

All Implemented Interfaces:
:   `IGISRouteFinder`

---

```
@AnyLogicInternalAPI
public class CachedGISRouteFinder
extends ChainedGISRouteFinder
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CachedGISRouteFinder(IGISRouteFinder base, Supplier<AnyLogicMapDB> dbSupplier, String routeCacheId, String distanceCacheId, UnaryOperator<double[]> cacheKeyFunction, boolean readOnlyRouteCache)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResultDouble` | `getDistance(double[] latLonPoints)` | Returns the distance by route with intermediate points. |
| `GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns the route build with the given input coordinates.  The result may depend on internal state of this route finder (e.g. |
