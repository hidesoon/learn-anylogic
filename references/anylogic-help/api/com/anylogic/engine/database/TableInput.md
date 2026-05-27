*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/TableInput.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class TableInput

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.TableInput

All Implemented Interfaces:
:   `Serializable`, `AutoCloseable`

---

```
@AnyLogicInternalAPI
public class TableInput
extends Object
implements Serializable, AutoCloseable
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.database.TableInput)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `TableInput(Utilities owner, String sql, Object... params)` |  |
| `TableInput(Utilities owner, Supplier<ResultSet> selectResultSet)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `boolean` | `absolute(int row)` |  |
| `void` | `close()` | Closes the underlying result set and drops any cached data |
| `boolean` | `first()` |  |
| `<T> T` | `getValue(int rowIndex, String columnLabel, Class<T> returnType)` |  |
| `<T> T` | `getValue(String columnLabel, Class<T> returnType)` |  |
| `void` | `loadAll()` |  |
| `boolean` | `next()` | Advances this input to the next table row |
| `int` | `size()` |  |
