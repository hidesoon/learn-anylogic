*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/Query.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class Query

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.connectivity.ConnectivityBase](ConnectivityBase.md "class in com.anylogic.engine.connectivity")

[com.anylogic.engine.connectivity.DatabaseAccessor](DatabaseAccessor.md "class in com.anylogic.engine.connectivity")

com.anylogic.engine.connectivity.Query

All Implemented Interfaces:
:   `Serializable`

---

```
@Deprecated
public class Query
extends DatabaseAccessor
```

Deprecated.

This class is deprecated and will be removed in future releases. Consider using [`Database`](Database.md "class in com.anylogic.engine.connectivity") API instead.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.Query)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Query(String name, Database database, boolean selectFromTable, String tableNameOrQueryText)` | Deprecated.  Creates new [`Query`](Query.md "class in com.anylogic.engine.connectivity") for work only with [`execute()`](#execute()) method |
| `Query(String name, Database database, boolean selectFromTable, String tableNameOrQueryText, String[][] mapping)` | Deprecated.  Creates new [`Query`](Query.md "class in com.anylogic.engine.connectivity") for work in the *Mapping* mode ([`executeAndMap()`](#executeAndMap()) method)  Note the [`execute()`](#execute()) method is still available for this object |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Object` | `createNewRowElementInstance_xjal()` | Deprecated.  Extension-point for element creation  In the *Mapping* mode, this method should be overridden to create specific element and return it |
| `final ResultSet` | `execute()` | Deprecated.  Executes query in the database and returns single [`ResultSet`](ResultSet.md "interface in com.anylogic.engine.connectivity")  If any error occurs, throws [`RuntimeException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class or interface in java.lang")  Connects [`Database`](Database.md "class in com.anylogic.engine.connectivity") if it is not connected. |
| `final int` | `executeAndMap()` | Deprecated.  This method fills underlying collection or agent population (created agents are started automatically) with elements created from rows of database Query result  This method works only in the *Mapping* mode |
| `final int` | `executeAndMap(boolean startAgents)` | Deprecated.  This method fills underlying collection or agent population with elements created from rows of database Query result  This method works only in the *Mapping* mode |
| `void` | `registerNewRowElement_xjal(Object element, boolean startAgents)` | Deprecated.  Extension-point for element creation  In the *Mapping* mode, this method should be overridden to start given element (previously created by [`createNewRowElementInstance_xjal()`](#createNewRowElementInstance_xjal()) and parametrized) add it to the underlying collection and return it |
| `String` | `toString()` | Deprecated. |
