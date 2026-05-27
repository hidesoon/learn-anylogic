*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtAgentContinuousDelegate.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExtAgentContinuousDelegate<E extends ExtAgentContinuous>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.AgentExtensionImpl](AgentExtensionImpl.md "class in com.anylogic.engine")

com.anylogic.engine.ExtAgentContinuousDelegate<E>

Type Parameters:
:   `E` - type of agent extension to delegate to. If you are creating new extension based on 'continuous space agent',
    please set the type to `ExtAgentContinuous`

All Implemented Interfaces:
:   `AgentExtension`, `ExtAgentContinuous`, `ExtAgentInteractive`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `ExtWithSpaceType`, `Serializable`

Direct Known Subclasses:
:   `ExtEntityContinuousDelegate`

---

```
@Deprecated
@AnyLogicInternalAPI
public abstract class ExtAgentContinuousDelegate<E extends ExtAgentContinuous>
extends AgentExtensionImpl
implements ExtAgentContinuous
```

Deprecated.

Base class for extensions delegating their 'continuous space agent' activity to an existing extension of agent

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExtAgentContinuousDelegate)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `final E` | `e` | Deprecated. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExtAgentContinuousDelegate(Agent owner, Class<E> extClass)` | Deprecated. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection_xjal(Agent a)` | Deprecated.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `String` | `agentInfo()` | Deprecated. |
| `<T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distance)` | Deprecated.  Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `<T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distance, LengthUnits units)` | Deprecated.  Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `boolean` | `connectTo(Agent a)` | Deprecated.  Creates a bi-directional connection between this agent and a given other agent. |
| `void` | `copyToAndDestroyOnSpaceTypeChange_xjal(ExtAgentInteractive newExt)` | Deprecated. |
| `void` | `deliver(Object msg, Agent dest)` | Deprecated.  Delivers a message to a given agent immediately during this method call. |
| `void` | `deliver(Object msg, MessageDeliveryType mode)` | Deprecated.  Delivers a message to an agent or a group of agents, as specified by the mode parameter immediately during this method call. |
| `boolean` | `disconnectFrom(Agent a)` | Deprecated.  Disconnects this agent from another given agent. |
| `void` | `disconnectFromAll()` | Deprecated.  Disconnects the agent from all other agents. |
| `double` | `distanceTo(double x, double y)` | Deprecated.  Calculates the distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceTo(double x, double y, double z)` | Deprecated.  Calculates the distance from this agent to a given point in continuous 3D space. |
| `double` | `distanceTo(double x, double y, double z, LengthUnits units)` | Deprecated.  Calculates the distance from this agent to a given point in continuous 3D space. |
| `double` | `distanceTo(double x, double y, LengthUnits units)` | Deprecated.  Calculates the distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceTo(Agent other)` | Deprecated.  Calculates the distance from this agent to another one in continuous 3D space. |
| `double` | `distanceTo(Agent other, LengthUnits units)` | Deprecated.  Calculates the distance from this agent to another one.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceTo(Point point)` | Deprecated.  Calculates the distance from this agent to the point.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceTo(Point point, LengthUnits units)` | Deprecated.  Calculates the distance from this agent to the point.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceToSq(double x, double y)` | Deprecated.  Calculates the square of distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceToSq(double x, double y, double z)` | Deprecated.  Calculates the square of distance from this agent to a given point in continuous 3D space.  *(this method has better performance compared to [`ExtAgentContinuous.distanceTo(double, double, double)`](ExtAgentContinuous.md#distanceTo(double,double,double)))* |
| `double` | `distanceToSq(Agent other)` | Deprecated.  Calculates the square of distance from this agent to another one in continuous space.  *(this method has better performance compared to [`ExtAgentContinuous.distanceTo(Agent)`](ExtAgentContinuous.md#distanceTo(com.anylogic.engine.Agent)))* |
| `Position` | `getAnimationPosition(Position out)` | Deprecated.  ... |
| `double` | `getAnimationX()` | Deprecated. |
| `double` | `getAnimationY()` | Deprecated. |
| `double` | `getAnimationZ()` | Deprecated. |
| `Agent` | `getConnectedAgent(int index)` | Deprecated.  Returns the connected agent with a given index. |
| `<T extends Agent> List<T>` | `getConnections()` | Deprecated.  Returns a collection of agents connected to this agent (bi-directionally), or empty collection if there have not been any connections yet. |
| `int` | `getConnectionsNumber()` | Deprecated.  Returns the number of agents connected to this agent. |
| `Agent` | `getEnvironment()` | Deprecated.  Returns the environment where this agent belongs to. |
| `Level` | `getLevel()` | Deprecated.  Returns the level this agent lives in, actual for agents in continuous space. |
| `<T extends Agent> T` | `getNearestAgent(Iterable<T> agents)` | Deprecated.  Returns the nearest agent from the given collection |
| `INetwork` | `getNetwork()` | Deprecated.  Returns the network this agent lives in, actual for agents in continuous space. |
| `INode` | `getNetworkNode()` | Deprecated.  Returns the network node this agent currently is located in, actual for agents in continuous space. |
| `double` | `getPresentationScaleOnOwnerSpace()` | Deprecated.  Returns the scale of the agent presentation animation on its space or `1.0` if space isn't defined or agent list is empty |
| `Agent` | `getRandomConnectedAgent()` | Deprecated.  Returns the randomly chosen connected agent. |
| `IRouteProvider` | `getRouteProvider()` | Deprecated.  Returns the provider of routes for agent movement |
| `Agent` | `getSpace()` | Deprecated.  Returns the agent representing space this agent lives in |
| `SpaceType` | `getSpaceType()` | Deprecated.  Returns the type of space this agent lives in, one of `SPACE_CONTINUOUS, SPACE_DISCRETE, SPACE_GIS, SPACE_NONE` |
| `double` | `getSpeed()` | Deprecated.  Returns the current value of the agent speed (measured in m/s). |
| `double` | `getSpeed(SpeedUnits units)` | Deprecated.  Returns the current value of the agent speed in continuous space. |
| `double` | `getTargetX()` | Deprecated.  Returns the x of the target location if moving, otherwise current x in continuous space. |
| `double` | `getTargetY()` | Deprecated.  Returns the y of the target location if moving, otherwise current y in continuous space. |
| `double` | `getTargetZ()` | Deprecated.  Returns the z of the target location if moving, otherwise current z in continuous space. |
| `double` | `getVelocity()` | Deprecated. |
| `boolean` | `isAnimationVisible_xjal()` | Deprecated. |
| `boolean` | `isAutomaticHorizontalRotation()` | Deprecated.  Returns `true` if agent is set to be rotated (in horizontal plane) during movement, `false` otherwise |
| `boolean` | `isAutomaticVerticalRotation()` | Deprecated.  Returns `true` if agent is set to be rotated (in vertical direction, along Z-axis) during movement in 3D, `false` otherwise.  The returned value has no effect if [`ExtAgentWithSpatialMetrics.isAutomaticHorizontalRotation()`](ExtAgentWithSpatialMetrics.md#isAutomaticHorizontalRotation()) is `false` |
| `boolean` | `isConnectedTo(Agent a)` | Deprecated.  Tests if this agent is connected to a given other agent. |
| `boolean` | `isMoving()` | Deprecated.  Tests if the agent is currently moving. |
| `void` | `jumpTo(double x, double y)` | Deprecated.  Instantly moves the agent to a given location (without changes to Z-coordinate, if any). |
| `void` | `jumpTo(double x, double y, double z)` | Deprecated.  Instantly moves the agent to a given location. |
| `void` | `jumpTo(INode node, Point location)` | Deprecated.  Instantly moves the agent to a given network location. |
| `void` | `jumpTo(Point location)` | Deprecated.  Instantly moves the agent to a given location. |
| `void` | `moveTo(double x, double y)` | Deprecated.  Starts movement in the direction of the given target location. |
| `void` | `moveTo(double x, double y, double z)` | Deprecated.  Starts movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(double x, double y, double z, Path3D path)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveTo(double x, double y, Path2D path)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveTo(Attractor attractor)` | Deprecated.  Starts movement to the given attractor.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(INode node, Point location)` | Deprecated.  Starts movement to the given network node.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Point location)` | Deprecated.  Starts movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Point location, Path3D path)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location. |
| `void` | `moveToInTime(double x, double y, double z, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double z, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double z, Path3D path, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, double z, Path3D path, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location. |
| `void` | `moveToInTime(double x, double y, Path2D path, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, Path2D path, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(Attractor attractor, double tripTime)` | Deprecated.  Starts movement to the given attractor.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Attractor attractor, double tripTime, TimeUnits units)` | Deprecated.  Starts movement to the given attractor.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, Point location, double tripTime)` | Deprecated.  Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, Point location, double tripTime, TimeUnits units)` | Deprecated.  Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, Path3D path, double tripTime)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(Point location, Path3D path, double tripTime, TimeUnits units)` | Deprecated.  Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents)` | Deprecated.  Starts movement to the nearest agent from the given collection. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents, double tripTime)` | Deprecated.  Starts movement to the nearest agent from the given collection. |
| `void` | `moveToStraight(double x, double y, double z)` | Deprecated.  Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraight(Point location)` | Deprecated.  Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(double x, double y, double z, double tripTime)` | Deprecated.  Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(double x, double y, double z, double tripTime, TimeUnits units)` | Deprecated.  Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime)` | Deprecated.  Starts straight movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime, TimeUnits units)` | Deprecated.  Starts straight movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `int` | `priority()` | Deprecated.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  This function is used for sorting extensions (in order for the overriding delegation to work) |
| `void` | `receive(Object msg)` | Deprecated.  Immediately delivers a message to this agent. |
| `void` | `removeConnection_xjal(Agent a)` | Deprecated.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `void` | `restoreConnections_xjal(List<?> connections)` | Deprecated.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `void` | `send(Object msg, Agent dest)` | Deprecated.  Sends a message to a given agent. |
| `void` | `send(Object msg, MessageDeliveryType mode)` | Deprecated.  Sends a message to an agent or a group of agents, as specified by the mode parameter. |
| `void` | `setArrivalCallback(ArrivalCallback arrivalCallback)` | Deprecated.  This method is designed for advanced users and library developers, for general purpose arrival processing please use "On arrival" action which can be found on the properties of Agent Type.  Sets the listener which will be notified when the agent arrives (onArrival) or when the agent movement is cancelled or redirected (onCancel). |
| `void` | `setAutomaticHorizontalRotation(boolean yes)` | Deprecated.  Tells agent to rotate automatically (in horizontal plane) during movements. |
| `void` | `setAutomaticVerticalRotation(boolean yes)` | Deprecated.  Tells agent to rotate automatically (in vertical direction, along Z-axis) during movements in 3D.  Has no effect if [`ExtAgentWithSpatialMetrics.isAutomaticHorizontalRotation()`](ExtAgentWithSpatialMetrics.md#isAutomaticHorizontalRotation()) is `false` |
| `void` | `setEnvironment_xjal(Agent environment)` | Deprecated.  **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `void` | `setLevel(Level level)` | Deprecated.  Sets this agent to live in the level, actual for agents in continuous space. |
| `void` | `setNetwork(INetwork network)` | Deprecated.  Sets this agent to live in the network, actual for agents in continuous space. |
| `void` | `setNetworkInternal(INetwork network, INode node, Position location)` | Deprecated. |
| `void` | `setNetworkNode(Attractor attractor)` | Deprecated.  Sets the current network location for the agent |
| `void` | `setNetworkNode(INode node)` | Deprecated.  Sets the current network location for the agent |
| `void` | `setNetworkNode(INode node, Point position)` | Deprecated.  Sets the current network location for the agent |
| `void` | `setRouteProvider(IRouteProvider routeProvider)` | Deprecated.  Stops agent If it is moving. |
| `void` | `setSpace(Agent space)` | Deprecated.  Sets the space for agent. |
| `void` | `setSpeed(double s)` | Deprecated.  Changes speed of the agent (measured in m/s).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setSpeed(double s, SpeedUnits units)` | Deprecated.  Changes speed of the agent in continuous space (measured in the given units).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setVelocity(double v)` | Deprecated. |
| `void` | `stop()` | Deprecated.  Stops movement, if any. |
| `double` | `timeToArrival()` | Deprecated.  Returns the time to arrival to the target location in continuous space, in model-time units.  If the agent is not moving, returns 0. |
| `double` | `timeToArrival(TimeUnits units)` | Deprecated.  Returns the time to arrival to the target location, in time units.  If the agent is not moving, returns 0. |
| `void` | `updatePosition()` | Deprecated.  Updates agent coordinates |
