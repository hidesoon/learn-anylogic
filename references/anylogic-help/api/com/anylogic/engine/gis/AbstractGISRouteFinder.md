*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AbstractGISRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AbstractGISRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.AbstractGISRouteFinder

All Implemented Interfaces:
:   `IGISRouteFinder`

Direct Known Subclasses:
:   `AnyLogicOnlineRouteFinder`, `BRouterOSMRouteFinder`, `GISStraightRouteFinder`, `GraphHopperRouteFinder`, `YoursOSMRouteFinder`

---

```
@AnyLogicInternalAPI
public abstract class AbstractGISRouteFinder
extends Object
implements IGISRouteFinder
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractGISRouteFinder()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns curve obtained "as is" from route provider, without generalization |
| `void` | `registerDistanceCache(BiConsumer<double[],GISResultDouble> distanceCachePut)` |  |
