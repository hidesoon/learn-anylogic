*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RailwayTrack.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RailwayTrack

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRailwayMarkup](AbstractRailwayMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.RailwayTrack

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasCenterPoint`, `HasLevel`, `RailMarkup`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<MarkupSegment>`

---

```
public class RailwayTrack
extends AbstractRailwayMarkup
implements Iterable<MarkupSegment>, HasBoundingRectangle, HasCenterPoint
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RailwayTrack)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RailwayTrack()` |  |
| `RailwayTrack(Agent owner, ShapeDrawMode drawMode, boolean isPublic, PathDrawingType drawingType, Paint color, double width, MarkupSegment... segments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegment segment)` | Adds segment to this markup element |
| `void` | `addToReservations(Agent... trains)` | Reserve the track for certain trains |
| `void` | `arcTo(double x, double y, double z, double startAngle, double endAngle, double ratioStartToEnd)` | Adds arc segment with two circular arcs (available for markup elements created with no-argument constructor) |
| `void` | `block()` | Block the track. |
| `void` | `cancelReservation()` | Cancel existing reservations for the track. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(double px, double py, double distance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Agent` | `getCar(int index)` | Returns a car on the track at a given position counted from the beginning of the track. |
| `List<Agent>` | `getCars()` | Returns the list of rail cars that are (maybe, partially) located of this track |
| `Position` | `getCenter(Position out)` |  |
| `Color` | `getColor()` | Returns the color of the shape, or `null` if shape has no color or has textured (in this case `#getFillTexture()` should be used instead) |
| `TrackDataSource` | `getDataSource()` |  |
| `PathDrawingType` | `getDrawingType()` | Returns the drawing type of this path |
| `RailwaySwitch` | `getEndSwitch()` | Get the switch at the end of the track |
| `Agent` | `getFirstCar()` | Returns the car closest to the beginning of the track, or null if the track is empty |
| `double` | `getFreeSpace(boolean fromstart)` | Tests the availability of space on the track. |
| `Agent` | `getLastCar()` | Returns the car closest to the end of the track, or null if the track is empty |
| `int` | `getNCars()` | Deprecated. use [`nCars()`](#nCars()) |
| `double` | `getNearestPoint(double x, double y, double z, LengthUnits units, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, double z, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y, z) point. |
| `double` | `getNearestPoint(double x, double y, LengthUnits units, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPoint(double x, double y, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPointOnRay(double x1, double y1, double x2, double y2, LengthUnits units, Point out)` | Calculates the intersection point between this element and the given ray. |
| `double` | `getNearestPointOnRay(double x1, double y1, double x2, double y2, Point out)` | Calculates the intersection point between this element and the given ray. |
| `RailwaySwitch` | `getOtherSwitch(RailwaySwitch sw)` | If the given switch is 'start switch' of this track, returns track's 'end switch', otherwise returns 'source switch'. |
| `Position` | `getPositionAtOffset(double offset, Position position)` | Returns the point located on the markup element with the given `offset` distance calculated from start point. |
| `List<PositionOnTrack>` | `getPositionsOnTrack()` | Returns a list of all PositionOnTrack elements on this track |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `RailwaySwitch` | `getStartSwitch()` | Get the switch at the start of the track |
| `RailwaySwitch` | `getSwitch(boolean atend)` | Returns the switch at the beginning or at the end of the track. |
| `Texture` | `getTexture()` | Returns the texture of the shape, if the shape has texture |
| `List<Agent>` | `getTrains()` | Get the list of trains that are currently (including partially) on the track |
| `double` | `getWidth()` | Returns the width of the track. |
| `double` | `getWidth(LengthUnits units)` | Returns the width of the track. |
| `boolean` | `isAvailableFor(Agent train)` | Check if the specified train can move through the track |
| `boolean` | `isBlocked()` | Check if the track is blocked |
| `boolean` | `isEmpty()` | Tests if the track is empty, i.e. |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of the markup element, calculated in 3D space. |
| `final double` | `length(LengthUnits units)` | Returns the length of the markup element, calculated in 3D space. |
| `void` | `lineTo(double x, double y, double z)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `int` | `nCars()` | Returns the number of cars on the track (including partially) |
| `void` | `removeFromReservations(Agent... trains)` | Cancel existing reservations for specified trains |
| `List<Agent>` | `reservations()` | Return all the trains that this track has been reserved for |
| `void` | `reserveFor(Agent... trains)` | Reserve the track for certain trains |
| `void` | `setBlocked(boolean blocked)` | Set track's block status |
| `void` | `setColor(Color color)` | Sets the color of the shape. |
| `void` | `setColor(Paint color)` | Sets the color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setDrawingType(PathDrawingType drawingType)` | Sets the drawing type of this path |
| `void` | `setWidth(double width)` | Deprecated. this method is deprecated and may be removed in the next release. |
| `void` | `setWidth(double width, LengthUnits units)` | Sets the width of the track, 0 means thinnest possible |
| `void` | `startDrawing(double x, double y, double z)` | Starts drawing (available for markup elements created with no-argument constructor) |
| `Path3D` | `toPath3D()` | Converts this markup element to [`Path3D`](../Path3D.md "interface in com.anylogic.engine") interface |
| `void` | `unblock()` | Unblock the track and allow trains to move through it |
