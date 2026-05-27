*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/CachedGISSearch.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class CachedGISSearch

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.gis.ChainedGISSearch](ChainedGISSearch.md "class in com.anylogic.engine.gis")

com.anylogic.engine.gis.CachedGISSearch

All Implemented Interfaces:
:   `IGISSearch`

---

```
@AnyLogicInternalAPI
public class CachedGISSearch
extends ChainedGISSearch
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CachedGISSearch(IGISSearch underlyingSearch, Supplier<AnyLogicMapDB> dbSupplier, String cacheId, Consumer<StringBuilder> cacheKeyModifier)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `GISResult<List<GISMarkupDescriptor>>` | `get(String query, boolean region, boolean visibleAreaOnly, double bottomLatitude, double leftLongitude, double topLatitude, double rightLongitude, boolean firstOnly)` |  |
