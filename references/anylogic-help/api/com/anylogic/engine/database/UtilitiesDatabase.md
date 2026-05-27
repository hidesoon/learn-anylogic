*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/UtilitiesDatabase.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class UtilitiesDatabase

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.UtilitiesDatabase

---

```
public class UtilitiesDatabase
extends Object
```

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static void` | `copyDatabaseTable(Connection sourceConnection, Connection targetConnection, String sourceTableName, String targetTableName)` |  |
| `static void` | `copyDatabaseTable(Connection sourceConnection, Connection targetConnection, String sourceTableName, String targetTableName, boolean clearTargetTable, boolean autoCommit)` |  |
| `static void` | `copyDatabaseTables(ProgressConsumer monitor, Connection sourceConnection, Connection targetConnection, List<String> sourceTableNames, List<String> targetTableNames, boolean clearTargetTable, boolean autoCommit)` |  |
| `static void` | `exportTables(ProgressConsumer monitor, Connection sourceDatabase, Connection targetDatabase, Collection<String> sqlStatements, List<String> sourceNames)` |  |
| `static String` | `getIdentifierQuoteString(Connection connection)` |  |
| `static boolean` | `logIfNeeded(Utilities agent, LoggingType loggingType, boolean staticEntry, Supplier<ILogEntry> logEntrySupplier)` | Logs information to database |
| `static boolean` | `logIfNeeded(Utilities agent, LoggingType loggingType, Supplier<ILogEntry> logEntrySupplier)` | Logs information to database |
| `static String` | `toStringDB(Object value)` |  |
| `static String` | `trimTableName(String s)` |  |
