*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/KeyValueTable.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class KeyValueTable<K,V>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.connectivity.ConnectivityBase](ConnectivityBase.md "class in com.anylogic.engine.connectivity")

[com.anylogic.engine.connectivity.DatabaseAccessor](DatabaseAccessor.md "class in com.anylogic.engine.connectivity")

com.anylogic.engine.connectivity.KeyValueTable<K,V>

All Implemented Interfaces:
:   `Serializable`

---

```
@Deprecated
public final class KeyValueTable<K,V>
extends DatabaseAccessor
```

Deprecated.

This class is deprecated and will be removed in future releases. Consider using [`Database`](Database.md "class in com.anylogic.engine.connectivity") API instead.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.KeyValueTable)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `KeyValueTable(String name, Database database, String tableName, String keyColumn, String valueColumn)` | Deprecated.  Creates [`KeyValueTable`](KeyValueTable.md "class in com.anylogic.engine.connectivity") based on the table with given `tableName` |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `containsKey(Object key)` | Deprecated.  Returns `true` if this [`KeyValueTable`](KeyValueTable.md "class in com.anylogic.engine.connectivity") contains a mapping for the specified key. |
| `boolean` | `containsValue(Object value)` | Deprecated.  Returns `true` if this [`KeyValueTable`](KeyValueTable.md "class in com.anylogic.engine.connectivity") maps one or more keys to the specified value. |
| `void` | `execute()` | Deprecated.  Loads (reloads) Key-Value mappings from database table  This method is automatically invoked if data is not loaded on first data-retrieving method call |
| `V` | `get(K key)` | Deprecated.  Returns the value to which the specified key is mapped, or `null` if this [`KeyValueTable`](KeyValueTable.md "class in com.anylogic.engine.connectivity") contains no mapping for the key. |
| `boolean` | `isEmpty()` | Deprecated.  Returns `true` if this [`KeyValueTable`](KeyValueTable.md "class in com.anylogic.engine.connectivity") contains no key-value mappings. |
| `Set<K>` | `keySet()` | Deprecated.  Returns a [`Set`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util") view of the keys contained in this table. |
| `int` | `size()` | Deprecated.  Returns the number of key-value mappings in this [`KeyValueTable`](KeyValueTable.md "class in com.anylogic.engine.connectivity"). |
| `Collection<V>` | `values()` | Deprecated.  Returns a [`Collection`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "class or interface in java.util") view of the values contained in this [`KeyValueTable`](KeyValueTable.md "class in com.anylogic.engine.connectivity"). |
