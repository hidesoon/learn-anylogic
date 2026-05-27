*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEntityContinuousDelegate.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExtEntityContinuousDelegate<E extends ExtEntity>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.AgentExtensionImpl](AgentExtensionImpl.md "class in com.anylogic.engine")

[com.anylogic.engine.ExtAgentContinuousDelegate](ExtAgentContinuousDelegate.md "class in com.anylogic.engine")<[ExtAgentContinuous](ExtAgentContinuous.md "interface in com.anylogic.engine")>

com.anylogic.engine.ExtEntityContinuousDelegate<E>

Type Parameters:
:   `E` - type of agent extension to delegate to. If you are creating new extension based on 'Entity', please
    set the type to `ExtEntity`

All Implemented Interfaces:
:   `AgentExtension`, `ExtAgentContinuous`, `ExtAgentInteractive`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `ExtDefaultAnimationProvider`, `ExtEntity`, `ExtWithSpaceType`, `Serializable`

---

```
@Deprecated
@AnyLogicInternalAPI
public abstract class ExtEntityContinuousDelegate<E extends ExtEntity>
extends ExtAgentContinuousDelegate<ExtAgentContinuous>
implements ExtEntity
```

Deprecated.

Base class for extensions delegating their 'Entity' activity to an existing extension of agent

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExtEntityContinuousDelegate)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `final ExtEntity` | `ee` | Deprecated. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExtEntityContinuousDelegate(Agent owner)` | Deprecated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAgentToContents(Agent entity)` | Deprecated.  Adds a given agent to the contents of this agent. |
| `<T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distance)` | Deprecated.  Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `<T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distance, LengthUnits units)` | Deprecated.  Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `List<Agent>` | `contents()` | Deprecated. |
| `ShapeTopLevelPresentationGroup` | `createDefaultAnimation()` | Deprecated. |
| `FlowchartBlock` | `currentBlock()` | Deprecated.  Returns the current flowchart block this agent is being processed in. |
| `void` | `destroyEntity()` | Deprecated.  Destroys the agent. |
| `double` | `distanceTo(double x, double y)` | Deprecated.  Calculates the distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceTo(double x, double y, LengthUnits units)` | Deprecated.  Calculates the distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceTo(Agent other)` | Deprecated.  Calculates the distance from this agent to another one in continuous 3D space. |
| `double` | `distanceTo(Agent other, LengthUnits units)` | Deprecated.  Calculates the distance from this agent to another one.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceTo(Point point)` | Deprecated.  Calculates the distance from this agent to the point.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceTo(Point point, LengthUnits units)` | Deprecated.  Calculates the distance from this agent to the point.  *The exact behavior of this method depends on the underlying space type.* |
| `Position` | `getAnimationPosition(Position out)` | Deprecated.  ... |
| `double` | `getAnimationX()` | Deprecated. |
| `double` | `getAnimationY()` | Deprecated. |
| `double` | `getAnimationZ()` | Deprecated. |
| `double` | `getBlockEnterTime()` | Deprecated.  Returns the time this agent entered its current flowchart block. |
| `Color` | `getColor()` | Deprecated.  Returns the color of the item default shape. |
| `ShapeTopLevelPresentationGroup` | `getDefaultAnimation()` | Deprecated. |
| `double` | `getFlowchartEntryTime()` | Deprecated.  Returns the time the agent has entered the first block in the flowchart, or `Double.NaN` if this agent hasn't yet visited any flowchart |
| `double` | `getHeight()` | Deprecated.  Returns the height of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getHeight(LengthUnits units)` | Deprecated.  Returns the height of the agent - used by conveyors and other blocks which require it during processing. |
| `int` | `getId()` | Deprecated.  Returns Id of agent. |
| `double` | `getLength()` | Deprecated.  Returns the length of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getLength(LengthUnits units)` | Deprecated.  Returns the length of the agent - used by conveyors and other blocks which require it during processing. |
| `<T extends Agent> T` | `getNearestAgent(Iterable<T> agents)` | Deprecated.  Returns the nearest agent from the given collection |
| `INetwork` | `getNetwork()` | Deprecated.  Returns the network this agent lives in, actual for agents in continuous space. |
| `INode` | `getNetworkNode()` | Deprecated.  Returns the network node this agent currently is located in, actual for agents in continuous space. |
| `double` | `getPresentationScaleOnOwnerSpace()` | Deprecated.  Returns the scale of the agent presentation animation on its space or `1.0` if space isn't defined or agent list is empty |
| `Agent` | `getSpace()` | Deprecated.  Returns the agent representing space this agent lives in |
| `SpaceType` | `getSpaceType()` | Deprecated.  Returns the type of space this agent lives in, one of `SPACE_CONTINUOUS, SPACE_DISCRETE, SPACE_GIS, SPACE_NONE` |
| `double` | `getSpeed()` | Deprecated.  Returns the current value of the agent speed (measured in m/s). |
| `double` | `getSpeed(SpeedUnits units)` | Deprecated.  Returns the current value of the agent speed in continuous space. |
| `double` | `getTargetX()` | Deprecated.  Returns the x of the target location if moving, otherwise current x in continuous space. |
| `double` | `getTargetY()` | Deprecated.  Returns the y of the target location if moving, otherwise current y in continuous space. |
| `double` | `getVelocity()` | Deprecated.  Returns the current value of the agent speed in continuous space. |
| `double` | `getWidth()` | Deprecated.  Returns the width of the agent - used by conveyors and other blocks which require it during processing. |
| `double` | `getWidth(LengthUnits units)` | Deprecated.  Returns the width of the agent - used by conveyors and other blocks which require it during processing. |
| `void` | `highlight(boolean yes)` | Deprecated.  Turns on/off highlighting of this agent animation. |
| `boolean` | `isAnimationVisible_xjal()` | Deprecated. |
| `boolean` | `isAutomaticHorizontalRotation()` | Deprecated.  Returns `true` if agent is set to be rotated (in horizontal plane) during movement, `false` otherwise |
| `boolean` | `isMoving()` | Deprecated.  Tests if the agent is currently moving. |
| `void` | `jumpTo(double x, double y)` | Deprecated.  Instantly moves the agent to a given location (without changes to Z-coordinate, if any). |
| `void` | `jumpTo(INode node, Point location)` | Deprecated.  Instantly moves the agent to a given network location. |
| `void` | `jumpTo(Point location)` | Deprecated.  Instantly moves the agent to a given location. |
| `void` | `moveTo(double x, double y)` | Deprecated.  Starts movement in the direction of the given target location. |
| `void` | `moveTo(INode node, Point location)` | Deprecated.  Starts movement to the given network node.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Point location)` | Deprecated.  Starts movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location. |
| `void` | `moveToInTime(double x, double y, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location. |
| `void` | `moveToInTime(INode node, Point location, double tripTime)` | Deprecated.  Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, Point location, double tripTime, TimeUnits units)` | Deprecated.  Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents)` | Deprecated.  Starts movement to the nearest agent from the given collection. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents, double tripTime)` | Deprecated.  Starts movement to the nearest agent from the given collection. |
| `void` | `moveToStraight(Point location)` | Deprecated.  Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime)` | Deprecated.  Starts straight movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime, TimeUnits units)` | Deprecated.  Starts straight movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `boolean` | `onClick()` | Deprecated.  Should be overridden to define the reaction on mouse click. |
| `int` | `priority()` | Deprecated.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  This function is used for sorting extensions (in order for the overriding delegation to work) |
| `boolean` | `removeAgentFromContents(Agent entity)` | Deprecated.  Removes the given agent from the contents of this agent. |
| `Agent` | `resourceUnitOfPool(Agent pool)` | Deprecated.  Returns the first occurrence of resource unit of a given pool among the seized resource units, or `null` if not found. |
| `List<Agent>` | `resourceUnits()` | Deprecated.  Returns the list of resource units seized by the agent, or empty list if there are none. |
| `List<Agent>` | `resourceUnitsOfPool(Agent pool)` | Deprecated.  Returns resource units currently seized by this agent from the given `ResourcePool` block |
| `List<Agent>` | `resourceUnitsOfSeize(Agent seize)` | Deprecated.  Return resource units currently seized by this agent in the given `Seize` block |
| `void` | `setArrivalCallback(ArrivalCallback arrivalCallback)` | Deprecated.  This method is designed for advanced users and library developers, for general purpose arrival processing please use "On arrival" action which can be found on the properties of Agent Type.  Sets the listener which will be notified when the agent arrives (onArrival) or when the agent movement is cancelled or redirected (onCancel). |
| `void` | `setAutomaticHorizontalRotation(boolean yes)` | Deprecated.  Tells agent to rotate automatically (in horizontal plane) during movements. |
| `void` | `setColor(Color color)` | Deprecated.  Sets the color of the item default shape. |
| `void` | `setFlowchartActivityType(FlowchartActivityType activityType, FlowchartBlock block)` | Deprecated.  Sets activity type info (used in e.g. |
| `void` | `setHeight(double height)` | Deprecated.  Sets the height of the agent (in meters) |
| `void` | `setHeight(double height, LengthUnits units)` | Deprecated.  Sets the height of the agent in the given units |
| `void` | `setLength(double length)` | Deprecated.  Sets the length of the agent (in meters) |
| `void` | `setLength(double length, LengthUnits units)` | Deprecated.  Sets the length of the agent in the given units |
| `void` | `setNetwork(INetwork network)` | Deprecated.  Sets this agent to live in the network, actual for agents in continuous space. |
| `void` | `setNetworkInternal(INetwork network, INode node, Position location)` | Deprecated. |
| `void` | `setNetworkNode(INode node)` | Deprecated.  Sets the current network location for the agent |
| `void` | `setNetworkNode(INode node, Point position)` | Deprecated.  Sets the current network location for the agent |
| `void` | `setSpace(Agent space)` | Deprecated.  Sets the space for agent. |
| `void` | `setSpeed(double speedInMPS)` | Deprecated.  Changes speed of the agent (measured in m/s).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setSpeed(double s, SpeedUnits units)` | Deprecated.  Changes speed of the agent in continuous space (measured in the given units).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setVelocity(double v)` | Deprecated.  Changes speed of the agent in continuous space (measured in pixels per model-time-unit).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setWidth(double width)` | Deprecated.  Sets the width of the agent (in meters) |
| `void` | `setWidth(double width, LengthUnits units)` | Deprecated.  Sets the width of the agent in the given units |
| `void` | `stop()` | Deprecated.  Stops movement, if any. |
| `double` | `timeToArrival()` | Deprecated.  Returns the time to arrival to the target location in continuous space, in model-time units.  If the agent is not moving, returns 0. |
| `double` | `timeToArrival(TimeUnits units)` | Deprecated.  Returns the time to arrival to the target location, in time units.  If the agent is not moving, returns 0. |
| `void` | `updatePosition()` | Deprecated.  Updates agent coordinates |
