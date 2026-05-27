*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtAgentWithSpatialMetricsDelegate.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExtAgentWithSpatialMetricsDelegate<E extends ExtAgentWithSpatialMetrics>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.AgentExtensionImpl](AgentExtensionImpl.md "class in com.anylogic.engine")

com.anylogic.engine.ExtAgentWithSpatialMetricsDelegate<E>

Type Parameters:
:   `E` - type of agent extension to delegate to. If you are creating new extension based on 'continuous or GIS space agent',
    please set the type to `ExtAgentWithSpatialMetrics`

All Implemented Interfaces:
:   `AgentExtension`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `Serializable`

Direct Known Subclasses:
:   `ExtEntityDelegate`

---

```
@AnyLogicInternalAPI
public abstract class ExtAgentWithSpatialMetricsDelegate<E extends ExtAgentWithSpatialMetrics>
extends AgentExtensionImpl
implements ExtAgentWithSpatialMetrics
```

Base class for extensions delegating their 'Continuous / GIS space agent' activity to an existing extension of agent

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExtAgentWithSpatialMetricsDelegate)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExtAgentWithSpatialMetricsDelegate(Agent owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `<T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distance)` | Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `<T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distance, LengthUnits units)` | Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `double` | `distanceTo(double x, double y)` | Calculates the distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceTo(double x, double y, LengthUnits units)` | Calculates the distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceTo(Agent other)` | Calculates the distance from this agent to another one.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceTo(Agent other, LengthUnits units)` | Calculates the distance from this agent to another one.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceTo(Point point)` | Calculates the distance from this agent to the point.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `distanceTo(Point point, LengthUnits units)` | Calculates the distance from this agent to the point.  *The exact behavior of this method depends on the underlying space type.* |
| `final E` | `e()` |  |
| `abstract Class<E>` | `extClass()` |  |
| `Position` | `getAnimationPosition(Position out)` | ... |
| `double` | `getAnimationX()` |  |
| `double` | `getAnimationY()` |  |
| `double` | `getAnimationZ()` |  |
| `Level` | `getLevel()` | Returns the level this agent lives in, actual for agents in continuous space. |
| `<T extends Agent> T` | `getNearestAgent(Iterable<T> agents)` | Returns the nearest agent from the given collection |
| `INetwork` | `getNetwork()` | Returns the network this agent lives in, actual for agents in continuous space. |
| `INode` | `getNetworkNode()` | Returns the network node this agent currently is located in, actual for agents in continuous space. |
| `double` | `getPresentationScaleOnOwnerSpace()` | Returns the scale of the agent presentation animation on its space or `1.0` if space isn't defined or agent list is empty |
| `IRouteProvider` | `getRouteProvider()` | Returns the provider of routes for agent movement |
| `Agent` | `getSpace()` | Returns the agent representing space this agent lives in |
| `SpaceType` | `getSpaceType()` | Returns the type of space this agent lives in, one of `SPACE_CONTINUOUS, SPACE_GIS` |
| `double` | `getSpeed()` | Returns the current value of the agent speed (measured in m/s). |
| `double` | `getSpeed(SpeedUnits units)` | Returns the current value of the agent speed. |
| `double` | `getTargetX()` | Returns the x of the target location if moving, otherwise current x.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `getTargetY()` | Returns the y of the target location if moving, otherwise current y.  *The exact behavior of this method depends on the underlying space type.* |
| `double` | `getVelocity()` | Deprecated. |
| `boolean` | `isAnimationVisible_xjal()` |  |
| `boolean` | `isAutomaticHorizontalRotation()` | Returns `true` if agent is set to be rotated (in horizontal plane) during movement, `false` otherwise |
| `boolean` | `isAutomaticVerticalRotation()` | This functions is valid only for specific set of spaces |
| `boolean` | `isMoving()` | Tests if the agent is currently moving. |
| `void` | `jumpTo(double x, double y)` | Instantly moves the agent to a given location (without changes to Z-coordinate, if any). |
| `void` | `jumpTo(INode node, Point location)` | Instantly moves the agent to a given network location. |
| `void` | `jumpTo(Point location)` | Instantly moves the agent to a given location. |
| `void` | `moveTo(double x, double y)` | Starts movement in the direction of the given target location. |
| `void` | `moveTo(INode node, Point location)` | Starts movement to the given network node.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Point location)` | Starts movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double tripTime)` | Starts movement in the direction of the given target location. |
| `void` | `moveToInTime(double x, double y, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location. |
| `void` | `moveToInTime(INode node, Point location, double tripTime)` | Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, Point location, double tripTime, TimeUnits units)` | Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime)` | Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents)` | Starts movement to the nearest agent from the given collection. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents, double tripTime)` | Starts movement to the nearest agent from the given collection. |
| `void` | `moveToStraight(Point location)` | Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime)` | Starts straight movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime, TimeUnits units)` | Starts straight movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `onExtensionRemoved(AgentExtension ext)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Default implementation does nothing |
| `int` | `priority()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  This function is used for sorting extensions (in order for the overriding delegation to work) |
| `void` | `setArrivalCallback(ArrivalCallback arrivalCallback)` | This method is designed for advanced users and library developers, for general purpose arrival processing please use "On arrival" action which can be found on the properties of Agent Type.  Sets the listener which will be notified when the agent arrives (onArrival) or when the agent movement is cancelled or redirected (onCancel). |
| `void` | `setAutomaticHorizontalRotation(boolean yes)` | Tells agent to rotate automatically (in horizontal plane) during movements. |
| `void` | `setLevel(Level level)` | Sets this agent to live in the level, actual for agents in continuous space. |
| `void` | `setNetwork(INetwork network)` | Sets this agent to live in the network, actual for agents in continuous space. |
| `void` | `setNetworkInternal(INetwork network, INode node, Position location)` |  |
| `void` | `setNetworkNode(INode node)` | Sets the current network location for the agent |
| `void` | `setNetworkNode(INode node, Point position)` | Sets the current network location for the agent |
| `void` | `setRouteProvider(IRouteProvider routeProvider)` | Stops agent If it is moving. |
| `void` | `setSpace(Agent space)` | Sets the space for agent. |
| `void` | `setSpeed(double speedInMPS)` | Changes speed of the agent (measured in m/s).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setSpeed(double s, SpeedUnits units)` | Changes speed of the agent (the units of the value depend on the specific space type).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setVelocity(double v)` | Deprecated. |
| `void` | `stop()` | Stops movement, if any. |
| `double` | `timeToArrival()` | Returns the time to arrival to the target location, in model-time units.  If the agent is not moving, returns 0. |
| `double` | `timeToArrival(TimeUnits units)` | Returns the time to arrival to the target location, in time units.  If the agent is not moving, returns 0. |
| `void` | `updatePosition()` | Updates agent coordinates |
