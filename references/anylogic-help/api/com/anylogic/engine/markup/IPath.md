*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/IPath.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface IPath<N extends INode>

Type Parameters:
:   `N` - network node based on `com.anylogic.engine.markup.INode` interface

All Superinterfaces:
:   `AnimationMovingLocationProvider`, `AnimationStaticLocationProvider`, `INetworkMarkupElement`, `Serializable`

All Known Implementing Classes:
:   `ConveyorPath`, `GISRoute`, `Path`

---

```
public interface IPath<N extends INode>
extends INetworkMarkupElement, AnimationMovingLocationProvider
```

This is the basic interface for implementation connection between nodes inside network.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Point` | `getEndPoint()` | Returns the location of the end point |
| `Point` | `getEndPoint(Point out)` | Returns the location of the end point |
| `Position` | `getEndPosition(Position out)` | Returns the end position |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `double` | `getLineWidth()` | Returns the line width of the markup element. |
| `String` | `getName()` | If the markup shape is declared as field in an agent class, e.g. |
| `N` | `getOtherNode(N n)` | If the given node is source of this path, returns path's target, otherwise returns source. |
| `default INode<?,?>` | `getPathEnd(PathEndType type)` |  |
| `Position` | `getPositionAtOffset(double offset, LengthUnits units, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)). |
| `Position` | `getPositionAtOffset(double offset, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)). |
| `IMarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `N` | `getSource()` | Returns source node of this path. |
| `Point` | `getStartPoint()` | Returns the location of the start point |
| `Point` | `getStartPoint(Point out)` | Returns the location of the start point |
| `Position` | `getStartPosition(Position out)` | Returns the start position |
| `N` | `getTarget()` | Returns target node of this path. |
| `boolean` | `isBidirectional()` | Returns the 'bidirectional' property (`true` by default). |
| `Iterator<? extends IMarkupSegment>` | `iterator()` | Returns iterator over segments of the path |
| `void` | `setBidirectional(boolean bidirectional)` | Sets the 'bidirectional' property (`true` by default). |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setLineWidth(double width)` | Sets the line width of the markup element, 0 means thinnest possible |
| `void` | `setSource(N node)` | Sets source node of this path. |
| `void` | `setTarget(N node)` | Sets source node of this path. |
