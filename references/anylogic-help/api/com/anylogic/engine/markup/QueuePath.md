*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/QueuePath.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class QueuePath

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSubunit](AbstractMarkupSubunit.md "class in com.anylogic.engine.markup")<[ServiceWLine](ServiceWLine.md "class in com.anylogic.engine.markup")<?>>

com.anylogic.engine.markup.QueuePath

All Implemented Interfaces:
:   `HasBoundingRectangle`, `QueueUnit`, `Serializable`

Direct Known Subclasses:
:   `QueueSerpentine`

---

```
public class QueuePath
extends AbstractMarkupSubunit<ServiceWLine<?>>
implements QueueUnit, HasBoundingRectangle
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.QueuePath)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `QueuePath(int capacity, ExceededQueuePolicy exceededQueuePolicy, MarkupSegment... segments)` |  |
| `QueuePath(ExceededQueuePolicy exceededQueuePolicy, MarkupSegment... segments)` | Creates queue with unlimited capacity and the given policy for processing in case of full queue |
| `QueuePath(MarkupSegment... segments)` | Creates queue with unlimited capacity |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegment segment)` | Adds segment to this markup element |
| `void` | `arcTo(double x, double y, double startAngle, double endAngle, double ratioStartToEnd)` | Adds arc segment with two circular arcs (available for markup elements created with no-argument constructor) |
| `int` | `capacity()` | Returns the capacity of the queue |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `contains(double px, double py, double distance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `boolean` | `containsSq(double px, double py, double squareDistance)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Rectangle2D` | `getBounds()` | Deprecated. |
| `Point` | `getEndPoint()` | Returns the location of the end point |
| `Point` | `getEndPoint(Point out)` | Returns the location of the end point |
| `Position` | `getEndPosition()` | Returns the end position |
| `Position` | `getEndPosition(Position out)` | Returns the end position |
| `ExceededQueuePolicy` | `getExceededQueuePolicy()` | Returns the behavior policy to handle the case when queue capacity is exceeded |
| `double` | `getNearestPoint(double x, double y, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `List<Agent>` | `getPeds()` | Returns the list of peds currently staying in the queue |
| `final Position` | `getPositionAtOffset(double offset, Position out)` | Returns the point located on the markup element with the given `offset` distance calculated from [start point](#getStartPoint(com.anylogic.engine.Point)). |
| `final Position` | `getPositionAtOffsetFromEnd(double offset, Position out)` | Returns the point located on the markup element with the given `offset` distance calculated from [end point](#getEndPoint(com.anylogic.engine.Point)). |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `Point` | `getStartPoint()` | Returns the location of the start point |
| `Point` | `getStartPoint(Point out)` | Returns the location of the start point |
| `Position` | `getStartPosition()` | Returns the start position |
| `Position` | `getStartPosition(Position out)` | Returns the start position |
| `boolean` | `isCapacityLimited()` | Returns `true` if this queue has limited capacity |
| `boolean` | `isReverse()` | Returns true if the queue is reverse; returns false otherwise. |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of the markup element. |
| `void` | `lineTo(double x, double y)` | Adds line segment (available for markup elements created with no-argument constructor) |
| `void` | `setCapacity(int capacity)` | Sets the capacity of queue |
| `int` | `size()` | Returns the number of agents (pedestrians) staying in the queue |
| `void` | `startDrawing(double x, double y)` | Starts drawing (available for markup elements created with no-argument constructor) |
