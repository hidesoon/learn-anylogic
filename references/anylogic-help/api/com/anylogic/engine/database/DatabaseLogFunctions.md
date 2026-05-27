*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseLogFunctions.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Enum Class DatabaseLogFunctions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[DatabaseLogFunctions](DatabaseLogFunctions.md "enum class in com.anylogic.engine.database")>

com.anylogic.engine.database.DatabaseLogFunctions

All Implemented Interfaces:
:   `DatabaseLoggingObjectDescriptor`, `Serializable`, `Comparable<DatabaseLogFunctions>`, `Constable`

---

```
@AnyLogicInternalAPI
public enum DatabaseLogFunctions
extends Enum<DatabaseLogFunctions>
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
| `String` | `getFunctionDefinition()` |  |
| `String` | `getName()` |  |
| `String` | `getType()` |  |
| `static DatabaseLogFunctions` | `valueOf(String name)` | Returns the enum constant of this class with the specified name. |
| `static DatabaseLogFunctions[]` | `values()` | Returns an array containing the constants of this enum class, in the order they are declared. |
