*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AnyLogicCustomSerialization.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Annotation Interface AnyLogicCustomSerialization

---

```
@AnyLogicInternalAPI
@Target(FIELD)
@Retention(RUNTIME)
public @interface AnyLogicCustomSerialization
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*
Annotation for custom serialization processing during save to snapshot operations.
Works with non-static transient fields only.
Has mode argument with default value [`AnyLogicCustomSerializationMode.REFERENCE`](AnyLogicCustomSerializationMode.md#REFERENCE)

Since:
:   7.0

Author:
:   AnyLogic North America, LLC <https://anylogic.com>
