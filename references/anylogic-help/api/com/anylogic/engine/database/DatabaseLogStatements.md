*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseLogStatements.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseLogStatements

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseLogStatements

---

```
@AnyLogicInternalAPI
public class DatabaseLogStatements
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `PreparedStatement` | `getInsertStatement(DatabaseLogTableType databaseLogTableType, String... fields)` |  |
| `PreparedStatement` | `getUpdateStatement(DatabaseLogTableType databaseLogTableType, String idColumnName, String... fields)` |  |
