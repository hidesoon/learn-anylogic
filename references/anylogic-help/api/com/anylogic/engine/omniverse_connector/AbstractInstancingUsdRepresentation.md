*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/AbstractInstancingUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class AbstractInstancingUsdRepresentation<A>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.omniverse\_connector.AbstractInstancingUsdRepresentation<A>

All Implemented Interfaces:
:   `InstancingUsdRepresentation<A>`, `UsdRepresentation<A>`

Direct Known Subclasses:
:   `BatchMarkupUsdRepresentation`, `CollectionUsdRepresentation`

---

```
@AnyLogicInternalCodegenAPI
public abstract class AbstractInstancingUsdRepresentation<A>
extends Object
implements InstancingUsdRepresentation<A>
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractInstancingUsdRepresentation(Iterable<A> collection, List<String> assetPath, String containerPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `addAttrUpdater(String name, Function<A,Object> valueProvider)` | Add binding to USD prim attribute |
| `abstract void` | `addVariantUpdater(String name, Function<A,Object> valueProvider)` | Add binding to USD prim variant |
| `void` | `disableCache()` |  |
| `abstract void` | `fillFrame(OmniFrame frame)` |  |
| `List<String>` | `getAssetPaths()` |  |
| `int` | `getCacheSize()` |  |
| `String` | `getContainerPath()` |  |
| `Iterable<A>` | `getObject()` |  |
| `boolean` | `isInstanceable()` | Return if USD prims will be instanceable |
| `void` | `setCacheSize(int cacheSize)` |  |
| `void` | `setInstanceable(boolean instanceable)` | Set if USD prims will be instanceable or not |
