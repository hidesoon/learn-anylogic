*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/AbstractUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class AbstractUsdRepresentation<A>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.omniverse\_connector.AbstractUsdRepresentation<A>

All Implemented Interfaces:
:   `UsdRepresentation<A>`

Direct Known Subclasses:
:   `AgentUsdRepresentation`, `CameraUsdRepresentation`, `ElevatorUsdRepresentation`, `JibCraneUsdRepresentation`, `LiftUsdRepresentation`, `OverheadCraneUsdRepresentation`, `PositionalMarkupUsdRepresentation`, `ShapeUsdRepresentation`

---

```
@AnyLogicInternalAPI
public class AbstractUsdRepresentation<A>
extends Object
implements UsdRepresentation<A>
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `USD_ATTR_VISIBILITY` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractUsdRepresentation(UsdContext context, A objectToWatch, String usdPrimPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAttrUpdater(com.anylogic.engine.omniverse_connector.FieldProvider<A> provider)` |  |
| `void` | `addAttrUpdater(String internalPrimPath, String attributeName, Function<A,Object> valueProvider)` | Add binding to USD prim attribute |
| `void` | `addAttrUpdater(String attributeName, Function<A,Object> valueProvider)` | Add binding to USD prim attribute |
| `void` | `addPositionUpdater(String primPath, Function<A,PositionAndScale> positionProvider, Consumer<PositionAndScale> transformator)` |  |
| `void` | `addPositionUpdater(String primPath, Function<A,PositionAndScale> positionProvider, Consumer<PositionAndScale> transformator, AbstractPositionWatcher.BasisType basis)` |  |
| `void` | `addPositionUpdater(Function<A,PositionAndScale> positionProvider)` | Add function to provide model element coordinates |
| `void` | `addVariantUpdater(boolean absolutePath, String primPath, String varsetName, Function<A,Object> variantProvider)` |  |
| `void` | `addVariantUpdater(String internalPrimPath, String varsetName, Function<A,Object> variantProvider)` | Add binding to USD prim variant |
| `void` | `addVariantUpdater(String varsetName, Function<A,Object> variantProvider)` | Add binding to USD prim variant |
| `void` | `addVisibilityListener()` | Add default attribute updaters for visibility attribute |
| `void` | `fillFrame(OmniFrame frame)` |  |
| `A` | `getObject()` |  |
