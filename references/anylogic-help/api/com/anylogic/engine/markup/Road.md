*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Road.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Road

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadConnectableElement](AbstractRoadConnectableElement.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Road

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasCenterPoint`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Road
extends AbstractRoadConnectableElement
implements HasBoundingRectangle, HasCenterPoint
```

Class representing a road segment with several forward and backward lanes. Road segment should have at least 1 forward or backward lane.
Road segment can have a median strip of the specified width that separates forward and backward directions. Road segment has incoming and
outgoing connection points at ends. Each lane has 1 incoming connection point, 1 outgoing connection point and a guideline connecting them.
Lanes of each direction are numbered starting from 0 from outmost to inmost, so the lane closest to the central line has the greatest index.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Road)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final float[]` | `DOUBLE_DASH` |  |
| `static final float[]` | `SINGLE_DASH` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Road()` | Creates a new road segments. |
| `Road(Agent owner, ShapeDrawMode drawMode, boolean isPublic, int forwardLanesCount, int backwardLanesCount, double medianStripWidthInMeters, Paint medianStripColor, MarkupSegment... axisSegments)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addSegment(MarkupSegment segment)` | Adds segment to this markup element |
| `double` | `averageSpeed(boolean isOnForwardSide, double offset)` | Returns the average speed (in meters per second) on the given road direction near the specified offset |
| `double` | `averageSpeed(boolean isOnForwardSide, double offset, SpeedUnits units)` | Returns the average speed (in the given units) on the given road direction near the specified offset |
| `List<MarkupSegment>` | `getAxisMarkupSegments()` | Returns list of markup segments representing road axis (the middle of median strip).  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `RoadConnectionPoint` | `getBackwardIncomingConnectionPoint(int backwardLaneIndex)` | Returns incoming connection point located at the beginning of backward lane with the specified index. |
| `List<MarkupSegment>` | `getBackwardLaneMarkupSegments(int backwardLaneIndex)` | Returns list of markup segments representing guideline of backward lane with the specified lane index. |
| `int` | `getBackwardLanesCount()` | Returns count of backward lanes. |
| `RoadConnectionPoint` | `getBackwardOutgoingConnectionPoint(int backwardLaneIndex)` | Returns outgoing connection point located at the end of backward lane with the specified index. |
| `List<RoadConnectionPoint>` | `getBeginConnectionPoints()` | Returns list of all connection points located at the beginning of road segment. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `List<BusStop>` | `getBusStops()` | Returns all bus stops contained in this road |
| `List<Agent>` | `getCars(boolean isOnForwardSide)` | Returns ordered list of cars located on the given direction. |
| `final Position` | `getCenter(Position out)` |  |
| `List<RoadConnectionPoint>` | `getConnectionPoints()` | Returns a list of connection points of the road element. |
| `List<RoadConnectionPoint>` | `getEndConnectionPoints()` | Returns list of all connection points located at end of road segment. |
| `RoadConnectionPoint` | `getForwardIncomingConnectionPoint(int forwardLaneIndex)` | Returns incoming connection point located at the beginning of forward lane with the specified index. |
| `List<MarkupSegment>` | `getForwardLaneMarkupSegments(int forwardLaneIndex)` | Returns list of markup segments representing guideline of forward lane with the specified lane index. |
| `int` | `getForwardLanesCount()` | Returns count of forward lanes. |
| `RoadConnectionPoint` | `getForwardOutgoingConnectionPoint(int forwardLaneIndex)` | Returns outgoing connection point located at the end of forward lane with the specified index. |
| `List<RoadConnectionPoint>` | `getIncomingConnectionPoints(PathEndType type)` | Returns list of incoming connection points located at the beginning of road segment. |
| `int` | `getLaneIndex(RoadConnectionPoint connectionPoint)` | Returns zero-based index of lane to which the specified connection point belongs to. |
| `Color` | `getMedianStripColor()` | Returns the color of the median strip, or `null` if median strip has no fill or has texture (in this case [`getMedianStripTexture()`](#getMedianStripTexture()) should be used instead) |
| `Texture` | `getMedianStripTexture()` | Returns the texture of the median strip color, if the median strip has texture |
| `double` | `getMedianStripWidth()` | Returns median strip width, **in pixels**. |
| `double` | `getMedianStripWidth(LengthUnits units)` | Returns median strip width measured in the given units. |
| `List<RoadConnectionPoint>` | `getOutgoingConnectionPoints(PathEndType type)` | Returns list of outgoing connection points located at the beginning of road segment. |
| `List<ParkingLot>` | `getParkingLots()` | Returns all parking lots contained in this road |
| `MarkupSegment` | `getSegment(int index)` | Returns the segment by its index |
| `int` | `getSegmentCount()` | Returns the number of segments |
| `List<StopLine>` | `getStopLines()` | Returns all stop lines contained in this road |
| `double` | `getWidth()` | Returns the total width of road segment which consists of width of all forward lanes, width of all backward lanes and width of median strip. |
| `double` | `getWidth(LengthUnits units)` | Returns the total width of road segment which consists of width of all forward lanes, width of all backward lanes and width of median strip. |
| `boolean` | `isConnectionPointOnForwardDirection(RoadConnectionPoint connectionPoint)` | Checks if the specified road connection point is located on forward direction of the road segment. |
| `Iterator<MarkupSegment>` | `iterator()` | Creates and returns read-only iterator over segments |
| `int` | `nCars(boolean isOnForwardSide)` | Returns number of cars located on the given direction. |
| `int` | `nCarsOnLane(boolean isOnForwardSide, int laneIndex)` | Returns number of cars located on located in the specified lane. |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setBackwardLanesCount(int backwardLanesCount)` | Sets number of backward lanes |
| `void` | `setDataSource(RoadDataSource dataSource)` |  |
| `void` | `setForwardLanesCount(int forwardLanesCount)` | Sets number of forward lanes |
| `void` | `setMedianStripColor(Color color)` | Sets the color of the median strip color. |
| `void` | `setMedianStripColor(Paint color)` | Sets the color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the median strip color. |
| `void` | `setMedianStripWidth(double medianStripWidthInPixels)` | Deprecated. this method is deprecated and may be removed in the next release. |
| `void` | `setMedianStripWidth(double medianStripWidth, LengthUnits units)` | Sets median strip width measured in the given units |
