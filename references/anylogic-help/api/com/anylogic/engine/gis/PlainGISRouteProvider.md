*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/PlainGISRouteProvider.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class PlainGISRouteProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.AbstractGISRouteProvider](AbstractGISRouteProvider.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.PlainGISRouteProvider

All Implemented Interfaces:
:   `IGISRouteProvider`, `IRouteProvider<Curve<GISMarkupSegment>>`, `Serializable`

---

```
@AnyLogicInternalAPI
public class PlainGISRouteProvider
extends AbstractGISRouteProvider
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.gis.PlainGISRouteProvider)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PlainGISRouteProvider()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `IGISRouteFinder` | `getRouteFinder()` |  |
| `AbstractGISRouteProvider` | `setRouteNotFoundBehavior(GISRouteNotFoundBehavior behavior)` | Configures this route provider to either [throw error](GISRouteNotFoundBehavior.md#THROW_ERROR) or [create a straight route](GISRouteNotFoundBehavior.md#CREATE_STRAIGHT_ROUTE) if the requested route can't be found (applicable for route providers supporting route search). |
