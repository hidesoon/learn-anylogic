*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseSQLBuilderBasic.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseSQLBuilderBasic

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseSQLBuilderBasic

---

```
@AnyLogicInternalAPI
public class DatabaseSQLBuilderBasic
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `DatabaseSQLBuilderBasic.PrettyFormatting` |  |
| `static class` | `DatabaseSQLBuilderBasic.QueryBuilder` |  |
| `static enum` | `DatabaseSQLBuilderBasic.ValuesAre` |  |
| `static enum` | `DatabaseSQLBuilderBasic.Where` |  |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `SQL_ADD` |  |
| `static final String` | `SQL_ALTER` |  |
| `static final String` | `SQL_AND` |  |
| `static final String` | `SQL_AS` |  |
| `static final String` | `SQL_BEFORE` |  |
| `static final String` | `SQL_CASCADE` |  |
| `static final String` | `SQL_CAST` |  |
| `static final String` | `SQL_CHECK` |  |
| `static final String` | `SQL_CLOSE_PARENTHESIS` |  |
| `static final String` | `SQL_COLUMN` |  |
| `static final String` | `SQL_COMMA` |  |
| `static final String` | `SQL_CONSTRAINT` |  |
| `static final String` | `SQL_COUNT` |  |
| `static final String` | `SQL_CREATE` |  |
| `static final String` | `SQL_DEFAULT` |  |
| `static final String` | `SQL_DELETE` |  |
| `static final String` | `SQL_DELETE_FROM` |  |
| `static final String` | `SQL_DISTINCT` |  |
| `static final String` | `SQL_DOT` |  |
| `static final String` | `SQL_DOUBLE_QUOTE` |  |
| `static final String` | `SQL_DROP` |  |
| `static final String` | `SQL_EQUALLY` |  |
| `static final String` | `SQL_EXISTS` |  |
| `static final String` | `SQL_FALSE` |  |
| `static final String` | `SQL_FOREIGN_KEY` |  |
| `static final String` | `SQL_FROM` |  |
| `static final String` | `SQL_GREATER` |  |
| `static final String` | `SQL_GROUP_BY` |  |
| `static final String` | `SQL_HAVING` |  |
| `static final String` | `SQL_IF` |  |
| `static final String` | `SQL_IN` |  |
| `static final String` | `SQL_INDEX` |  |
| `static final String` | `SQL_INNER` |  |
| `static final String` | `SQL_INSERT_INTO` |  |
| `static final String` | `SQL_IS` |  |
| `static final String` | `SQL_IS_NULL` |  |
| `static final String` | `SQL_JOIN` |  |
| `static final String` | `SQL_LEFT` |  |
| `static final String` | `SQL_LIKE` |  |
| `static final String` | `SQL_LIMIT` |  |
| `static final String` | `SQL_MAX` |  |
| `static final String` | `SQL_MODIFY` |  |
| `static final String` | `SQL_NOT` |  |
| `static final String` | `SQL_NULL` |  |
| `static final String` | `SQL_ON` |  |
| `static final String` | `SQL_OPEN_PARENTHESIS` |  |
| `static final String` | `SQL_ORDER_BY` |  |
| `static final String` | `SQL_PRIMARY_KEY` |  |
| `static final String` | `SQL_REFERENCES` |  |
| `static final String` | `SQL_RENAME_TO` |  |
| `static final String` | `SQL_SELECT` |  |
| `static final String` | `SQL_SET` |  |
| `static final String` | `SQL_SINGLE_QUOTE` |  |
| `static final String` | `SQL_TABLE` |  |
| `static final String` | `SQL_TRUE` |  |
| `static final String` | `SQL_UNDERLINE` |  |
| `static final String` | `SQL_UNIQUE` |  |
| `static final String` | `SQL_UNIQUE_AUTOINC_COLUMN_TYPE` |  |
| `static final String` | `SQL_UPDATE` |  |
| `static final String` | `SQL_VALUES` |  |
| `static final String` | `SQL_VIEW` |  |
| `static final String` | `SQL_WHERE` |  |
| `static final String` | `SQL_WHITESPACE` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static StringBuilder` | `appendValue(StringBuilder sb, String value)` | '{value}' | NULL |
| `static String` | `buildDeleteFromTable(String tableName, String[]... where)` | DELETE FROM {tableName} WHERE [{where[i][0]} = '{where[i][1]}' AND ...] |
| `static String` | `buildSelectFrom(String[] whatToSelect, String tableName, String[]... where)` | SELECT {whatToSelect} FROM {tableName} WHERE [{where[i][0]} = '{where[i][1]}' AND ...] |
| `static String` | `insertInto(String tableName, String[] columnNames, DatabaseSQLBuilderBasic.ValuesAre howToInsertValues, String... values)` | INSERT INTO {TABLE\_NAME} VALUES ('{value[i]}', ...) |
| `static String` | `prepareInsertInto(String tableName, String... fields)` |  |
| `static String` | `prepareUpdateSet(String tableName, String unicFieldName, DatabaseSQLBuilderBasic.Where where, String... fields)` |  |
