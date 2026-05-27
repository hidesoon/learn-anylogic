*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DeleteQuery.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DeleteQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DeleteQuery

---

```
public class DeleteQuery
extends Object
```

DeleteQuery for building and execution of DELETE SQL statements

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DeleteQuery(ModelDBConnectivity database, com.querydsl.sql.RelationalPath<?> table)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `long` | `execute()` | Executes delete query |
| `com.querydsl.sql.dml.SQLDeleteClause` | `getDSLQuery()` |  |
| `DeleteQuery` | `where(com.querydsl.core.types.Predicate condition)` | Add a condition to identify rows that have to be deleted |
| `DeleteQuery` | `where(com.querydsl.core.types.Predicate... conditions)` | Add conditions to identify rows that have to be deleted |
