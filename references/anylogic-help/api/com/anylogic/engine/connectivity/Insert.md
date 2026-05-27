*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/Insert.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class Insert

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.connectivity.ConnectivityBase](ConnectivityBase.md "class in com.anylogic.engine.connectivity")

[com.anylogic.engine.connectivity.DatabaseAccessor](DatabaseAccessor.md "class in com.anylogic.engine.connectivity")

com.anylogic.engine.connectivity.Insert

All Implemented Interfaces:
:   `Serializable`

---

```
@Deprecated
public abstract class Insert
extends DatabaseAccessor
```

Deprecated.

This class is deprecated and will be removed in future releases. Consider using [`Database`](Database.md "class in com.anylogic.engine.connectivity") API instead.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.Insert)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Insert(String name, Database database, String tableName, String[] columnNames)` | Deprecated.  Creates new [`Insert`](Insert.md "class in com.anylogic.engine.connectivity") object for table with given name with names of columns to fill specified |
| `Insert(String name, Database database, String tableName, String[] columnNames, String[] valueTexts)` | Deprecated.  Creates new [`Insert`](Insert.md "class in com.anylogic.engine.connectivity") object for table with given name with names of columns to fill specified |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `evaluateValues_xjal(Object[] values)` | Deprecated.  This method should fill `values` array |
| `int` | `execute()` | Deprecated.  Performs insertion of one row with current values (provided with [`evaluateValues_xjal(Object[])`](#evaluateValues_xjal(java.lang.Object%5B%5D)) method) |
| `void` | `finish()` | Deprecated.  Resets this object (after multiple insertion operations) - releases resources.  May be called after all [`execute()`](#execute()) operations completed.  Called automatically on underlying [`Database`](Database.md "class in com.anylogic.engine.connectivity") destroy and disconnect |
| `String` | `toString()` | Deprecated. |
