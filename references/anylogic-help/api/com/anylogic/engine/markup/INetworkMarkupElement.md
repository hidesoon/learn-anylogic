*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/INetworkMarkupElement.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface INetworkMarkupElement

All Superinterfaces:
:   `Serializable`

All Known Subinterfaces:
:   `INode<N,P>`, `IPath<N>`

All Known Implementing Classes:
:   `AreaNode`, `ConveyorCustomStation`, `ConveyorMarkupElement`, `ConveyorNode`, `ConveyorPath`, `ConveyorPathPart`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorSimpleStation`, `ConveyorSpur`, `ConveyorStation`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `GISMarkupElement`, `GISNode`, `GISPoint`, `GISRegion`, `GISRoute`, `NetworkMarkupElement`, `NetworkPortImpl`, `Node`, `PalletRack`, `Path`, `PointNode`, `PolygonalNode`, `PositionOnConveyor`, `QueueArea`, `RectangularNode`

---

```
public interface INetworkMarkupElement
extends Serializable
```

Basic interface for markup element which could be used in network.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double x, double y)` | Check this element contains a point with given coordinates. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `INetwork` | `getNetwork()` |  |
| `Agent` | `getSpace()` | Returns the space where the markup element is defined |
| `default Point` | `randomPointInside()` | Returns the randomly chosen point inside the shape area.  This method utilises Random Number Generator of the Presentable object containing this shape. |
| `default Point` | `randomPointInside(Point out)` | Returns the randomly chosen point inside the shape area.  This method utilises Random Number Generator of the Presentable object containing this shape. |
| `default Point` | `randomPointInside(Random rng)` | Returns the randomly chosen point inside the fill-area of the polyline (like if it was closed). |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
