*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtAgentContinuous.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtAgentContinuous

All Superinterfaces:
:   `AgentExtension`, `ExtAgentInteractive`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `ExtWithSpaceType`, `Serializable`

All Known Implementing Classes:
:   `ExtAgentContinuousDelegate`, `ExtEntityContinuousDelegate`

---

```
public interface ExtAgentContinuous
extends ExtAgentInteractive, ExtAnimationParams, ExtAgentWithSpatialMetrics, ExtWithSpaceType
```

An extension of agent designed to support agent based modeling in continuous (3D) space, in particular:
- time (continuous or discrete)
- 3D continuous space
- connections between agents, networks (e.g. social) and their visualization
- communication - message passing and broadcasting

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `distanceTo(double x, double y)` | Calculates the distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceTo(double x, double y, double z)` | Calculates the distance from this agent to a given point in continuous 3D space. |
| `double` | `distanceTo(double x, double y, double z, LengthUnits units)` | Calculates the distance from this agent to a given point in continuous 3D space. |
| `double` | `distanceTo(Agent other)` | Calculates the distance from this agent to another one in continuous 3D space. |
| `double` | `distanceToSq(double x, double y)` | Calculates the square of distance from this agent to a given point in the projection to the horizontal plane (i.e. |
| `double` | `distanceToSq(double x, double y, double z)` | Calculates the square of distance from this agent to a given point in continuous 3D space.  *(this method has better performance compared to [`distanceTo(double, double, double)`](#distanceTo(double,double,double)))* |
| `double` | `distanceToSq(Agent other)` | Calculates the square of distance from this agent to another one in continuous space.  *(this method has better performance compared to [`distanceTo(Agent)`](#distanceTo(com.anylogic.engine.Agent)))* |
| `double` | `getSpeed(SpeedUnits units)` | Returns the current value of the agent speed in continuous space. |
| `double` | `getTargetX()` | Returns the x of the target location if moving, otherwise current x in continuous space. |
| `double` | `getTargetY()` | Returns the y of the target location if moving, otherwise current y in continuous space. |
| `double` | `getTargetZ()` | Returns the z of the target location if moving, otherwise current z in continuous space. |
| `double` | `getVelocity()` | Deprecated. this function is deprecated since AnyLogic 7.1. |
| `boolean` | `isAutomaticVerticalRotation()` | Returns `true` if agent is set to be rotated (in vertical direction, along Z-axis) during movement in 3D, `false` otherwise.  The returned value has no effect if [`ExtAgentWithSpatialMetrics.isAutomaticHorizontalRotation()`](ExtAgentWithSpatialMetrics.md#isAutomaticHorizontalRotation()) is `false` |
| `void` | `jumpTo(double x, double y, double z)` | Instantly moves the agent to a given location. |
| `void` | `moveTo(double x, double y, double z)` | Starts movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(double x, double y, double z, Path3D path)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveTo(double x, double y, Path2D path)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveTo(Attractor attractor)` | Starts movement to the given attractor.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Point location, Path3D path)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, double z, double tripTime)` | Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double z, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double z, Path3D path, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, double z, Path3D path, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, Path2D path, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, Path2D path, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(Attractor attractor, double tripTime)` | Starts movement to the given attractor.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Attractor attractor, double tripTime, TimeUnits units)` | Starts movement to the given attractor.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, Path3D path, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(Point location, Path3D path, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToStraight(double x, double y, double z)` | Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(double x, double y, double z, double tripTime)` | Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(double x, double y, double z, double tripTime, TimeUnits units)` | Starts straight movement in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `setAutomaticVerticalRotation(boolean yes)` | Tells agent to rotate automatically (in vertical direction, along Z-axis) during movements in 3D.  Has no effect if [`ExtAgentWithSpatialMetrics.isAutomaticHorizontalRotation()`](ExtAgentWithSpatialMetrics.md#isAutomaticHorizontalRotation()) is `false` |
| `void` | `setNetworkNode(Attractor attractor)` | Sets the current network location for the agent |
| `void` | `setSpeed(double s, SpeedUnits units)` | Changes speed of the agent in continuous space (measured in the given units).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setVelocity(double v)` | Deprecated. this function is deprecated since AnyLogic 7.1. |
| `void` | `stop()` | Stops movement, if any. |
| `double` | `timeToArrival()` | Returns the time to arrival to the target location in continuous space, in model-time units.  If the agent is not moving, returns 0. |
