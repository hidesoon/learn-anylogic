*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorNode<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorNode<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `INetworkMarkupElement`, `INode<ConveyorNode<?>,ConveyorPath<?>>`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `ConveyorCustomStation`, `ConveyorPointNode`, `ConveyorPortImpl`, `ConveyorTransitionalNode`

---

```
public abstract class ConveyorNode<T extends Agent>
extends ConveyorMarkupElement<T>
implements INode<ConveyorNode<?>,ConveyorPath<?>>, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorNode)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(ConveyorPath<?> path, PathEndType type)` |  |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ConveyorPath<?>` | `getConnection(int index)` | Returns connection of this node with another node by index. |
| `List<ConveyorPath<?>>` | `getConnections()` | Returns the list of ConveyorPath<?> objects connected to this node |
| `int` | `getConnectionsCount()` | Amount of the node's connections to other nodes. |
| `Color` | `getFillColor()` | Returns the fill color of the shape, or `null` if shape has no fill color or has textured fill (in this case [`INode.getFillTexture()`](INode.md#getFillTexture()) should be used instead) |
| `Texture` | `getFillTexture()` | Returns the fill texture of the shape, if the shape has fill texture |
| `List<ConveyorPath<?>>` | `getIncomingPaths()` | Returns the list of all incoming conveyors, i.e. |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`INode.getLineTexture()`](INode.md#getLineTexture()) should be used instead) |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `ConveyorNetwork` | `getNetwork()` |  |
| `List<ConveyorPath<?>>` | `getOutgoingPaths()` | Returns the list of all outgoing conveyors, i.e. |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `Position` | `getTransferPositionByPercent(ConveyorPath<?> path1, ConveyorPath<?> path2, double percent, Position out)` |  |
| `double` | `getX()` | Get X coordinate of this element |
| `Point` | `getXYZ(Point out)` | Returns the location of this element |
| `double` | `getY()` | Get Y coordinate of this element |
| `final double` | `getZ()` | Get Z coordinate of this element |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setFillColor(Color fillColor)` | Sets the fill color of the shape. |
| `void` | `setFillColor(Paint fillColor)` | Sets the fill color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setLineColor(Color lineColor)` | Sets the line color of the markup element. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setXYZ(double x, double y, double z)` | Sets the location of this node. |
