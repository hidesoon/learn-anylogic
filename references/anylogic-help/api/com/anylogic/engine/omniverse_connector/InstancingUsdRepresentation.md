*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/InstancingUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Interface InstancingUsdRepresentation<T>

All Superinterfaces:
:   `UsdRepresentation<T>`

All Known Implementing Classes:
:   `AbstractInstancingUsdRepresentation`, `BatchMarkupUsdRepresentation`, `CollectionUsdRepresentation`, `MarkupCollectionUsdRepresentation`, `PopulationUsdRepresentation`, `PositionalMarkupCollectionUsdRepresentation`, `Shape3DObjectCollectionUsdRepresentation`, `ShapeCollectionUsdRepresentation`, `UsdElementCollectionUsdRepresentation`

---

```
@AnyLogicInternalCodegenAPI
public interface InstancingUsdRepresentation<T>
extends UsdRepresentation<T>
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAttrUpdater(String name, Function<T,Object> valueProvider)` | Add binding to USD prim attribute |
| `void` | `addVariantUpdater(String name, Function<T,Object> valueProvider)` | Add binding to USD prim variant |
| `void` | `disableCache()` |  |
| `List<String>` | `getAssetPaths()` |  |
| `int` | `getCacheSize()` |  |
| `String` | `getContainerPath()` |  |
| `boolean` | `isInstanceable()` |  |
| `void` | `setCacheSize(int cacheSize)` |  |
| `void` | `setInstanceable(boolean instanceable)` |  |
