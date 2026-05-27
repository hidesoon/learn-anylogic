*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Intersection.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Intersection

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadConnectableElement](AbstractRoadConnectableElement.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Intersection

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Intersection
extends AbstractRoadConnectableElement
implements HasBoundingRectangle
```

Class representing area of intersection of several (2 or more) road segments. Contains 1 or more incoming road connection points,
1 or more outgoing connection points and guidelines connecting pairs of incoming and outgoing connection points.
Each pair of incoming and outgoing connection points
cannot have more than 1 guideline. Provides functionality for automatic generation of intersection area border.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Intersection)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Intersection()` | Creates a new instance of road intersection. |
| `Intersection(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean showLaneConnectors, PathEnd<Road>[] roadEnds, RoadLanesConnector... lanes)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `Intersection(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean showLaneConnectors, Road road1, PathEndType type1, Road road2, PathEndType type2, RoadLanesConnector... connectors)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection(Road startRoad, int startRoadLane, Road endRoad, int endRoadLane)` | Adds roads connection |
| `void` | `addConnection(Road startRoad, int startRoadLane, Road endRoad, int endRoadLane, MarkupSegment... guideLine)` | Adds roads connection |
| `void` | `addConnection(Road startRoad, int startRoadLane, Road endRoad, int endRoadLane, List<MarkupSegment> guideLine)` | Adds roads connection |
| `void` | `addRoad(Road road, PathEndType type)` | Adds road to this intersection |
| `int` | `countCars(Road from, Road to)` | Returns the total number of cars that moved through the intersection from one specified road to another specified road. |
| `static List<MarkupSegment>` | `generateDefaultGuideline(RoadConnectionPoint inRoadConnectionPoint, RoadConnectionPoint outRoadConnectionPoint)` |  |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `List<Agent>` | `getCars()` | Returns unordered list of cars located on this intersection / connection |
| `RoadConnectionPoint` | `getConnectionPoint(boolean isIncoming, Road connectedWithRoadSegment, int roadSegmentLaneIndex)` | Returns connection point that is directed at the specified direction, connected with the specified road segment and corresponds to the specified lane index in this road segment. |
| `RoadConnectionPoint` | `getConnectionPoint(RoadConnectionPoint connectedPoint)` | Returns connection point that is connected to the specified point, or null if such connection point does not exist. |
| `List<RoadConnectionPoint>` | `getConnectionPoints()` | Returns a list of connection points of the road element. |
| `Map<Pair<RoadConnectionPoint,RoadConnectionPoint>,List<MarkupSegment>>` | `getGuidelines()` | Returns map from pairs (incoming and outgoing) of road connection points to guidelines connecting the specified incoming and outgoing connection points. |
| `List<RoadConnectionPoint>` | `getIncomingConnectionPoints()` | Returns list of all incoming connection points of the element. |
| `List<RoadLanesConnector>` | `getLanesConnectors()` | Returns the list of lane connectors inside this intersection |
| `List<RoadConnectionPoint>` | `getOutgoingConnectionPoints()` | Returns list of all outgoing connection points of the element. |
| `int` | `nCars()` | Returns number of cars located on this intersection / connection |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetStats()` | Resets counters of cars for all lane connectors on this intersection |
| `void` | `setDataSource(RoadBasicDataSource dataSource)` |  |
| `void` | `setGuideline(RoadConnectionPoint inRoadConnectionPoint, RoadConnectionPoint outRoadConnectionPoint)` | Sets a guideline between the specified connection points. |
| `void` | `setGuideline(RoadConnectionPoint inRoadConnectionPoint, RoadConnectionPoint outRoadConnectionPoint, List<MarkupSegment> guideline)` |  |
| `void` | `setRoads(Road road1, PathEndType type1, Road road2, PathEndType type2)` | Adds 2 roads to this markup element. |
| `void` | `showLaneConnectors(boolean showLaneConnectors)` | Shows or hides lane connectors |
| `int` | `traffic(Road from, Road to)` | Returns the traffic of car flow from one specified road to another specified road, measured in cars per hour. |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
