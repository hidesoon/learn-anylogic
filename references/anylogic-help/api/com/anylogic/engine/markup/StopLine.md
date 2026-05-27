*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/StopLine.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class StopLine<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadMarkup](AbstractRoadMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadPart](AbstractRoadPart.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractRoadSidePart](AbstractRoadSidePart.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.StopLine<T>

All Implemented Interfaces:
:   `AggregatableAnimationElement`, `IDescriptor`, `HasBoundingRectangle`, `HasLevel`, `IMarkupLibraryDescriptor`, `ISignalable`, `IStopLineDescriptor<T>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class StopLine<T extends Agent>
extends AbstractRoadSidePart
implements ISignalable, IStopLineDescriptor<T>, HasBoundingRectangle
```

Markup element that marks a position on one or several lanes on a road. This element is determined by segment that
crosses one or several guidelines within other markup elements.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.StopLine)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `StopLine()` | Creates a new position on road. |
| `StopLine(Road road, IStopLineDescriptor<T> d, ShapeDrawMode drawMode, boolean isPublic, boolean isOnForwardSide, double offset, int laneIndexFrom, int laneIndexTo, RoadSignType... roadSigns)` |  |
| `StopLine(Road road, ShapeDrawMode drawMode, boolean isPublic, boolean isOnForwardSide, double offset, int laneIndexFrom, int laneIndexTo, RoadSignType... roadSigns)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addEndOfSpeedLimitSign()` | Adds "end of speed limit" sign to this stop line |
| `void` | `addSpeedLimitSign(double speedLimit, SpeedUnits units)` | Adds "speed limit" sign to this stop line |
| `void` | `addYieldSign()` | Adds "yield" sign to this stop line |
| `double` | `averageSpeed()` | Returns the actual average speed near this stop line |
| `double` | `averageSpeed(SpeedUnits units)` | Returns the actual average speed near this stop line |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `int` | `getLaneIndexFrom()` | Returns the starting lane covered by stop line, inclusive |
| `int` | `getLaneIndexTo()` | Returns the ending lane covered by stop line, inclusive |
| `double` | `getLength()` |  |
| `TrafficLightSignal` | `getSignal()` | Returns current signal of stop line |
| `double` | `getSpeedLimit(SpeedUnits units)` | If this stop line has "speed limit" sign, returns the actual speed limit value, measured in the given units |
| `boolean` | `isEndOfSpeedLimitSign()` | Returns `true` if this stop line has "end of speed limit" sign |
| `boolean` | `isSpeedLimitSign()` | Returns `true` if this stop line has "speed limit" sign |
| `boolean` | `isYieldSign()` | Returns `true` if this stop line has "yield" sign |
| `void` | `onCarPassed(T car, int laneIndex)` | Callback for "On car passed" action, executed for each car passing through this stop line |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `int` | `queueSize()` | Returns size of queue before the stop line as sum of each lane's queue. |
| `int` | `queueSize(int laneIndex)` | Returns size of queue before the stop line on specified lane If lane index is invalid, an error will occur. |
| `void` | `registerListener(SignalChangeListener stateChangeListener)` | Allows to register a CarSettings instance as a listener of signal change events |
| `void` | `setLaneIndexFrom(int laneIndexFrom)` | Sets the starting lane covered by stop line, inclusive |
| `void` | `setLaneIndexTo(int laneIndexTo)` | Sets the ending lane covered by stop line, inclusive |
| `void` | `setSignal(TrafficLightSignal signal)` | Changes the current signal. |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
