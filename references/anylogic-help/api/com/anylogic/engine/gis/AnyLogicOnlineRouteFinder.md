*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AnyLogicOnlineRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AnyLogicOnlineRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteFinder](AbstractGISRouteFinder.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.AnyLogicOnlineRouteFinder

All Implemented Interfaces:
:   `IGISRouteFinder`

---

```
public class AnyLogicOnlineRouteFinder
extends AbstractGISRouteFinder
```

AnyLogic online route provider
**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AnyLogicOnlineRouteFinder(RoutingMethod routingMethod, RouteProviderTransportType transportType)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResultDouble` | `getDistance(double[] latLonPoints)` | Returns the distance by route with intermediate points. |
| `GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns curve obtained "as is" from route provider, without generalization |
| `void` | `setUrlParamsEncoder(UnaryOperator<String> urlParamsEncoder)` |  |
