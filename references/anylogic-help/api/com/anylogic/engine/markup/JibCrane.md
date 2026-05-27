*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/JibCrane.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class JibCrane<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.Crane](Crane.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.JibCrane<T>

All Implemented Interfaces:
:   `IMaintenanceable`, `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `IMaintenanceableMarkup`, `IMarkupLibraryDescriptor`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.IJibCraneDescriptor<T>`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class JibCrane<T extends Agent>
extends Crane<T>
implements HasBoundingRectangle, IMaintenanceableMarkup, com.anylogic.engine.markup.material_handling.IJibCraneDescriptor<T>, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.JibCrane)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `JibCrane()` |  |
| `JibCrane(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, com.anylogic.engine.markup.material_handling.IJibCraneDescriptor<T> descriptor, double x, double y, double z, double jibLengthMeters, double craneHeightMeters, double jibAngleRadians, double trolleyLocationMeters, boolean blockedZoneEnabled, double blockedZoneStartAngleRadians, double blockedZoneAngleRadians, Color color, Color cabinColor, JibCraneDrawingType type)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `JibCrane(com.anylogic.engine.markup.material_handling.IJibCraneDescriptor<T> d)` | Deprecated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `void` | `fail()` | Sets the crane to `failed` state |
| `Position` | `getAbsoluteHookPosition()` | Returns the current absolute hook position as an instance of `Position` in pixels. |
| `double` | `getBlockedZoneAngle(AngleUnits units)` | Returns the delta angle of the crane's blocked zone. |
| `double` | `getBlockedZoneStartAngle(AngleUnits units)` | Returns the initial angle of the crane's blocked zone. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `Color` | `getCabinColor()` | Returns the color of the crane's cabin |
| `Color` | `getColor()` | Returns the crane's color |
| `double` | `getCraneHeight()` | Returns the crane's height in pixels. |
| `double` | `getCraneHeight(LengthUnits units)` | Returns the crane's height in the specified length units. |
| `Position` | `getCurrentHookPosition()` | Returns the current relative hook position as an instance of `Position` in pixels. |
| `IDowntime<?>[]` | `getDowntimeBlocks()` |  |
| `Position` | `getInitialHookPoint()` | Returns the initial hook point in **pixels**, calculated according to the crane's dimensions and converted to pixels with crane's space. |
| `Position` | `getInitialHookPoint(LengthUnits units)` | Returns the initial hook point in the specified length units. |
| `Position` | `getInitialHookPoint(Function<Double,Double> meterToPx)` |  |
| `double` | `getInitialHookPosition(LengthUnits units)` | Returns the initial offset of the crane's hook in the specified length units. |
| `double` | `getInitialJibAngle(AngleUnits units)` | Returns the initial jib angle. |
| `double` | `getInitialTrolleyPosition(LengthUnits units)` | Returns the initial offset of the crane's trolley in the specified length units. |
| `double` | `getJibLength()` | Returns the crane's jib length in pixels. |
| `double` | `getJibLength(LengthUnits units)` | Returns the crane's jib length in the specified length units. |
| `com.anylogic.engine.markup.material_handling.IJibCraneDescriptor<T>` | `getLibraryDescriptor()` |  |
| `double` | `getLiftingSpeed(SpeedUnits units)` | Deprecated. - will be deleted in the next release because the crane's motion parameters became dynamic. |
| `JibCraneMovementMode` | `getMovementMode()` | Returns movement mode of the crane. |
| `Object` | `getPMLProxy()` |  |
| `double` | `getRotation()` | *This method shouldn't be called by user  (is public due to technical reasons)* |
| `double` | `getRotationSpeed(RotationSpeedUnits units)` | Deprecated. - will be deleted in the next release because the crane's motion parameters became dynamic. |
| `JibCraneState` | `getState()` |  |
| `double` | `getStatisticsStartTime()` |  |
| `double` | `getTrolleySpeed(SpeedUnits units)` | Deprecated. - will be deleted in the next release because the crane's motion parameters became dynamic. |
| `JibCraneDrawingType` | `getType()` | Returns the type of the crane. |
| `double` | `getUtilization()` | Returns the crane utilization: the fraction of time the crane was operating. |
| `boolean` | `isBlockedZoneEnabled()` | Returns `true` if the crane has enabled blocked zone and `false` otherwise. |
| `boolean` | `isFailed()` | Returns `true` if the crane is failed and `false` otherwise. |
| `boolean` | `isLoaded()` | Returns `true` if crane loaded. |
| `boolean` | `isMaintenanceActive(IDowntime<?> block)` |  |
| `boolean` | `isObstacle()` | Returns `true` if this crane is considered an obstacle by transporters moving in free space mode. |
| `boolean` | `isReady()` | Returns `true` if the crane is ready to operate, i.e. |
| `double` | `liftingSpeed(T agent, boolean isLoaded, SpeedUnits units)` | Returns the hoist speed specified by the parameter value of this crane in the specified `units`. |
| `double` | `mtbf()` | Returns mean time between failures in model time units. |
| `double` | `mtbf(IDowntime<?> downtime)` | Returns mean time between failures for specified Downtime block (in model time units). |
| `double` | `mtbf(IDowntime<?> downtime, TimeUnits units)` | Returns mean time between failures for specified Downtime block (in specified time units). |
| `double` | `mtbf(TimeUnits units)` | Returns mean time between failures in specified time units. |
| `double` | `mttr()` | Returns mean time to repair in model time units. |
| `double` | `mttr(IDowntime<?> downtime)` | Returns mean time to repair for specified Downtime block (in model time units). |
| `double` | `mttr(IDowntime<?> downtime, TimeUnits units)` | Returns mean time to repair for specified Downtime block (in specified time units). |
| `double` | `mttr(TimeUnits units)` | Returns mean time to repair in specified time units. |
| `void` | `onLoading(T agent)` | Calls the crane's `onLoading()` callback code |
| `void` | `onRelease(T agent)` |  |
| `void` | `onSeize(T agent)` |  |
| `void` | `onUnloading(T agent)` | Calls the crane's `onUnloading()` callback code |
| `void` | `repair()` | Repairs the crane from `failed` state |
| `void` | `resetStats()` | Resets the crane utilization statistics. |
| `void` | `restartMaintenanceTriggers(IDowntime<?> block)` |  |
| `double` | `rotationSpeed(T agent, boolean isLoaded, RotationSpeedUnits units)` | Returns the jib rotation speed specified by the parameter value of this crane in the specified `units`. |
| `void` | `setBlockedZone(double startAngle, double deltaAngle, AngleUnits units)` | Sets the specified blocked zone of the crane in the specified angle units. |
| `void` | `setBlockedZoneAngle(double angle, AngleUnits units)` | Sets the delta angle of the crane's blocked zone in the specified angle units and updates animation. |
| `void` | `setBlockedZoneEnabled(boolean blockedZoneEnabled)` | Enables the crane's blocked zone if the parameter is `true` and disables if `false` |
| `void` | `setBlockedZoneStartAngle(double angle, AngleUnits units)` | Sets the initial angle of the crane's blocked zone in the specified units and updates animation. |
| `void` | `setCabinColor(Color cabinColor)` | Sets the specified color of the crane's cabin |
| `void` | `setColor(Color color)` | Sets the specified color of the crane |
| `void` | `setCraneHeight(double height, LengthUnits units)` | Sets the crane's height in the specified length units and updates animation. |
| `void` | `setDowntimeBlocks(IDowntime<?>[] downtimeBlocks)` |  |
| `void` | `setInitialHookPosition(double hookPosition, LengthUnits units)` | Sets the initial hook position in the specified length units. |
| `void` | `setInitialJibAngle(double angle, AngleUnits units)` | Sets the initial angle of the crane's jib in the specified angle units. |
| `void` | `setInitialTrolleyPosition(double trolleyPosition, LengthUnits units)` | Sets the initial offset of the crane's trolley in the specified length units. |
| `void` | `setJibLength(double length, LengthUnits units)` | Sets the crane's jib length in the specified length units and updates animation. |
| `void` | `setMovementMode(JibCraneMovementMode movementMode)` | Changes the movement mode on-the-go. |
| `void` | `setObstacle(boolean isObstacle)` | Sets this crane as an obstacle for transporters moving in free space mode. |
| `void` | `setType(JibCraneDrawingType type)` | Sets the type of the crane. |
| `void` | `startMaintenanceManually(IDowntime<?> block)` |  |
| `void` | `stopMaintenanceManually(IDowntime<?> block)` |  |
| `double` | `trolleySpeed(T agent, boolean isLoaded, SpeedUnits units)` | Returns the trolley speed specified by the parameter value of this crane in the specified `units`. |
| `void` | `updateDynamicProperties()` | Updates dynamic properties of this shape only (without structural contents, if any) in a given context.  Method should be overridden for shapes with dynamic properties. |
