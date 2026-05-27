*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/DatabaseLoggingObjectDescriptor.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Interface DatabaseLoggingObjectDescriptor

All Known Implementing Classes:
:   `DatabaseLogFunctions`, `DatabaseLogTableType`, `DatabaseLogViews`

---

```
@AnyLogicInternalAPI
public interface DatabaseLoggingObjectDescriptor
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Set<LoggingType>` | `EMPTY` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `String` | `getCreateSQL()` |  |
| `default Set<LoggingType>` | `getLoggingTypes()` |  |
| `String` | `getName()` |  |
| `default String` | `getSaveSQL()` |  |
| `String` | `getType()` |  |
