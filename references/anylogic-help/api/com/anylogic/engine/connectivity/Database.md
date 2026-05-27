*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/connectivity/Database.html>*

---

Package [com.anylogic.engine.connectivity](package-summary.md)

# Class Database

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.connectivity.ConnectivityBase](ConnectivityBase.md "class in com.anylogic.engine.connectivity")

com.anylogic.engine.connectivity.Database

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `DatabaseConstants`, `Serializable`

---

```
public final class Database
extends ConnectivityBase
implements DatabaseConstants, com.anylogic.engine.internal.Child
```

Database connection manager class

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.connectivity.Database)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Database(Presentable owner, String name, String fileName)` | Creates new [`Database`](Database.md "class in com.anylogic.engine.connectivity") object for interaction with file-based (Access or Excel) database |
| `Database(Presentable owner, String name, String fileName, String login, char[] password)` | Creates new [`Database`](Database.md "class in com.anylogic.engine.connectivity") object for interaction with file-based (Access or Excel) database |
| `Database(Presentable owner, String name, String jdbcDriver, String connectionURL, String login, char[] password)` | Creates new [`Database`](Database.md "class in com.anylogic.engine.connectivity") object for interaction with database |
| `Database(Presentable owner, String name, String sqlJdbcDriver, String host, String databaseName, String login, char[] password)` | Creates new [`Database`](Database.md "class in com.anylogic.engine.connectivity") object for interaction with MS SQL Server database |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `closeResultSet(ResultSet rs)` | Deprecated. call [`ResultSet.close()`](ResultSet.md#close()) method instead |
| `boolean` | `connect()` | The method connects a data source, specified by constructor parameters. |
| `void` | `disconnect()` | Disconnects currently connected database  This method call has no effect if this [`Database`](Database.md "class in com.anylogic.engine.connectivity") object is not connected  It is **strongly recommended** that user explicitly commits or rolls back an active transaction (if any has been explicitly opened via [`Connection.setAutoCommit(boolean)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.sql/java/sql/Connection.html#setAutoCommit(boolean) "class or interface in java.sql")) prior to calling the this method. |
| `Connection` | `getConnection()` | Returns existing [`Connection`](https://docs.oracle.com/en/java/javase/17/docs/api/java.sql/java/sql/Connection.html "class or interface in java.sql") to the database or connects to the database if not connected  If any error occurs, throws [`RuntimeException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class or interface in java.lang") |
| `DatabaseDescriptor` | `getDbDescriptor()` |  |
| `Integer` | `getFieldType(String sTableName, String sFieldName)` | The methods returns SQL-type of specified field. |
| `Object` | `getMatrix(String sqlQuery, String type)` | The method executes specified SQL query and returns the produced values as 2D array of values of specified type. |
| `ResultSet` | `getQueryResultSet(String queryText, String listOfFields, String keyField, String keyFieldValue)` | The method returns result set produced by querying data from specified fields and rows of specified query. |
| `ResultSet` | `getResultSet(String sqlQuery)` | The method executes specified SQL query and returns the produced result as [`ResultSet`](ResultSet.md "interface in com.anylogic.engine.connectivity") object. |
| `Map<String,String>` | `getRow(String sqlQuery)` | The method executes specified SQL query and returns the produced values. |
| `static ResultSet` | `getSQLResultSet(ResultSet rs)` |  |
| `static Statement` | `getSQLStatement(Statement statement)` | Returns Java SQL [`Statement`](https://docs.oracle.com/en/java/javase/17/docs/api/java.sql/java/sql/Statement.html "class or interface in java.sql"), backed by given [`Statement`](Statement.md "interface in com.anylogic.engine.connectivity") object |
| `Statement` | `getStatement()` | The method creates and returns each time new statement  Please call [`Statement.close()`](Statement.md#close()) method after all needed operations are completed |
| `ResultSet` | `getTableResultSet(String tableName, String listOfFields, String keyField, String keyFieldValue)` | The method returns result set produced by querying data from specified fields and rows of specified table. |
| `String` | `getValue(String sqlQuery)` | The method executes specified SQL query and returns the produced value. |
| `boolean` | `modify(String sqlQuery)` | The method executes specified SQL query. |
| `void` | `releaseStatement(Statement statement)` | Deprecated. call [`Statement.close()`](Statement.md#close()) method instead |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `void` | `setExcelStreamingMode(DatabaseExcelStreamingMode mode)` | Sets excel streaming mode to improve speed while working with large excel files DatabaseExcelStreamingMode.READ allows to read huge collection of data a bit faster WARNING: streaming mode is not supported if Excel file is encrypted. |
| `String` | `toString()` | Returns formatted database connection properties (excluding password value) |
