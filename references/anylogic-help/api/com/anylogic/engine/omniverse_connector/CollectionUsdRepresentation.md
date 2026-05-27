*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/CollectionUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class CollectionUsdRepresentation<A>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractInstancingUsdRepresentation](AbstractInstancingUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<A>

com.anylogic.engine.omniverse\_connector.CollectionUsdRepresentation<A>

All Implemented Interfaces:
:   `InstancingUsdRepresentation<A>`, `UsdRepresentation<A>`

Direct Known Subclasses:
:   `MarkupCollectionUsdRepresentation`, `PopulationUsdRepresentation`, `PositionalMarkupCollectionUsdRepresentation`, `ShapeCollectionUsdRepresentation`, `UsdElementCollectionUsdRepresentation`

---

```
@AnyLogicInternalAPI
public class CollectionUsdRepresentation<A>
extends AbstractInstancingUsdRepresentation<A>
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CollectionUsdRepresentation(UsdContext context, A singleObject, String assetPath, String containerPath)` |  |
| `CollectionUsdRepresentation(UsdContext context, Iterable<A> population, List<String> assetPath, String containerPath, Function<A,String> idProvider)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAttrUpdater(String pathInsidePrim, String attrName, Function<A,Object> valueProvider)` | Add binding to USD prim attribute |
| `void` | `addAttrUpdater(String attrName, Function<A,Object> valueProvider)` | Add binding to USD prim attribute |
| `void` | `addPositionUpdater(String primPath, Function<A,PositionAndScale> positionProvider)` | Add function to provide model element coordinates |
| `void` | `addPositionUpdater(String primPath, Function<A,PositionAndScale> positionProvider, Consumer<PositionAndScale> transformator)` |  |
| `void` | `addVariantUpdater(String pathInsidePrim, String varsetName, Function<A,Object> variantProvider)` | Add binding to USD prim variant |
| `void` | `addVariantUpdater(String varsetName, Function<A,Object> variantProvider)` | Add binding to USD prim variant |
| `void` | `fillFrame(OmniFrame frame)` |  |
| `OmniFrame.FrameInfo` | `generate(boolean fullFrame)` |  |
| `void` | `useReplicatedShapes(boolean useReplicatedShapes)` |  |
