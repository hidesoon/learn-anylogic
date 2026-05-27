*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/INetwork.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface INetwork<N extends INode<N,P>,P extends IPath<N>>

Type Parameters:
:   `N` - network node, an instance of `INode`
:   `P` - network path, an instance of `IPath`

All Superinterfaces:
:   `IRouteProvider<ShortestPathData<N,P>>`, `Serializable`

All Known Implementing Classes:
:   `AbstractNetwork`, `ConveyorNetwork`, `GISNetwork`, `Network`

---

```
public interface INetwork<N extends INode<N,P>,P extends IPath<N>>
extends IRouteProvider<ShortestPathData<N,P>>
```

Basic interface of network for agent movement based on markup elements.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `add(N n)` | Adds node to network. |
| `void` | `add(P p)` | Adds relation to network. |
| `Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
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
| `INetworkMarkupElement` | `getNearestNetworkElement(double x, double y, double z, Point out)` | Looking for the closest markup element in this network to the given coordinates. |
| `INetworkMarkupElement` | `getNearestNetworkElement(Point givenPoint, Point out)` | Looking for the closest markup element in this network to the given point. |
| `N` | `getNearestNode(Point p)` | Looking for the closest node in this network to the given point. |
| `N` | `getNode(int index)` |  |
| `int` | `getNodeCount()` | Amount of nodes in this network. |
| `P` | `getPath(int index)` |  |
| `int` | `getPathCount()` | Amount of paths in this network. |
| `double` | `getPlainDistance(Point firstPoint, Point secondPoint)` | Straight line distance between two points. |
| `double` | `getPlainDistance(Point firstPoint, Point secondPoint, LengthUnits units)` | Straight line distance between two points in given units of length. |
| `Position` | `getPosition(ShortestPathData<N,P> data, double reverseOffset, LengthUnits units, Position out)` | Calculates current position on the shortest path through network by the given offset |
| `Position` | `getPosition(ShortestPathData<N,P> data, double reverseOffset, Position out)` | Calculates current position on the shortest path through network by the given offset |
| `List<INetwork<?,?>>` | `getRelatedNetworks()` |  |
| `Agent` | `getSpace()` | Returns the space where the markup element is defined |
| `List<N>` | `nodes()` |  |
| `List<P>` | `paths()` |  |
| `List<NetworkPort>` | `ports()` |  |
