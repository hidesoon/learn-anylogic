*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/INode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface INode<N extends INode<N,P>,P extends IPath<N>>

Type Parameters:
:   `N` - network node, an instance of `INode`
:   `P` - network path, an instance of `IPath`

All Superinterfaces:
:   `AnimationStaticLocationProvider`, `INetworkMarkupElement`, `Serializable`

All Known Implementing Classes:
:   `AreaNode`, `ConveyorCustomStation`, `ConveyorNode`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorTransferTable`, `ConveyorTransitionalNode`, `ConveyorTurnStation`, `ConveyorTurntable`, `GISNode`, `GISPoint`, `GISRegion`, `NetworkPortImpl`, `Node`, `PointNode`, `PolygonalNode`, `QueueArea`, `RectangularNode`

---

```
public interface INode<N extends INode<N,P>,P extends IPath<N>>
extends INetworkMarkupElement, AnimationStaticLocationProvider
```

Basic interface for network node.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(P path, PathEndType type)` |  |
| `Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `P` | `getConnection(int index)` | Returns connection of this node with another node by index. |
| `int` | `getConnectionsCount()` | Amount of the node's connections to other nodes. |
| `Color` | `getFillColor()` | Returns the fill color of the shape, or `null` if shape has no fill color or has textured fill (in this case [`getFillTexture()`](#getFillTexture()) should be used instead) |
| `Texture` | `getFillTexture()` | Returns the fill texture of the shape, if the shape has fill texture |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `String` | `getName()` |  |
| `double` | `getTransferDistance(P path1, P path2)` |  |
| `Position` | `getTransferPositionByPercent(P path1, P path2, double percent, Position out)` |  |
| `void` | `setFillColor(Paint color)` | Sets the fill color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
