*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AbstractLinkToAgent.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface AbstractLinkToAgent<T extends Agent,A extends Agent>

All Superinterfaces:
:   `Serializable`

All Known Subinterfaces:
:   `LinkToAgent<T,A>`, `LinkToAgentCollection<T,A>`

All Known Implementing Classes:
:   `LinkToAgentCollectionImpl`, `LinkToAgentImpl`, `LinkToAgentStandardImpl`

---

```
public interface AbstractLinkToAgent<T extends Agent,A extends Agent>
extends Serializable
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `doConnect_xjal(T a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `doDisconnect_xjal(T a)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `AbstractLinkToAgent<A,T>` | `getBidirectionalPeer_xjal(T agent)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `LinkToAgentAnimationSettings` | `getLinkToAgentCommonAnimationSettings()` | Returns link animation settings shared by the all the agents having this link.  Changes to these settings apply to drawing of all links of this type |
| `LinkToAgentAnimationSettings` | `getLinkToAgentMyAnimationSettings()` | Returns link animation settings for this particular agent.  Changes to these settings apply to drawing of this link only inside its agent |
| `A` | `getOwner()` |  |
| `boolean` | `isDeliverToAgent_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `onDestroy()` | Discards the link and disconnects it if it is bidirectional. |
| `void` | `onReceive(Object msg, Agent sender)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Override for custom on receive action |
