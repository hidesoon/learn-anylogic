*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/LRUCache.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class LRUCache<K,V>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.util.AbstractMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html "class or interface in java.util")<K,V>

[java.util.HashMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html "class or interface in java.util")<K,V>

[java.util.LinkedHashMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html "class or interface in java.util")<K,V>

com.anylogic.engine.LRUCache<K,V>

All Implemented Interfaces:
:   `Serializable`, `Cloneable`, `Map<K,V>`

---

```
@AnyLogicInternalAPI
public class LRUCache<K,V>
extends LinkedHashMap<K,V>
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.LRUCache)

## Nested Class Summary

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final boolean` | `DEFAULT_ACCESS_ORDER` |  |
| `static final int` | `DEFAULT_INITITAL_CAPACITY` |  |
| `static final float` | `DEFAULT_LOAD_FACTOR` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `LRUCache(int cacheSize)` | Constructs an empty `LRUCache` instance with the specified cache capacity. |
| `LRUCache(int cacheSize, float loadFactor, boolean accessOrder)` | Constructs an empty `LRUCache` instance with the specified cache capacity, load factor and ordering mode. |

## Method Summary
