*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/BulkConveyorBelt.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class BulkConveyorBelt

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractFluidMarkup](AbstractFluidMarkup.md "class in com.anylogic.engine.markup")<[BulkConveyorDataSource](BulkConveyorDataSource.md "interface in com.anylogic.engine.markup")>

com.anylogic.engine.markup.BulkConveyorBelt

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasCenterPoint`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class BulkConveyorBelt
extends AbstractFluidMarkup<BulkConveyorDataSource>
implements HasCenterPoint
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.BulkConveyorBelt)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `BulkConveyorBelt()` |  |
| `BulkConveyorBelt(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double width, Paint color, boolean drawStands, double standsLevel, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `BulkConveyorBelt(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double width, Paint color, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegmentLine segment)` | Adds segment to this markup element |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(double px, double py, double distance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Position` | `getCenter(Position out)` |  |
| `Point` | `getEndPoint()` | Returns the location of the end point |
| `Point` | `getEndPoint(Point out)` | Returns the location of the end point |
| `Position` | `getEndPosition()` | Returns the end position |
| `Position` | `getEndPosition(Position out)` | Returns the end position |
| `double` | `getLineWidth()` | Returns the width of the conveyor belt |
| `final Point` | `getPointAtOffset(double offset, LengthUnits units, Point out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)).  This method may be slightly faster in some cases but returns no orientation information (rotations). |
| `final Point` | `getPointAtOffset(double offset, Point out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)).  This method may be slightly faster in some cases but returns no orientation information (rotations). |
| `final Position` | `getPositionAtOffset(double offset, LengthUnits units, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)). |
| `final Position` | `getPositionAtOffset(double offset, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)). |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `double` | `getStandsLevel()` | Returns the base level Z-level to draw conveyor stands from. |
| `Point` | `getStartPoint()` | Returns the location of the start point |
| `Point` | `getStartPoint(Point out)` | Returns the location of the start point |
| `Position` | `getStartPosition()` | Returns the start position |
| `Position` | `getStartPosition(Position out)` | Returns the start position |
| `boolean` | `isDrawStands()` | Returns `true` if this conveyor is drawn with stands |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of the markup element, calculated in 3D space. |
| `final double` | `length(LengthUnits units)` | Returns the length of the markup element, calculated in 3D space. |
| `void` | `setDrawStands(boolean drawStands)` | Sets to draw stands for conveyor or not |
| `void` | `setLineWidth(double width)` | Sets the width of the conveyor belt |
| `void` | `setStandsLevel(double standsLevel)` | Set the base Z-level to draw conveyor stands from. |
| `void` | `startDrawing(double x, double y, double z)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
