*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/OverheadCraneBridge.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class OverheadCraneBridge

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Crane](Crane.md "class in com.anylogic.engine.markup")<[Agent](../Agent.md "class in com.anylogic.engine")>

com.anylogic.engine.markup.OverheadCraneBridge

All Implemented Interfaces:
:   `IMaintenanceable`, `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasLevel`, `IMaintenanceableMarkup`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class OverheadCraneBridge
extends Crane<Agent>
implements com.anylogic.engine.markup.material_handling.IMaterialFallible, IMaintenanceableMarkup, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.OverheadCraneBridge)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OverheadCraneBridge()` |  |
| `OverheadCraneBridge(double bridgeLocation, double trolleyLocation, Color bridgeColor)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `attachAgentAnimation(Agent agent)` | Attaches agent's position to the hook coordinates. |
| `double` | `averageCycleTime()` | Returns average agent operation time in model time units. |
| `double` | `averageCycleTime(TimeUnits units)` | Returns average agent operation time in specified time units. |
| `boolean` | `canArriveAt(Point hookDestination)` | Returns `true` if the hook can reach specified point. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `detachAgentAnimation()` | Detaches the agent that was previously attached to hook. |
| `void` | `fail()` | Sets the bridge to `failed` state |
| `Position` | `getAbsoluteHookPosition()` | Returns the current absolute hook position as an instance of `Position` in pixels. |
| `Agent` | `getAgent()` | Returns the agent that have seized the bridge. |
| `List<Agent>` | `getAgentsInQueue()` | Returns list of agents that represents bridge's own queue. |
| `Color` | `getBridgeColor()` | Returns the color of the bridge |
| `Position` | `getBridgePosition()` | Returns coordinates of bridge's center. |
| `List<OverheadCraneBridge>` | `getBridgesOnRouteTo(Point absolutePoint)` | Returns list of bridges that are currently located between the bridge and destination point. |
| `OverheadCrane` | `getCrane()` | Returns the crane the bridge belongs to. |
| `double` | `getCraneHeight()` |  |
| `double` | `getCraneHeight(LengthUnits units)` |  |
| `double` | `getCurrentBridgeOffset(LengthUnits units)` | Returns current bridge offset in specified units (from left to right for crane with zero rotation). |
| `double` | `getCurrentBridgeSpeed(SpeedUnits units)` | Returns current bridge speed in specified units. |
| `double` | `getCurrentHoistSpeed(SpeedUnits units)` | Returns current hoist speed in specified units. |
| `double` | `getCurrentHookOffset(LengthUnits units)` | Returns current hook height in specified units. |
| `double` | `getCurrentTrolleyOffset(LengthUnits units)` | Returns current trolley offset in specified units (from top to bottom for crane with zero rotation). |
| `double` | `getCurrentTrolleySpeed(SpeedUnits units)` | Returns current trolley speed in specified units. |
| `BridgeDirection` | `getDirection()` | Returns current direction of the bridge. |
| `double` | `getDistanceTo(Point absolutePoint, LengthUnits units)` | Returns bridge's distance to specified point. |
| `double` | `getDistanceToTarget(LengthUnits units)` | Returns bridge's distance to current target. |
| `IDowntime<?>[]` | `getDowntimeBlocks()` |  |
| `Position` | `getHookPosition()` | Returns hook's coordinates. |
| `int` | `getIndex()` | Returns bridge index. |
| `double` | `getInitialBridgeOffset(LengthUnits units)` | Returns the initial offset of the bridge in the specified length units. |
| `double` | `getInitialHookOffset(LengthUnits units)` | Returns the initial offset of the bridge's hook in the specified length units. |
| `Point` | `getInitialHookPoint()` | Returns the initial hook point in **pixels**, calculated according to the crane's dimensions and converted to pixels with crane's space. |
| `Point` | `getInitialHookPoint(LengthUnits units)` | Returns the initial hook point in the specified length units. |
| `Point` | `getInitialHookPoint(Function<Double,Double> meterToPx)` |  |
| `double` | `getInitialTrolleyOffset(LengthUnits units)` | Returns the initial offset of the bridge's trolley in the specified length units. |
| `Object` | `getPMLProxy()` |  |
| `double` | `getPriority()` | Returns current bridge's movement priority. |
| `CraneProgram` | `getProgram()` | Returns clone of current bridge program. |
| `double` | `getRotation()` |  |
| `OverheadCraneBridgeState` | `getState()` | Returns the bridge's current state. |
| `double` | `getStatisticsStartTime()` |  |
| `Point` | `getTargetPoint()` | Returns bridge's target point. |
| `Position` | `getTrolleyPosition()` | Returns coordinates of trolley's center. |
| `double` | `getUtilization()` | Returns the bridge utilization: the fraction of time the crane was operating. |
| `double` | `getX()` | Returns the X coordinate of this crane |
| `Point` | `getXYZ()` | Returns the point location of this element |
| `double` | `getY()` | Returns the Y coordinate of this crane |
| `double` | `getZ()` | Returns Z-coordinate of this crane relative to crane's level |
| `boolean` | `isFailed()` | Returns `true` if the bridge is failed and `false` otherwise. |
| `boolean` | `isMaintenanceActive(IDowntime<?> block)` |  |
| `boolean` | `isReady()` | Returns `true` if bridge is ready to operate, i.e. |
| `void` | `moveByProgram(CraneProgram program)` | Orders the bridge to move by program. |
| `void` | `moveTo(Point absolutePoint, double safeHeight, boolean remainsAtTarget)` | Orders the bridge to move to specified point. |
| `double` | `mtbf()` | Returns mean time between failures in model time units. |
| `double` | `mtbf(IDowntime<?> downtime)` | Returns mean time between failures for specified Downtime block (in model time units). |
| `double` | `mtbf(IDowntime<?> downtime, TimeUnits units)` | Returns mean time between failures for specified Downtime block (in specified time units). |
| `double` | `mtbf(TimeUnits units)` | Returns mean time between failures in specified time units. |
| `double` | `mttr()` | Returns mean time to repair in model time units. |
| `double` | `mttr(IDowntime<?> downtime)` | Returns mean time to repair for specified Downtime block (in model time units). |
| `double` | `mttr(IDowntime<?> downtime, TimeUnits units)` | Returns mean time to repair for specified Downtime block (in specified time units). |
| `double` | `mttr(TimeUnits units)` | Returns mean time to repair in specified time units. |
| `int` | `numberOfAgentsHandled()` | Returns total number of agents that have been handled by the bridge. |
| `int` | `numberOfConflicts()` |  |
| `void` | `onLoading(Agent agent)` |  |
| `void` | `onUnloading(Agent agent)` |  |
| `void` | `repair()` | Repairs the bridge from `failed` state |
| `void` | `resetStats()` | Resets the crane utilization statistics. |
| `void` | `restartMaintenanceTriggers(IDowntime<?> block)` |  |
| `void` | `setBridgeColor(Color bridgeColor)` | Sets the specified color of the bridge |
| `void` | `setInitialBridgeOffset(double bridgeOffset, LengthUnits units)` | Sets the initial bridge position in the specified length units. |
| `void` | `setInitialHookOffset(double hookOffset, LengthUnits units)` | Sets the initial hook height in the specified length units. |
| `void` | `setInitialTrolleyOffset(double trolleyOffset, LengthUnits units)` | Sets the initial trolley position in the specified length units. |
| `void` | `setX(double x)` | Sets the X coordinate of this crane |
| `void` | `setXYZ(Point point)` | Places the crane into the argument point location |
| `void` | `setY(double y)` | Sets the Y coordinate of this crane |
| `void` | `setZ(double z)` | Sets the Z coordinate of this crane |
| `void` | `startMaintenanceManually(IDowntime<?> block)` |  |
| `void` | `stopMaintenanceManually(IDowntime<?> block)` |  |
| `double` | `timeInState(OverheadCraneBridgeState state)` | Returns total time in model time units spent by the bridge in the given state. |
| `double` | `timeInState(OverheadCraneBridgeState state, TimeUnits units)` | Returns total time in specified time units spent by the bridge in the given state. |
| `double` | `totalDistanceInConflict()` | Returns total distance in meters traveled by the bridge in any state while giving way to another bridge. |
| `double` | `totalDistanceInConflict(LengthUnits units)` | Returns total distance in specified length units traveled by the bridge in any state while giving way to another bridge. |
| `double` | `totalTimeInConflicts()` | Returns total time in model time units spent by the bridge giving way to other bridges or not moving to avoid collisions. |
| `double` | `totalTimeInConflicts(TimeUnits units)` | Returns total time in specified time units spent by the bridge giving way to other bridges or not moving to avoid collisions. |
| `double` | `totalTransportationDistance()` | Returns total distance in meters traveled by the bridge in MOVING\_LOADED state. |
| `double` | `totalTransportationDistance(LengthUnits units)` | Returns total distance in specified length units traveled by the bridge in MOVING\_LOADED state. |
| `double` | `totalTravelledDistance()` | Returns total distance in meters traveled by the bridge including movement in manual mode and situations where the bridge had to give way to another bridge. |
| `double` | `totalTravelledDistance(LengthUnits units)` | Returns total distance in specified length units traveled by the bridge including movement in manual mode and situations where the bridge had to give way to another bridge. |
| `double` | `totalTravellingTime()` | Returns total time in model time units that the bridge spent moving for any reason. |
| `double` | `totalTravellingTime(TimeUnits units)` | Returns total time in specified time units that the bridge spent moving for any reason. |
