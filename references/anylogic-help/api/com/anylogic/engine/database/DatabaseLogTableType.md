*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseLogTableType.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Enum Class DatabaseLogTableType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[DatabaseLogTableType](DatabaseLogTableType.md "enum class in com.anylogic.engine.database")>

com.anylogic.engine.database.DatabaseLogTableType

All Implemented Interfaces:
:   `DatabaseLoggingObjectDescriptor`, `Serializable`, `Comparable<DatabaseLogTableType>`, `Constable`

---

```
@AnyLogicInternalAPI
public enum DatabaseLogTableType
extends Enum<DatabaseLogTableType>
implements DatabaseLoggingObjectDescriptor
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getCreateSQL()` |  |
| `Set<LoggingType>` | `getLoggingTypes()` |  |
| `String` | `getName()` |  |
| `String` | `getType()` |  |
| `static DatabaseLogTableType` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static DatabaseLogTableType[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
