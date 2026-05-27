*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseDescriptorRegistry.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class DatabaseDescriptorRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.DatabaseDescriptorRegistry

All Implemented Interfaces:
:   `Closeable`, `AutoCloseable`

---

```
@AnyLogicInternalAPI
public class DatabaseDescriptorRegistry
extends Object
implements Closeable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `DatabaseDescriptorRegistry()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `close()` |  |
| `Connection` | `getConnection(DatabaseDescriptor dd)` |  |
