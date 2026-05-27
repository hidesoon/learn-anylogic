*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/InsertQuery.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class InsertQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.InsertQuery

---

```
public class InsertQuery
extends Object
```

InsertQuery for building and execution INSERT SQL statements

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `InsertQuery(ModelDBConnectivity database, com.querydsl.sql.RelationalPath<?> table)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `InsertQuery` | `columns(com.querydsl.core.types.Path<?>... columns)` | Set columns to insert |
| `long` | `execute()` | Executes insert query |
| `com.querydsl.sql.dml.SQLInsertClause` | `getDSLQuery()` |  |
| `<T> InsertQuery` | `set(com.querydsl.core.types.Path<T> column, com.querydsl.core.types.Expression<? extends T> value)` | Set column with its value to insert |
| `InsertQuery` | `values(Object... values)` | Set values for columns |
