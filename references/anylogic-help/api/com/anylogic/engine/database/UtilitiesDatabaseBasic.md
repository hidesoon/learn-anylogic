*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/UtilitiesDatabaseBasic.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class UtilitiesDatabaseBasic

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.UtilitiesDatabaseBasic

---

```
@AnyLogicInternalAPI
public class UtilitiesDatabaseBasic
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static long` | `convertToRelativeTime(Timestamp t, LocalDateTime beginPoint, long repeatTime)` |  |
| `static void` | `copyDatabaseTable(Connection sourceConnection, Connection targetConnection, String sourceTableName, String targetTableName)` |  |
| `static void` | `copyDatabaseTable(Connection sourceConnection, Connection targetConnection, String sourceTableName, String targetTableName, boolean clearTargetTable, boolean autoCommit)` |  |
| `static void` | `copyDatabaseTables(ProgressConsumer monitor, Connection sourceConnection, Connection targetConnection, List<String> sourceTableNames, List<String> targetTableNames, boolean clearTargetTable, boolean autoCommit)` |  |
| `static void` | `exportTables(ProgressConsumer monitor, Connection sourceDatabase, Connection targetDatabase, Collection<String> sqlStatements, List<String> sourceNames)` |  |
| `static String` | `getIdentifierQuoteString(Connection connection)` |  |
| `static LocalDateTime` | `getStartOfDay(Timestamp t)` |  |
| `static boolean` | `isInt(double value)` | Determines whether provided double value is integer or not. |
| `static boolean` | `isMariaDb(Connection connection)` |  |
| `static boolean` | `isMicrosoftAccess(Connection connection)` |  |
| `static boolean` | `isOracleDB(Connection connection)` |  |
| `static String` | `trimTableName(String s)` |  |
