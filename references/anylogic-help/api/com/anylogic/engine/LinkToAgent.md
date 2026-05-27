*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LinkToAgent.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface LinkToAgent<T extends Agent,A extends Agent>

All Superinterfaces:
:   `AbstractLinkToAgent<T,A>`, `Serializable`

All Known Implementing Classes:
:   `LinkToAgentImpl`

---

```
public interface LinkToAgent<T extends Agent,A extends Agent>
extends AbstractLinkToAgent<T,A>
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `connectTo(T a)` | Creates a uni-directional connection between this agent and a given other agent. |
| `void` | `deliver(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `boolean` | `disconnect()` | Disconnects this agent from another given agent. |
| `T` | `getConnectedAgent()` | Returns connected agent |
| `boolean` | `isConnected()` | Tests if this link is connected to some agent. |
| `void` | `send(Object msg)` | Sends a message to connected agent. |
