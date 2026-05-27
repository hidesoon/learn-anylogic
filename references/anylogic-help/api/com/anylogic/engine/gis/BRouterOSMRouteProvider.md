*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/BRouterOSMRouteProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class BRouterOSMRouteProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteProvider](AbstractGISRouteProvider.md "class in com.anylogic.engine.gis")

[com.anylogic.engine.gis.AbstractGISRouteProviderWithCache](AbstractGISRouteProviderWithCache.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.BRouterOSMRouteProvider

All Implemented Interfaces:
:   `IGISRouteProvider`, `IRouteProvider<Curve<GISMarkupSegment>>`, `Serializable`

---

```
@AnyLogicInternalAPI
public class BRouterOSMRouteProvider
extends AbstractGISRouteProviderWithCache
```

Online route provider
[BRouter](http://brouter.de/brouter/)

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.BRouterOSMRouteProvider)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `CACHE_ID_PREFIX_BROUTER` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `BRouterOSMRouteProvider(RouteProviderTransportType transportType, int precisionInMeters)` |  |

## Method Summary
