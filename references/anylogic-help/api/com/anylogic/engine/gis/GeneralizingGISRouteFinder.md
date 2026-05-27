*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GeneralizingGISRouteFinder.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GeneralizingGISRouteFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.ChainedGISRouteFinder](ChainedGISRouteFinder.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.GeneralizingGISRouteFinder

Record Components:
:   `latLonPoints` - (lat, lon) pairs representing, the start, then optional intermediate, and the end points.

All Implemented Interfaces:
:   `IGISRouteFinder`

---

```
@AnyLogicInternalAPI
public class GeneralizingGISRouteFinder
extends ChainedGISRouteFinder
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Returns *generalized* curve obtained from route provider.
**Note the different format of returned result**.
This method also calculates the real length of curve segments using the data from the route provider.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GeneralizingGISRouteFinder(IGISRouteFinder base, int precisionInMeters)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResultDouble` | `getDistance(double[] latLonPoints)` | Returns the distance by route with intermediate points. |
| `int` | `getPrecisionInMeters()` |  |
| `GISResult<double[]>` | `getRoute(double[] latLonPoints)` | Returns the route build with the given input coordinates.  The result may depend on internal state of this route finder (e.g. |
