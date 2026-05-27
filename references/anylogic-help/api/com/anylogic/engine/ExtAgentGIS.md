*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtAgentGIS.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtAgentGIS

All Superinterfaces:
:   `AgentExtension`, `ExtAgentInteractive`, `ExtAgentWithSpatialMetrics`, `ExtAnimationParams`, `ExtWithSpaceType`, `Serializable`

---

```
public interface ExtAgentGIS
extends ExtAgentInteractive, ExtAnimationParams, ExtAgentWithSpatialMetrics, ExtWithSpaceType
```

An extension of Agent designed to support agent based modeling in continuous GIS space, in particular:
- time (continuous or discrete)
- continuous 2D space based on GIS map
- connections between agents, networks (e.g. social) and their visualization
- communication - message passing and broadcasting

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double` | `distanceByRoute(Agent agent)` | Calculates the distance from this agent to another one by route.  In case of GIS space returns distance measured in meters |
| `double` | `distanceTo(double x, double y)` | Calculates the distance from this GIS agent to a given point (latitude, longitude) in continuous GIS space, measured in meters. |
| `double` | `distanceTo(Agent other)` | Calculates the distance from this agent to another one in GIS space.  In case of GIS space returns distance measured in meters |
| `double` | `getGISHeading()` | Returns current heading angle (measured in radians CW, starting from North direction) of agent moving in continuous GIS space. |
| `ShapeGISMap` | `getGISMap()` | Returns the GIS map the agent is moving on. |
| `double` | `getLat()` | Returns the current (up-to-date) latitude of the agent in continuous GIS space. |
| `double` | `getLon()` | Returns the current (up-to-date) longitude of the agent in continuous GIS space. |
| `<T extends Agent> T` | `getNearestAgentByRoute(Iterable<T> agents)` | Returns the nearest agent from the given collection. |
| `double` | `getTargetLat()` | Returns the latitude of the target location if moving, otherwise current latitude in GIS space, measured in degrees (-90 ... |
| `double` | `getTargetLon()` | Returns the longitude of the target location if moving, otherwise current longitude in GIS space, measured in degrees (-180 ... |
| `double` | `getTargetX()` | Returns the latitude of the target location if moving, otherwise current latitude in GIS space, measured in degrees (-90 ... |
| `double` | `getTargetY()` | Returns the longitude of the target location if moving, otherwise current longitude in GIS space, measured in degrees (-180 ... |
| `double` | `getVelocity()` | Deprecated. |
| `boolean` | `isAnimationVisible_xjal()` |  |
| `void` | `jumpTo(double x, double y)` | Instantly moves the agent to a given location in GIS space. |
| `void` | `jumpTo(String geographicPlace)` | Finds first geographic point on the Earth and calls method jumpTo(latitude, longitude) with coordinates of the found point |
| `void` | `moveTo(double x, double y)` | Starts movement in the direction of the given target location in continuous GIS space.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(String geographicPlace)` | Finds first geographic point on the Earth and calls method moveTo(latitude, longitude) with coordinates of the found point |
| `void` | `setVelocity(double v)` | Deprecated. |
