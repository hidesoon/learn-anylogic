*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseSQLBuilderBasic.QueryBuilder.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseSQLBuilderBasic.QueryBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseSQLBuilderBasic.QueryBuilder

Enclosing class:
:   [DatabaseSQLBuilderBasic](DatabaseSQLBuilderBasic.md "class in com.anylogic.engine.database")

---

```
@AnyLogicInternalAPI
public static class DatabaseSQLBuilderBasic.QueryBuilder
extends Object
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `QueryBuilder()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `$(int number)` |  |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `$(String text)` |  |
| `<T> DatabaseSQLBuilderBasic.QueryBuilder` | `commaSeparated(Consumer<T> elementGenerator, T... elements)` | Adds comma-separated names as is |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `names(String... names)` | Adds comma-separated names as is |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `newLine(DatabaseSQLBuilderBasic.PrettyFormatting prettyFormatting)` |  |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `prepare(DatabaseSQLBuilderBasic.Where whereOperator)` |  |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `question()` |  |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `questions(int count)` |  |
| `StringBuilder` | `sb()` |  |
| `String` | `toString()` |  |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `value(String value)` |  |
| `DatabaseSQLBuilderBasic.QueryBuilder` | `values(DatabaseSQLBuilderBasic.ValuesAre howToInsertValues, String[] values, int nQuestions)` |  |
