*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/QuerySupport.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class QuerySupport

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.QuerySupport

---

```
@AnyLogicInternalAPI
public class QuerySupport
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Class supporting query execution.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `QuerySupport(ModelDBConnectivity database)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T> T` | `castFromDB(Object value, Class<T> type)` |  |
| `static Object` | `castToDB(Object value)` |  |
| `<T> T` | `fetchResult(boolean cached, boolean mustBeUnique, Class<T> returnType, String sql, Object... params)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `<R> Object` | `getCachedValue(com.querydsl.sql.SQLBindings sqlBindings, String operation, Supplier<R> f)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `PreparedStatement` | `prepareStatement(String sql, Object[] params)` | Creates a [`PreparedStatement`](https://docs.oracle.com/en/java/javase/17/docs/api/java.sql/java/sql/PreparedStatement.html "class or interface in java.sql") object (which may be used to executes insert, delete and update statements in AnyLogic database) with the given SQL query string and and fills in the given objects as parameters.  Objects passed as parameters are converted automatically to match database format (e.g. |
| `boolean` | `selectExists(boolean cached, String sql, Object... params)` | Returns `true` if the given sql and params returns at least one result This function caches its results, to speed up default behavior Use selectExists(false, sql, params) to get non cached result every time |
| `<T> List<T>` | `selectValues(Class<T> returnType, String sql, Object... params)` | List the results for given sql and params Given sql query must return single column An empty list is returned for no results |
