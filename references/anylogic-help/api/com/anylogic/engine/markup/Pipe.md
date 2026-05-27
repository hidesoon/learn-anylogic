*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Pipe.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Pipe

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractFluidMarkup](AbstractFluidMarkup.md "class in com.anylogic.engine.markup")<[PipeDataSource](PipeDataSource.md "interface in com.anylogic.engine.markup")>

com.anylogic.engine.markup.Pipe

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasCenterPoint`, `HasLevel`, `LevelElement`, `LevelMarkup`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Pipe
extends AbstractFluidMarkup<PipeDataSource>
implements HasCenterPoint
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Pipe)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Pipe()` |  |
| `Pipe(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double diameter, Paint color, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegmentLine segment)` | Adds a segment to this element |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(double px, double py, double distance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `Position` | `getCenter(Position out)` |  |
| `double` | `getDiameter()` | Returns the diameter of the pipe |
| `Point` | `getEndPoint()` | Returns the Point object with coordinates of the pipe's ending point. |
| `Point` | `getEndPoint(Point out)` | Returns the Point object with coordinates of the pipe's ending point. |
| `Position` | `getEndPosition()` | Returns the end position |
| `Position` | `getEndPosition(Position out)` |  |
| `final Point` | `getPointAtOffset(double offset, LengthUnits units, Point out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)).  This method may be slightly faster in some cases but returns no orientation information (rotations). |
| `final Point` | `getPointAtOffset(double offset, Point out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)).  This method may be slightly faster in some cases but returns no orientation information (rotations). |
| `final Position` | `getPositionAtOffset(double offset, LengthUnits units, Position out)` | Returns the Position object with coordinates and orientation of the point that is located at the given offset distance (in pixels) from the pipe's starting point. |
| `final Position` | `getPositionAtOffset(double offset, Position out)` | Returns the Position object with coordinates and orientation of the point that is located at the given offset distance (in pixels) from the pipe's starting point. |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by the provided index |
| `int` | `getSegmentCount()` | Returns the number of the pipe's segments. |
| `Point` | `getStartPoint()` | Returns the Point object with coordinates of the pipe's starting point. |
| `Point` | `getStartPoint(Point out)` | Returns the Point object with coordinates of the pipe's starting point. |
| `Position` | `getStartPosition()` | Returns the start position |
| `Position` | `getStartPosition(Position out)` | Returns the Position object with coordinates and orientation of the pipe's starting point. |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of the markup element, calculated in 3D space. |
| `final double` | `length(LengthUnits units)` | Returns the length of the markup element, calculated in 3D space. |
| `void` | `setDiameter(double diameter)` | Sets the diameter of the pipe |
| `void` | `startDrawing(double x, double y, double z)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
