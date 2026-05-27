*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/ChainedGISRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class ChainedGISRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.ChainedGISRouteFinder

All Implemented Interfaces:
:   `IGISRouteFinder`

Direct Known Subclasses:
:   `CachedGISRouteFinder`, `GeneralizingGISRouteFinder`, `ServerCaringGISRouteFinder`, `StrangeRouteGuard`

---

```
@AnyLogicInternalAPI
public abstract class ChainedGISRouteFinder
extends Object
implements IGISRouteFinder
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `registerDistanceCache(BiConsumer<double[],GISResultDouble> distanceCachePut)` |  |
