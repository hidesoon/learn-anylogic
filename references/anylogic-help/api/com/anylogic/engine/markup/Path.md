*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Path.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Path

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.NetworkMarkupElement](NetworkMarkupElement.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Path

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `AnimationMovingLocationProvider`, `AnimationStaticLocationProvider`, `HasBoundingRectangle`, `HasCenterPoint`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `IPath<Node>`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.IPathDescriptor<Agent>`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<MarkupSegment>`

---

```
public class Path
extends NetworkMarkupElement
implements IPath<Node>, Iterable<MarkupSegment>, com.anylogic.engine.markup.material_handling.IPathDescriptor<Agent>, HasBoundingRectangle, HasCenterPoint
```

Implementation of `IPath` for network in continuous space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Path)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Path()` |  |
| `Path(Agent owner)` |  |
| `Path(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean bidirectional, boolean isLimitSpeed, double maxSpeedInMPS, boolean limitNumberOfTransporters, int maxNumberOfTransporters, PathDrawingType drawingType, Paint color, double lineWidth, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `Path(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean bidirectional, boolean isLimitSpeed, double maxSpeedInMPS, boolean limitNumberOfTransporters, int maxNumberOfTransporters, PathDrawingType drawingType, Paint color, double lineWidth, Node source, Node target, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `Path(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean bidirectional, boolean isLimitSpeed, double maxSpeedInMPS, boolean limitNumberOfTransporters, int maxNumberOfTransporters, PathDrawingType drawingType, Paint color, double lineWidth, Node source, Node target, com.anylogic.engine.markup.material_handling.IPathDescriptor descriptor, MarkupSegment... segments)` |  |
| `Path(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean bidirectional, PathDrawingType drawingType, Paint color, double lineWidth, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegment segment)` | Adds segment to this markup element |
| `void` | `arcTo(double x, double y, double z, double startAngle, double endAngle, double ratioStartToEnd)` | Adds arc segment with two circular arcs (available for markup elements created with no-argument constructor) |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(double px, double py, double distance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `default NetworkPort` | `createPort(IPath<?> path, PathEndType endType)` |  |
| `default NetworkPort` | `createPort(IPath<?> path, PathEndType endType, NetworkPort pairedPort)` |  |
| `NetworkPort` | `createPort(PathEndType endType)` | Creates and returns a Network Port located on specified path's end |
| `NetworkPort` | `createPort(PathEndType endType, NetworkPort pairedPort)` | Creates and returns a Network Port located on specified path's end and pairs created port with specified one |
| `NetworkPort` | `createPortInternal(PathEndType endType)` |  |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Position` | `getCenter(Position out)` |  |
| `PathDrawingType` | `getDrawingType()` | Returns the drawing type of this path |
| `Point` | `getEndPoint()` | Returns the location of the end point |
| `Point` | `getEndPoint(Point out)` | Returns the location of the end point |
| `Position` | `getEndPosition()` | Returns the end position |
| `Position` | `getEndPosition(Position out)` | Returns the end position |
| `Color` | `getLineColor()` | Returns the color of the path, or `null` if path has no color or has texture (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `Texture` | `getLineTexture()` | Returns the texture of the path, if the path has it |
| `double` | `getLineWidth()` | Returns the width of the path. |
| `double` | `getLineWidth(LengthUnits units)` | Returns line width |
| `com.anylogic.engine.markup.material_handling.IPathDescriptor<Agent>` | `getMaterialLibraryDescriptor()` |  |
| `int` | `getMaxNumberOfTransporters()` | Returns the maximum allowed number of transporters on this path |
| `double` | `getMaxSpeed(SpeedUnits units)` | Returns max allowed speed on this path in specified speed units |
| `double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPointOnRay(double x1, double y1, double x2, double y2, LengthUnits units, Point out)` | Calculates the intersection point between this element and the given ray. |
| `double` | `getNearestPointOnRay(double x1, double y1, double x2, double y2, Point out)` | Calculates the intersection point between this element and the given ray. |
| `int` | `getNumberOfTransporters()` | Returns the number of transporters currently located on this path |
| `Node` | `getOtherNode(Node n)` | If the given node is source of this path, returns path's target, otherwise returns source. |
| `final Point` | `getPointAtOffset(double offset, LengthUnits units, Point out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)).  This method may be slightly faster in some cases but returns no orientation information (rotations). |
| `final Point` | `getPointAtOffset(double offset, Point out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)).  This method may be slightly faster in some cases but returns no orientation information (rotations). |
| `Position` | `getPosition(double value, double maxValue, Position out)` | Returns position with offset corresponding to the given `value`, assuming that `0` is start and `maxValue` is end |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `final Position` | `getPositionAtOffset(double offset, LengthUnits units, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](IPath.md#getStartPoint(com.anylogic.engine.Point)). |
| `final Position` | `getPositionAtOffset(double offset, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](IPath.md#getStartPoint(com.anylogic.engine.Point)). |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `Node` | `getSource()` | Returns source node of this path. |
| `Point` | `getStartPoint()` | Returns the location of the start point |
| `Point` | `getStartPoint(Point out)` | Returns the location of the start point |
| `Position` | `getStartPosition()` | Returns the start position |
| `Position` | `getStartPosition(Position out)` | Returns the start position |
| `Node` | `getTarget()` | Returns target node of this path. |
| `Agent` | `getTransporter(int index)` | Returns the transporter with the specified index |
| `List<Agent>` | `getTransporters()` | Returns the list of all transporters currently located on this path |
| `boolean` | `isBidirectional()` | Returns the 'bidirectional' property (`true` by default). |
| `boolean` | `isLimitNumberOfTransporters()` | Returns true if the number of transporters is limited on this path, false otherwise |
| `boolean` | `isLimitSpeed()` | Returns true if speed is limited on this path, false otherwise |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of the markup element, calculated in 3D space. |
| `final double` | `length(LengthUnits units)` | Returns the length of the markup element, calculated in 3D space. |
| `void` | `lineTo(double x, double y, double z)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `final Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `final Position` | `randomPositionInside(Random rng, Position out)` | Returns the randomly chosen position along the path. |
| `void` | `setBidirectional(boolean bidirectional)` | Sets the 'bidirectional' property (`true` by default). |
| `void` | `setDrawingType(PathDrawingType drawingType)` | Sets the drawing type of this path |
| `void` | `setLimitNumberOfTransporters(boolean limitNumberOfTransporters)` | Enables limiting the number of transporters on this path if the argument is true, disables it otherwise |
| `void` | `setLimitSpeed(boolean limitSpeed)` | Enables speed limit on this path if the argument is true, disables it if the argument is false The element should be uninitialized |
| `void` | `setLineColor(Color color)` | Sets the color of the path. |
| `void` | `setLineColor(Paint color)` | Sets the color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the path. |
| `void` | `setLineWidth(double widthInPixels)` | Sets the width of the path, 0 means thinnest possible |
| `void` | `setLineWidth(double lineWidth, LengthUnits units)` | Sets line width |
| `void` | `setMaxNumberOfTransporters(int maxNumberOfTransporters)` | Sets the maximum allowed number of transporters on this path |
| `void` | `setMaxSpeed(double maxSpeed, SpeedUnits units)` | Sets the maximum allowed speed in specified units |
| `void` | `setSource(Node node)` | Sets source node of this path. |
| `void` | `setTarget(Node node)` | Sets source node of this path. |
| `void` | `startDrawing(double x, double y, double z)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `Path3D` | `toPath3D()` | Converts this markup element to [`Path3D`](../Path3D.md "interface in com.anylogic.engine") interface |
