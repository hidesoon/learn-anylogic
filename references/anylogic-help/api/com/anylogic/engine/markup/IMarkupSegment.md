*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/IMarkupSegment.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Interface IMarkupSegment

All Known Implementing Classes:
:   `AbstractMarkupSegment`, `GISMarkupSegment`, `GISMarkupSegmentLine`, `MarkupSegment`, `MarkupSegmentArc`, `MarkupSegmentLine`

---

```
public interface IMarkupSegment
```

This interface represents a segment of `IPath`.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addTo(Path2D path)` | Deprecated. |
| `double` | `getDistanceSq(double x, double y)` | For horizontal segments, calculates and returns *the square of distance* to the point (in the XY-projection). |
| `double` | `getDistanceSq(Point givenPoint)` | Calculates and returns *the square of distance* to the given point. |
| `Point` | `getEnd(Point out)` | Gets end point of markup segment. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | For horizontal segments, calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPointOnRay2D(double x1, double y1, double x2, double y2, Point out)` | Calculates (and sets in the 'out' object) the point where this segment intersects the given ray with the minimum distance from ray beginning (if there are several intersection points like in arc segments). |
| `double` | `getOffsetOfPoint(double x, double y)` | Calculates distance by segment to the given point. |
| `Point` | `getStart(Point out)` | Gets start point of markup segment. |
| `double` | `length()` | Returns the length of the path segment |
| `void` | `setEnd(Point endPoint)` | Sets end point of this segment. |
| `void` | `setStart(Point startPoint)` | Sets start point of this segment. |
| `void` | `setStartNextTo(IMarkupSegment previousSegment)` | Sets coordinates of the end of the specified segment as start coordinates of this segment. |
