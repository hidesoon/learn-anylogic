*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/CachedSelectQuery.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class CachedSelectQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.CachedSelectQuery

---

```
@AnyLogicInternalAPI
public class CachedSelectQuery
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CachedSelectQuery(Connection connection, com.querydsl.sql.Configuration configuration, com.querydsl.core.types.Expression<?> table)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `<RT> RT` | `valueOf(com.querydsl.core.types.Expression<RT> column)` |  |
| `<T> CachedSelectQuery` | `where(com.querydsl.core.types.dsl.SimpleExpression<T> column, T value)` |  |
