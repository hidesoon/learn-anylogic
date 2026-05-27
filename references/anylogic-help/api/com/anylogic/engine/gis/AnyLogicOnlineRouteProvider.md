*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AnyLogicOnlineRouteProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AnyLogicOnlineRouteProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteProvider](AbstractGISRouteProvider.md "class in com.anylogic.engine.gis")

[com.anylogic.engine.gis.AbstractGISRouteProviderWithCache](AbstractGISRouteProviderWithCache.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.AnyLogicOnlineRouteProvider

All Implemented Interfaces:
:   `IGISRouteProvider`, `IRouteProvider<Curve<GISMarkupSegment>>`, `Serializable`

---

```
@AnyLogicInternalAPI
public class AnyLogicOnlineRouteProvider
extends AbstractGISRouteProviderWithCache
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.AnyLogicOnlineRouteProvider)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `CACHE_ID_PREFIX_ANYLOGIC_ROUTE` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AnyLogicOnlineRouteProvider(RoutingMethod routingMethod, RouteProviderTransportType transportType, int precisionInMeters)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static String` | `getRouteCacheId(RoutingMethod routingMethod, RouteProviderTransportType transportType)` |  |
