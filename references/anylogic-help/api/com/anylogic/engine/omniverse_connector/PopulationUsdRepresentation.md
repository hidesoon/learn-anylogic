*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/PopulationUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class PopulationUsdRepresentation<C extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractInstancingUsdRepresentation](AbstractInstancingUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<A>

[com.anylogic.engine.omniverse\_connector.CollectionUsdRepresentation](CollectionUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<C>

com.anylogic.engine.omniverse\_connector.PopulationUsdRepresentation<C>

Type Parameters:
:   `C` - agent class

All Implemented Interfaces:
:   `InstancingUsdRepresentation<C>`, `UsdRepresentation<C>`

---

```
public class PopulationUsdRepresentation<C extends Agent>
extends CollectionUsdRepresentation<C>
```

Associates a population or collections of agents with USD prims

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `PopulationUsdRepresentation(UsdContext context, C singleObject, String assetPath, String container)` |  |
| `PopulationUsdRepresentation(UsdContext context, Iterable<C> population, String assetPath, String containerPath)` |  |
| `PopulationUsdRepresentation(UsdContext context, Iterable<C> population, List<String> assetPath, String containerPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addPositionTransformator(Consumer<PositionAndScale> positionTransform)` | Sets the position transformation function that will be applied to the positions of the agent before applying to the connected USD prim. |
| `void` | `addVisibilityListener(Function<C,Shape> shapeProvider)` | Add default attribute updaters for visibility attribute |
| `void` | `setBasis(AbstractPositionWatcher.BasisType basis)` |  |
