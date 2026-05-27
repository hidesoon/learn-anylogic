*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/ModelDatabase.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class ModelDatabase

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.database.ModelDBConnectivity](ModelDBConnectivity.md "class in com.anylogic.engine.database")

com.anylogic.engine.database.ModelDatabase

---

```
public class ModelDatabase
extends ModelDBConnectivity
```

This class represents the built-in AnyLogic Model Database. Almost all the methods of this class are internal.
The database object may be accessed from `getEngine().getModelDatabase()`
and may be used for [import](#importFromExternalDB(java.sql.Connection,java.lang.String,java.lang.String,boolean,boolean)) /
[export](#exportToExternalDB(java.lang.String,java.sql.Connection,java.lang.String,boolean,boolean)) with external data sources.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ModelDatabase(Engine engine, ModelProperties modelProperties, DatabaseLogState logState)` | **This constructor is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `ResultSet` | `execute(String sqlStatement)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `exportToExternalDB(String sourceTableName, Connection targetConnection, String targetTableName, boolean clearTargetTable, boolean autoCommit)` | Exports a single table data from this database to an external database. |
| `void` | `importFromExternalDB(Connection sourceConnection, String sourceTableName, String targetTableName, boolean clearTargetTable, boolean autoCommit)` | Imports a single table data from an external database. |
| `ModelDBConfiguration` | `initConfiguration()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isLoggingOn(LoggingType loggingType)` |  |
| `void` | `log(ILogEntry logEntry)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `resetBeforeStart()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ResultSet` | `select(String sqlQuery)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ResultSet` | `selectFrom(String tableName)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `updateImportedTables()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ResultSet` | `wrapResultSet(ResultSet results)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
