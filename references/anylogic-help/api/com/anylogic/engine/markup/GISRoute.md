*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/GISRoute.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class GISRoute

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.GISMarkupElement](GISMarkupElement.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.GISRoute

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `AnimationMovingLocationProvider`, `AnimationStaticLocationProvider`, `INetworkMarkupElement`, `IPath<GISNode>`, `SVGElement`, `UsdElement`, `Serializable`, `Iterable<GISMarkupSegment>`

---

```
public class GISRoute
extends GISMarkupElement
implements IPath<GISNode>, Iterable<GISMarkupSegment>
```

Implementation of `IPath` for network in GIS space.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.GISRoute)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `GISRoute(ShapeGISMap owner, boolean bidirectional, GISMarkupSegment... segments)` | Creates GIS route based on the array of segments. |
| `GISRoute(ShapeGISMap owner, boolean isPermanent, Paint lineColor, double lineWidth, LineStyle lineStyle, boolean bidirectional, GISNode source, GISNode target, GISMarkupSegmentDescriptor... segmentDescriptors)` | Creates GIS route based on the array of segments with specific drawing attributes. |
| `GISRoute(ShapeGISMap owner, boolean isPermanent, Paint lineColor, double lineWidth, LineStyle lineStyle, boolean bidirectional, GISNode source, GISNode target, GISMarkupSegment... segments)` | Creates GIS route based on the array of segments with specific drawing attributes. |
| `GISRoute(ShapeGISMap map, Curve<? extends GISMarkupSegment> curve)` | Creates unidirectional GIS route based on curve. |
| `GISRoute(ShapeGISMap map, Curve<? extends GISMarkupSegment> curve, boolean bidirectional)` | Creates GIS route based on curve. |
| `GISRoute(ShapeGISMap map, Curve<? extends GISMarkupSegment> curve, GISPoint source, GISPoint target, boolean bidirectional)` | Creates GIS route for network. |
| `GISRoute(ShapeGISMap owner, GISMarkupSegment... segments)` | Creates unidirectional GIS route based on the array of segments. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(GISMarkupSegment segment)` | Adds segment to this markup element |
| `boolean` | `contains(double lat, double lon)` | Check this element contains a point with given coordinates. |
| `boolean` | `contains(double lat, double lon, double distance)` | Test if GIS Route contains the point with the given coordinates, using the given tolerance |
| `boolean` | `containsSq(double lat, double lon, double squareDistance)` | Test if GIS Route contains the point with the given coordinates, using the given tolerance |
| `Point` | `getEndPoint()` | Returns the location of the end point |
| `Point` | `getEndPoint(Point out)` | Returns the location of the end point |
| `Position` | `getEndPosition(Position position)` | Returns the end position |
| `double` | `getNearestPoint(double lat, double lon, Point out)` | Calculates (using the `out` object) the point in GIS Route element nearest to the given point. |
| `double` | `getNearestPoint(Point givenPoint, Point out)` | Calculates (using the `output` object) the point in this space markup element nearest to the given point. |
| `GISNode` | `getOtherNode(GISNode n)` | If the given node is source of this path, returns path's target, otherwise returns source. |
| `Position` | `getPosition(double value, double maxValue, Position out)` | Returns position with offset corresponding to the given `value`, assuming that `0` is start and `maxValue` is end |
| `Position` | `getPosition(int index, int totalNumber, Position out)` | Returns the item position with the given index.  In case of any wrong argument returns zero-index position (position for index=0 with totalNumber=1). |
| `Position` | `getPositionAtOffset(double offset, LengthUnits units, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](IPath.md#getStartPoint(com.anylogic.engine.Point)). |
| `Position` | `getPositionAtOffset(double offset, Position out)` | Returns the point (+rotations) located on the markup element with the given `offset` distance calculated from [start point](IPath.md#getStartPoint(com.anylogic.engine.Point)). |
| `Presentable` | `getPresentable()` |  |
| `GISMarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `GISNode` | `getSource()` | Returns source node of this path. |
| `Point` | `getStartPoint()` | Returns the location of the start point |
| `Point` | `getStartPoint(Point out)` | Returns the location of the start point |
| `Position` | `getStartPosition(Position position)` | Returns the start position |
| `GISNode` | `getTarget()` | Returns target node of this path. |
| `boolean` | `isBidirectional()` | Returns the 'bidirectional' property (`true` by default). |
| `Iterator<GISMarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `final double` | `length()` | Returns the length of markup element, used e.g. |
| `final double` | `length(LengthUnits units)` | Returns the length of markup element, used e.g. |
| `final Point` | `randomPointInside(Random rng, Point out)` | Returns the randomly chosen point inside/along the given space markup element. |
| `void` | `setBidirectional(boolean bidirectional)` | Sets the 'bidirectional' property (`true` by default). |
| `void` | `setSource(GISNode node)` | Sets source node of this path. |
| `void` | `setTarget(GISNode node)` | Sets source node of this path. |
