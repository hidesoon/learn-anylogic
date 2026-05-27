*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/IRouteProvider.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface IRouteProvider<T extends IPathData>

Type Parameters:
:   `T` - a route data an agent will use to calculate
    a route length and determine its position on a route

All Superinterfaces:
:   `Serializable`

All Known Subinterfaces:
:   `IGISRouteProvider`, `INetwork<N,P>`

All Known Implementing Classes:
:   `AbstractGISRouteProvider`, `AbstractGISRouteProviderWithCache`, `AbstractNetwork`, `AnyLogicOnlineRouteProvider`, `BRouterOSMRouteProvider`, `ConveyorNetwork`, `GISNetwork`, `GraphHopperRouteProvider`, `Network`, `PlainGISRouteProvider`, `YoursOSMRouteProvider`

---

```
public interface IRouteProvider<T extends IPathData>
extends Serializable
```

This is a base interface to create a route for an agent.
Route provider has several implementations: network, straight movement,
specific movement in GIS space such as movement by roads.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`IPathData`](IPathData.md "interface in com.anylogic.engine")[`Agent`](Agent.md "class in com.anylogic.engine")

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `getDistance(Point startPoint, Point endPoint)` | Creates a route from one point to another and calculates its length. |
| `double` | `getLength(T pathData)` | Retrieves length of the specified route. |
| `T` | `getPathData(Point startPoint, Point endPoint, T out)` | Retrieves the route data an agent will use to calculate the route length and determine its position on the route by calling [`getLength(IPathData)`](#getLength(T)) and [`getPositionAtOffset(IPathData, double, Position)`](#getPositionAtOffset(T,double,com.anylogic.engine.Position)) respectively. |
| `Position` | `getPositionAtOffset(T pathData, double reverseOffset, Position out)` | Retrieves agent's position on the route. |
