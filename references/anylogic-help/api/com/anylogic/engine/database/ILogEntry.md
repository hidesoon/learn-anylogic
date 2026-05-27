*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/ILogEntry.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Interface ILogEntry

---

```
@AnyLogicInternalAPI
public interface ILogEntry
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `default Object` | `getCompoundKey()` |  |
| `PreparedStatement` | `getSQLStatement(ModelDBConnectivity database)` |  |
| `default void` | `initCompound(ILogEntry prev)` |  |
| `default boolean` | `isBatch()` |  |
| `default boolean` | `isCompound()` |  |
| `default boolean` | `isCompoundLast()` |  |
| `default boolean` | `nextStatement()` |  |
