*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/OverheadCrane.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class OverheadCrane<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Crane](Crane.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.OverheadCrane<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class OverheadCrane<T extends Agent>
extends Crane<T>
implements HasBoundingRectangle, com.anylogic.engine.markup.material_handling.IMaterialFallible, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.OverheadCrane)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OverheadCrane()` | Creates new OverheadCrane with 1 bridge. |
| `OverheadCrane(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, com.anylogic.engine.markup.material_handling.IOverheadCraneDescriptor<T> descriptor, double x, double y, double z, double rotation, double runwayLengthMeters, double craneWidthMeters, double craneHeightMeters, double bridgeWidthMeters, double safetyGap, Color color, Color trolleyColor, OverheadCraneDrawingType type, OverheadCraneGirderDrawingType girderType, OverheadCraneBridge... bridges)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addBridge(OverheadCraneBridge bridge)` | The method adds bridge to crane. |
| `void` | `attachAgentAnimation(OverheadCraneBridge bridge, T agent)` |  |
| `double` | `averageCycleTime(OverheadCraneBridge bridge, TimeUnits units)` |  |
| `double` | `bridgeAcceleration(T agent, boolean isLoaded, AccelerationUnits units)` | Returns the bridge acceleration specified by the parameter value of this crane in the specified `units`. |
| `double` | `bridgeDeceleration(T agent, boolean isLoaded, AccelerationUnits units)` | Returns the bridge deceleration specified by the parameter value of this crane in the specified `units`. |
| `double` | `bridgeSpeed(T agent, boolean isLoaded, SpeedUnits units)` | Deprecated. the method will be removed, use [`getMaximumBridgeSpeed(T agent, boolean isLoaded, SpeedUnits units)`](#getMaximumBridgeSpeed(T,boolean,com.anylogic.engine.SpeedUnits)) instead |
| `boolean` | `canArriveAt(OverheadCraneBridge bridge, Point hookDestination)` |  |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `detachAgentAnimation(OverheadCraneBridge bridge)` |  |
| `void` | `fail()` | Sets the crane to `failed` state |
| `void` | `fail(OverheadCraneBridge overheadCraneBridge)` |  |
| `SVGElement` | `findSVGElement(long svgId)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Position` | `getAbsoluteHookPosition()` | Returns the current absolute hook position as an instance of `Position` in pixels. |
| `Position` | `getAbsoluteHookPosition(OverheadCraneBridge overheadCraneBridge)` | Returns the current absolute hook position of the specified bridge as an instance of `Position` in pixels. |
| `Agent` | `getAgent(OverheadCraneBridge bridge)` |  |
| `List<Agent>` | `getAgents()` |  |
| `List<Agent>` | `getAgentsInQueue()` | Returns list of agents that represents crane's general queue. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `OverheadCraneBridge` | `getBridge(int index)` | Returns crane's bridge with specified index. |
| `double` | `getBridgeDistanceTo(OverheadCraneBridge bridge, Point p, LengthUnits units)` |  |
| `Position` | `getBridgePosition(OverheadCraneBridge bridge)` |  |
| `CraneProgram` | `getBridgeProgram(OverheadCraneBridge bridge)` |  |
| `List<OverheadCraneBridge>` | `getBridges()` | Returns unmodifiable list of crane's bridges. |
| `List<OverheadCraneBridge>` | `getBridgesOnRouteTo(OverheadCraneBridge bridge, Point p)` |  |
| `double` | `getBridgeWidth()` | Returns width of the bridge in pixels |
| `double` | `getBridgeWidth(LengthUnits units)` | Returns bridge width in specified units. |
| `Color` | `getColor()` | Returns the color of hook and crane's rails for `OVERHEAD_CRANE_BRIDGE` crane type |
| `double` | `getCraneHeight()` | Returns the crane's height in pixels. |
| `double` | `getCraneHeight(LengthUnits units)` | Returns the crane's height in the specified length units. |
| `double` | `getCraneWidth()` | Returns the width of the crane in pixels. |
| `double` | `getCraneWidth(LengthUnits units)` | Returns the width of the crane specified units. |
| `double` | `getCurrentBridgeOffset(OverheadCraneBridge bridge, LengthUnits units)` |  |
| `double` | `getCurrentBridgeSpeed(OverheadCraneBridge bridge, SpeedUnits units)` | Returns the current bridge speed. |
| `double` | `getCurrentHoistSpeed(OverheadCraneBridge bridge, SpeedUnits units)` | Returns the current hoist speed. |
| `double` | `getCurrentHookOffset(OverheadCraneBridge bridge, LengthUnits units)` |  |
| `Point` | `getCurrentHookPosition()` |  |
| `Point` | `getCurrentHookPosition(OverheadCraneBridge bridge)` |  |
| `double` | `getCurrentTrolleyOffset(OverheadCraneBridge bridge, LengthUnits units)` |  |
| `double` | `getCurrentTrolleySpeed(OverheadCraneBridge bridge, SpeedUnits units)` | Returns the current trolley speed. |
| `BridgeDirection` | `getDirection(OverheadCraneBridge bridge)` |  |
| `IDowntime<?>[]` | `getDowntimeBlocks()` |  |
| `OverheadCraneGirderDrawingType` | `getGirderType()` | Returns the type of the crane's girder. |
| `Position` | `getHookPosition(OverheadCraneBridge bridge)` |  |
| `double` | `getInitialBridgePosition(LengthUnits units)` | Deprecated. the method will be removed, use [`OverheadCraneBridge.getInitialBridgeOffset(LengthUnits)`](OverheadCraneBridge.md#getInitialBridgeOffset(com.anylogic.engine.LengthUnits)) instead |
| `Point` | `getInitialHookPoint()` | Returns the initial hook point in **pixels**, calculated according to the crane's dimensions and converted to pixels with crane's space. |
| `Point` | `getInitialHookPoint(LengthUnits units)` | Returns the initial hook point in the specified length units. |
| `double` | `getInitialHookPosition(LengthUnits units)` | Deprecated. the method will be removed, use [`OverheadCraneBridge.getInitialHookOffset(LengthUnits)`](OverheadCraneBridge.md#getInitialHookOffset(com.anylogic.engine.LengthUnits)) instead |
| `double` | `getInitialTrolleyPosition(LengthUnits units)` | Deprecated. the method will be removed, use [`OverheadCraneBridge.getInitialTrolleyOffset(LengthUnits)`](OverheadCraneBridge.md#getInitialTrolleyOffset(com.anylogic.engine.LengthUnits)) instead |
| `com.anylogic.engine.markup.material_handling.IOverheadCraneDescriptor<T>` | `getLibraryDescriptor()` |  |
| `double` | `getMaximumBridgeSpeed(T agent, boolean isLoaded, SpeedUnits units)` | Returns the maximum bridge speed specified by the parameter value of this crane in the specified `units`. |
| `double` | `getMaximumHoistSpeed(T agent, boolean isLoaded, SpeedUnits units)` | Returns the maximum hoist speed specified by the parameter value of this crane in specified `units`. |
| `double` | `getMaximumTrolleySpeed(T agent, boolean isLoaded, SpeedUnits units)` | Returns the maximum trolley speed specified by the parameter value of this crane in specified `units`. |
| `OverheadCraneMovementMode` | `getMovementMode()` | Returns the movement mode of the crane. |
| `int` | `getNumberOfBridges()` | Returns number of crane's bridges |
| `Object` | `getPMLProxy(OverheadCraneBridge bridge)` |  |
| `double` | `getPriority(OverheadCraneBridge bridge)` |  |
| `List<Agent>` | `getQueue(Crane<Agent> crane)` |  |
| `double` | `getRotation()` | Returns rotation of the crane. |
| `double` | `getRunwayLength()` | Returns runway length in pixels. |
| `double` | `getRunwayLength(LengthUnits units)` | Returns runway length in specified units. |
| `double` | `getSafetyGap()` | Returns the safety gap of the crane. |
| `double` | `getSafetyGap(LengthUnits units)` | Returns the safety gap of the crane. |
| `OverheadCraneBridgeState` | `getState(OverheadCraneBridge bridge)` |  |
| `double` | `getStatisticsStartTime()` |  |
| `Point` | `getTargetPoint(OverheadCraneBridge bridge)` |  |
| `Color` | `getTrolleyColor()` | Returns the color of the crane's trolley |
| `Position` | `getTrolleyPosition(OverheadCraneBridge bridge)` |  |
| `OverheadCraneDrawingType` | `getType()` | Returns the crane's type. |
| `double` | `getUtilization()` | Returns the crane utilization: the value is calculated as mean of crane's bridges utilization. |
| `double` | `getUtilization(OverheadCraneBridge overheadCraneBridge)` |  |
| `double` | `hoistSpeed(T agent, boolean isLoaded, SpeedUnits units)` | Deprecated. the method will be removed, use [`getMaximumHoistSpeed(T agent, boolean isLoaded, SpeedUnits units)`](#getMaximumHoistSpeed(T,boolean,com.anylogic.engine.SpeedUnits)) instead |
| `boolean` | `isAccelerationEnabled()` | Returns value of parameter isAccelerationEnabled. |
| `boolean` | `isFailed()` | Returns `true` if the crane is failed and `false` otherwise. |
| `boolean` | `isFailed(OverheadCraneBridge overheadCraneBridge)` |  |
| `boolean` | `isLoaded()` |  |
| `boolean` | `isLoaded(OverheadCraneBridge overheadCraneBridge)` |  |
| `boolean` | `isObstacle()` | Returns `true` if this crane is considered an obstacle by transporters moving in free space mode. |
| `boolean` | `isReady()` | Returns `true` if the crane is ready to work with new agent and `false` otherwise. |
| `boolean` | `isReady(OverheadCraneBridge overheadCraneBridge)` |  |
| `void` | `moveBridge(OverheadCraneBridge bridge, Point absolutePoint, double safeHeight, boolean remainsAtTarget)` |  |
| `void` | `moveBridgeByProgram(OverheadCraneBridge bridge, CraneProgram program)` |  |
| `double` | `mtbf(OverheadCraneBridge bridge, IDowntime<?> downtime)` |  |
| `double` | `mtbf(OverheadCraneBridge bridge, IDowntime<?> downtime, TimeUnits units)` |  |
| `double` | `mttr(OverheadCraneBridge bridge, IDowntime<?> downtime)` |  |
| `double` | `mttr(OverheadCraneBridge bridge, IDowntime<?> downtime, TimeUnits units)` |  |
| `int` | `numberOfAgentsHandled()` | Returns number of agents handled by crane: the value is calculated as sum per crane's bridges. |
| `int` | `numberOfAgentsHandled(OverheadCraneBridge bridge)` |  |
| `int` | `numberOfConflicts(OverheadCraneBridge bridge)` |  |
| `void` | `onBridgeMovementFinished(OverheadCraneBridge bridge)` | Calls the crane's `onBridgeMovementFinished()` callback code |
| `void` | `onBridgeStateChange(T agent, OverheadCraneBridge bridge, OverheadCraneBridgeState type)` | Calls the crane's `onBridgeStateChange()` callback code |
| `void` | `onLoading(OverheadCraneBridge bridge, T agent)` | Calls crane's `onLoading()` callback code |
| `void` | `onLoading(T agent)` |  |
| `void` | `onRelease(OverheadCraneBridge bridge, T agent)` | Calls crane's `onRelease()` callback code |
| `void` | `onSeize(OverheadCraneBridge bridge, T agent)` | Calls crane's `onSeize()` callback code |
| `void` | `onTargetReached(OverheadCraneBridge bridge)` | Calls the crane's `onTargetReached()` callback code |
| `void` | `onUnloading(OverheadCraneBridge bridge, T agent)` | Calls crane's `onUnloading()` callback code |
| `void` | `onUnloading(T agent)` |  |
| `void` | `repair()` | Repairs the crane from `failed` state |
| `void` | `repair(OverheadCraneBridge overheadCraneBridge)` |  |
| `void` | `resetStats()` | Resets statistics for all bridges. |
| `void` | `resetStats(OverheadCraneBridge overheadCraneBridge)` |  |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setAccelerationEnabled(boolean value)` | Sets parameter isAccelerationEnabled. |
| `void` | `setBridgeWidth(double bridgeWidth, LengthUnits units)` | Sets bridge width length in specified units |
| `void` | `setColor(Color color)` | Sets the specified color of hook and crane's rails for `OVERHEAD_CRANE_BRIDGE` crane type |
| `void` | `setCraneHeight(double craneHeight, LengthUnits units)` | Sets crane height in specified units. |
| `void` | `setCraneWidth(double craneWidth, LengthUnits units)` | Sets crane width in specified units. |
| `void` | `setDowtimeBlocks(IDowntime<?>[] downtimeBlocks)` |  |
| `void` | `setGirderType(OverheadCraneGirderDrawingType girderType)` | Sets the crane's girder type |
| `void` | `setInitialBridgePosition(double bridgePosition, LengthUnits units)` | Deprecated. the method will be removed, use [`OverheadCraneBridge.setInitialBridgeOffset(double, LengthUnits)`](OverheadCraneBridge.md#setInitialBridgeOffset(double,com.anylogic.engine.LengthUnits)) |
| `void` | `setInitialHookPosition(double hookPosition, LengthUnits units)` | Deprecated. the method will be removed, use [`OverheadCraneBridge.setInitialHookOffset(double, LengthUnits)`](OverheadCraneBridge.md#setInitialHookOffset(double,com.anylogic.engine.LengthUnits)) |
| `void` | `setInitialTrolleyPosition(double trolleyPosition, LengthUnits units)` | Deprecated. the method will be removed, use [`OverheadCraneBridge.setInitialTrolleyOffset(double, LengthUnits)`](OverheadCraneBridge.md#setInitialTrolleyOffset(double,com.anylogic.engine.LengthUnits)) |
| `void` | `setLevel(Level level)` |  |
| `void` | `setMovementMode(OverheadCraneMovementMode movementMode)` | Sets movement mode. |
| `void` | `setObstacle(boolean isObstacle)` | Sets this crane as an obstacle for transporters moving in free space mode. |
| `void` | `setRotation(double rotation)` | Sets rotation of crane |
| `void` | `setRunwayLength(double length, LengthUnits units)` | Sets runway length in specified units |
| `void` | `setSafetyGap(double safetyGap, LengthUnits units)` | Sets the value for the safety gap of the crane. |
| `void` | `setTrolleyColor(Color trolleyColor)` | Sets the specified color of the crane's trolley |
| `void` | `setType(OverheadCraneDrawingType type)` | Sets the crane's type |
| `double` | `timeInState(OverheadCraneBridge bridge, OverheadCraneBridgeState state, TimeUnits units)` |  |
| `double` | `totalDistanceInConflict(OverheadCraneBridge bridge, LengthUnits units)` |  |
| `double` | `totalTimeInConflicts(OverheadCraneBridge bridge, TimeUnits units)` |  |
| `double` | `totalTransportationDistance(OverheadCraneBridge bridge, LengthUnits units)` |  |
| `double` | `totalTravelledDistance(OverheadCraneBridge bridge, LengthUnits units)` |  |
| `double` | `totalTravellingTime(OverheadCraneBridge bridge, TimeUnits units)` |  |
| `double` | `trolleyAcceleration(T agent, boolean isLoaded, AccelerationUnits units)` | Returns the trolley acceleration specified by the parameter value of this crane in the specified `units`. |
| `double` | `trolleyDeceleration(T agent, boolean isLoaded, AccelerationUnits units)` | Returns the trolley deceleration specified by the parameter value of this crane in the specified `units`. |
| `double` | `trolleySpeed(T agent, boolean isLoaded, SpeedUnits units)` | Deprecated. the method will be removed, use [`getMaximumTrolleySpeed(T agent, boolean isLoaded, SpeedUnits units)`](#getMaximumTrolleySpeed(T,boolean,com.anylogic.engine.SpeedUnits)) instead |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
| `SVGElement` | `updateSVGProperties(List<SVGCommand> output, ShapeDrawMode drawMode, boolean publicOnly, SVGElement owner, SVGElement elbehind, boolean isInReplicatedShape)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Updates SVG properties of the element that are then sent to the rendering client. |
| `void` | `validateInitialPosition(OverheadCraneBridge bridge, double offsetM)` |  |
