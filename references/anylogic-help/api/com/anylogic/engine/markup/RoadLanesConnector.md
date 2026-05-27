*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/RoadLanesConnector.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class RoadLanesConnector

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.markup.RoadLanesConnector

All Implemented Interfaces:
:   `ISignalable`, `Serializable`

---

```
public class RoadLanesConnector
extends Object
implements Serializable, ISignalable
```

Road lanes connector inside an intersection. Connects one lane of road incoming to the intersection with one lane of
the outgoing road.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.RoadLanesConnector)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `RoadLanesConnector(Road startRoad, int startRoadLane, Road endRoad, int endRoadLane)` |  |
| `RoadLanesConnector(Road startRoad, int startRoadLane, Road endRoad, int endRoadLane, MarkupSegment... guideLine)` |  |
| `RoadLanesConnector(Road startRoad, int startRoadLane, Road endRoad, int endRoadLane, List<MarkupSegment> guideLine)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `int` | `countCars()` | Returns total number of cars passed through the connector |
| `Road` | `getEndRoad()` | Returns the road this connector ends at |
| `int` | `getEndRoadLane()` | Returns the lane number on the road this connector ends at |
| `List<MarkupSegment>` | `getGuideLine()` | Returns the guide line, in the form of segments list |
| `TrafficLightSignal` | `getSignal()` | Returns current signal of road lanes connector |
| `Road` | `getStartRoad()` | Returns the road this connector starts at |
| `int` | `getStartRoadLane()` | Returns the lane number on the road this connector starts at |
| `void` | `registerListener(SignalChangeListener stateChangeListener)` | Allows to register a CarSettings instance as a listener of signal change events |
| `void` | `resetStats()` | Resets total cars counter |
| `void` | `setDataSource(RoadLaneConnectorDataSource dataSource)` |  |
| `void` | `setSignal(TrafficLightSignal signal)` | Changes the current signal. |
| `String` | `toString()` |  |
| `int` | `traffic()` | Returns the traffic of car flow through the connector, measured in cars per hour. |
