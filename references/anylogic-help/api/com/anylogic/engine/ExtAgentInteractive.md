*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtAgentInteractive.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtAgentInteractive

All Superinterfaces:
:   `AgentExtension`, `Serializable`

All Known Subinterfaces:
:   `ExtAgentContinuous`, `ExtAgentDiscrete`, `ExtAgentGIS`

All Known Implementing Classes:
:   `ExtAgentContinuousDelegate`, `ExtEntityContinuousDelegate`

---

```
public interface ExtAgentInteractive
extends AgentExtension
```

An extension of [`Agent`](Agent.md "class in com.anylogic.engine") designed to support agent communication,
in particular:
- time (continuous or discrete)
- connections between agents, networks (e.g. social) and their visualisation
- communication - message passing and broadcasting
Also, there are several extension classes for different space types.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addConnection_xjal(Agent a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `String` | `agentInfo()` |  |
| `boolean` | `connectTo(Agent a)` | Creates a bi-directional connection between this agent and a given other agent. |
| `void` | `copyToAndDestroyOnSpaceTypeChange_xjal(ExtAgentInteractive newExt)` |  |
| `void` | `deliver(Object msg, Agent dest)` | Delivers a message to a given agent immediately during this method call. |
| `void` | `deliver(Object msg, MessageDeliveryType mode)` | Delivers a message to an agent or a group of agents, as specified by the mode parameter immediately during this method call. |
| `boolean` | `disconnectFrom(Agent a)` | Disconnects this agent from another given agent. |
| `void` | `disconnectFromAll()` | Disconnects the agent from all other agents. |
| `Agent` | `getConnectedAgent(int index)` | Returns the connected agent with a given index. |
| `<T extends Agent> List<T>` | `getConnections()` | Returns a collection of agents connected to this agent (bi-directionally), or empty collection if there have not been any connections yet. |
| `int` | `getConnectionsNumber()` | Returns the number of agents connected to this agent. |
| `Agent` | `getEnvironment()` | Returns the environment where this agent belongs to. |
| `Agent` | `getRandomConnectedAgent()` | Returns the randomly chosen connected agent. |
| `SpaceType` | `getSpaceType()` | Returns the type of space this agent lives in, one of `SPACE_CONTINUOUS, SPACE_DISCRETE, SPACE_GIS, SPACE_NONE` |
| `boolean` | `isConnectedTo(Agent a)` | Tests if this agent is connected to a given other agent. |
| `void` | `receive(Object msg)` | Immediately delivers a message to this agent. |
| `void` | `removeConnection_xjal(Agent a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `void` | `restoreConnections_xjal(List<?> connections)` | Deprecated. |
| `void` | `send(Object msg, Agent dest)` | Sends a message to a given agent. |
| `void` | `send(Object msg, MessageDeliveryType mode)` | Sends a message to an agent or a group of agents, as specified by the mode parameter. |
| `void` | `setEnvironment_xjal(Agent environment)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
