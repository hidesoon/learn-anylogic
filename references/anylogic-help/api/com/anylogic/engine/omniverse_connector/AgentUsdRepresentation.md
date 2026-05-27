*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/AgentUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class AgentUsdRepresentation<A extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractUsdRepresentation](AbstractUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<A>

com.anylogic.engine.omniverse\_connector.AgentUsdRepresentation<A>

Type Parameters:
:   `A` - agent class

All Implemented Interfaces:
:   `UsdRepresentation<A>`

---

```
public class AgentUsdRepresentation<A extends Agent>
extends AbstractUsdRepresentation<A>
```

Associates a single agent with a prim

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AgentUsdRepresentation(UsdContext context, A agent, String usdOwnerPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `AgentUsdRepresentation<A>` | `addPositionTransformator(Consumer<PositionAndScale> positionTransform)` | Sets the position transformation function that will be applied to the positions of the agent before applying to the connected USD prim. |
