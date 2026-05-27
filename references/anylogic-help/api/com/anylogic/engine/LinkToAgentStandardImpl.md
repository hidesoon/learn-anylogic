*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LinkToAgentStandardImpl.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class LinkToAgentStandardImpl<T extends Agent,A extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.LinkToAgentStandardImpl<T,A>

All Implemented Interfaces:
:   `AbstractLinkToAgent<T,A>`, `AgentDestroyListener`, `LinkToAgentAnimationSettings`, `LinkToAgentCollection<T,A>`, `Serializable`

---

```
public class LinkToAgentStandardImpl<T extends Agent,A extends Agent>
extends Object
implements LinkToAgentCollection<T,A>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.LinkToAgentStandardImpl)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `LinkToAgentStandardImpl(A owner, LinkToAgentAnimationSettings commonAnimationSettings)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `connectTo(T a)` | Creates a connection to a given other agent. |
| `void` | `copyFrom_xjal(LinkToAgentAnimationSettings linkToAgentMyAnimationSettings)` |  |
| `void` | `deliver(Object msg, T dest)` |  |
| `void` | `deliverToAllConnected(Object msg)` |  |
| `void` | `deliverToRandomConnected(Object msg)` |  |
| `boolean` | `disconnectFrom(Agent a)` | Disconnects this agent from another given agent. |
| `void` | `disconnectFromAll()` | Disconnects the agent from all other agents. |
| `void` | `doConnect_xjal(T a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `doDisconnect_xjal(T a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `double` | `getArrowLocation()` |  |
| `LineArrowStyle` | `getArrowStyle()` |  |
| `AbstractLinkToAgent<A,T>` | `getBidirectionalPeer_xjal(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `T` | `getConnectedAgent(int index)` | Returns the connected agent with a given index. |
| `List<T>` | `getConnections()` | Returns a collection of agents connected to this agent (bi-directionally), or empty collection if there have not been any connections yet. |
| `int` | `getConnectionsNumber()` | Returns the number of agents connected to this agent. |
| `Color` | `getLineColor()` |  |
| `LineStyle` | `getLineStyle()` |  |
| `double` | `getLineWidth()` |  |
| `LinkToAgentAnimationSettings` | `getLinkToAgentCommonAnimationSettings()` | Returns link animation settings shared by the all the agents having this link.  Changes to these settings apply to drawing of all links of this type |
| `LinkToAgentAnimationSettings` | `getLinkToAgentMyAnimationSettings()` | Returns link animation settings for this particular agent.  Changes to these settings apply to drawing of this link only inside its agent |
| `A` | `getOwner()` |  |
| `T` | `getRandomConnectedAgent()` | Returns the randomly chosen connected agent. |
| `boolean` | `isConnectedTo(Agent a)` | Tests if this agent is connected to a given other agent. |
| `boolean` | `isDeliverToAgent_xjal()` | Override this function for agent links which should call agent's "On Receive" code (which is defined in a standard 'connections' link). |
| `boolean` | `isVisible()` |  |
| `void` | `onDestroy()` | Discards the link and disconnects it if it is bidirectional. |
| `void` | `onDestroy(Agent agent)` |  |
| `void` | `onReceive(Object msg, Agent sender)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Override for custom on receive action |
| `void` | `send(Object msg, T dest)` | Sends a message to a given agent. |
| `void` | `sendToAllConnected(Object msg)` | Sends a message to all connected agents. |
| `void` | `sendToRandomConnected(Object msg)` | Sends a message to a randomly chosen connected agent. |
| `void` | `setArrowLocation(double arrowLocation)` |  |
| `void` | `setArrowStyle(LineArrowStyle arrowStyle)` |  |
| `void` | `setLineColor(Color lineColor)` |  |
| `void` | `setLineStyle(LineStyle lineStyle)` |  |
| `void` | `setLineWidth(double lineWidth)` |  |
| `void` | `setVisible(boolean visible)` |  |
| `int` | `size()` | Returns the number of agents connected to this agent.  The same as [`LinkToAgentCollection.getConnectionsNumber()`](LinkToAgentCollection.md#getConnectionsNumber()) |
