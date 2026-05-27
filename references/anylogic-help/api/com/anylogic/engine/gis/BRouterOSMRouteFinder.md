*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/BRouterOSMRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class BRouterOSMRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteFinder](AbstractGISRouteFinder.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.BRouterOSMRouteFinder

All Implemented Interfaces:
:   `IGISRouteFinder`

---

```
@AnyLogicInternalAPI
public class BRouterOSMRouteFinder
extends AbstractGISRouteFinder
```

Online route provider [BRouter](http://brouter.de/brouter/)
**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `BRouterOSMRouteFinder(RouteProviderTransportType transportType)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResultDouble` | `getDistance(double[] latLonPoints)` | Returns the distance by route with intermediate points. |
| `GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns curve obtained "as is" from route provider, without generalization |
