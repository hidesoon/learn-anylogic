*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/Update.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class Update

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.connectivity.ConnectivityBase](ConnectivityBase.md "class in com.anylogic.engine.connectivity")

[com.anylogic.engine.connectivity.DatabaseAccessor](DatabaseAccessor.md "class in com.anylogic.engine.connectivity")

com.anylogic.engine.connectivity.Update

All Implemented Interfaces:
:   `Serializable`

---

```
@Deprecated
public abstract class Update
extends DatabaseAccessor
```

Deprecated.

This class is deprecated and will be removed in future releases. Consider using [`Database`](Database.md "class in com.anylogic.engine.connectivity") API instead.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.Update)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Update(String name, Database database, String tableName, String keyColumnName, String[][] columnsToUpdate)` | Deprecated.  Creates new [`Update`](Update.md "class in com.anylogic.engine.connectivity") object for table with given name with names of key column to be checked and columns to be updated specified |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `abstract void` | `evaluateValues_xjal(Object[] keyValues, Object[][] updateValues)` | Deprecated.  This method should be overridden to fill `keyValues` and `updateValues` arrays |
| `int` | `execute()` | Deprecated.  Performs update of rows with current values (provided with [`evaluateValues_xjal(Object[], Object[][])`](#evaluateValues_xjal(java.lang.Object%5B%5D,java.lang.Object%5B%5D%5B%5D)) method) |
| `void` | `finish()` | Deprecated.  Resets this object (after multiple update operations) - releases resources  May be called after all [`execute()`](#execute()) operations completed.  Called automatically on underlying [`Database`](Database.md "class in com.anylogic.engine.connectivity") destroy and disconnect |
| `String` | `toString()` | Deprecated. |
