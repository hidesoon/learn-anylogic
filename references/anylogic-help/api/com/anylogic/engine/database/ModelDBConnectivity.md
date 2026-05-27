*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/ModelDBConnectivity.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class ModelDBConnectivity

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.ModelDBConnectivity

Direct Known Subclasses:
:   `ModelDatabase`

---

```
@AnyLogicInternalAPI
public abstract class ModelDBConnectivity
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Base class for built-in model database connectivity.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `AL_DB_OBJECTS` |  |
| `static final String` | `AL_ID_COLUMN_NAME` |  |
| `static final String` | `AL_LOG_TYPE_TABLE` |  |
| `static final String` | `AL_LOG_TYPE_VIEW` |  |
| `static final String` | `AL_OBJECT_NAME` |  |
| `static final String` | `AL_OBJECT_TYPE` |  |
| `static final String` | `AL_OBJECT_USAGE` |  |
| `static final String` | `AL_OBJECT_USAGE_LOG` |  |
| `static final String` | `AL_SELECTED_LOG_OBJECT_NAME` |  |
| `static final String` | `AL_SELECTED_LOG_OBJECT_TYPE` |  |
| `static final String` | `AL_SELECTED_LOG_OBJECTS` |  |
| `static final String` | `AL_VIEW_DEFINITION` |  |
| `static final String` | `AL_VIEW_NAME` |  |
| `static final String` | `AL_VIEWS_TABLE_NAME` |  |
| `static final String` | `CREATE_VIEW_SQL` |  |
| `static final String` | `CURRENT_VERSION` |  |
| `static final String` | `DATABASE_DB_PATH` |  |
| `static final String` | `DATABASE_DIRECTORY` |  |
| `static final String` | `DROP_SQL_OBJECT` |  |
| `static final String` | `LOG_OBJECT_SUFFIX` |  |
| `static final String` | `PUBLIC_SCHEMA_NAME` |  |
| `static final String` | `SQL_FUNCTION` |  |
| `static final String` | `UNIQUE_AUTOINC_COLUMN_NAME` | Deprecated. |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ModelDBConnectivity()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `disconnect()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `final Connection` | `getConnection()` |  |
| `static String` | `getCreateTableSQL(String tableName, String tableContent, boolean cached)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `com.querydsl.sql.Configuration` | `getDSLConfiguration()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `DatabaseLogStatements` | `getLogStatements()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `QuerySupport` | `getQuerySupport()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `ModelDBConfiguration` | `initConfiguration()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setConfiguration(ModelDBConfiguration configuration)` | There are 2 ways to define configuration: Call [`setConfiguration(ModelDBConfiguration)`](#setConfiguration(com.anylogic.engine.database.ModelDBConfiguration)) once before using [`getConnection()`](#getConnection()) Override [`initConfiguration()`](#initConfiguration()) and it will be lazily invoked during [`getConnection()`](#getConnection()) |
