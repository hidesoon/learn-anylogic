*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AbstractGISRouteProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AbstractGISRouteProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.AbstractGISRouteProvider

All Implemented Interfaces:
:   `IGISRouteProvider`, `IRouteProvider<Curve<GISMarkupSegment>>`, `Serializable`

Direct Known Subclasses:
:   `AbstractGISRouteProviderWithCache`, `PlainGISRouteProvider`

---

```
@AnyLogicInternalAPI
public abstract class AbstractGISRouteProvider
extends Object
implements IGISRouteProvider
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.AbstractGISRouteProvider)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractGISRouteProvider()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final double` | `getDistance(double... latLonPoints)` | Calculates distance by route with intermediate points. |
| `final Curve<GISMarkupSegment>` | `getPathData(double... latLonPoints)` | Create route with intermediate points specified by pairs of latitude and longitude. |
| `final Curve<GISMarkupSegment>` | `getPathData(double startLat, double startLon, double endLat, double endLon)` | Creates route from one point to another. |
| `final boolean` | `isThrowError()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `AbstractGISRouteProvider` | `setRouteNotFoundBehavior(GISRouteNotFoundBehavior behavior)` | Configures this route provider to either [throw error](GISRouteNotFoundBehavior.md#THROW_ERROR) or [create a straight route](GISRouteNotFoundBehavior.md#CREATE_STRAIGHT_ROUTE) if the requested route can't be found (applicable for route providers supporting route search). |
