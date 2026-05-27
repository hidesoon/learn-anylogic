*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/database/CodeValue.html>*

---

Package [com.anylogic.engine.database](package-summary.md)

# Class CodeValue

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.database.CodeValue

All Implemented Interfaces:
:   `Serializable`

---

```
public class CodeValue
extends Object
implements Serializable
```

Class containing some executable action / evaluatable expression code inside.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.database.CodeValue)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CodeValue(String code)` | Creates new expression / action descriptor |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `<T> T` | `execute(CodeValueExecutor context, Class<T> returnType, Object... argDescriptors)` |  |
| `<T> T` | `execute(CodeValueExecutor context, Object... argDescriptors)` | Executes/evaluates the code value, e.g. |
| `String` | `getCode()` | Returns the original code string contained in this object |
