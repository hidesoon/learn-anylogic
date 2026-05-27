*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEntity.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtEntity

All Superinterfaces:
:   `AgentExtension`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `ExtDefaultAnimationProvider`, `Serializable`

All Known Implementing Classes:
:   `ExtEntityContinuousDelegate`, `ExtEntityDelegate`

---

```
public interface ExtEntity
extends ExtAgentWithSpatialMetrics, ExtDefaultAnimationProvider
```

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAgentToContents(Agent agent)` | Adds a given agent to the contents of this agent. |
| `List<Agent>` | `contents()` |  |
| `FlowchartBlock` | `currentBlock()` | Returns the current flowchart block this agent is being processed in. |
| `void` | `destroyEntity()` | Destroys the agent. |
| `double` | `getBlockEnterTime()` | Returns the time this agent entered its current flowchart block. |
| `Color` | `getColor()` | Returns the color of the item default shape. |
| `double` | `getFlowchartEntryTime()` | Returns the time the agent has entered the first block in the flowchart, or `Double.NaN` if this agent hasn't yet visited any flowchart |
| `double` | `getHeight()` | Returns the height of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getHeight(LengthUnits units)` | Returns the height of the agent - used by conveyors and other blocks which require it during processing. |
| `int` | `getId()` | Returns Id of agent. |
| `double` | `getLength()` | Returns the length of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getLength(LengthUnits units)` | Returns the length of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getWidth()` | Returns the width of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getWidth(LengthUnits units)` | Returns the width of the agent - used by conveyors and other blocks which require it during processing. |
| `default void` | `highlight(boolean yes)` | Turns on/off highlighting of this agent animation. |
| `boolean` | `removeAgentFromContents(Agent agent)` | Removes the given agent from the contents of this agent. |
| `Agent` | `resourceUnitOfPool(Agent pool)` | Returns the first occurrence of resource unit of a given pool among the seized resource units, or `null` if not found. |
| `List<Agent>` | `resourceUnits()` | Returns the list of resource units seized by the agent, or empty list if there are none. |
| `List<Agent>` | `resourceUnitsOfPool(Agent pool)` | Returns resource units currently seized by this agent from the given `ResourcePool` block |
| `List<Agent>` | `resourceUnitsOfSeize(Agent seize)` | Return resource units currently seized by this agent in the given `Seize` block |
| `void` | `setColor(Color color)` | Sets the color of the item default shape. |
| `void` | `setFlowchartActivityType(FlowchartActivityType activityType, FlowchartBlock block)` | Sets activity type info (used in e.g. |
| `void` | `setHeight(double heightInMeters)` | Sets the height of the agent (in meters) |
| `void` | `setHeight(double height, LengthUnits units)` | Sets the height of the agent in the given units |
| `void` | `setLength(double lengthInMeters)` | Sets the length of the agent (in meters) |
| `void` | `setLength(double length, LengthUnits units)` | Sets the length of the agent in the given units |
| `void` | `setWidth(double widthInMeters)` | Sets the width of the agent (in meters) |
| `void` | `setWidth(double width, LengthUnits units)` | Sets the width of the agent in the given units |
