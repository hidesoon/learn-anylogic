*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LinkToAgentCollection.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface LinkToAgentCollection<T extends Agent,A extends Agent>

All Superinterfaces:
:   `AbstractLinkToAgent<T,A>`, `Serializable`

All Known Implementing Classes:
:   `LinkToAgentCollectionImpl`, `LinkToAgentStandardImpl`

---

```
public interface LinkToAgentCollection<T extends Agent,A extends Agent>
extends AbstractLinkToAgent<T,A>
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `connectTo(T a)` | Creates a connection to a given other agent. |
| `void` | `deliver(Object msg, T dest)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `void` | `deliverToAllConnected(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `void` | `deliverToRandomConnected(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `default int` | `disconnectByCondition(Predicate<T> condition)` | Disconnects this agent from other agents which satisfy the given condition. |
| `boolean` | `disconnectFrom(Agent a)` | Disconnects this agent from another given agent. |
| `void` | `disconnectFromAll()` | Disconnects the agent from all other agents. |
| `T` | `getConnectedAgent(int index)` | Returns the connected agent with a given index. |
| `<E extends T> List<E>` | `getConnections()` | Returns a collection of agents connected to this agent (bi-directionally), or empty collection if there have not been any connections yet. |
| `int` | `getConnectionsNumber()` | Returns the number of agents connected to this agent. |
| `T` | `getRandomConnectedAgent()` | Returns the randomly chosen connected agent. |
| `boolean` | `isConnectedTo(Agent a)` | Tests if this agent is connected to a given other agent. |
| `void` | `send(Object msg, T dest)` | Sends a message to a given agent. |
| `void` | `sendToAllConnected(Object msg)` | Sends a message to all connected agents. |
| `void` | `sendToRandomConnected(Object msg)` | Sends a message to a randomly chosen connected agent. |
| `int` | `size()` | Returns the number of agents connected to this agent.  The same as [`getConnectionsNumber()`](#getConnectionsNumber()) |
