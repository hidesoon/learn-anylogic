*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtEnvironmentInteractive.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtEnvironmentInteractive

All Superinterfaces:
:   `AgentExtension`, `Serializable`

All Known Subinterfaces:
:   `ExtEnvironmentContinuous`, `ExtEnvironmentDiscrete`, `ExtEnvironmentGIS`, `ExtEnvironmentWithLayout`, `ExtEnvironmentWithMetrics`

---

```
public interface ExtEnvironmentInteractive
extends AgentExtension
```

Extension interface for agent space with communication enabled.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default void` | `applyNetwork()` | Discards all existing connections and establishes new connection network according to the current network settings. |
| `void` | `applyNetwork(Random r)` | Discards all existing connections and establishes new connection network according to the current network settings, using the specified random number generator, if required by network type. |
| `boolean` | `areStepsEnabled()` | Tests if the time steps are enabled. |
| `void` | `deliverToAllAgentsInside(Object msg)` | Immediately delivers a message to all agents in the space. |
| `void` | `deliverToRandomAgentInside(Object msg)` | Immediately delivers a message to a random agent in the space, if there are any agents. |
| `void` | `disableSteps()` | Disables time steps. |
| `void` | `enableSteps(double stepDuration)` | Enables discrete time steps with a given duration. |
| `double` | `getNetworkConnectionsPerAgent()` | Returns the average (or exact) number of connections per agent. |
| `double` | `getNetworkNeighborLinkProbability()` | Returns the probability of an agent connection to be a neighbor. |
| `int` | `getNetworkScaleFreeM()` | Returns the M parameter of a scale free network. |
| `NetworkType` | `getNetworkType()` | Returns the network type. |
| `SpaceType` | `getSpaceType()` | Returns the space type of this space, one of `SPACE_CONTINUOUS, SPACE_DISCRETE, SPACE_GIS, SPACE_NONE` |
| `default Agent` | `randomAgentExcept(Agent agent)` | Returns a randomly chosen agent in the space except the given agent or `null` if there are no such agents |
| `Agent` | `randomAgentExcept(Random r, Agent agent)` | Returns a randomly chosen agent in the space except the given agent or `null` if there are no such agents. |
| `default Agent` | `randomAgentInside()` | Returns a randomly chosen agent in the space or `null` if there are no agents |
| `Agent` | `randomAgentInside(Random r)` | Returns a randomly chosen agent in the space or `null` if there are no agents. |
| `void` | `register_xjal(Agent a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `register_xjal(AgentList<?> population)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setNetworkRandom(double connectionsPerAgent)` | Sets network type to random with a given average number of connections per agent. |
| `void` | `setNetworkRingLattice(int connectionsPerAgent)` | Sets network type to ring lattice. |
| `void` | `setNetworkScaleFree(int m)` | Sets the network type to "scale free". |
| `void` | `setNetworkSmallWorld(int connectionsPerAgent, double neighborLinkProbability)` | Sets network type to "small world". |
| `void` | `setNetworkType_xjal(NetworkType networkType)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setNetworkUserDefined()` | Sets network type to user-defined. |
| `int` | `size()` | Returns the number of agents registered with this space. |
| `String` | `toStringNetwork_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `String` | `toStringSpace_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `unregister_xjal(Agent a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
