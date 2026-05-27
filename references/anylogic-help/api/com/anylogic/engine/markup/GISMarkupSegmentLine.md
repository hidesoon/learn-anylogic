*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISMarkupSegmentLine.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISMarkupSegmentLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkupSegment](AbstractMarkupSegment.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.GISMarkupSegment](GISMarkupSegment.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.GISMarkupSegmentLine

All Implemented Interfaces:
:   `IMarkupSegment`, `Serializable`

---

```
public class GISMarkupSegmentLine
extends GISMarkupSegment
```

Straight markup segment for GIS space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISMarkupSegmentLine)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISMarkupSegmentLine()` |  |
| `GISMarkupSegmentLine(double slat, double slon, double elat, double elon)` |  |
| `GISMarkupSegmentLine(double slat, double slon, double elat, double elon, boolean isGeodesic)` |  |
| `GISMarkupSegmentLine(double slat, double slon, double elat, double elon, double realLength)` |  |
| `GISMarkupSegmentLine(double slat, double slon, double elat, double elon, double realLength, boolean isGeodesic)` |  |
| `GISMarkupSegmentLine(GISMarkupSegment s, double realLength)` |  |
| `GISMarkupSegmentLine(GISMarkupSegment s, double realLength, boolean isGeodesic)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addTo(Path2D path)` | Adds this segment to the given path assuming that path is currently positioned on the start point of this segment |
| `double` | `getDistanceSq(double lat, double lon)` | Calculates and returns the square of distance to the given latitude and longitude |
| `double` | `getDistanceSq(Point givenPoint)` | Calculates and returns *the square of distance* to the given point. |
| `Point` | `getEnd(Point out)` | Gets end point of markup segment. |
| `Position` | `getEnd(Position out)` | Returns the location of the end position of the segment |
| `double` | `getNearestPoint(double lat, double lon, Point out)` | Calculates (using the `out` object) the point in this space markup element nearest to the given (lat, lon) point. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | For horizontal segments, calculates (using the `output` object) the point in this space markup element nearest to the given (x, y) point. |
| `double` | `getNearestPointOnRay2D(double lat1, double lon1, double lat2, double lon2, Point out)` | Calculates (and sets in the 'out' object) the point where this segment intersects the given ray with the minimum distance from ray beginning (if there are several intersection points like in arc segments). |
| `double` | `getOffsetOfPoint(double lat, double lon)` | Calculates distance by segment to the given point. |
| `Point` | `getStart(Point out)` | Gets start point of markup segment. |
| `Position` | `getStart(Position out)` | Returns the location of the start position of the segment |
| `void` | `initialize()` |  |
| `void` | `setStart(Point startPoint)` | Sets start point of this segment. |
