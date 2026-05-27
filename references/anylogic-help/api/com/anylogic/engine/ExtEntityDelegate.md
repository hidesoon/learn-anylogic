*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEntityDelegate.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExtEntityDelegate<E extends ExtEntity>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.AgentExtensionImpl](AgentExtensionImpl.md "class in com.anylogic.engine")

[com.anylogic.engine.ExtAgentWithSpatialMetricsDelegate](ExtAgentWithSpatialMetricsDelegate.md "class in com.anylogic.engine")<E>

com.anylogic.engine.ExtEntityDelegate<E>

Type Parameters:
:   `E` - type of agent extension to delegate to. If you are creating new extension based on 'Entity', please
    set the type to `ExtEntity`

All Implemented Interfaces:
:   `AgentExtension`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `ExtDefaultAnimationProvider`, `ExtEntity`, `Serializable`

---

```
@AnyLogicInternalAPI
public abstract class ExtEntityDelegate<E extends ExtEntity>
extends ExtAgentWithSpatialMetricsDelegate<E>
implements ExtEntity
```

Base class for extensions delegating their 'Entity' activity to an existing extension of agent

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExtEntityDelegate)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExtEntityDelegate(Agent owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAgentToContents(Agent entity)` | Adds a given agent to the contents of this agent. |
| `List<Agent>` | `contents()` |  |
| `ShapeTopLevelPresentationGroup` | `createDefaultAnimation()` |  |
| `FlowchartBlock` | `currentBlock()` | Returns the current flowchart block this agent is being processed in. |
| `void` | `destroyEntity()` | Destroys the agent. |
| `double` | `getBlockEnterTime()` | Returns the time this agent entered its current flowchart block. |
| `Color` | `getColor()` | Returns the color of the item default shape. |
| `ShapeTopLevelPresentationGroup` | `getDefaultAnimation()` |  |
| `double` | `getFlowchartEntryTime()` | Returns the time the agent has entered the first block in the flowchart, or `Double.NaN` if this agent hasn't yet visited any flowchart |
| `double` | `getHeight()` | Returns the height of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getHeight(LengthUnits units)` | Returns the height of the agent - used by conveyors and other blocks which require it during processing. |
| `int` | `getId()` | Returns Id of agent. |
| `double` | `getLength()` | Returns the length of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getLength(LengthUnits units)` | Returns the length of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getWidth()` | Returns the width of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getWidth(LengthUnits units)` | Returns the width of the agent - used by conveyors and other blocks which require it during processing. |
| `void` | `highlight(boolean yes)` | Turns on/off highlighting of this agent animation. |
| `boolean` | `onClick()` | Should be overridden to define the reaction on mouse click. |
| `int` | `priority()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  This function is used for sorting extensions (in order for the overriding delegation to work) |
| `boolean` | `removeAgentFromContents(Agent entity)` | Removes the given agent from the contents of this agent. |
| `Agent` | `resourceUnitOfPool(Agent pool)` | Returns the first occurrence of resource unit of a given pool among the seized resource units, or `null` if not found. |
| `List<Agent>` | `resourceUnits()` | Returns the list of resource units seized by the agent, or empty list if there are none. |
| `List<Agent>` | `resourceUnitsOfPool(Agent pool)` | Returns resource units currently seized by this agent from the given `ResourcePool` block |
| `List<Agent>` | `resourceUnitsOfSeize(Agent seize)` | Return resource units currently seized by this agent in the given `Seize` block |
| `void` | `setColor(Color color)` | Sets the color of the item default shape. |
| `void` | `setFlowchartActivityType(FlowchartActivityType activityType, FlowchartBlock block)` | Sets activity type info (used in e.g. |
| `void` | `setHeight(double height)` | Sets the height of the agent (in meters) |
| `void` | `setHeight(double height, LengthUnits units)` | Sets the height of the agent in the given units |
| `void` | `setLength(double length)` | Sets the length of the agent (in meters) |
| `void` | `setLength(double length, LengthUnits units)` | Sets the length of the agent in the given units |
| `void` | `setWidth(double width)` | Sets the width of the agent (in meters) |
| `void` | `setWidth(double width, LengthUnits units)` | Sets the width of the agent in the given units |
