*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/AbstractNetwork.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class AbstractNetwork<N extends INode<N,P>,P extends IPath<N>,Owner>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupAggregator](AbstractMarkupAggregator.md "class in com.anylogic.engine.markup")<Owner>

com.anylogic.engine.markup.AbstractNetwork<N,P,Owner>

All Implemented Interfaces:
:   `IRouteProvider<ShortestPathData<N,P>>`, `INetwork<N,P>`, `Serializable`

Direct Known Subclasses:
:   `ConveyorNetwork`, `GISNetwork`, `Network`

---

```
@AnyLogicInternalAPI
public abstract class AbstractNetwork<N extends INode<N,P>,P extends IPath<N>,Owner>
extends AbstractMarkupAggregator<Owner>
implements INetwork<N,P>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.AbstractNetwork)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractNetwork(Owner owner, String name)` |  |
| `AbstractNetwork(Owner owner, String name, boolean isPublic, boolean visible)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(N n)` | Adds node to network. |
| `void` | `add(P p)` | Adds relation to network. |
| `double` | `getDistance(Point startPoint, Point endPoint)` | Creates a route from one point to another and calculates its length. |
| `double` | `getDistance(Point source, Point target, ShortestPathData<N,P> data)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, N from, N to, ShortestPathData<N,P> data)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, N from, N to, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, N from, P to, double toOffset, ShortestPathData<N,P> data)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, N from, P to, double toOffset, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, P from, double fromOffset, N to, ShortestPathData<N,P> data)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, P from, double fromOffset, N to, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, P from, double fromOffset, P to, double toOffset, ShortestPathData<N,P> data)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(Point source, Point target, P from, double fromOffset, P to, double toOffset, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance between two points using the network paths. |
| `double` | `getDistance(N from, N to, ShortestPathData<N,P> data)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getDistance(N from, N to, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getDistance(N from, P to, double toOffset, ShortestPathData<N,P> data)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getDistance(N from, P to, double toOffset, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getDistance(P from, double fromOffset, N to, ShortestPathData<N,P> data)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getDistance(P from, double fromOffset, N to, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getDistance(P from, double fromOffset, P to, double toOffset, ShortestPathData<N,P> data)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getDistance(P from, double fromOffset, P to, double toOffset, ShortestPathData<N,P> data, LengthUnits units)` | Calculates the distance from source object in the network to the target object. |
| `double` | `getLength(ShortestPathData<N,P> pathData)` | Retrieves length of the specified route. |
| `INetworkMarkupElement` | `getNearestNetworkElement(double x, double y, double z, Point out)` | Looking for the closest markup element in this network to the given coordinates. |
| `INetworkMarkupElement` | `getNearestNetworkElement(Agent agent, Point out)` | Looking for the closest markup element in this network to the given agent. |
| `INetworkMarkupElement` | `getNearestNetworkElement(Point givenPoint, Point out)` | Looking for the closest markup element in this network to the given point. |
| `N` | `getNearestNode(double x, double y, double z, Point out)` | Looking for the closest node in this network to the given coordinates. |
| `N` | `getNearestNode(Agent agent, Point out)` | Looking for the closest node in this network to the given agent. |
| `N` | `getNearestNode(Point givenPoint)` | Looking for the closest node in this network to the given point. |
| `N` | `getNearestNode(Point givenPoint, Point out)` | Looking for the closest node in this network to the given point. |
| `P` | `getNearestPath(double x, double y, double z, Point out)` | Looking for the closest path in this network to the given coordinates. |
| `P` | `getNearestPath(Agent agent, Point out)` | Looking for the closest path in this network to the given agent. |
| `P` | `getNearestPath(Point givenPoint, Point out)` | Looking for the closest path in this network to the given point. |
| `N` | `getNode(int index)` |  |
| `int` | `getNodeCount()` | Amount of nodes in this network. |
| `P` | `getPath(int index)` |  |
| `int` | `getPathCount()` | Amount of paths in this network. |
| `ShortestPathData<N,P>` | `getPathData(Point startPoint, Point endPoint, ShortestPathData<N,P> out)` | Retrieves the route data an agent will use to calculate the route length and determine its position on the route by calling [`IRouteProvider.getLength(IPathData)`](../IRouteProvider.md#getLength(T)) and [`IRouteProvider.getPositionAtOffset(IPathData, double, Position)`](../IRouteProvider.md#getPositionAtOffset(T,double,com.anylogic.engine.Position)) respectively. |
| `abstract double` | `getPlainDistance(Point firstPoint, Point secondPoint)` | Straight line distance between two points. |
| `double` | `getPlainDistance(Point firstPoint, Point secondPoint, LengthUnits units)` | Straight line distance between two points in given units of length. |
| `Position` | `getPosition(ShortestPathData<N,P> data, double offset, LengthUnits units, Position out)` | Calculates current position on the shortest path through network by the given offset |
| `Position` | `getPosition(ShortestPathData<N,P> data, double offset, Position out)` | Calculates current position on the shortest path through network by the given offset |
| `Position` | `getPositionAtOffset(ShortestPathData<N,P> pathData, double offset, Position out)` | Retrieves agent's position on the route. |
| `List<INetwork<?,?>>` | `getRelatedNetworks()` |  |
| `List<N>` | `nodes()` |  |
| `List<P>` | `paths()` |  |
| `List<NetworkPort>` | `ports()` |  |
