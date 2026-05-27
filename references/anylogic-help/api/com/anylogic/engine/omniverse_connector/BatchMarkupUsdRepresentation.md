*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/BatchMarkupUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class BatchMarkupUsdRepresentation<T extends AbstractMarkup>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractInstancingUsdRepresentation](AbstractInstancingUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<T>

com.anylogic.engine.omniverse\_connector.BatchMarkupUsdRepresentation<T>

All Implemented Interfaces:
:   `InstancingUsdRepresentation<T>`, `UsdRepresentation<T>`

---

```
@AnyLogicInternalAPI
public class BatchMarkupUsdRepresentation<T extends AbstractMarkup>
extends AbstractInstancingUsdRepresentation<T>
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `BatchMarkupUsdRepresentation(UsdContext context, Iterable<T> collection, List<String> assetPath, String containerPath, String innerPath, String parentContainerPath, BiFunction<T,String,AbstractUsdRepresentation<T>> factory)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addAttrUpdater(String pathInsidePrim, String attrName, Function<T,Object> valueProvider)` | Adds an attribute updater for a prim depending on the element state |
| `void` | `addAttrUpdater(String name, Function<T,Object> valueProvider)` | Add binding to USD prim attribute |
| `void` | `addVariantUpdater(String pathInsidePrim, String varsetName, Function<T,Object> variantProvider)` | Adds a variant updater (a set of alternative configurations) for a prim |
| `void` | `addVariantUpdater(String name, Function<T,Object> valueProvider)` | Add binding to USD prim variant |
| `void` | `fillFrame(OmniFrame frame)` |  |
