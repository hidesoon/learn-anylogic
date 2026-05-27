*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/ModelDBLogs.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class ModelDBLogs

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.ModelDBLogs

---

```
@AnyLogicInternalAPI
public class ModelDBLogs
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

This class is responsible for storing model logs on the database side.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ModelDBLogs(ModelDBConnectivity database)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `clearIncompleteLogEntries()` |  |
| `static void` | `createLogSchema(Connection connection)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `static void` | `deleteExistingLogObjects(Connection connection)` | This method deletes all the model log data (if any were turned on) from the model database |
| `void` | `flushIncompleteLogEntries()` |  |
| `void` | `log(ILogEntry logEntry)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
