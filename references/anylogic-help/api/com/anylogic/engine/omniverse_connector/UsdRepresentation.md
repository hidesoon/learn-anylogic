*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/UsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Interface UsdRepresentation<T>

Type Parameters:
:   `T` - type of element of the model (an agent, a shape, and so on)

All Known Subinterfaces:
:   `InstancingUsdRepresentation<T>`

All Known Implementing Classes:
:   `AbstractInstancingUsdRepresentation`, `AbstractUsdRepresentation`, `AgentUsdRepresentation`, `BatchMarkupUsdRepresentation`, `CameraUsdRepresentation`, `CollectionUsdRepresentation`, `ElevatorUsdRepresentation`, `JibCraneUsdRepresentation`, `LiftUsdRepresentation`, `MarkupCollectionUsdRepresentation`, `OverheadCraneUsdRepresentation`, `PopulationUsdRepresentation`, `PositionalMarkupCollectionUsdRepresentation`, `PositionalMarkupUsdRepresentation`, `Shape3DObjectCollectionUsdRepresentation`, `ShapeCollectionUsdRepresentation`, `ShapeUsdRepresentation`, `UsdElementCollectionUsdRepresentation`

---

```
public interface UsdRepresentation<T>
```

Base interface for object represents the connection between the AnyLogic element and its USD prim

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAttrUpdater(String pathInsidePrim, String attrName, Function<T,Object> valueProvider)` | Adds an attribute updater for a prim depending on the element state |
| `void` | `addAttrUpdater(String name, Function<T,Object> valueProvider)` | Adds an attribute updater for a prim depending on the element state |
| `void` | `addVariantUpdater(String pathInsidePrim, String varsetName, Function<T,Object> variantProvider)` | Adds a variant updater (a set of alternative configurations) for a prim |
| `void` | `addVariantUpdater(String name, Function<T,Object> valueProvider)` | Adds a variant updater (a set of alternative configurations) for a prim |
| `void` | `fillFrame(OmniFrame frame)` |  |
| `Object` | `getObject()` |  |
