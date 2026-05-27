*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LinkToAgentImpl.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class LinkToAgentImpl<T extends Agent,A extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.LinkToAgentImpl<T,A>

All Implemented Interfaces:
:   `AbstractLinkToAgent<T,A>`, `AgentDestroyListener`, `LinkToAgent<T,A>`, `LinkToAgentAnimationSettings`, `Serializable`

---

```
public class LinkToAgentImpl<T extends Agent,A extends Agent>
extends Object
implements LinkToAgent<T,A>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.LinkToAgentImpl)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `LinkToAgentImpl(A owner, LinkToAgentAnimationSettings commonAnimationSettings)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `connectTo(T a)` | Creates a uni-directional connection between this agent and a given other agent. |
| `void` | `copyFrom_xjal(LinkToAgentAnimationSettings linkToAgentMyAnimationSettings)` |  |
| `void` | `deliver(Object msg)` |  |
| `boolean` | `disconnect()` | Disconnects this agent from another given agent. |
| `void` | `doConnect_xjal(T a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `doDisconnect_xjal(T a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `double` | `getArrowLocation()` |  |
| `LineArrowStyle` | `getArrowStyle()` |  |
| `AbstractLinkToAgent<A,T>` | `getBidirectionalPeer_xjal(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `T` | `getConnectedAgent()` | Returns connected agent |
| `Color` | `getLineColor()` |  |
| `LineStyle` | `getLineStyle()` |  |
| `double` | `getLineWidth()` |  |
| `LinkToAgentAnimationSettings` | `getLinkToAgentCommonAnimationSettings()` | Returns link animation settings shared by the all the agents having this link.  Changes to these settings apply to drawing of all links of this type |
| `LinkToAgentAnimationSettings` | `getLinkToAgentMyAnimationSettings()` | Returns link animation settings for this particular agent.  Changes to these settings apply to drawing of this link only inside its agent |
| `A` | `getOwner()` |  |
| `boolean` | `isConnected()` | Tests if this link is connected to some agent. |
| `boolean` | `isDeliverToAgent_xjal()` | Override this function for agent links which should call agent's "On Receive" code (which is defined in a standard 'connections' link). |
| `boolean` | `isVisible()` |  |
| `void` | `onDestroy()` | Discards the link and disconnects it if it is bidirectional. |
| `void` | `onDestroy(Agent agent)` |  |
| `void` | `onReceive(Object msg, Agent sender)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Override for custom on receive action |
| `void` | `send(Object msg)` | Sends a message to connected agent. |
| `void` | `setArrowLocation(double arrowLocation)` |  |
| `void` | `setArrowStyle(LineArrowStyle arrowStyle)` |  |
| `void` | `setLineColor(Color lineColor)` |  |
| `void` | `setLineStyle(LineStyle lineStyle)` |  |
| `void` | `setLineWidth(double lineWidth)` |  |
| `void` | `setVisible(boolean visible)` |  |
