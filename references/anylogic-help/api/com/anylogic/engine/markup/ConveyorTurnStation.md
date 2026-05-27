*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorTurnStation.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorTurnStation<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorNode](ConveyorNode.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorTransitionalNode](ConveyorTransitionalNode.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorTurnStation<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<ConveyorNode<?>,ConveyorPath<?>>`, `com.anylogic.engine.markup.material_handling.IConveyorTurnStationDescriptor<T>`, `com.anylogic.engine.markup.material_handling.IMaterialAreaLocation<T>`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.IMaterialPointLocation<T>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ConveyorTurnStation<T extends Agent>
extends ConveyorTransitionalNode<T>
implements com.anylogic.engine.markup.material_handling.IConveyorTurnStationDescriptor<T>
```

Turn station is the graphical space markup element that is used to define turn stations.
Turn station rotates agents (material items) passing through it. Items can be rotated by any angle divisible by 90°.

Once placed on a conveyor, the turn station divides it into two independent conveyors, working in the same conveyor network.
Turn station can connect only two conveyors forming a straight line.

Turn station has its own transportation speed (it may differ from the speed of the connected conveyors).

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorTurnStation)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorTurnStation()` |  |
| `ConveyorTurnStation(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `ConveyorTurnStation(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, double x, double y, double z, Paint fillColor, Paint lineColor, com.anylogic.engine.markup.material_handling.IConveyorTurnStationDescriptor<T> descriptor, PathEnd<ConveyorPath<?>>... pathEnds)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `angle(T agent, AngleUnits units)` |  |
| `boolean` | `contains(Agent agent)` | Returns true is the given agent (material item) is on the turn station, returns false otherwise. |
| `void` | `fail()` | Initiates turn station failure. |
| `T` | `getAgent(int index)` | Returns the agent (material item) that is currently located on the turn station. |
| `List<T>` | `getAgents()` | Returns the list of agents (material items) that are currently located on the turn station. |
| `com.anylogic.engine.markup.material_handling.IConveyorTurnStationDescriptor<T>` | `getLibraryDescriptor()` |  |
| `ConveyorTurnStationMode` | `getMode()` | Returns the turn station's rotation mode. |
| `double` | `getRotationSpeed(RotationSpeedUnits units)` | Returns the turn station's rotation speed (in the specified rotation units). |
| `double` | `getSpeed(SpeedUnits units)` | Returns the speed of the turn station in the specified speed units. |
| `boolean` | `isFailed()` | Returns true if the turn station failed (broke down) and is not operating, returns false otherwise. |
| `boolean` | `isObstacle()` | Returns true if this turnstation is considered an obstacle by transporters moving in free space mode. |
| `boolean` | `isTakeSpeedOfConnectedConveyors()` |  |
| `void` | `onLeadingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onLeadingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTrailingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTrailingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `AgentOrientation` | `orientation(T agent)` |  |
| `void` | `postInitialize()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `removeAgent(Agent agent)` | Removes the given agent from the turn station. |
| `void` | `repair()` | Repairs the turn station, makes it available again. |
| `void` | `setMode(ConveyorTurnStationMode mode)` | Sets the turn station's rotation mode. |
| `void` | `setObstacle(boolean isObstacle)` | Sets this turnstation as an obstacle for transporters moving in free space mode. |
| `void` | `setRotationSpeed(double rotationSpeed, RotationSpeedUnits units)` | Sets the turn station's rotation speed (in the specified speed units) when switching from one conveyor to another. |
| `void` | `setSpeed(double speed, SpeedUnits units)` | Sets the new speed of the turn station in the specified speed units. |
| `int` | `size()` | Returns the current number of agents (material items) on the turn station. |
