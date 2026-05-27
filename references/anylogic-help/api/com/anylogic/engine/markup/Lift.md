*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/Lift.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class Lift<A extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.AbstractLevelMarkup](AbstractLevelMarkup.md "class in com.anylogic.engine.markup")

com.anylogic.engine.markup.Lift<A>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `HasBoundingRectangle`, `HasLevel`, `IMarkupLibraryDescriptor`, `LevelElement`, `LevelMarkup`, `com.anylogic.engine.markup.material_handling.ILiftDescriptor<A>`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class Lift<A extends Agent>
extends AbstractLevelMarkup
implements com.anylogic.engine.markup.material_handling.ILiftDescriptor<A>, HasBoundingRectangle, AbstractPositionalMarkup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.Lift)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `final MarkupPort` | `eastPort` | Lift's `NetworkPort` located to east |
| `final MarkupPort` | `northPort` | Lift's `NetworkPort` located to north |
| `final MarkupPort` | `southPort` | Lift's `NetworkPort` located to south |
| `final MarkupPort` | `westPort` | Lift's `NetworkPort` located to west |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Lift()` |  |
| `Lift(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, double x, double y, double z, double widthInMeters, double depthInMeters, double rotation, Paint fillColor, Paint lineColor, LiftPlatformDrawingType platformType, com.anylogic.engine.markup.material_handling.ILiftDescriptor<A> descriptor)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `List<MarkupPort>` | `collectAllPairedPorts(Predicate<MarkupPort> filter)` |  |
| `boolean` | `comparison(A agent1, A agent2)` | Returns the result of evaluating the expression specified by the user in "agent1 is preferred to agent2" parameter. |
| `boolean` | `contains(double px, double py)` | Test if the shape contains the point with the given coordinates (relative to this shape's container, i.e. |
| `double` | `droppingOffTime(A agent, TimeUnits units)` | Returns the time specified for agent movement between the center of the lift and the starting point of network path/conveyor. |
| `void` | `fail()` | Initiates the lift's failure. |
| `Agent` | `getAgentFromQueue(int index)` | Returns the agent from the queue with the specified index. |
| `BoundingRectangle` | `getBoundingRectangle()` |  |
| `double` | `getDepth(LengthUnits units)` | Returns the depth of the markup shape. |
| `Color` | `getFillColor()` | Returns the fill color of the shape, or `null` if shape has no fill color or has textured fill (in this case [`getFillTexture()`](#getFillTexture()) should be used instead) |
| `Texture` | `getFillTexture()` | Returns the fill texture of the shape, if the shape has fill texture |
| `double` | `getFloorElevation(LengthUnits units)` | Returns the distance between the lift and the surface you are using as level in the specified length units. |
| `com.anylogic.engine.markup.material_handling.ILiftDescriptor<A>` | `getLibraryDescriptor()` |  |
| `double` | `getLiftingSpeed(SpeedUnits units)` | Returns the speed of the lift movement in the specified speed units. |
| `List<Lift<?>>` | `getLiftLandings()` | Returns all landings this lift has, including itself. |
| `Color` | `getLineColor()` | Returns the line color of the markup element, or `null` if markup element has no line color or has textured line (in this case [`getLineTexture()`](#getLineTexture()) should be used instead) |
| `Texture` | `getLineTexture()` | Returns the line texture of the markup element, if the markup element has line texture |
| `Lift<?>` | `getMainLanding()` | Returns the main landing out of the collection of lift elements connected to each other. |
| `Lift<?>` | `getPlatformFloor()` |  |
| `LiftPlatformDrawingType` | `getPlatformType()` | Returns platform type. |
| `double` | `getPlatformZ()` |  |
| `double` | `getRotation()` | Returns the rotation of the shape. |
| `LiftSelectionMode` | `getSelectionMode()` | Returns the type of agent selection pattern for this lift, i.e. |
| `double` | `getWidth(LengthUnits units)` | Returns the width of the markup shape. |
| `double` | `getX()` | Returns the x coordinate of the markup element. |
| `Point` | `getXYZ()` | Returns coordinates of the markup element. |
| `double` | `getY()` | Returns the y coordinate of the markup element. |
| `double` | `getZ()` | Returns the z coordinate of the markup element. |
| `double` | `getZHeight(LengthUnits units)` |  |
| `void` | `initializeLiftLandings()` |  |
| `boolean` | `isFailed()` | Returns `true` if the lift failed (broke down) and is not operating, otherwise returns `false`. |
| `boolean` | `isMainLanding()` | Returns `true` if this lift is set as the main landing. |
| `boolean` | `isObstacle()` | Returns `true` if the lift is obstacle for transporters and `else` otherwise. |
| `void` | `onDropoffFinished(A agent)` | Calls `onDropoffFinished()` code of the lift |
| `void` | `onPickupStarted(A agent)` | Calls `onPickupStarted()` code of the lift |
| `double` | `pickingUpTime(A agent, TimeUnits units)` | Returns the time specified for agent movement between the ending point of network path/conveyor and the center. |
| `List<MarkupPort>` | `ports()` | Returns all ports of this element |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `priority(A agent)` | Returns the priority of the agent. |
| `int` | `queueSize()` | Returns the number of agents (material items) in the lift's queue. |
| `void` | `repair()` | Repairs the lift. |
| `void` | `setDepth(double depth, LengthUnits units)` | Sets the depth of the markup shape. |
| `void` | `setFillColor(Color fillColor)` | Sets the fill color of the shape. |
| `void` | `setFillColor(Paint fillColor)` | Sets the fill color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the shape. |
| `void` | `setFloorElevation(double floorLevel, LengthUnits units)` | Sets the distance between the lift and the surface you are using as level in the specified length units. |
| `void` | `setLiftingSpeed(double speed, SpeedUnits units)` | Set the speed of the lift movement in the specified speed units. |
| `void` | `setLineColor(Color lineColor)` | Sets the line color of the markup element. |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color (or [`Texture`](../presentation/Texture.md "class in com.anylogic.engine.presentation")) of the markup element. |
| `void` | `setMainLanding(boolean isMain)` | Sets the lift as the main landing. |
| `void` | `setMainLanding(Lift<?> mainLift)` | Assigns the main landing status to a lift from a collection of lift elements connected to each other. |
| `void` | `setObstacle(boolean isObstacle)` | Sets wether this lift is an obstacle for transporters. |
| `void` | `setPlatformType(LiftPlatformDrawingType platformType)` | Sets platform type |
| `void` | `setRotation(double rotation)` | Sets the rotation of the shape. |
| `void` | `setSelectionMode(LiftSelectionMode mode)` | Sets the new type of agent selection pattern for this lift, i.e. |
| `void` | `setWidth(double width, LengthUnits units)` | Sets the width of the markup shape. |
| `void` | `setX(double x)` | Sets the x coordinate of the markup element. |
| `void` | `setXYZ(double x, double y, double z)` | Sets coordinates of the markup element. |
| `void` | `setY(double y)` | Sets the y coordinate of the markup element. |
| `void` | `setZ(double z)` | Sets the z coordinate of the markup element. |
