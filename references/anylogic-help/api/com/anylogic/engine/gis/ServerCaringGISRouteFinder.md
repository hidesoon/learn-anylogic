*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/ServerCaringGISRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class ServerCaringGISRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.ChainedGISRouteFinder](ChainedGISRouteFinder.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.ServerCaringGISRouteFinder

All Implemented Interfaces:
:   `IGISRouteFinder`

---

```
@AnyLogicInternalAPI
public class ServerCaringGISRouteFinder
extends ChainedGISRouteFinder
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
This is a short-circuiting proxy provider which disables itself for a
configured period of time, once the underlying provider returns null

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ServerCaringGISRouteFinder(IGISRouteFinder base, long networkRecoveryTimeoutInMillis)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResultDouble` | `getDistance(double[] latLonPoints)` | Returns the distance by route with intermediate points. |
| `GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns the route build with the given input coordinates.  The result may depend on internal state of this route finder (e.g. |
