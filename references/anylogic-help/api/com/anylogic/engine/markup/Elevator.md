*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Elevator.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Elevator<A extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Elevator<A>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `IMarkupLibraryDescriptor`, `LevelElement`, `LevelMarkup`, `IElevatorDescriptor<A>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Elevator<A extends Agent>
extends AbstractLevelMarkup
implements HasBoundingRectangle, IElevatorDescriptor<A>, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Elevator)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static interface` | `Elevator.Call<T extends Agent>` | Class describing elevator call at certain level |

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Elevator()` |  |
| `Elevator(Agent owner, ShapeDrawMode drawMode, boolean isPublic, double x, double y, double widthInMeters, double depthInMeters, double cabinHeightInMeters, double lineWidth, double rotation, Paint lineColor, Paint fillColor, boolean drawShaft, ElevatorDoorsConfiguration doorsConfiguration, IElevatorDescriptor<A> descriptor)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Level[]` | `accessibleLevels()` | Returns array of levels, which can be served by elevator |
| `void` | `addAccessibleLevels(Level... levels)` | Adds levels that can be served by elevator. |
| `void` | `addToLevels()` | Used when elevator markup is created by code - adds elevator to all its levels as an obstacle and adds shafts. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `deleteCallsOnLevel(Level level)` | Removes all pickup tasks from the level. |
| `void` | `disableDoor(Level level, ElevatorDoor door)` | Disables elevator door on the level. |
| `void` | `dropOffPeds(Collection<? extends Agent> peds)` | Starts drop off for the pedestrians in the list. |
| `void` | `enableDoor(Level level, ElevatorDoor door)` | Enables elevator door on the level. |
| `void` | `fail()` | Initiates the elevator's failure. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getCabinHeight(LengthUnits units)` | Returns elevator cabin height |
| `double` | `getCabinZ()` |  |
| `List<? extends Elevator.Call<A>>` | `getCalls()` | Returns list of elevator calls |
| `int` | `getCapacity()` | Returns the number of pedestrian elevator can transfer at once |
| `ElevatorDirection` | `getCurrentDirection()` | Returns current movement direction of the elevator. |
| `Level` | `getCurrentLevel()` | Returns elevator current level. |
| `double` | `getDepth()` | Returns the depth of the markup shape, in meters. |
| `double` | `getDepth(LengthUnits units)` | Returns the depth of the markup shape. |
| `ElevatorDoorsConfiguration` | `getDoorsConfiguration()` | Returns elevator doors configuration. |
| `Paint` | `getFillPaint()` |  |
| `IElevatorDescriptor<A>` | `getLibraryDescriptor()` |  |
| `Paint` | `getLinePaint()` |  |
| `double` | `getLineWidth()` | Returns elevator line width (in pixels) |
| `Elevator<A>` | `getMarkup()` |  |
| `ElevatorMovementMode` | `getMovementMode()` | Returns elevator movement mode. |
| `Level` | `getNearestLevel()` | Returns nearest level level - current level if elevator is not between levels, next level along direction if elevator is moving and closest otherwise. |
| `Set<A>` | `getPeds()` | Returns the list of pedestrians that are currently inside elevator |
| `Level` | `getPedTargetLevel(Agent ped)` | Returns target level of a pedestrian, specified in PedElevator block. |
| `Color` | `getPlatformColor()` | Returns the platform color of the elevator markup, or `null` if markup element has no platform color or has textured platform (in this case [`getPlatformTexture()`](#getPlatformTexture()) should be used instead) |
| `Texture` | `getPlatformTexture()` | Returns the platform texture of the elevator markup, or `null` if markup element has no platform texture (in this case [`getPlatformColor()`](#getPlatformColor()) should be used instead) |
| `double` | `getRotation()` | Returns the rotation of the shape. |
| `List<Level>` | `getRoute()` | Returns the list of levels which the elevator is going to visit according to current tasks. |
| `List<ElevatorShaft>` | `getShafts()` |  |
| `double` | `getSpeed()` | Returns elevator speed. |
| `double` | `getSpeed(SpeedUnits units)` | Returns elevator speed |
| `ElevatorState` | `getState()` | Returns current elevator state |
| `Level` | `getTargetLevel()` | Returns target level when the elevator is in manual mode and moving, `null` otherwise. |
| `double` | `getTimePerLevel()` | Returns time to move between two neighboring levels |
| `double` | `getTimePerLevel(TimeUnits units)` | Returns time to move between two neighboring levels |
| `Set<A>` | `getWaitingPeds()` | Returns set of pedestrians waiting for elevator on all levels |
| `Set<A>` | `getWaitingPeds(Level level)` | Returns set of pedestrians waiting for elevator on the level |
| `Color` | `getWallColor()` | Returns the wall color of the elevator markup, or `null` if markup element has no wall color or has textured wall (in this case [`getWallTexture()`](#getWallTexture()) should be used instead) |
| `Texture` | `getWallTexture()` | Returns the wall texture of the elevator markup, or `null` if markup element has no wall texture (in this case [`getWallColor()`](#getWallColor()) should be used instead) |
| `double` | `getWidth()` | Returns the width of the markup shape, in meters. |
| `double` | `getWidth(LengthUnits units)` | Returns the width of the markup shape. |
| `double` | `getX()` | Returns the x coordinate of the markup element. |
| `Point` | `getXYZ()` | Returns coordinates of the markup element. |
| `double` | `getY()` | Returns the y coordinate of the markup element. |
| `double` | `getZ()` | *This method shouldn't be called by user  (is public due to technical reasons)* |
| `boolean` | `isAllLevels()` | Returns `true` if elevator supposed to serve all levels in owner agent, `false` otherwise |
| `boolean` | `isDoorEnabled(Level level, ElevatorDoor door)` | Returns `true` if the door on the level is enabled, `false` otherwise. |
| `boolean` | `isDrawShaft()` | Returns `true` if the elevator's shaft is drawn, otherwise returns `false`. |
| `boolean` | `isFailed()` | Returns `true` if the elevator failed (broke down) and is not operating, otherwise returns `false`. |
| `boolean` | `isManualMode()` | Returns `true` if the elevator is in manual mode, `false` otherwise. |
| `boolean` | `isShaftsInitialized_xjal()` |  |
| `double` | `meanWaitingTime()` | Returns mean time (in model time units) pedestrian spent waiting for elevator on all levels |
| `double` | `meanWaitingTime(Level level)` | Returns mean time (in model time units) pedestrian spent waiting for elevator on specified level |
| `double` | `meanWaitingTime(Level level, TimeUnits units)` | Returns mean time (in units) pedestrian spent waiting for elevator on specified level |
| `double` | `meanWaitingTime(TimeUnits units)` | Returns mean time (in units) pedestrian spent waiting for elevator on all levels |
| `double` | `minStayTime()` | Returns minimum time elevator will spend on the level before moving further. |
| `double` | `minStayTime(TimeUnits units)` | Returns minimum time elevator will spend on the level before moving further. |
| `void` | `moveTo(Level level)` | Sends the elevator to specified level. |
| `void` | `moveTo(Level level, boolean stayInManualMode)` | Sends the elevator to specified level. |
| `int` | `nDroppedOffPeds(Level level)` | Returns number of pedestrians elevator dropped off at specified level |
| `int` | `nPickedUpPeds(Level level)` | Returns number of pedestrians elevator picked up at specified level |
| `int` | `nTransportedPeds()` | Returns number of pedestrians transported by the elevator |
| `void` | `onArrival(Level level, List<A> waitingPeds)` | Calls `onArrival()` code of the elevator |
| `void` | `onDeparture(Level level)` | Calls `onDeparture()` code of the elevator |
| `void` | `onFailed()` | Calls `onFailed()` code of the elevator |
| `void` | `onRepaired()` | Calls `onRepaired()` code of the elevator |
| `void` | `onStateChanged(ElevatorState newState)` | Calls `onStateChanged()` code of the elevator. |
| `void` | `pickUpPeds(Collection<? extends Agent> peds)` | Starts pickup for the pedestrians in the list. |
| `void` | `repair()` | Repairs the elevator. |
| `void` | `resetStats()` | Resets all elevator statistics. |
| `void` | `setAllLevels(boolean allLevels)` | Sets whether elevator should serve all levels in owner agent |
| `void` | `setCabinHeight(double cabinHeight, LengthUnits units)` | Sets elevator cabin height |
| `void` | `setCapacity(int capacity)` | Sets elevator capacity |
| `void` | `setDepth(double depth)` | Sets the depth of the markup shape. |
| `void` | `setDepth(double depth, LengthUnits units)` | Sets the depth of the markup shape. |
| `void` | `setDoorsConfiguration(ElevatorDoorsConfiguration doorsConfiguration)` | Sets elevator doors configuration. |
| `void` | `setDrawShaft(boolean drawShaft)` | Sets whether elevator's shaft should be drawn. |
| `void` | `setLineWidth(double lineWidth)` | Sets elevator line width (in pixels) |
| `void` | `setManualMode(boolean on)` | Changes current mode of the elevator. |
| `void` | `setMarkup(Elevator<A> markup)` |  |
| `void` | `setMovementMode(ElevatorMovementMode movementMode)` | Sets elevator movement mode. |
| `void` | `setPlatformColor(Paint platformColor)` | Sets the platform color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the elevator markup. |
| `void` | `setRotation(double rotation)` | Sets the rotation of the shape. |
| `void` | `setSpeed(double speed)` | Sets elevator speed. |
| `void` | `setSpeed(double speed, SpeedUnits units)` | Sets elevator speed. |
| `void` | `setTimePerLevel(double timePerLevel)` | Sets elevator time per level. |
| `void` | `setTimePerLevel(double timePerLevel, TimeUnits units)` | Sets time per level. |
| `void` | `setVisible(boolean visible)` | Sets the visibility of the markup element. |
| `void` | `setWallColor(Paint wallColor)` | Sets the wall color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the elevator markup. |
| `void` | `setWidth(double width)` | Sets the width of the markup shape. |
| `void` | `setWidth(double width, LengthUnits units)` | Sets the width of the markup shape. |
| `void` | `setX(double x)` | Sets the x coordinate of the markup element. |
| `void` | `setXYZ(double x, double y, double z)` | Sets coordinates of the markup element. |
| `void` | `setY(double y)` | Sets the y coordinate of the markup element. |
| `double` | `timeInState(ElevatorState state)` | Returns time (in model time units) elevator spent in specified state since model start or since last `resetStats()` call |
| `double` | `timeInState(ElevatorState state, TimeUnits units)` | Returns time (in units) elevator spent in specified state since model start or since last `resetStats()` call |
| `double` | `totalTravelTime()` | Returns total time (in model time units) elevator was moving since model start or since last `resetStats()` call |
| `double` | `totalTravelTime(TimeUnits units)` | Returns total time (in units) elevator was moving since model start or since last `resetStats()` call |
| `double` | `utilization()` | Returns the elevator utilization: the fraction of time the elevator was operating. |
