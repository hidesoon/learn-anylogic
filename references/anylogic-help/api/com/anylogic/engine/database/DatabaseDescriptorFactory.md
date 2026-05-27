*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseDescriptorFactory.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseDescriptorFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseDescriptorFactory

---

```
@AnyLogicInternalAPI
public class DatabaseDescriptorFactory
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static DatabaseDescriptor` | `createCustomDescriptor(String jdbcDriver, String connectionURL, String login, String password)` |  |
| `static DatabaseDescriptor` | `createDbDescriptor(DatabaseType dbType, String host, String databaseName, String login, String password)` |  |
| `static DatabaseDescriptor` | `createFileDescriptor(String fileName, String login, String password)` |  |
| `static DatabaseDescriptor` | `createFileDescriptor(String fileName, String login, String password, DatabaseExcelStreamingMode mode)` |  |
