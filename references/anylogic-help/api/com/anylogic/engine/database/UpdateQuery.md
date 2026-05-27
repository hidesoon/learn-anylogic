*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/UpdateQuery.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class UpdateQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.UpdateQuery

---

```
public class UpdateQuery
extends Object
```

UpdateQuery for building and execution of UPDATE SQL statements

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `UpdateQuery(ModelDBConnectivity database, com.querydsl.sql.RelationalPath<?> table)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `long` | `execute()` | Executes update query |
| `com.querydsl.sql.dml.SQLUpdateClause` | `getDSLQuery()` |  |
| `<T> UpdateQuery` | `set(com.querydsl.core.types.Path<T> column, com.querydsl.core.types.Expression<? extends T> value)` | Set column with its value to update with |
| `<T> UpdateQuery` | `set(com.querydsl.core.types.Path<T> column, T value)` | Set column with its value to update with |
| `UpdateQuery` | `set(List<? extends com.querydsl.core.types.Path<?>> columns, List<?> values)` | Set columns with its values to update with |
| `UpdateQuery` | `where(com.querydsl.core.types.Predicate condition)` | Add a condition to identify rows that have to be updated |
| `UpdateQuery` | `where(com.querydsl.core.types.Predicate... conditions)` | Add conditions to identify rows that have to be updated |
