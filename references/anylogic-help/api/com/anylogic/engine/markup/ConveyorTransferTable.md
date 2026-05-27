*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorTransferTable.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorTransferTable<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorNode](ConveyorNode.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorTransitionalNode](ConveyorTransitionalNode.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorTransferTable<T>

All Implemented Interfaces:
:   `AbstractPositionalMarkup`, `AggregatableAnimationElement`, `AnimationStaticLocationProvider`, `HasLevel`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `INode<ConveyorNode<?>,ConveyorPath<?>>`, `com.anylogic.engine.markup.material_handling.IConveyorTransferTableDescriptor<T>`, `com.anylogic.engine.markup.material_handling.IMaterialAreaLocation<T>`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.IMaterialPointLocation<T>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ConveyorTransferTable<T extends Agent>
extends ConveyorTransitionalNode<T>
implements com.anylogic.engine.markup.material_handling.IConveyorTransferTableDescriptor<T>
```

Transfer table is the space markup element that is used to define transfer tables in the material handling models.
Agents (material items) passing through it keep their current orientation on in space.
Once placed on a conveyor, the transfer table divides it into two independent conveyors, working in the same conveyor network.
Transfer table may connect up to 4 conveyors at right angle (90°).

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorTransferTable)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorTransferTable()` |  |
| `ConveyorTransferTable(Agent owner, ShapeDrawMode drawMode, boolean isPublic)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `ConveyorTransferTable(Agent owner, ShapeDrawMode drawMode, boolean isPublic, boolean isObstacle, double x, double y, double z, Paint fillColor, Paint lineColor, com.anylogic.engine.markup.material_handling.IConveyorTransferTableDescriptor<T> descriptor, PathEnd<ConveyorPath<?>>... pathEnds)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(Agent agent)` | Returns true is the given agent (material item) is on the transfer table, returns false otherwise. |
| `void` | `fail()` | Initiates transfer table failure. |
| `T` | `getAgent(int index)` | Returns the agent (material item) that is currently located on the transfer table |
| `List<T>` | `getAgents()` | Returns the list of agents (material items) that are currently located on the transfer table. |
| `com.anylogic.engine.markup.material_handling.IConveyorTransferTableDescriptor<T>` | `getLibraryDescriptor()` |  |
| `double` | `getSpeed(SpeedUnits units)` | Returns the speed of the transfer table in the specified speed units. |
| `double` | `getSwitchingDelay(TimeUnits units)` | Returns the time (in the specified time units) required to turn the transfer table towards another conveyor. |
| `boolean` | `isFailed()` | Returns true if the transfer table failed (broke down) and is not operating, returns false otherwise. |
| `boolean` | `isObstacle()` | Returns true if this transfer table is considered an obstacle by transporters moving in free space mode. |
| `boolean` | `isTakeSpeedOfConnectedConveyors()` |  |
| `void` | `onLeadingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onLeadingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTrailingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTrailingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `recalculatePriorities()` |  |
| `boolean` | `removeAgent(Agent agent)` | Removes the given agent from the transfer table. |
| `void` | `repair()` | Repairs the transfer table, makes it available again. |
| `void` | `setObstacle(boolean isObstacle)` | Sets this transfer table as an obstacle for transporters moving in free space mode. |
| `void` | `setSpeed(double speed, SpeedUnits units)` | Sets the new speed of the transfer table in the specified speed units. |
| `void` | `setSwitchingDelay(double delay, TimeUnits units)` | Sets the time (in the specified time units) required to turn the transfer table towards another conveyor. |
| `void` | `setTakeSpeedOfConnectedConveyors(boolean takeSpeedOfConnectedConveyors)` |  |
| `int` | `size()` | Returns the current number of agents (material items) on the transfer table. |
