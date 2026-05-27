*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/SelectQuery.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class SelectQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.database.SelectQueryBasic](SelectQueryBasic.md "class in com.anylogic.engine.database")<[SelectQuery](SelectQuery.md "class in com.anylogic.engine.database")>

com.anylogic.engine.database.SelectQuery

---

```
public class SelectQuery
extends SelectQueryBasic<SelectQuery>
```

SelectQuery for building and execution of SELECT SQL statements

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `SelectQuery(ModelDatabase database, com.querydsl.sql.RelationalPathBase<?> table, Utilities owner)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `double[]` | `arrayOfDouble(com.querydsl.core.types.Expression<? extends Number> valueColumn)` | Executes the given SELECT query which should return 1 column with numbers. |
| `int[]` | `arrayOfInt(com.querydsl.core.types.Expression<? extends Number> valueColumn)` | Executes the given SELECT query which should return 1 column with numbers. |
| `ResultSet` | `getResults(com.querydsl.core.types.Expression<?>... columns)` | Get the results as an JDBC result set |
| `TableFunction` | `tableFunction(TableFunction tableFunction, com.querydsl.core.types.Expression<? extends Number> argumentColumn, com.querydsl.core.types.Expression<? extends Number> valueColumn)` | Executes the given SELECT query which should return 2 columns of data: the first column contains arguments numbers, the second column contains values numbers. |
