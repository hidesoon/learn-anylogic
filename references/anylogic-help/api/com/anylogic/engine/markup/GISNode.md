*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.GISMarkupElement](GISMarkupElement.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.GISNode

All Implemented Interfaces:
:   `IGeographicSearchEntry`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `INetworkMarkupElement`, `INode<GISNode,GISRoute>`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `GISPoint`, `GISRegion`

---

```
public abstract class GISNode
extends GISMarkupElement
implements INode<GISNode,GISRoute>, IGeographicSearchEntry
```

Implementation of `INode` for network in GIS space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISNode)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(GISRoute path, PathEndType type)` |  |
| `final Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final GISRoute` | `getConnection(int index)` | Returns connection of this node with another node by index. |
| `final int` | `getConnectionsCount()` | Amount of the node's connections to other nodes. |
| `Color` | `getFillColor()` | Returns the fill color of the shape, or `null` if shape has no fill color or has textured fill (in this case [`INode.getFillTexture()`](INode.md#getFillTexture()) should be used instead) |
| `Texture` | `getFillTexture()` | Returns the fill texture of the shape, if the shape has fill texture |
| `String` | `getTitle()` | Returns the title of this geographic place |
| `final double` | `getTransferDistance(GISRoute path1, GISRoute path2)` |  |
| `Position` | `getTransferPositionByPercent(GISRoute path1, GISRoute path2, double percent, Position out)` |  |
| `void` | `setFillColor(Paint color)` | Sets the fill color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setTitle(String title)` | Sets the title of this geographic place |
