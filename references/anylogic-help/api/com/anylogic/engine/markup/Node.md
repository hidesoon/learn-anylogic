*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Node.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Node

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Node

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<Node,Path>`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>`, `SVGElement`, `UsdElement`, `Serializable`

Direct Known Subclasses:
:   `AreaNode`, `NetworkPortImpl`, `PointNode`

---

```
public abstract class Node
extends NetworkMarkupElement
implements INode<Node,Path>, com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>, LevelMarkup
```

Implementation of `INode` for network in continuous space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Node)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Node()` |  |
| `Node(Agent owner)` |  |
| `Node(Agent owner, ShapeDrawMode drawMode, boolean isPublic, Paint fillColor, boolean limitSpeed, double maxSpeedInMPS, PathEnd<Path>... pathEnds)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `Node(Agent owner, ShapeDrawMode drawMode, boolean isPublic, Paint fillColor, PathEnd<Path>... pathEnds)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(Path path, PathEndType type)` |  |
| `final Class<? extends ExtAgentWithSpatialMetrics>` | `getCompatibleAgentExtensionClass()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final Path` | `getConnection(int index)` | Returns connection of this node with another node by index. |
| `final int` | `getConnectionsCount()` | Amount of the node's connections to other nodes. |
| `Color` | `getFillColor()` | Returns the fill color of the shape, or `null` if shape has no fill color or has textured fill (in this case [`getFillTexture()`](#getFillTexture()) should be used instead) |
| `Texture` | `getFillTexture()` | Returns the fill texture of the shape, if the shape has fill texture |
| `abstract Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `abstract Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>` | `getMaterialLibraryDescriptor()` |  |
| `double` | `getMaxSpeed(SpeedUnits units)` | Returns max allowed speed in this node in specified speed units |
| `int` | `getNumberOfTransporters()` | Returns the number of path-guided transporters inside node which is a part of a network. |
| `final double` | `getTransferDistance(Path path1, Path path2)` |  |
| `Position` | `getTransferPositionByPercent(Path path1, Path path2, double percent, Position out)` |  |
| `Agent` | `getTransporter(int index)` | Returns the path-guided transporter with specified index inside the node which is a part of a network. |
| `List<Agent>` | `getTransporters()` | Returns the list of path-guided transporters inside the node which is a part of a network. |
| `abstract double` | `getZ()` | Returns the z coordinate of the node. |
| `boolean` | `isLimitSpeed()` | Return true if speed is limited in this node, false otherwise |
| `void` | `setFillColor(Color fillColor)` | Sets the fill color of the shape. |
| `void` | `setFillColor(Paint fillColor)` | Sets the fill color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setLimitSpeed(boolean limitSpeed)` | Enables speed limit in this node if the argument is true, disables it if the argument is false The element should be uninitialized |
| `abstract void` | `setLineColor(Color lineColor)` | Sets the line color of the markup element. |
| `abstract void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setMaxSpeed(double maxSpeed, SpeedUnits units)` | Sets the maximum allowed speed in specified units |
