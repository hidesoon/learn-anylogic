*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISNetwork.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISNetwork

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<Owner>

[com.anylogic.engine.markup.AbstractNetwork](AbstractNetwork.md "class in com.anylogic.engine.markup")<[GISNode](GISNode.md "class in com.anylogic.engine.markup"),[GISRoute](GISRoute.md "class in com.anylogic.engine.markup"),[ShapeGISMap](../presentation/ShapeGISMap.md "class in com.anylogic.engine.presentation")>

com.anylogic.engine.markup.GISNetwork

All Implemented Interfaces:
:   `IRouteProvider<ShortestPathData<GISNode,GISRoute>>`, `INetwork<GISNode,GISRoute>`, `Serializable`

---

```
public class GISNetwork
extends AbstractNetwork<GISNode,GISRoute,ShapeGISMap>
```

Implementation of network for agent movement in GIS space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISNetwork)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISNetwork(ShapeGISMap map, String name)` | Creates an empty network without nodes and edges. |
| `GISNetwork(ShapeGISMap map, String name, boolean visible)` | Creates an empty network without nodes and edges. |
| `GISNetwork(ShapeGISMap map, String name, boolean visible, GISMarkupElement... markupShapes)` | Creates network with nodes and edges in GIS space and initializes it. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAll(GISMarkupElement... markupShapes)` | Adds nodes and relations to this network. |
| `Stream<? extends AbstractMarkup>` | `elementsInternal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `GISNode` | `getNearestNode(double lat, double lon)` | Returns the node in this network that is the closest to the given latitude and longitude |
| `double` | `getPlainDistance(Point firstPoint, Point secondPoint)` | Straight line distance between two points. |
| `Agent` | `getSpace()` | Returns the space where the markup element is defined |
| `void` | `initialize()` | Initialization of markup aggregator (e.g. |
