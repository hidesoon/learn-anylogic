*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseDescriptor.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseDescriptor

All Implemented Interfaces:
:   `Serializable`

---

```
@AnyLogicInternalAPI
public class DatabaseDescriptor
extends Object
implements Serializable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.database.DatabaseDescriptor)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DatabaseDescriptor(DatabaseType type, String jdbcDriver, String connectionURL, Properties connectionInfo)` |  |
| `DatabaseDescriptor(DatabaseType type, String jdbcDriver, String connectionURL, Properties connectionInfo, String fileName)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Connection` | `createConnection()` |  |
| `boolean` | `equals(Object obj)` |  |
| `String` | `getConnectionPassword()` |  |
| `String` | `getFileName()` |  |
| `DatabaseType` | `getType()` |  |
| `int` | `hashCode()` |  |
| `void` | `setExcelStreamingMode(DatabaseExcelStreamingMode mode)` |  |
