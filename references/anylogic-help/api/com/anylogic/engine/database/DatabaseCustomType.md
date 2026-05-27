*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseCustomType.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseCustomType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseCustomType

---

```
@AnyLogicInternalAPI
public class DatabaseCustomType
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DatabaseCustomType(DatabaseColumnTypeEnum category, String tableName, String columnName, String reference)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static DatabaseCustomType` | `createCode(String tableName, String columnName)` |  |
| `static DatabaseCustomType` | `createEnum(String tableName, String columnName, String reference)` |  |
| `DatabaseColumnTypeEnum` | `getCategory()` |  |
| `String` | `getColumnName()` |  |
| `String` | `getReference()` |  |
| `String` | `getTableName()` |  |
