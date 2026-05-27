*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/markup/ConveyorSimpleStation.html>*

---

Package [com.anylogic.engine.markup](package-summary.md)

# Class ConveyorSimpleStation<T extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.markup.AbstractMarkup](AbstractMarkup.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.MarkupShape](MarkupShape.md "class in com.anylogic.engine.markup")

[com.anylogic.engine.markup.ConveyorMarkupElement](ConveyorMarkupElement.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorPathPart](ConveyorPathPart.md "class in com.anylogic.engine.markup")<T>

[com.anylogic.engine.markup.ConveyorStation](ConveyorStation.md "class in com.anylogic.engine.markup")<T>

com.anylogic.engine.markup.ConveyorSimpleStation<T>

All Implemented Interfaces:
:   `IMaintenanceable`, `AggregatableAnimationElement`, `HasLevel`, `IMaintenanceableMarkup`, `IMarkupLibraryDescriptor`, `INetworkMarkupElement`, `com.anylogic.engine.markup.material_handling.IConveyorSimpleStationDescriptor<T>`, `com.anylogic.engine.markup.material_handling.IMaterialAreaLocation<T>`, `com.anylogic.engine.markup.material_handling.IMaterialFallible`, `com.anylogic.engine.markup.material_handling.IMaterialMarkupLibraryDescriptor`, `com.anylogic.engine.markup.material_handling.IMaterialPointLocation<T>`, `SVGElement`, `UsdElement`, `Serializable`

---

```
public class ConveyorSimpleStation<T extends Agent>
extends ConveyorStation<T>
implements com.anylogic.engine.markup.material_handling.IConveyorSimpleStationDescriptor<T>, IMaintenanceableMarkup
```

Use the Station space markup element to draw a simple processing station on a conveyor.

The station can process more than 1 material item at a time. The number of items to process is defined in the Capacity parameter.
If two or more material items must be processed simultaneously, the station will wait until the required number of agents arrives.

The time required to process the specified number of material items is defined by the Delay parameter.

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.markup.ConveyorSimpleStation)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ConveyorSimpleStation(ConveyorPath<? extends T> conveyor)` |  |
| `ConveyorSimpleStation(ConveyorPath<? extends T> conveyor, ShapeDrawMode drawMode, boolean isPublic, double offset, double lengthInMeters)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |
| `ConveyorSimpleStation(ConveyorPath<? extends T> conveyor, ShapeDrawMode drawMode, boolean isPublic, double offsetInPixels, double lengthInMeters, Paint fillColor, Paint lineColor, com.anylogic.engine.markup.material_handling.IConveyorSimpleStationDescriptor<T> descriptor)` | Deprecated. deprecated in version 8.4, will be removed in the future releases |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `contains(Agent agent)` | Returns true if the given agent (material item) is inside the station, returns false otherwise. |
| `void` | `fail()` | Initiates station failure. |
| `T` | `getAgent(int index)` | Returns the agent (material item) that is currently located in the station |
| `List<T>` | `getAgents()` | Returns the list of agents (material items) that are currently located in the station, returns null if none. |
| `int` | `getCapacity()` | Returns the number of agents (material items) that may be processed by the station. |
| `ConveyorSimpleStationDelayType` | `getDelayType()` |  |
| `IDowntime<?>[]` | `getDowntimeBlocks()` |  |
| `Color` | `getFillColor()` | Returns fill color of this element |
| `Texture` | `getFillTexture()` | Returns fill texture of this element |
| `com.anylogic.engine.markup.material_handling.IConveyorSimpleStationDescriptor<T>` | `getLibraryDescriptor()` |  |
| `Color` | `getLineColor()` | Returns line color of this element |
| `Texture` | `getLineTexture()` | Returns line texture of this element |
| `ConveyorSimpleStationLoadingMode` | `getLoadingMode()` |  |
| `Object` | `getPMLProxy()` |  |
| `ConveyorSimpleStationProcessingMode` | `getProcessingMode()` |  |
| `int` | `getQuantity()` | Deprecated. the method may be removed in next release, use [`getCapacity()`](#getCapacity()) instead |
| `boolean` | `getResourceChoiceCondition(T agent, List<T> allAgents, Agent unit, Object pool)` |  |
| `Object` | `getResourceDestinationType()` | Returns the type of destination the resources are sent to. |
| `ConveyorSimpleStationState` | `getState()` |  |
| `double` | `getStatisticsStartTime()` |  |
| `boolean` | `getTaskMayPreemptOtherTasks()` |  |
| `double` | `getUtilization()` | Returns the station utilization: the fraction of time the station was busy. |
| `boolean` | `isCustomizeResourceChoice()` |  |
| `boolean` | `isFailed()` | Returns true if the station failed (broke down) and is not operating, returns false otherwise. |
| `boolean` | `isMaintenanceActive(IDowntime<?> block)` |  |
| `boolean` | `isProcessing()` | Returns true if the station is processing agents (material items), returns false otherwise. |
| `boolean` | `isProcessing(Agent agent)` | Returns true if the station is processing the agent (material item), returns false otherwise. |
| `boolean` | `isSeizeFromOnePool()` | Returns true if the station will be using resource units of the same pool, returns false otherwise. |
| `boolean` | `isUseResources()` | Returns true if the station is using resource units, returns false otherwise. |
| `double` | `meanStateTime(ConveyorSimpleStationState state, TimeUnits units)` |  |
| `boolean` | `movingGoHome(T agent, List<T> allAgents, Agent unit)` |  |
| `double` | `mtbf()` | Returns mean time between failures in model time units. |
| `double` | `mtbf(IDowntime<?> downtime)` | Returns mean time between failures for specified Downtime block (in model time units). |
| `double` | `mtbf(IDowntime<?> downtime, TimeUnits units)` | Returns mean time between failures for specified Downtime block (in specified time units). |
| `double` | `mtbf(TimeUnits units)` | Returns mean time between failures in specified time units. |
| `double` | `mttr()` | Returns mean time to repair in model time units. |
| `double` | `mttr(IDowntime<?> downtime)` | Returns mean time to repair for specified Downtime block (in model time units). |
| `double` | `mttr(IDowntime<?> downtime, TimeUnits units)` | Returns mean time to repair for specified Downtime block (in specified time units). |
| `double` | `mttr(TimeUnits units)` | Returns mean time to repair in specified time units. |
| `void` | `onLeadingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onLeadingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onProcessFinished(T agent, List<T> allAgents)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onProcessStarted(T agent, List<T> allAgents)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTaskResumed(T agent, List<T> allAgents, Agent unit)` |  |
| `void` | `onTaskSuspended(T agent, List<T> allAgents, Agent unit)` |  |
| `void` | `onTaskTerminated(T agent, List<T> allAgents, Agent unit)` |  |
| `void` | `onTrailingEdgeEnter(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `void` | `onTrailingEdgeExit(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Callback action. |
| `double` | `priority(T agent, List<T> allAgents)` |  |
| `double` | `processTime(T agent, List<T> allAgents, TimeUnits units)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.   Returns delay for the given agent(s) |
| `boolean` | `removeAgent(Agent agent)` | Removes the given agent from the station. |
| `void` | `repair()` | Repairs station, makes it available again. |
| `void` | `resetStats()` |  |
| `Attractor` | `resourceDestinationAttractor(T agent, List<T> allAgents, Agent unit)` |  |
| `INode<?,?>` | `resourceDestinationNode(T agent, List<T> allAgents, Agent unit)` |  |
| `double` | `resourceDestinationX(T agent, List<T> allAgents, Agent unit)` |  |
| `double` | `resourceDestinationY(T agent, List<T> allAgents, Agent unit)` |  |
| `double` | `resourceDestinationZ(T agent, List<T> allAgents, Agent unit)` |  |
| `Object` | `resourcePool(T agent, List<T> allAgents)` |  |
| `int` | `resourceQuantity(T agent, List<T> allAgents)` |  |
| `Object[][]` | `resourceSets(T agent, List<T> allAgents)` |  |
| `void` | `restartMaintenanceTriggers(IDowntime<?> block)` |  |
| `boolean` | `sendResources(T agent, List<T> allAgents, Agent unit)` |  |
| `void` | `setCapacity(int capacity)` | Sets the number of agents (material items) that may be processed by the station. |
| `void` | `setDelayType(ConveyorSimpleStationDelayType type)` |  |
| `void` | `setDowntimeBlocks(IDowntime<?>[] downtimeBlocks)` |  |
| `void` | `setFillColor(Paint fillColor)` | Sets the fill color of this element |
| `void` | `setLineColor(Paint lineColor)` | Sets the line color of this element |
| `void` | `setLoadingMode(ConveyorSimpleStationLoadingMode mode)` |  |
| `void` | `setProcessingMode(ConveyorSimpleStationProcessingMode mode)` | Cannot be changed in runtime |
| `void` | `setQuantity(int quantity)` | Deprecated. the method may be removed in next release, use `#setCapacity()` instead |
| `void` | `setResourceDestinationType(Object resourceDestinationType)` |  |
| `void` | `setSeizeFromOnePool(boolean seizeFromOnePool)` |  |
| `void` | `setTaskMayPreemptOtherTasks(boolean value)` |  |
| `void` | `setUseResources(boolean useResources)` |  |
| `int` | `size()` | Returns the current number of agents (material items) inside the station |
| `void` | `startMaintenanceManually(IDowntime<?> block)` |  |
| `void` | `stopMaintenanceManually(IDowntime<?> block)` |  |
| `void` | `stopProcess()` | Stops the station when called. |
| `void` | `stopProcess(Agent agent)` | Stops processing of specified agent. |
| `TaskPreemptionPolicy` | `taskPreemptionPolicy(T agent, List<T> allAgents)` |  |
| `double` | `totalStateTime(ConveyorSimpleStationState state, TimeUnits units)` |  |
