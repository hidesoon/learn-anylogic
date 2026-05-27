*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/PointNode.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class PointNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Node](Node.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.PointNode

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasBoundingRectangle`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<Node,Path>`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.INodeDescriptor<Agent>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class PointNode
extends Node
implements HasBoundingRectangle, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.PointNode)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PointNode()` |  |
| `PointNode(Agent owner)` |  |
| `PointNode(Agent owner, double x, double y, double z)` |  |
| `PointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double radius, Paint fillColor)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double radius, Paint fillColor, boolean limitSpeed, double maxSpeedInMPS, PathEnd<Path>[] pathends)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `PointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double radius, Paint fillColor, boolean limitSpeed, double maxSpeedInMPS, PathEnd<Path>[] pathends, PathConnector<Path,Node>... connectors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, double radius, Paint fillColor, PathEnd<Path>[] pathEnds, PathConnector<Path,Node>... connectors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `PointNode(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double z, PathEnd<Path>[] pathEnds, PathConnector<Path,Node>... connectors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnector(PathConnector<Path,Node> connector)` | Adds internal path connector to the inside of this node. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Collection<Path>` | `getConnectedExternalPaths(Path path)` |  |
| `Collection<Path>` | `getConnectedInternalPaths(Path path)` |  |
| `PathConnector<Path,Node>` | `getConnector(Path path1, Path path2)` | Return a connection between two paths inside the node. |
| `List<PathConnector<Path,Node>>` | `getConnectors()` |  |
| `Color` | `getLineColor()` | The same as [`Node.getFillColor()`](Node.md#getFillColor()) |
| `Texture` | `getLineTexture()` | The same as [`Node.getFillTexture()`](Node.md#getFillTexture()) |
| `double` | `getNearestPoint(double x, double y, double z, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, Point output)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `double` | `getRadius()` | Returns the radius of this point node |
| `Position` | `getTransferPositionByPercent(Path path1, Path path2, double percent, Position out)` |  |
| `double` | `getX()` | Returns the x coordinate |
| `Point` | `getXYZ()` | Returns (x, y, z) coordinates of this node |
| `Point` | `getXYZ(Point out)` | Returns (x, y, z) coordinates of this node |
| `double` | `getY()` | Returns the y coordinate |
| `double` | `getZ()` | Returns the z coordinate of the node. |
| `Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setLineColor(Color lineColor)` | The same as [`Node.setFillColor(Color)`](Node.md#setFillColor(java.awt.Paint)) |
| `void` | `setLineColor(Paint lineColor)` | The same as [`Node.setFillColor(Paint)`](Node.md#setFillColor(java.awt.Paint)) |
| `void` | `setPos(double x, double y)` | Sets coordinates of the point node |
| `void` | `setPos(double x, double y, double z)` | Sets coordinates of the point node |
| `void` | `setRadius(double radius)` | Sets the radius of this point node. |
