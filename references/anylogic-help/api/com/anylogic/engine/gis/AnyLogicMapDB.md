*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/AnyLogicMapDB.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class AnyLogicMapDB

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.AnyLogicMapDB

---

```
@AnyLogicInternalAPI
public class AnyLogicMapDB
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `AnyLogicMapDB.DBFile` |  |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `CACHE_PATH_PROPERTY_NAME` |  |
| `static final String` | `DB_DIR` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AnyLogicMapDB(String cachePath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `MapDBCache<double[],double[]>` | `getRouteCache(String cacheId)` |  |
| `MapDBCache<String,List<GISMarkupDescriptor>>` | `getSearchCache(String cacheId)` |  |
| `MapDBCache<int[],byte[]>` | `getTileCache(String cacheId)` |  |
| `static AnyLogicMapDB` | `instance()` |  |
