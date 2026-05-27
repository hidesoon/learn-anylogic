*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/MapDBCache.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class MapDBCache<K,V>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.MapDBCache<K,V>

All Implemented Interfaces:
:   `com.anylogic.engine.internal.gis.ICache<K,V>`

---

```
@AnyLogicInternalAPI
public class MapDBCache<K,V>
extends Object
implements com.anylogic.engine.internal.gis.ICache<K,V>
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `MapDBCache(org.mapdb.HTreeMap<K,V> map, boolean readOnly, com.anylogic.engine.gis.AnyLogicMapDB.DBChangeListener autoCommitter)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `V` | `get(K key)` |  |
| `void` | `put(K key, V value)` |  |
| `V` | `remove(K key)` |  |
