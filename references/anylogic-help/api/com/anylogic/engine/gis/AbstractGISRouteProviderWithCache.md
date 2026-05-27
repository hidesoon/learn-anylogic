*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AbstractGISRouteProviderWithCache.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AbstractGISRouteProviderWithCache

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteProvider](AbstractGISRouteProvider.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.AbstractGISRouteProviderWithCache

All Implemented Interfaces:
:   `IGISRouteProvider`, `IRouteProvider<Curve<GISMarkupSegment>>`, `Serializable`

Direct Known Subclasses:
:   `AnyLogicOnlineRouteProvider`, `BRouterOSMRouteProvider`, `GraphHopperRouteProvider`, `YoursOSMRouteProvider`

---

```
@AnyLogicInternalAPI
public abstract class AbstractGISRouteProviderWithCache
extends AbstractGISRouteProvider
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.AbstractGISRouteProviderWithCache)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractGISRouteProviderWithCache(com.anylogic.engine.gis.AbstractGISRouteProviderWithCache.GISRouteFinderConfig routeFinderConfig)` | Subclasses should call this super-constructor at start and `#initialize()` at the end of their constructor code. |

## Method Summary
