*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExtSpace.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Interface ExtSpace

All Superinterfaces:
:   `AgentExtension`, `Serializable`

---

```
public interface ExtSpace
extends AgentExtension
```

This extension:

* Tracks moving agents (either straight movement or through network or on the GIS map)
* Owns animator for agents created dynamically in flowcharts and for agents which jumped from their original space (implemented using replicated embedded object presentation shape)

## Nested Class Summary

| Modifier and Type | Interface | Description |
| --- | --- | --- |
| `static interface` | `ExtSpace.SpaceAgentIterable` |  |

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAgent(Agent a)` |  |
| `void` | `addMovingAgent(com.anylogic.engine.AgentMovement amd)` |  |
| `ExtSpace.SpaceAgentIterable` | `agents()` |  |
| `ShapeGISMap` | `getGISMap()` | In case of GIS space, returns [`ShapeGISMap`](presentation/ShapeGISMap.md "class in com.anylogic.engine.presentation") object |
| `void` | `removeAgent(Agent a)` |  |
| `boolean` | `removeMovingAgent(com.anylogic.engine.AgentMovement amd)` |  |
| `void` | `setupSpace(ShapeGISMap gisMap)` | Sets the space to be based on given `gisMap`. |
